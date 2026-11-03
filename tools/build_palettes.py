#!/usr/bin/env python3
"""Build palettes.css for the M3 custom theme.

Reads the four light palettes from the spreadsheet, corrects the surface-container
levels, generates the matching dark schemes with Material's colour algorithm, and
writes one CSS file that the theme imports.

Usage (from the project library repo folder):
    python tools/build_palettes.py "docs/Anvil-M3 color mapping 4 palette.xlsx" \
        ../m3-custom-theme/theme/assets/m3x/palettes.css

Needs: pip install openpyxl materialyoucolor
"""
import re
import sys

import openpyxl
from materialyoucolor.dynamiccolor.material_dynamic_colors import (
    MaterialDynamicColors as M,
)
from materialyoucolor.hct import Hct
from materialyoucolor.scheme.scheme_tonal_spot import SchemeTonalSpot

# Key colour of each palette, found by matching the spreadsheet against the
# algorithm: (hue, chroma 48, tone 50). Every checked colour matched within 2 steps.
KEY_HUES = {
    "professional_blue": 272.2,
    "warm_coral": 25.4,
    "calm_teal": 196.4,
    "sophisticated_purple": 298.6,
}

# Spreadsheet slot name -> Material colour name.
LIB = {
    "Primary": "primary", "On Primary": "onPrimary",
    "Primary Container": "primaryContainer",
    "On Primary Container": "onPrimaryContainer",
    "Secondary": "secondary", "On Secondary": "onSecondary",
    "Secondary Container": "secondaryContainer",
    "On Secondary Container": "onSecondaryContainer",
    "Tertiary": "tertiary", "On Tertiary": "onTertiary",
    "Tertiary Container": "tertiaryContainer",
    "On Tertiary Container": "onTertiaryContainer",
    "Error": "error", "On Error": "onError",
    "On Error Container": "onErrorContainer",
    "Background": "background", "On Background": "onBackground",
    "Surface": "surface", "On Surface": "onSurface",
    "Surface Variant": "surfaceVariant",
    "On Surface Variant": "onSurfaceVariant",
    "Outline": "outline", "Outline Variant": "outlineVariant",
    "Inverse Surface": "inverseSurface",
    "Inverse On Surface": "inverseOnSurface",
    "Surface Container Low": "surfaceContainerLow",
    "Surface Container": "surfaceContainer",
    "Surface Container High": "surfaceContainerHigh",
    "Surface Container Highest": "surfaceContainerHighest",
}

# Slots regenerated because the spreadsheet values are wrong (see
# docs/palette-corrections.md).
CORRECTED = ["Surface Container", "Surface Container High",
             "Surface Container Highest"]

# Published M3 baseline dark scheme: the dark partner of the base theme's colours.
# Every value was checked to sit on the expected Material tone (80, 20, 30, 90...).
BASE_DARK = {
    "Primary": "#D0BCFF", "On Primary": "#381E72",
    "Primary Container": "#4F378B", "On Primary Container": "#EADDFF",
    "Secondary": "#CCC2DC", "On Secondary": "#332D41",
    "Secondary Container": "#4A4458", "On Secondary Container": "#E8DEF8",
    "Tertiary": "#EFB8C8", "On Tertiary": "#492532",
    "Tertiary Container": "#633B48", "On Tertiary Container": "#FFD8E4",
    "Error": "#F2B8B5", "On Error": "#601410", "On Error Container": "#F9DEDC",
    "Background": "#141218", "On Background": "#E6E0E9",
    "Surface": "#141218", "On Surface": "#E6E0E9",
    "Surface Variant": "#49454F", "On Surface Variant": "#CAC4D0",
    "Outline": "#938F99", "Outline Variant": "#49454F",
    "Inverse Surface": "#E6E0E9", "Inverse On Surface": "#322F35",
    "Surface Container Low": "#1D1B20", "Surface Container": "#211F26",
    "Surface Container High": "#2B2930", "Surface Container Highest": "#36343B",
}


def rgb(hexcolor):
    h = hexcolor.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgba(hexcolor, alpha):
    r, g, b = rgb(hexcolor)
    return f"rgba({r}, {g}, {b}, {alpha})"


def slug(name):
    return "--anvil-m3-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def derived(c, mode):
    """The overlay and disabled slots, computed from the main colours."""
    d = {
        "On Disabled": rgba(c["On Surface"], 0.38),
        "Disabled Container": rgba(c["On Surface"], 0.12),
        "Disabled Container 2": rgba(c["On Surface"], 0.04),
        "Primary Overlay 1": rgba(c["Primary"], 0.05),
        "Primary Overlay 2": rgba(c["Primary"], 0.08),
        "Primary Overlay 3": rgba(c["Primary"], 0.12),
        "Error Overlay 1": rgba(c["Error"], 0.08),
        "Error Overlay 2": rgba(c["Error"], 0.12),
        "On Surface Variant Overlay 1": rgba(c["On Surface Variant"], 0.08),
        "On Surface Variant Overlay 2": rgba(c["On Surface Variant"], 0.12),
        "Inverse On Surface Overlay 1": rgba(c["Inverse On Surface"], 0.08),
        "Inverse On Surface Overlay 2": rgba(c["Inverse On Surface"], 0.12),
    }
    if mode == "light":
        light, dark = "255, 255, 255", "0, 0, 0"
    else:
        # Dark mode swaps the roles: the "light" overlay sits on the (now light)
        # primary colour, so it is dark; the "dark" overlay sits on dark surfaces.
        light = ", ".join(map(str, rgb(c["On Primary"])))
        dark = ", ".join(map(str, rgb(c["On Secondary Container"])))
    d["Light Overlay 1"] = f"rgba({light}, 0.08)"
    d["Light Overlay 2"] = f"rgba({light}, 0.12)"
    d["Dark Overlay 1"] = f"rgba({dark}, 0.08)"
    d["Dark Overlay 2"] = f"rgba({dark}, 0.12)"
    d["Dark Overlay 3"] = f"rgba({dark}, 0.16)"
    return d


