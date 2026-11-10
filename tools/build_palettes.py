#!/usr/bin/env python3
"""Build the colour files of the M3 custom theme.

Every palette except default is the Material 3 Content scheme of its source
colour (Material colour specification 2021, standard contrast). The Content
scheme keeps the source colour as Primary Container and gives Secondary and
Tertiary strong colour of their own, so the palettes stay vivid. Material's
contrast rules set every light and dark colour, and the build stops if any
text or control colour falls below the WCAG AA minimum on any background.
The default palette keeps the base theme's own colours.

Writes three files into the app repo. All three are generated and are never
edited by hand. To change a colour, change SOURCE below and rebuild.

    theme/assets/m3x/palettes.css       the colours of every palette, light and dark
    theme/parameters.yaml               Anvil's colour list and colour presets
    client_code/_utils/m3x_presets.py   which Anvil preset belongs to which palette

Usage (from the project library repo folder):
    python tools/build_palettes.py ../m3-custom-theme

Needs: pip install materialyoucolor
"""

import re
import sys
from pathlib import Path

from materialyoucolor.dynamiccolor.material_dynamic_colors import (
    MaterialDynamicColors as M,
)
from materialyoucolor.hct import Hct
from materialyoucolor.dynamiccolor.dynamic_scheme import DynamicScheme
from materialyoucolor.dynamiccolor.variant import Variant
from materialyoucolor.palettes.tonal_palette import TonalPalette

# Source colours of each palette (primary, secondary, tertiary), in the order
# the palettes are offered. Each source colour sets the hue and strength of its
# colour family. The primary source colour is used as is for Primary Container.
SOURCE = {
    "professional_blue": ("#0F0FFA", "#2F6BFF", "#B5179E"),
    "warm_coral": ("#FF5722", "#E8505B", "#00A6A6"),
    "calm_teal": ("#00807B", "#0097C4", "#F0647A"),
    "sophisticated_purple": ("#9A33DF", "#6A4CFF", "#E0338F"),
    "sky_blue": ("#0072B1", "#00A0B0", "#8A5CFF"),
    "forest_green": ("#007F15", "#00A37A", "#2D7DFF"),
    "desert_rose": ("#C83B76", "#A23CB4", "#E8641E"),
}

# The palette and mode an app starts with: the colours Anvil's Theme editor holds.
START = ("professional_blue", "light")

# Anvil colour name -> Material colour role.
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

# M3 colour roles the base theme does not hold. They are
# generated for every palette and reach the CSS as --m3x-color-* variables.
EXTRA = {
    "Error Container": "errorContainer",
    "Inverse Primary": "inversePrimary",
    "Surface Tint": "surfaceTint",
    "Surface Dim": "surfaceDim",
    "Surface Bright": "surfaceBright",
    "Surface Container Lowest": "surfaceContainerLowest",
    "Scrim": "scrim",
    "Shadow": "shadow",
    "Primary Fixed": "primaryFixed",
    "Primary Fixed Dim": "primaryFixedDim",
    "On Primary Fixed": "onPrimaryFixed",
    "On Primary Fixed Variant": "onPrimaryFixedVariant",
    "Secondary Fixed": "secondaryFixed",
    "Secondary Fixed Dim": "secondaryFixedDim",
    "On Secondary Fixed": "onSecondaryFixed",
    "On Secondary Fixed Variant": "onSecondaryFixedVariant",
    "Tertiary Fixed": "tertiaryFixed",
    "Tertiary Fixed Dim": "tertiaryFixedDim",
    "On Tertiary Fixed": "onTertiaryFixed",
    "On Tertiary Fixed Variant": "onTertiaryFixedVariant",
}

