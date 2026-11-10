# Slider (M3 Expressive)

Base component `m3.Slider`, extended by m3x with the property `size`. CSS `theme/assets/m3x/slider-expressive.css`. The base edits are listed in `docs/upstream-edits.md`.

## 1. What it is

The base slider already has the M3 Expressive look at the extra-small size: a 16 px track split by a 4 x 44 px handle with a 6 px gap at each side. M3 Expressive adds four larger sizes. With the default value (`size` standard) the slider is the base slider, unchanged.

## 2. Anatomy (M3 specification)

| Size | Track | Handle | Track end corners |
|---|---|---|---|
| standard (extra small) | 16 px | 44 px | fully round |
| small | 24 px | 44 px | 8 px |
| medium | 40 px | 52 px | 12 px |
| large | 56 px | 68 px | 16 px |
| xlarge | 96 px | 108 px | 28 px |

- The ends of the track beside the handle keep 2 px corners. Markers stay centred on the track. The value label sits above the taller handle.
- The value label is fixed to the window, so it shows above the handle on a scrolled page (a fix to the base slider, for all sizes).

Sources: Jetpack Compose `SliderTokens` (extra small) and the M3 sliders specification (the larger sizes).

## 3. API (added property)

| Name | Type | Default | Meaning |
|---|---|---|---|
| `size` | enum | `'standard'` | `standard`, `small`, `medium`, `large` or `xlarge`. |
