# Palette corrections

Source: `docs/Anvil-M3 color mapping 4 palette.xlsx` (46 colour slots, 4 palettes, light values only).

## What was checked

Each palette was compared with Material's colour algorithm (2021 specification). The key colour of each palette was found by search, and every colour checked (19 slots per palette) matched within 2 colour steps:

| Palette | Key colour hue |
|---|---|
| professional_blue | 272.2 |
| warm_coral | 25.4 |
| calm_teal | 196.4 |
| sophisticated_purple | 298.6 |

The spreadsheet's overlay and disabled colours are exact formulas of the main colours, and the build script verifies this for every palette.

## Corrections made

| Palette | Slot | Spreadsheet | Used |
|---|---|---|---|
| professional_blue | Surface Container | #FAF8FF | #EEEDF4 |
| professional_blue | Surface Container High | #EEECEF | #E9E7EF |
| professional_blue | Surface Container Highest | #E3E1E6 | #E3E2E9 |
| warm_coral | Surface Container | #FFF8F7 | #FCEAE7 |
| warm_coral | Surface Container High | #F9EAE8 | #F7E4E2 |
| warm_coral | Surface Container Highest | #F4E4E2 | #F1DEDC |
| calm_teal | Surface Container | #F4FBFA | #E9EFEE |
| calm_teal | Surface Container High | #E2E9E8 | #E3E9E9 |
| calm_teal | Surface Container Highest | #D7DDD3 | #DDE4E3 |
| sophisticated_purple | Surface Container | #FEF7FF | #F2ECF4 |
| sophisticated_purple | Surface Container High | #F3EDF7 | #ECE6EE |
| sophisticated_purple | Surface Container Highest | #E6E1E5 | #E6E0E9 |

Reason: in the spreadsheet, **Surface Container** equals **Surface** in all four palettes, so the container ladder (Low, Container, High, Highest) had no step between Surface and Surface Container Low. The High and Highest values were also one step off, and two had the wrong tint (the calm_teal Highest is yellow-green and the sophisticated_purple Highest has no purple tint). All three slots were regenerated from each palette's key colour.

**Primary Overlay 3** uses an opacity of 0.12 (the M3 state layer for focus and pressed) in place of the spreadsheet's 0.11.

## Kept as in the spreadsheet

The on-container colours (for example `On Primary Container`) use the classic M3 tone 10, darker than the algorithm's tone 30. They give higher contrast and match the base theme, so they are kept. Error is `#BA1A1A` in all four palettes, and `On Error Container` is `#410002`.

## Dark schemes

Generated from the same key colours with the same algorithm. Not in the spreadsheet. To change a dark colour, edit `tools/build_palettes.py` (the `generate` function) and rebuild.
