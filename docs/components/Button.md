# Button (M3 Expressive)

Base component `m3.Button`, extended by m3x with the properties `size`, `shape`, `toggle` and `selected`. CSS `theme/assets/m3x/button-expressive.css`. Gap E1. The base edits are listed in `docs/upstream-edits.md`.

## 1. What it is

M3 Expressive gives buttons five sizes, a choice of round or square shape, a shape change when pressed, and toggle buttons that stay selected. With the default values (`size` standard, `shape` round, `toggle` False) the button is the base button, unchanged.

## 2. Anatomy (M3 specification)

| Size | Height | Padding at each side | Icon | Icon to label | Square corner | Pressed corner | Outline | Label |
|---|---|---|---|---|---|---|---|---|
| xsmall | 32 px | 16 px | 20 px | 8 px | 12 px | 8 px | 1 px | Label large |
| small | 40 px | 16 px | 20 px | 8 px | 12 px | 8 px | 1 px | Label large |
| medium | 56 px | 24 px | 24 px | 8 px | 16 px | 12 px | 1 px | Title medium |
| large | 96 px | 48 px | 32 px | 12 px | 28 px | 16 px | 2 px | Headline small |
| xlarge | 136 px | 64 px | 40 px | 16 px | 28 px | 16 px | 3 px | Headline large |

- Round buttons have fully rounded ends; square buttons have the square corner above. A pressed button takes the pressed corner. Shapes change in 200 ms (emphasized).
- Sized outlined buttons use Outline Variant for the outline.
- Toggle colours, unselected then selected: filled Surface Container with On Surface Variant, then Primary with On Primary; tonal Secondary Container, then Secondary with On Secondary; elevated Surface Container Low with Primary, then Primary with On Primary; outlined an Outline Variant outline with On Surface Variant, then Inverse Surface with Inverse On Surface. Text buttons have no toggle.
- A selected toggle button switches shape: round becomes square, square becomes round.

Sources: Jetpack Compose `ButtonXSmallTokens`, `ButtonSmallTokens`, `ButtonMediumTokens`, `ButtonLargeTokens`, `ButtonXLargeTokens`, `FilledButtonTokens`, `TonalButtonTokens`, `OutlinedButtonTokens` and `ToggleButton`, and the M3 buttons specification.

## 3. How it works

- `size` adds the size classes to the button; `shape` square adds the square class.
- With `toggle` True, a click switches `selected` before the `click` event is raised, so a handler reads the new value. The button carries `aria-pressed`.
- A `font_size` or `icon_size` set on the button still wins over the size's values.

## 4. API (added properties)

| Name | Type | Default | Meaning |
|---|---|---|---|
| `size` | enum | `'standard'` | `standard` (the base button), `xsmall`, `small`, `medium`, `large` or `xlarge`. |
| `shape` | enum | `'round'` | `round` or `square`. |
| `toggle` | boolean | `False` | True: a click switches `selected`. |
| `selected` | boolean | `False` | True: a toggle button is shown as selected. |