# The base theme's own light colours, exactly as in Anvil's M3 theme v1.2.6
# (tag base-v1.2.6, theme/parameters.yaml). The default palette keeps them, so
# an app on the default palette looks exactly like the base theme.
BASE_LIGHT = {
    "Primary": "#6750A4", "Primary Container": "#EADDFF",
    "On Primary": "#FFFFFF", "On Primary Container": "#21005E",
    "Secondary": "#625B71", "Secondary Container": "#E8DEF8",
    "On Secondary": "#FFFFFF", "On Secondary Container": "#1D192B",
    "Tertiary": "#7D5260", "Tertiary Container": "#FFD8E4",
    "On Tertiary": "#FFFFFF", "On Tertiary Container": "#370B1E",
    "Error": "#B3261E", "Background": "#FFFBFE", "Surface": "#FFFBFE",
    "On Background": "#1C1B1F", "On Surface": "#1C1B1F",
    "Surface Variant": "#E7E0EC", "On Surface Variant": "#49454E",
    "Outline": "#79747E",
    "On Disabled": "rgba(29, 27, 32, 0.38)",
    "Disabled Container": "rgba(29, 27, 32, 0.12)",
    "Light Overlay 1": "rgba(255, 255, 255, 0.08)",
    "Light Overlay 2": "rgba(255, 255, 255, 0.12)",
    "Dark Overlay 1": "rgba(29, 25, 43, 0.08)",
    "Dark Overlay 2": "rgba(29, 25, 43, 0.12)",
    "Primary Overlay 1": "rgba(103, 80, 164, 0.05)",
    "Primary Overlay 2": "rgba(103, 80, 164, 0.08)",
    "Primary Overlay 3": "rgba(103, 80, 164, 0.12)",
    "Outline Variant": "#C4C7C5", "On Error": "#FFFFFF",
    "Surface Container Low": "#F7F2FA", "Surface Container High": "#ECE6F0",
    "Surface Container Highest": "#E6E0E9",
    "Disabled Container 2": "rgba(29, 27, 32, 0.04)",
    "Error Overlay 1": "rgba(179, 38, 30, 0.08)",
    "Error Overlay 2": "rgba(179, 38, 30, 0.12)",
    "Dark Overlay 3": "rgba(29, 25, 43, 0.16)",
    "On Error Container": "#410E0B", "Surface Container": "#F3EDF7",
    "Inverse Surface": "#322F35", "Inverse On Surface": "#F5EFF7",
    "On Surface Variant Overlay 1": "rgba(73,69,79, 0.08)",
    "On Surface Variant Overlay 2": "rgba(73,69,79, 0.12)",
    "Inverse On Surface Overlay 1": "rgba(245,239,247, 0.08)",
    "Inverse On Surface Overlay 2": "rgba(245,239,247, 0.12)",
}

# Anvil's colour list order: the base theme's order, then the extra roles.
ORDER = list(BASE_LIGHT) + list(EXTRA)

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

# The extra roles of the M3 baseline scheme, from Jetpack Compose Material 3
# (androidx-main, compose/material3/.../tokens/ColorLightTokens.kt and
# ColorDarkTokens.kt). Shadow is black in both modes, as the M3 specification sets.
BASE_EXTRA_LIGHT = {
    "Error Container": "#F9DEDC", "Inverse Primary": "#D0BCFF",
    "Surface Tint": "#6750A4", "Surface Dim": "#DED8E1",
    "Surface Bright": "#FEF7FF", "Surface Container Lowest": "#FFFFFF",
    "Scrim": "#000000", "Shadow": "#000000",
    "Primary Fixed": "#EADDFF", "Primary Fixed Dim": "#D0BCFF",
    "On Primary Fixed": "#21005D", "On Primary Fixed Variant": "#4F378B",
    "Secondary Fixed": "#E8DEF8", "Secondary Fixed Dim": "#CCC2DC",
    "On Secondary Fixed": "#1D192B", "On Secondary Fixed Variant": "#4A4458",
    "Tertiary Fixed": "#FFD8E4", "Tertiary Fixed Dim": "#EFB8C8",
    "On Tertiary Fixed": "#31111D", "On Tertiary Fixed Variant": "#633B48",
}
BASE_EXTRA_DARK = dict(
    BASE_EXTRA_LIGHT,
    **{"Error Container": "#8C1D18", "Inverse Primary": "#6750A4",
       "Surface Tint": "#D0BCFF", "Surface Dim": "#141218",
       "Surface Bright": "#3B383E", "Surface Container Lowest": "#0F0D13"},
)


