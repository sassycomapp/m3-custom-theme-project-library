# FloatingActionButton

Component `m3.FloatingActionButton` (`client_code/_Components/FloatingActionButton/`), CSS `theme/assets/m3x/fab.css`, tokens `--m3x-fab-*` in `theme/assets/m3x/tokens.css`.

## 1. What it is

A floating action button (FAB) holds the most important action on a screen, such as "Compose" or "Create". It is a large, raised button with an icon. An extended FAB also shows a label. A screen has at most one FAB.

## 2. Anatomy (M3 Expressive specification)

| Part | Regular | Medium | Large |
|---|---|---|---|
| Size | 56 px | 80 px | 96 px |
| Corner | Large (16 px) | Large increased (20 px) | Extra large (28 px) |
| Icon | 24 px | 28 px | 36 px |
| Extended FAB padding at each end | 16 px | 26 px | 28 px |
| Space between icon and label | 8 px | 12 px | 16 px |
| Label | Title medium | Title large | Headline small |

| Part | Value |
|---|---|
| Colours (tonal) | Primary Container, Secondary Container or Tertiary Container, with the matching On colour for the icon and label |
| Colours (filled) | Primary, Secondary or Tertiary, with the matching On colour |
| Elevation | Level 3; level 4 on hover |
| States | Hover, focus and pressed layers in the content colour. Focus ring: 3 px Secondary, 2 px outside |
| Floating position | 16 px from the bottom and right edges of the window |

Sources: Jetpack Compose `FabBaselineTokens`, `FabMediumTokens`, `FabLargeTokens`, `ExtendedFabSmallTokens`, `ExtendedFabMediumTokens`, `ExtendedFabLargeTokens`, `FabPrimaryContainerTokens` (v0_14_0) and the Compose `FloatingActionButton` layout. The large icon is 36 px, the size Compose uses.

## 3. How it works

- Setting `text` turns the FAB into an extended FAB.
- With `floating` set to `True`, the FAB is fixed in the bottom right corner of the window, above the page content, and stays there when the page scrolls. Otherwise it sits in line in its container.
- The FAB has a 16 px outer margin, because its level 4 shadow reaches further outside the button than the standard outer margin holds (rule 5.5).
- The `tooltip` is also the button's name for screen readers. An icon-only FAB needs one.
- M3 defines no disabled FAB. Anvil components can be disabled, so a disabled FAB takes the standard disabled colours and raises no events.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `icon` | icon | `mi:add` | The icon. |
| `text` | string | `''` | The label. A label makes an extended FAB. |
| `size` | enum | `regular` | `regular`, `medium` or `large`. |
| `appearance` | enum | `primary_container` | `primary_container`, `secondary_container`, `tertiary_container`, `primary`, `secondary`, `tertiary`. |
| `floating` | boolean | `False` | Fixed in the bottom right corner of the window. |
| `tooltip` | string | `''` | Hover text and screen-reader name. |
| `enabled` | boolean | `True` | Standard. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Events: `click` (default), `show`, `hide`.
