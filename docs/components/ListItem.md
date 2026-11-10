# ListItem

Component `m3.ListItem` (`client_code/_Components/ListItem/`), CSS `theme/assets/m3x/list-item.css`, tokens `--m3x-list-item-*` in `theme/assets/m3x/tokens.css`.

## 1. What it is

A list is a column of items, each about one thing: a message, a contact, a setting. A ListItem is one row of a list. It has a headline and can have supporting text, a small overline above the headline, a leading element at the start (an icon, an avatar or an image) and trailing elements at the end (a short text, an icon, or a control such as a Switch).

## 2. Anatomy (M3 specification)

| Part | Value |
|---|---|
| Container | Surface; at least 56 px high (one line), 72 px (two lines) or 88 px (three lines); 16 px padding at the sides, 10 px above and below; 12 px between elements |
| Headline | Body large, On Surface, one line |
| Supporting text | Body medium, On Surface Variant; one line, or two lines in a three-line item |
| Overline | Label small, On Surface Variant |
| Leading icon | 24 px, On Surface Variant |
| Leading avatar | 40 px circle, Primary Container, initials in Title medium, On Primary Container |
| Leading image | 56 px square, corner small (8 px) |
| Trailing text | Label small, On Surface Variant |
| Trailing icon | 24 px, On Surface Variant |
| Divider (optional) | 1 px Outline Variant, inset 16 px at each side |
| Selected | Secondary Container, corner large (16 px), all content On Secondary Container |
| Clickable states | Hover, focus and pressed layers in the headline colour. Focus ring: 3 px Secondary, inside the item |
| Disabled | All content On Surface at 38 % |

Sources: Jetpack Compose `ListTokens` (29.0.0) and the M3 lists specification.

## 3. How it works

- A list is made of ListItems placed one under another in a container. Use a LinearPanel, or a ColumnPanel with its spacing set to none, so that no gaps appear between the items. A Card with the `outlined` appearance gives the list a frame.
- Only one leading element is shown: an icon if set, otherwise an avatar if set, otherwise an image.
- A ListItem is a container: a control added to it (in code with `add_component`, or by dropping it on the item in the designer) goes into the trailing slot at the end of the item. A click on that control belongs to the control, not to the item.
- With `clickable` set to `True`, the item reacts to the mouse, can be reached with the Tab key and clicked with Enter or Space, and raises `click`. A disabled item raises no events.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `headline` | string | `'List item'` | The main text. |
| `supporting_text` | string | `''` | The second line. |
| `overline` | string | `''` | The small line above the headline. |
| `three_line` | boolean | `False` | The supporting text may take two lines; the item is at least 88 px high. |
| `leading_icon` | icon | `''` | An `mi:` icon at the start. |
| `leading_avatar_text` | string | `''` | Initials in a round avatar at the start. |
| `leading_image` | uri | `''` | An image at the start. |
| `trailing_text` | string | `''` | A short text at the end. |
| `trailing_icon` | icon | `''` | An `mi:` icon at the end. |
| `clickable` | boolean | `False` | The item can be clicked. |
| `selected` | boolean | `False` | Selected look. |
| `enabled` | boolean | `True` | Standard. |
| `divider` | boolean | `False` | A line under the item. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Events: `click` (default), `show`, `hide`.

Slot: `list-item-trailing-slot`.

## 5. Use

```python
for person in people:
    item = m3.ListItem(headline=person["name"], supporting_text=person["email"],
                       leading_avatar_text=person["initials"], clickable=True)
    item.tag.person = person
    item.add_event_handler("click", self.open_person)
    self.people_panel.add_component(item)
```
