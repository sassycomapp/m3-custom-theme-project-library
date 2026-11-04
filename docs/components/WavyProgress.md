# Wavy progress indicators

The `wavy` property of `m3.LinearProgressIndicator` and `m3.CircularProgressIndicator`. Drawing code `client_code/_utils/m3x_wavy.py`, CSS `theme/assets/m3x/wavy-progress.css`, tokens `--m3x-progress-*` in `theme/assets/m3x/tokens.css`. Gap E3.

## 1. What it is

M3 Expressive gives both progress indicators a wavy variant: the part that shows the progress is drawn as a moving wave instead of a straight line. The wave adds energy to long waits and makes them feel shorter. The track (the part not yet done) stays straight.

## 2. Anatomy (M3 Expressive specification)

| Part | Linear | Circular |
|---|---|---|
| Size | The full width, 10 px high | 48 px |
| Active indicator | Primary, 4 px thick, a wave with 3 px amplitude and a 40 px wavelength (20 px when indeterminate) | Primary, 4 px thick, a wave with 1.6 px amplitude, eight waves round the circle |
| Track | Secondary Container, 4 px thick, straight | Secondary Container, 4 px thick |
| Gap between indicator and track | 4 px | 4 px |
| Stop indicator | A 4 px dot of the active colour at the end of the track (determinate only) | None |
| Wave motion | One wavelength per second | One wavelength per second |
| Flat zone | Below 10 % and from 95 % of the progress, the wave is flat | Same |

Sources: Jetpack Compose `LinearProgressIndicatorTokens` and `CircularProgressIndicatorTokens`, and `WavyProgressIndicatorDefaults` in the Compose `WavyProgressIndicator`.

## 3. How it works

- Setting `wavy` to `True` hides the component's own drawing and puts the wavy drawing in its place. Every property setter of the component updates the wavy drawing, so `type`, `progress` and the colour properties work the same way as without the wave.
- The linear wave is a repeating SVG shape used as a mask over a block of the indicator colour. The colour therefore always comes from the theme, or from `progress_color` when that is set.
- The circular wave is an SVG path whose radius rises and falls eight times round the circle. The path is drawn with a length of 100, so the progress percentage is directly the length of the visible part.
- With the device's reduced-motion setting on, the wave stands still. An indeterminate indicator keeps moving, because its movement is what tells the user the app is busy.
- The base component files carry the added property and one update call per setter, each marked with an `m3x` comment and logged in `docs/upstream-edits.md`.

## 4. API

| Component | Added property | Type | Default |
|---|---|---|---|
| `LinearProgressIndicator` | `wavy` | boolean | `False` |
| `CircularProgressIndicator` | `wavy` | boolean | `False` |

All other properties and events are the base components' own.
