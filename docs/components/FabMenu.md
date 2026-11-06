# FabMenu

Component `m3.FabMenu` (`client_code/_Components/FabMenu/`), CSS `theme/assets/m3x/fab-menu.css`, tokens `--m3x-fab-menu-*` in `theme/assets/m3x/tokens.css`. Gap C19.

## 1. What it is

A FAB menu is a floating action button (FAB) that opens a short stack of related actions, such as Share, Duplicate and Delete. While the menu is open, the FAB turns into a round close button. It is new in M3 Expressive and suits two to six actions.

## 2. Anatomy (M3 specification)

| Part | Value |
|---|---|
| Closed button | A FAB: regular 56 px (corner large), medium 80 px (corner large increased) or large 96 px (corner extra large); icon 24, 28 or 36 px; X Container colour; elevation level 3 |
| Open button | A 56 px round close button with a 20 px close icon, X colour. The FAB's icon turns and fades into the close icon |
| Actions | 56 px high, fully rounded pills, X Container colour, elevation level 3; 24 px padding at each side; an optional 24 px icon 8 px before a Title medium label |
| Stack | Right-aligned with the button, 4 px between actions, 8 px above the button |
| Motion | The button changes shape and colour in 300 ms (emphasized). The actions rise into place one after another, the nearest first, 30 ms apart; they leave in 200 ms. No motion when the device asks for reduced motion |
| Colour sets | primary, secondary or tertiary (X): the closed button and the actions are X Container with On X Container; the open button is X with On X |

Sources: Jetpack Compose `FabMenuBaselineTokens`, `FloatingActionButtonMenu` and the FAB token files, and the M3 FAB menu specification.

## 3. How it works

- A click on the button opens the menu; a second click, a click outside, or the Escape key closes it.
- Choosing an action closes the menu and raises `item_click` with `item` (the action's text) and `index` (its position, from 0, top to bottom).
- The stack is drawn on the page body, outside Anvil's containers (lesson 19), and follows the button when the page scrolls. With little room above the button, it opens below instead.
- The page keeps the closed button's full size, so nothing moves when the button shrinks to the close button.
- With `floating` True, the button sits 16 px from the bottom right corner of the window.
- Keyboard: on the button, Up or Down opens the menu on the last or first action, or moves into a menu already open (lesson 21); Enter or Space opens it on the first action. In the menu, Up, Down, Home and End move between actions, Enter or Space chooses, Escape closes and returns to the button, and Tab closes.
- The button has `aria-haspopup="menu"`, `aria-expanded` and the name in `label`; the actions have the role `menuitem`.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `icon` | icon | `'mi:add'` | The icon on the closed button. |
| `items` | text[] | empty | The actions, top to bottom. |
| `item_icons` | text[] | empty | Optional: one `mi:` icon per action, in the same order. |
| `color` | enum | `'primary'` | `primary`, `secondary` or `tertiary`. |
| `size` | enum | `'regular'` | The closed button's size: `regular`, `medium` or `large`. |
| `floating` | boolean | `False` | True: fixed in the bottom right corner of the window. |
| `label` | string | `'Actions'` | The name screen readers announce. |
| `enabled` | boolean | `True` | Standard. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Method: `close()`.

Events: `item_click` (default, with `item` and `index`), `opened`, `closed`, `show`, `hide`.

Toolbox: Buttons section.

## 5. Usage

```python
def fab_menu_1_item_click(self, item, index, **event_args):
    if item == "Delete":
        self.delete_selected()
```
