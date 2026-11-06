# Tooltips

Plain tooltip: the `tooltip` property of the base theme's components (CSS `.anvil-m3-tooltip` in `theme.css`). Rich tooltip: class `m3.RichTooltip` (`client_code/_utils/m3x_tooltip.py`), CSS `theme/assets/m3x/rich-tooltip.css`, tokens `--m3x-rich-tooltip-*` in `theme/assets/m3x/tokens.css`. Gap C13.

## 1. What it is

A tooltip explains the element it is attached to. M3 defines two kinds:

- **Plain tooltip**: one short line naming or describing a control, such as "Saves the draft". It appears while the pointer rests on the control.
- **Rich tooltip**: a small card with an optional subhead, supporting text and an optional action, for more context. It appears on hover or focus, or, when persistent, on a click and stays until the user closes it.

## 2. Anatomy (M3 specification)

| Part | Plain tooltip | Rich tooltip |
|---|---|---|
| Container | Inverse Surface, corner extra small (4 px), at least 24 px high, at most 280 px wide | Surface Container, corner medium (12 px), elevation level 2, at most 320 px wide, 12 px padding above and 16 px at the sides |
| Subhead | | Title small, On Surface Variant |
| Text | Inverse On Surface | Body medium, On Surface Variant |
| Action | | A text button, Label large, Primary |
| Position | Below the control, aligned to its start | Below the control, aligned to its start; flips above when there is no room |

Sources: the base theme's tooltip and Jetpack Compose `RichTooltipTokens`.

## 3. How it works

- The rich tooltip is attached to any component in code with `attach(component)`. It is drawn on the page body and placed with the same positioning helper as the base theme's plain tooltip (`_utils/fui.py`), so it follows the component when the page scrolls.
- A rich tooltip that is not persistent appears 500 ms after the pointer rests on the component, or when the component gets keyboard focus, and disappears 150 ms after the pointer leaves. The pointer can move onto the tooltip, for example to reach the action, without it disappearing. The component is linked to it with `aria-describedby`.
- A persistent rich tooltip opens when the component is clicked and closes on a second click, a click elsewhere, the Escape key or the action. It is announced as a dialog.
- `detach()` removes the tooltip from the component.

## 4. API

```python
m3.RichTooltip(text, subhead=None, action_text=None, on_action=None, persistent=False)
```

| Argument | Meaning |
|---|---|
| `text` | The supporting text. |
| `subhead` | An optional title above the text. |
| `action_text` | The label of an optional action button. |
| `on_action` | A function called with no arguments when the action is clicked. The tooltip then closes. |
| `persistent` | `True`: opens on click and stays until closed. `False`: appears on hover and focus. |

Methods: `attach(component)` (returns the tooltip), `detach()`, `show()`, `hide()`.
