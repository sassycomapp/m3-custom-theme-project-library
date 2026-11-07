# Side sheet (check against the M3 specification)

The base side sheet inside `NavigationRailLayout` and `NavigationDrawerLayout`, with its content component `m3.SidesheetContent`. CSS fixes `theme/assets/m3x/sidesheet-fixes.css`, tokens `--m3x-sidesheet-*`. Gap E8.

## 1. Result of the check

Compose has no side sheet tokens, so the base was compared with the M3 side sheet specification.

| Part | Specification | Base | Result |
|---|---|---|---|
| Standard sheet (600 px and wider) | Surface, no elevation, 256 to 400 px wide, an Outline Variant divider against the content | 300 px, page background (Surface), Outline Variant left border | Matches |
| Content | Title (Title large), close button, content, optional footer with actions | `SidesheetContent` slots for title, close button, content and footer | Matches |
| Padding | 24 px | 24 px, but 16 px on the leading side | Fixed: 24 px on every side |
| Modal sheet (under 600 px) | Surface Container Low, elevation level 1, corner large (16 px) on the leading edge, scrim | Older tinted background, level 1, 20 px corners, scrim | Fixed: Surface Container Low and 16 px corners |
| Motion | Emphasized easing, about 300 ms | 250 ms with the browser's default easing | Fixed: emphasized, 300 ms; none with reduced motion |

## 2. How the fixes apply

The base rules live in `theme.css` itself, which the browser reads after the imported m3x files, so the fixes use a doubled class (`.anvil-m3-sidesheet.anvil-m3-sidesheet`) to win (lesson 24). No base file is edited.

## 3. API

Unchanged.
