# Snackbar

Class `m3.Snackbar` (`client_code/_utils/m3x_snackbar.py`), CSS `theme/assets/m3x/snackbar.css`, tokens `--m3x-snackbar-*` in `theme/assets/m3x/tokens.css`.

## 1. What it is

A Snackbar is a brief message at the bottom of the screen about something the app has done, such as "Message sent". It can offer one action, such as "Undo", and a close button. It leaves the screen by itself after a set time.

## 2. Anatomy (M3 specification)

| Part | Value |
|---|---|
| Container | Inverse Surface, corner extra small (4 px), elevation level 3, at least 48 px high, at most 600 px wide, 16 px from the bottom and sides of the screen |
| Text | Body medium, Inverse On Surface, one or two lines, 14 px above and below |
| Action | A text button with a Label large label in Inverse Primary, 40 px high |
| Close button | A 48 px icon button with a 24 px close icon in Inverse On Surface |
| Padding | 16 px before the text, 8 px after the last button |
| Durations | Short 4 seconds, long 10 seconds, or indefinite |
| Motion | Enters by fading in and rising 8 px, with the emphasised decelerate easing. Leaves by fading out with the emphasised accelerate easing |

Sources: Jetpack Compose `SnackbarTokens` (v0_103) and the Compose `Snackbar` and `SnackbarHost` layout, and the M3 snackbar specification.

## 3. How it works

- A Snackbar is not placed in a form, because it is a passing message, not part of a page. The app creates it in code and calls `show()`. It has no toolbox entry for that reason.
- `show()` puts the Snackbar in a queue. Only one Snackbar is on screen at a time; each one appears when the one before it has left. This is the M3 rule.
- The Snackbar is drawn in a fixed area at the bottom of the page, above Anvil's dialogs, so a Snackbar shown from inside a Dialog is still visible.
- A Snackbar with the duration "indefinite" stays until the user acts. If it has neither an action nor a close button, the close button is added, so the user can always remove it.
- The message is announced to screen readers (`role="status"`).

## 4. API

```python
m3.Snackbar(text, action_text=None, on_action=None, on_dismiss=None,
            show_close=False, duration="short")
```

| Argument | Meaning |
|---|---|
| `text` | The message. |
| `action_text` | The label of the action button. `None` shows no action. |
| `on_action` | A function called with no arguments when the action is clicked. The Snackbar then leaves. |
| `on_dismiss` | A function called with no arguments when the Snackbar leaves for any reason. |
| `show_close` | `True` shows the close button. |
| `duration` | `"short"` (4 s), `"long"` (10 s), `"indefinite"`, or a number of seconds. |

Methods: `show()` shows the Snackbar after any Snackbar already on screen. `dismiss()` removes it from the screen or from the queue.

## 5. Use

```python
m3.Snackbar("Photo deleted.", action_text="Undo", on_action=restore_photo).show()
```
