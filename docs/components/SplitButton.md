# SplitButton

Component `m3.SplitButton` (`client_code/_Components/SplitButton/`), CSS `theme/assets/m3x/split-button.css`, tokens `--m3x-split-*` in `theme/assets/m3x/tokens.css` and per size in `split-button.css`.

## 1. What it is

A split button joins two buttons: a leading button for the main action, such as "Save", and a trailing arrow button that opens a menu of related actions, such as "Save as draft" and "Save a copy". It is new in M3 Expressive.

## 2. Anatomy (M3 specification)

| Part | Value |
|---|---|
| Join | The two buttons sit 2 px apart. Outer corners are fully round; inner corners are small |
| Menu open | The trailing button becomes fully round and its arrow turns to point up |
| Pressed | The pressed button's inner corners round a little more |
| Colours | Filled: Primary, On Primary. Tonal: Secondary Container, On Secondary Container. Elevated: Surface Container Low, Primary, elevation level 1. Outlined: no fill, 1 px Outline Variant border, On Surface Variant |
| Menu | Surface Container, corner extra small, elevation level 2, 8 px above and below the options; options 48 px high, Label large, On Surface, 12 px side padding; 112 to 280 px wide, aligned to the button's right edge |

Sizes:

| Size | Height | Leading padding (start, end) | Trailing padding | Arrow | Inner corner (pressed) | Label | Icon |
|---|---|---|---|---|---|---|---|
| xsmall | 32 px | 12, 10 px | 13 px | 22 px | 4 px (8 px) | Label large | 20 px |
| small | 40 px | 16, 12 px | 13 px | 22 px | 4 px (12 px) | Label large | 20 px |
| medium | 56 px | 24, 24 px | 15 px | 26 px | 4 px (12 px) | Title medium | 24 px |
| large | 96 px | 48, 48 px | 29 px | 38 px | 8 px (20 px) | Headline small | 32 px |
| xlarge | 136 px | 64, 64 px | 43 px | 50 px | 12 px (20 px) | Headline large | 40 px |

Sources: Jetpack Compose `SplitButtonXSmallTokens`, `SplitButtonSmallTokens`, `SplitButtonMediumTokens`, `SplitButtonLargeTokens`, `SplitButtonXLargeTokens`, the `Button*Tokens` files and `MenuTokens`, and the M3 split button specification.

## 3. How it works

- A click on the leading button raises `click`.
- A click on the trailing button opens the menu of `menu_items`; a second click closes it. With no `menu_items` the trailing button does nothing.
- The menu is drawn on the page body, outside Anvil's containers (lesson 19), and follows the button when the page scrolls.
- Choosing an option closes the menu and raises `item_click` with `item` (the option's text) and `index` (its position, from 0).
- Keyboard: on the trailing button, Down or Up opens the menu on the first or last option. In the menu, Up, Down, Home and End move between options, Enter or Space chooses, Tab closes. Escape closes the menu and returns to the trailing button wherever the focus is. A click outside closes the menu.
- The trailing button has `aria-haspopup="menu"` and `aria-expanded`; the options have the role `menuitem`.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `text` | string | `'Save'` | The label of the main action. |
| `icon` | icon | `''` | An optional icon before the label. |
| `menu_items` | text[] | empty | The menu options. |
| `appearance` | enum | `'filled'` | `filled`, `tonal`, `elevated` or `outlined`. |
| `size` | enum | `'small'` | `xsmall`, `small`, `medium`, `large` or `xlarge`. |
| `enabled` | boolean | `True` | Standard. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Events: `click` (default), `item_click` (with `item` and `index`), `show`, `hide`.

Toolbox: Buttons section.

## 5. Usage

```python
def split_button_1_item_click(self, item, index, **event_args):
    if index == 0:
        self.save_draft()
```
