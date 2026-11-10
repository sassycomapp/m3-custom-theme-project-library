# ButtonGroup

Component `m3.ButtonGroup` (`client_code/_Components/ButtonGroup/`), CSS `theme/assets/m3x/button-group.css`, tokens `--m3x-button-group-*` in `theme/assets/m3x/tokens.css`.

## 1. What it is

A button group is a row of related buttons. M3 Expressive defines two types:

- **Connected**: the buttons are joined into one bar, for choosing between options, such as "Day", "Week" or "Month". It replaces the M3 segmented button.
- **Standard**: the buttons stand apart, for a set of related actions, such as "Share", "Save" and "Print".

The buttons can be plain actions, or toggle buttons where one button (single selection) or any number of buttons (multiple selection) are selected.

## 2. Anatomy (M3 Expressive specification)

| Part | Value |
|---|---|
| Buttons | 40 px high, 16 px padding at each end, label Label large, optional 20 px icon 8 px before the label |
| Connected group | 2 px between buttons. The outer corners of the first and last buttons are full; the inner corners are small (8 px). A selected button becomes fully round |
| Standard group | 12 px between buttons, every button fully round |
| Filled colours | Unselected Surface Container with On Surface Variant; selected Primary with On Primary |
| Tonal colours | Unselected Secondary Container with On Secondary Container; selected Secondary with On Secondary |
| Outlined colours | Unselected no fill, 1 px Outline Variant outline, On Surface Variant; selected Inverse Surface with Inverse On Surface |
| States | Hover, focus and pressed layers in the content colour. Focus ring: 3 px Secondary, 2 px outside |
| Disabled | Containers and outlines On Surface at 12 %, content On Surface at 38 % |
| Motion | The corner change of a newly selected button follows the emphasised easing, medium 1 duration |

Sources: Jetpack Compose `ButtonGroupSmallTokens` (v0_11_0), `ConnectedButtonGroupSmallTokens` (14_1_0), `ButtonSmallTokens` (v0_11_0), `FilledButtonTokens`, `TonalButtonTokens` and `OutlinedButtonTokens`, and the M3 button groups specification. The buttons use the small button size (40 px).

## 3. How it works

- The group is built from its `items` (and optional `icons`), one button each.
- With `single` selection, exactly one button is selected: clicking another button selects it and raises `change`. With `multiple` selection, each click switches that button and raises `change`. With `none`, no button is selected and the buttons are actions.
- Every click raises `click` with an `index` argument, the position of the clicked button.
- Selected buttons carry `aria-pressed="true"` for screen readers.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `items` | text[] | `Day`, `Week`, `Month` | The label of each button. |
| `icons` | text[] | empty | Optional `mi:` icons, one per button, in the same order. |
| `type` | enum | `connected` | `connected` or `standard`. |
| `selection` | enum | `single` | `none`, `single` or `multiple`. |
| `selected_index` | number | first button | The selected button (single selection), counting from 0. |
| `selected_indices` | list | `[]` | All selected buttons (multiple selection). |
| `appearance` | enum | `filled` | `filled`, `tonal` or `outlined`. |
| `full_width` | boolean | `False` | The group fills its container and the buttons share the width. |
| `enabled` | boolean | `True` | Standard. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Events: `change` (default), `click` (with `index`), `show`, `hide`.
