# IconButton and ToggleIconButton (M3 Expressive)

Base components `m3.IconButton` and `m3.ToggleIconButton`, extended by m3x with the properties `size`, `button_width` and `shape`. CSS `theme/assets/m3x/iconbutton-expressive.css`. Gap E2. The base edits are listed in `docs/upstream-edits.md`.

## 1. What it is

M3 Expressive gives icon buttons five sizes, three widths, a choice of round or square shape, a shape change when pressed, and a shape change when a toggle icon button is selected. With the default values (`size` standard, `button_width` default, `shape` round) the icon button is the base icon button, unchanged.

## 2. Anatomy (M3 specification)

| Size | Height | Icon | Space beside the icon: narrow / default / wide | Square corner | Pressed corner | Outline |
|---|---|---|---|---|---|---|
| xsmall | 32 px | 20 px | 4 / 6 / 10 px | 12 px | 8 px | 1 px |
| small | 40 px | 24 px | 4 / 8 / 14 px | 12 px | 8 px | 1 px |
| medium | 56 px | 24 px | 12 / 16 / 24 px | 16 px | 12 px | 1 px |
| large | 96 px | 32 px | 16 / 32 / 48 px | 28 px | 16 px | 2 px |
| xlarge | 136 px | 40 px | 32 / 48 / 72 px | 28 px | 16 px | 3 px |

- At the default width a round icon button is a circle. The touch target is never smaller than 48 px.
- A selected ToggleIconButton switches shape: round becomes the square corner, square becomes round. Shapes change in 200 ms (emphasized).
- The colours stay the base appearance colours (standard, filled, tonal, outlined).

Sources: Jetpack Compose `XSmallIconButtonTokens`, `SmallIconButtonTokens`, `MediumIconButtonTokens`, `LargeIconButtonTokens` and `XLargeIconButtonTokens`, and the M3 icon buttons specification.

## 3. API (added properties)

| Name | Type | Default | Meaning |
|---|---|---|---|
| `size` | enum | `'standard'` | `standard` (the base icon button), `xsmall`, `small`, `medium`, `large` or `xlarge`. |
| `button_width` | enum | `'default'` | `narrow`, `default` or `wide`: the space beside the icon, for Expressive sizes. |
| `shape` | enum | `'round'` | `round` or `square`. |
