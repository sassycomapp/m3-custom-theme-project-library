"""Build the theme's component inventory from the component definitions.

Reads every component the theme offers in its Anvil toolbox, and its two layouts,
from the theme repository, and writes:
  docs/component-inventory.yaml  - read by the Mybizz test suite scanner
  docs/base-inventory.md         - the same facts for people and agents

Usage: python3 tools/build_inventory.py <path to the m3-custom-theme repository>
"""
import ast, os, re, sys
import yaml

THEME = sys.argv[1] if len(sys.argv) > 1 else "../m3-custom-theme"
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CC = os.path.join(THEME, "client_code")
ADDED_DOCS = {f[:-3] for f in os.listdir(os.path.join(HERE, "docs", "components")) if f.endswith(".md")}

def yaml_component(folder):
    with open(os.path.join(folder, "form_template.yaml")) as f:
        d = yaml.safe_load(f)
    props = []
    for p in d.get("properties", []) or []:
        props.append({
            "name": p["name"], "type": p.get("type", ""),
            "options": p.get("options"), "default": p.get("default_value"),
            "description": (p.get("description") or "").strip(),
            "writeback": bool(p.get("allow_binding_writeback") or p.get("supportsWriteback")),
            "writeback_events": p.get("binding_writeback_events"),
        })
    events = [e["name"] for e in d.get("events", []) or []]
    slots = list((d.get("slots") or {}).keys())
    return props, events, slots, bool(d.get("custom_component_container") or d.get("layout_metadata"))

def py_component(path, parent_props, parent_events):
    tree = ast.parse(open(path).read())
    dicts = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
            try:
                dicts[node.targets[0].id] = ast.literal_eval(node.value)
            except Exception:
                pass
    props, events = [], None
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            for st in node.body:
                if isinstance(st, ast.Assign) and isinstance(st.targets[0], ast.Name):
                    name = st.targets[0].id
                    if name in ("_anvil_properties_", "_anvil_events_") and isinstance(st.value, ast.List):
                        out = []
                        for el in st.value.elts:
                            if isinstance(el, ast.Name) and el.id in dicts:
                                out.append(dicts[el.id])
                            elif isinstance(el, ast.Starred):
                                out.append("*")
                        if name == "_anvil_properties_":
                            props = out
                        else:
                            events = out
    result = []
    for p in props:
        if p == "*":
            result.extend(parent_props)
        else:
            result.append({"name": p["name"], "type": p.get("type", ""), "options": p.get("options"),
                           "default": p.get("default_value"), "description": (p.get("description") or "").strip(),
                           "writeback": bool(p.get("supportsWriteback") or p.get("allow_binding_writeback")),
                           "writeback_events": p.get("binding_writeback_events")})
    seen, props = set(), []
    for p in result:
        if p["name"] not in seen:
            seen.add(p["name"]); props.append(p)
    if events is None:
        ev = list(parent_events)
    else:
        ev = []
        for e in events:
            ev.extend(parent_events if e == "*" else [e["name"]])
    return props, list(dict.fromkeys(ev))

def toolbox_types():
    text = open(os.path.join(THEME, "anvil.yaml")).read()
    return sorted(set(re.findall(r"type: (m3\.[A-Za-z_.]+)", text)))

inventory = {}
yaml_cache = {}
for t in toolbox_types():
    parts = t.split(".")[2:]          # after m3._Components
    folder = os.path.join(CC, "_Components", *parts)
    if os.path.isdir(folder) and os.path.exists(os.path.join(folder, "form_template.yaml")):
        props, events, slots, container = yaml_component(folder)
        yaml_cache[parts[-1]] = (props, events)
    else:
        inventory[t] = None             # resolved below
        continue
    inventory[t] = {"properties": props, "events": events, "slots": slots, "container": container}

PARENTS = {"InteractiveCard": ("Card", "InteractiveCard.py"), "ToggleIconButton": ("IconButton", "ToggleIconButton.py"),
           "TextBox": ("TextInput", "TextInput/TextBox.py"), "TextArea": ("TextInput", "TextInput/TextArea.py")}
for t, v in list(inventory.items()):
    if v is not None:
        continue
    name = t.split(".")[-1]
    parent, rel = PARENTS[name]
    pp, pe = yaml_component(os.path.join(CC, "_Components", parent))[:2]
    props, events = py_component(os.path.join(CC, "_Components", rel), pp, pe)
    inventory[t] = {"properties": props, "events": events, "slots": [], "container": False}

for lay in ("NavigationDrawerLayout", "NavigationRailLayout"):
    props, events, slots, _ = yaml_component(os.path.join(CC, "Layouts", lay))
    inventory["m3.Layouts." + lay] = {"properties": props, "events": events, "slots": slots, "container": True, "layout": True}

for t, v in inventory.items():
    v["specification"] = (t.split(".")[-1] + ".md") if t.split(".")[-1] in ADDED_DOCS else "base-inventory.md"

with open(os.path.join(HERE, "docs", "component-inventory.yaml"), "w") as f:
    f.write("# Generated by tools/build_inventory.py from the theme's component definitions. Do not edit by hand.\n")
    yaml.safe_dump({"components": inventory}, f, sort_keys=True, allow_unicode=True, width=200)

def cell(x):
    if x is None or x == "" or x == []:
        return ""
    if isinstance(x, list):
        return ", ".join(str(i) for i in x)
    return str(x).replace("|", "\\|").replace("\n", " ")

lines = ["---", 'title: "base-inventory"', "---",
         "# m3-custom-theme: component inventory", "",
         "Every component the theme offers in the Anvil toolbox, and its two layouts, with each property, the events it raises and the slots a layout offers. This file and `component-inventory.yaml` are generated from the theme's component definitions by `tools/build_inventory.py`, so they always match the theme. A component the theme adds also has its own specification in `docs/components/`, named in its entry.", "",
         "A property marked writeback can be bound with `writeback:<property>` in a form template.", ""]
for t in sorted(inventory):
    v = inventory[t]
    lines += [f"## `{t}`", ""]
    lines += [f"Specification: `{v['specification']}`." if v["specification"] != "base-inventory.md" else "Specification: this file.", ""]
    if v.get("slots"):
        lines += ["Slots: " + ", ".join(f"`{s}`" for s in v["slots"]) + ".", ""]
    lines += ["Events: " + (", ".join(f"`{e}`" for e in v["events"]) if v["events"] else "none") + ".", ""]
    lines += ["| Property | Type | Options | Default | Writeback | Description |", "|---|---|---|---|---|---|"]
    for p in v["properties"]:
        wb = "yes" + (f" ({cell(p['writeback_events'])})" if p.get("writeback_events") else "") if p["writeback"] else ""
        lines.append(f"| `{p['name']}` | {cell(p['type'])} | {cell(p['options'])} | {cell(p['default'])} | {wb} | {cell(p.get('description'))} |")
    lines.append("")
lines.append("*Generated file: change the theme, then run the generator.*")
open(os.path.join(HERE, "docs", "base-inventory.md"), "w").write("\n".join(lines) + "\n")
print(len(inventory), "components")