def rgb(hexcolor):
    h = hexcolor.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgba(hexcolor, alpha):
    r, g, b = rgb(hexcolor)
    return f"rgba({r}, {g}, {b}, {alpha})"


def css_name(slot):
    """The CSS variable of a slot: --anvil-m3-* for base slots, --m3x-color-* for
    the extra roles."""
    prefix = "--m3x-color-" if slot in EXTRA else "--anvil-m3-"
    return prefix + re.sub(r"[^a-z0-9]+", "-", slot.lower()).strip("-")


def title(palette, mode):
    return f"{palette.replace('_', ' ').title()} {mode.title()}"


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


def hct(hexcolor):
    return Hct.from_int(0xFF000000 | int(hexcolor.lstrip("#"), 16))


def generate(sources, dark):
    """The Material colours of a palette in one mode: the Content scheme of the
    primary source colour, with the secondary and tertiary families taken from
    their own source colours."""
    primary, secondary, tertiary = (hct(c) for c in sources)
    scheme = DynamicScheme(
        primary, Variant.CONTENT, 0.0, dark, spec_version="2021",
        primary_palette=TonalPalette.from_hct(primary),
        secondary_palette=TonalPalette.from_hct(secondary),
        tertiary_palette=TonalPalette.from_hct(tertiary))
    return {name: "#%06X" % (getattr(M, role).get_hct(scheme).to_int() & 0xFFFFFF)
            for name, role in dict(LIB, **EXTRA).items()}


def luminance(hexcolor):
    channels = []
    for v in rgb(hexcolor):
        v /= 255
        channels.append(v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)))
    return (lb + 0.05) / (la + 0.05)


SURFACES = ["Background", "Surface", "Surface Bright", "Surface Dim",
            "Surface Container Lowest", "Surface Container Low",
            "Surface Container", "Surface Container High",
            "Surface Container Highest"]


def contrast_pairs():
    """(background, foreground, minimum): WCAG AA, 4.5 for text, 3 for outlines."""
    pairs = []
    for role in ("Primary", "Secondary", "Tertiary", "Error"):
        pairs.append((role, "On " + role, 4.5))
        pairs.append((role + " Container", "On " + role + " Container", 4.5))
        pairs += [(s, role, 4.5) for s in SURFACES]
        if role != "Error":
            fixed = role + " Fixed"
            pairs += [(fixed, "On " + fixed, 4.5),
                      (fixed, "On " + fixed + " Variant", 4.5),
                      (fixed + " Dim", "On " + fixed, 4.5)]
    for s in SURFACES:
        pairs += [(s, "On Surface", 4.5), (s, "On Surface Variant", 4.5),
                  (s, "Outline", 3.0)]
    pairs += [("Background", "On Background", 4.5),
              ("Surface Variant", "On Surface Variant", 4.5),
              ("Inverse Surface", "Inverse On Surface", 4.5),
              ("Inverse Surface", "Inverse Primary", 4.5)]
    return pairs


def check(name, mode, colours):
    for back, fore, minimum in contrast_pairs():
        ratio = contrast(colours[back], colours[fore])
        if ratio < minimum:
            raise SystemExit(f"{name} {mode}: {fore} on {back} is {ratio:.2f}:1, "
                             f"below {minimum}:1")


def build():
    """Return {palette: {"light": colours, "dark": colours}}."""
    base_dark = dict(BASE_DARK)
    base_dark.update(derived(base_dark, "dark"))
    schemes = {"default": {"light": dict(BASE_LIGHT, **BASE_EXTRA_LIGHT),
                           "dark": dict(base_dark, **BASE_EXTRA_DARK)}}
    for name, sources in SOURCE.items():
        schemes[name] = {}
        for mode in ("light", "dark"):
            colours = generate(sources, mode == "dark")
            check(name, mode, colours)
            colours.update(derived(colours, mode))
            schemes[name][mode] = colours
    for name, modes in schemes.items():
        for mode, colours in modes.items():
            missing = set(ORDER) - set(colours)
            if missing:
                raise SystemExit(f"{name} {mode}: missing {sorted(missing)}")
    return schemes


