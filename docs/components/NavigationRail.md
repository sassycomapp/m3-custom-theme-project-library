# NavigationRailLayout (M3 Expressive rail)

Base layout `m3.NavigationRailLayout`, extended by m3x with the properties `rail_style` and `rail_expanded`. CSS `theme/assets/m3x/navigation-rail.css`, tokens `--m3x-rail-*` in `theme/assets/m3x/tokens.css`. Gap E5. The base edits are listed in `docs/upstream-edits.md`.

## 1. What it is

M3 Expressive replaces the 80 px navigation rail with a 96 px rail that has a menu button at the top. The menu button expands the rail to 220 px, where each destination shows its icon and full label side by side; it takes the place of a standard navigation drawer on larger windows. With the default value (`rail_style` standard) the layout keeps the base rail. Phone widths (under 600 px) keep the base behaviour in both styles: the rail becomes a bottom app bar or a modal drawer, as `navigation_rail_collapse_to` says.

## 2. Anatomy (M3 specification)

| Part | Value |
|---|---|
| Collapsed rail | 96 px wide, Surface, no elevation; menu button 16 px from the top, 48 px touch target, centred; destinations 20 px below it, 4 px apart |
| Collapsed destination | Icon (24 px) in a 56 x 32 px fully rounded active indicator, label below 4 px apart, Label medium |
| Expanded rail | 220 px wide, Surface, no elevation; the page content moves over to match |
| Expanded destination | Icon and label 8 px apart in one 56 px high fully rounded indicator, 16 px from each side of the rail, Label large; long labels end with an ellipsis; a badge count sits at the end |
| Colours | Active indicator Secondary Container with an On Secondary Container icon; active label Secondary (collapsed) or On Secondary Container (expanded); inactive icons and labels On Surface Variant |
| Motion | Width changes in 300 ms (emphasized); no motion when the device asks for reduced motion |

Sources: Jetpack Compose `NavigationRailCollapsedTokens`, `NavigationRailExpandedTokens`, `NavigationRailVerticalItemTokens`, `NavigationRailHorizontalItemTokens`, `NavigationRailBaselineItemTokens` and `NavigationRailColorTokens`, and the M3 navigation rail specification.

## 3. How it works

- The menu button switches `rail_expanded`. Its icon is `menu` while collapsed and `menu_open` while expanded; it carries `aria-expanded` and the label "Expand navigation" or "Collapse navigation".
- The expanded rail is a standard rail: it pushes the page content over rather than covering it. With the side sheet open, the content narrows by the rail's width and the side sheet's.
- `navigation_rail_vertical_align` still places the destinations at the top, centre or bottom; the menu button stays at the top.
- The destinations are the base NavigationLink components; nothing changes for them.

## 4. API (added properties)

| Name | Type | Default | Meaning |
|---|---|---|---|
| `rail_style` | enum | `'standard'` | `standard` (the base 80 px rail) or `expressive`. |
| `rail_expanded` | boolean | `False` | True: an expressive rail is expanded. The menu button switches it. |
| `rail_adaptive` | boolean | `False` | True: an expressive rail expands by itself on large and extra-large windows (1200 px and wider) and collapses on smaller ones (Step 9). The menu button still switches it until the window changes size class. |
