# NavigationBar

Component `m3.NavigationBar` (`client_code/_Components/NavigationBar/`), CSS `theme/assets/m3x/navigation-bar.css`, tokens `--m3x-navigation-bar-*` in `theme/assets/m3x/tokens.css`. Gap C8.

## 1. What it is

A navigation bar sits at the bottom of the screen on phones and lets the user move between the three to five main destinations of an app, such as "Home", "Messages" and "Profile". Each destination has an icon and a label. On wider screens, the navigation rail of `NavigationRailLayout` does the same job at the side.

## 2. Anatomy (M3 Expressive specification)

| Part | Value |
|---|---|
| Container | Surface Container, 64 px high, the full width of the screen |
| Destination | Icon above label, 4 px between them, sharing the width equally |
| Icon | 24 px. Selected: On Secondary Container. Not selected: On Surface Variant |
| Active indicator | A 56 × 32 px pill behind the icon, fully rounded, Secondary Container |
| Label | Label medium. Selected: Secondary. Not selected: On Surface Variant |
| Badge | A `m3x-badge` at the top right of the icon: a dot, or a count up to 999+ |
| States | Hover, focus and pressed layers on the active indicator. Focus ring: 3 px Secondary around the indicator |

Sources: Jetpack Compose `NavigationBarTokens` and `NavigationBarVerticalItemTokens` (v0_11_0), and the M3 navigation bar specification.

## 3. How it works

- The navigation bar shows the destinations. The app shows the selected destination, normally by opening a form or showing a panel in the `change` event.
- The selected destination carries `aria-current="page"` for screen readers, and a destination with a badge describes the badge (for example "3 new").
- With `fixed` set to `True`, the bar is fixed to the bottom edge of the window, above the page content. The page then needs 64 px of space at its bottom, so the bar does not cover the last content.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `items` | text[] | `Home`, `Search`, `Profile` | The label of each destination. |
| `icons` | text[] | `mi:home`, `mi:search`, `mi:person` | One `mi:` icon per destination, in the same order. |
| `badges` | list | `None` | One badge per destination: `None` for no badge, `0` for a dot, a number for a count. |
| `selected_index` | number | `0` | The selected destination, counting from 0. |
| `selected_text` | string (read only) | | The label of the selected destination. |
| `fixed` | boolean | `False` | Fixed to the bottom edge of the window. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Events: `change` (default), `show`, `hide`.