def block(selector, colours, indent=""):
    lines = [f"{indent}{selector} {{"]
    lines += [f"{indent}  {css_name(s)}: {colours[s]};" for s in ORDER]
    lines.append(f"{indent}}}")
    return "\n".join(lines)


def emit_css(schemes):
    out = ["/* Generated by tools/build_palettes.py in m3-custom-theme-project-library.",
           "   Do not edit by hand.",
           "   Choose a palette with data-m3x-palette on the html element, and a mode",
           "   with data-m3x-theme (light, dark or system). With no palette attribute,",
           "   the colours are the Anvil colour preset chosen in the Theme editor.",
           "   See m3-custom-theme.md, Step 4. */", ""]
    # Dark values are written twice (explicit dark, and "system" under the media
    # query) so that both selectors win over the palette's light block.
    for name, modes in schemes.items():
        p = f'[data-m3x-palette="{name}"]'
        out.append(f"/* Palette: {name} */")
        out.append(block(f":root{p}", modes["light"]))
        out.append(block(f':root{p}[data-m3x-theme="dark"]', modes["dark"]))
        out.append("@media (prefers-color-scheme: dark) {")
        out.append(block(f':root{p}[data-m3x-theme="system"]', modes["dark"], "  "))
        out.append("}\n")
    out.append("/* Native form controls and scrollbars follow the mode */")
    out.append(':root[data-m3x-theme="dark"] { color-scheme: dark; }')
    out.append("@media (prefers-color-scheme: dark) {\n"
               '  :root[data-m3x-theme="system"] { color-scheme: dark; }\n}')
    return "\n".join(out) + "\n"


def yaml_colours(colours, indent):
    return [f"{indent}- {{color: '{colours[s]}', name: {s}}}" for s in ORDER]


def emit_parameters(schemes, old_text):
    """Replace the color_scheme section of parameters.yaml. The rest is kept."""
    roles_at = old_text.index("\nroles:")
    lines = ["color_scheme:", "  colors:"]
    lines += yaml_colours(schemes[START[0]][START[1]], "  ")
    lines += ["  preset_groups:", "  - name: Colour Scheme", "    options:"]
    for name, modes in schemes.items():
        for mode in ("light", "dark"):
            lines.append("    - colors:")
            lines += yaml_colours(modes[mode], "      ")
            lines.append(f"      name: {title(name, mode)}")
    return "\n".join(lines) + old_text[roles_at:]


def emit_presets(schemes):
    keys = {}
    for name, modes in schemes.items():
        for mode in ("light", "dark"):
            primary = modes[mode]["Primary"].upper()
            if primary in keys:
                raise SystemExit(f"Primary {primary} is not unique")
            keys[primary] = (name, mode)
    rows = "\n".join(f'    "{k}": ("{n}", "{m}"),' for k, (n, m) in keys.items())
    return (
        '"""Which Anvil colour preset belongs to which palette and mode.\n\n'
        "Generated by tools/build_palettes.py in m3-custom-theme-project-library.\n"
        "Do not edit by hand. Each preset is recognised by its Primary colour.\n"
        '"""\n\n'
        "PALETTES = (\n" + "".join(f'    "{n}",\n' for n in schemes) + ")\n\n"
        "BY_PRIMARY = {\n" + rows + "\n}\n"
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    app = Path(sys.argv[1])
    schemes = build()
    css = app / "theme/assets/m3x/palettes.css"
    params = app / "theme/parameters.yaml"
    presets = app / "client_code/_utils/m3x_presets.py"
    params_text = params.read_text()
    with open(css, "w", newline="\n") as f:
        f.write(emit_css(schemes))
    with open(params, "w", newline="\n") as f:
        f.write(emit_parameters(schemes, params_text))
    with open(presets, "w", newline="\n") as f:
        f.write(emit_presets(schemes))
    for path in (css, params, presets):
        print(f"wrote {path}")
