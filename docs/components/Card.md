# Card and InteractiveCard (check against the M3 specification)

Base components `m3.Card` and `m3.InteractiveCard`. CSS fix `theme/assets/m3x/card-fixes.css`.

## 1. Result of the check

The base cards were compared with the current M3 card tokens (Jetpack Compose `ElevatedCardTokens`, `FilledCardTokens` and `OutlinedCardTokens`). M3 Expressive adds no new card variants.

| Part | Specification | Base | Result |
|---|---|---|---|
| Shape | Corner medium (12 px) | 12 px | Matches |
| Elevated | Surface Container Low, level 1; hover level 2; pressed level 1 | Same | Matches |
| Filled | Surface Container Highest, level 0; hover level 1; pressed level 0 | Same | Matches |
| Outlined | Surface, 1 px Outline Variant, level 0; hover level 1; pressed level 0 | Same | Matches |
| Hover and pressed state layers | On Surface at 8 % and 10 % | The base overlays, which follow the palette and the light or dark mode | Matches |
| Disabled | Elevated: Surface, level 1, 38 %. Filled: Surface Variant, 38 %. Outlined: Outline at 12 %, 38 % | Elevated and filled match; outlined kept Outline Variant | Fixed: a disabled outlined card's border uses Outline |
| Enabled by default | Every component is enabled unless told otherwise | `InteractiveCard.enabled` had no default, so a card created in code without `enabled=True` was disabled | Fixed: `enabled` defaults to True |

## 2. API

Unchanged.
