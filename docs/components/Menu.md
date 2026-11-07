# Menus (M3 Expressive)

The base menus (ButtonMenu, IconButtonMenu, AvatarMenu, DropdownMenu and Menu), restyled by one app-wide m3x setting, plus the m3x property `selected` on MenuItem. CSS `theme/assets/m3x/menu-expressive.css`. Setting in `client_code/_utils/m3x_theming.py`. Gap E6. The base edits are listed in `docs/upstream-edits.md`.

## 1. What it is

M3 Expressive refreshes menus: a more rounded container, shorter items in Body large, rounded selected items, and two colour styles, standard and vibrant. An app uses one menu style throughout, so the style is one setting for the whole app, not a property on each menu.

## 2. Anatomy (M3 specification)

| Part | Baseline (the base menu) | Expressive standard | Expressive vibrant |
|---|---|---|---|
| Container | Surface Container, corner 4 px, elevation level 2 | Surface Container Low, corner 16 px, elevation level 2, 4 px padding | Tertiary Container, otherwise as standard |
| Item | 48 px high, Label large, On Surface | 44 px high, 16 px side padding, corner 4 px, Body large, On Surface; icons 20 px, On Surface Variant, 12 px before the label | On Tertiary Container labels and icons, otherwise as standard |
| Hover | Base state layer | State layer in the label colour; the item's corners round to 12 px | as standard |
| Selected item | Secondary Container, On Secondary Container | Tertiary Container, On Tertiary Container, corner 12 px | Tertiary, On Tertiary, corner 12 px |
| Disabled item | Base | Label colour at 38 % | as standard |

Sources: Jetpack Compose `MenuTokens`, `StandardMenuTokens`, `VibrantMenuTokens` and `SegmentedMenuTokens`, and the M3 menus specification.

## 3. How it works

- `m3x_theming.set_menu_style(style)` sets `data-m3x-menu-style` on the page's root element; `baseline` removes it. Menus open on the page body, so one attribute styles every menu. `m3x_theming.get_menu_style()` returns the style in use.
- `MenuItem.selected` marks an item as the current choice, with `aria-current`. A DropdownMenu marks the item of its `selected_value` automatically.

## 4. API

`m3x_theming.MENU_STYLES` is `("baseline", "standard", "vibrant")`.

| Function | Meaning |
|---|---|
| `set_menu_style(style)` | Choose the menu style for the whole app. Call once at start-up. |
| `get_menu_style()` | The style in use. |

Added MenuItem property:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `selected` | boolean | `False` | True: the item is shown as selected. |

## 5. Usage

```python
from m3._utils import m3x_theming

m3x_theming.set_menu_style("standard")
```