def generate(hue, dark):
    scheme = SchemeTonalSpot(Hct.from_hct(hue, 48, 50), dark, 0.0,
                             spec_version="2021")
    return {name: "#%06X" % (getattr(M, key).get_hct(scheme).to_int() & 0xFFFFFF)
            for name, key in LIB.items()}


def read_sheet(path):
    sheet = openpyxl.load_workbook(path).worksheets[0]
    header = [c.value for c in sheet[1]]
    names = header[2:6]
    slots, order = {n: {} for n in names}, []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        slot = re.split(r":| --", row[1])[0].strip()
        order.append(slot)
        for n, value in zip(names, row[2:6]):
            slots[n][slot] = value.strip()
    return names, slots, order


def build(path):
    names, sheet, order = read_sheet(path)
    assert set(names) == set(KEY_HUES), names
    schemes, report = {}, []
    for name in names:
        light_gen, dark_gen = generate(KEY_HUES[name], False), generate(
            KEY_HUES[name], True)
        light = {s: v.upper() if v.startswith("#") else v
                 for s, v in sheet[name].items()}
        for slot in CORRECTED:
            report.append((name, slot, light[slot], light_gen[slot]))
            light[slot] = light_gen[slot]
        main = {s: light[s] for s in LIB}
        # Integrity check: the formulas reproduce the spreadsheet's own overlay
        # slots, except Primary Overlay 3 (sheet 0.11, M3 state layer is 0.12).
        for slot, value in derived(main, "light").items():
            if slot != "Primary Overlay 3" and light.get(slot) != value:
                raise SystemExit(f"{name}: {slot} sheet {light.get(slot)} != {value}")
        light.update(derived(main, "light"))
        dark = {s: dark_gen[s] for s in LIB}
        dark.update(derived(dark, "dark"))
        schemes[name] = (light, dark)
    base_dark = dict(BASE_DARK)
    base_dark.update(derived(base_dark, "dark"))
    return order, schemes, base_dark, report


def block(selector, colours, order, indent=""):
    lines = [f"{indent}{selector} {{"]
    for slot in order + ["On Background"]:
        if slot in colours and not (slot == "On Background" and order.count(slot)):
            lines.append(f"{indent}  {slug(slot)}: {colours[slot]};")
    if "On Background" in order:
        lines.append(f"{indent}  {slug('On Background')}: {colours['On Background']};")
    lines.append(f"{indent}}}")
    return "\n".join(lines)


def emit(order, schemes, base_dark):
    out = ["/* Generated by tools/build_palettes.py in m3-custom-theme-project-library.",
           "   Do not edit by hand. Source: docs/Anvil-M3 color mapping 4 palette.xlsx.",
           "   Choose a palette with data-m3x-palette on the html element, and a mode",
           "   with data-m3x-theme (light, dark or system). No attribute = the base",
           "   theme's own light colours. See m3-custom-theme.md, Step 4. */", ""]
    # Dark values are written twice (explicit dark, and "system" under the media
    # query) so that both selectors win over the palette's light block.
    out.append("/* Base colours, dark */")
    sel_none = ":root:not([data-m3x-palette])"
    out.append(block(f'{sel_none}[data-m3x-theme="dark"]', base_dark, order))
    out.append("@media (prefers-color-scheme: dark) {")
    out.append(block(f'{sel_none}[data-m3x-theme="system"]', base_dark, order, "  "))
    out.append("}\n")
    for name, (light, dark) in schemes.items():
        p = f'[data-m3x-palette="{name}"]'
        out.append(f"/* Palette: {name} */")
        out.append(block(f":root{p}", light, order))
        out.append(block(f':root{p}[data-m3x-theme="dark"]', dark, order))
        out.append("@media (prefers-color-scheme: dark) {")
        out.append(block(f':root{p}[data-m3x-theme="system"]', dark, order, "  "))
        out.append("}\n")
    out.append("/* Native form controls and scrollbars follow the mode */")
    out.append(':root[data-m3x-theme="dark"] { color-scheme: dark; }')
    out.append("@media (prefers-color-scheme: dark) {\n"
               '  :root[data-m3x-theme="system"] { color-scheme: dark; }\n}')
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    order, schemes, base_dark, report = build(sys.argv[1])
    with open(sys.argv[2], "w", newline="\n") as f:
        f.write(emit(order, schemes, base_dark))
    print(f"wrote {sys.argv[2]}")
    print("Corrections (palette, slot, spreadsheet value, value used):")
    for row in report:
        print("  ", *row)
