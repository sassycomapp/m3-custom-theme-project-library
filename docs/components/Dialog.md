# Dialog

Component `m3.Dialog` (`client_code/_Components/Dialog/`), CSS `theme/assets/m3x/dialog.css`, tokens `--m3x-dialog-*` in `theme/assets/m3x/tokens.css`. Gap C1.

## 1. What it is

A Dialog interrupts the user with a short, focused task or decision: a confirmation, a choice, or a small form. M3 defines two kinds:

- **Basic dialog**: a floating card in the middle of the screen, over a scrim (a dimmed layer that covers the page).
- **Full-screen dialog**: covers the whole screen, with a top bar holding a close button, the headline and one action. M3 uses it for longer tasks on phones.

## 2. Anatomy (M3 specification)

| Part | Basic dialog | Full-screen dialog |
|---|---|---|
| Container | Surface Container High, corner extra large (28 px), elevation level 3, padding 24 px, width 280 to 560 px | Surface, no corners, no shadow, fills the screen |
| Icon (optional) | 24 px, secondary colour, centred above the headline; the headline is then centred | Not used |
| Headline | Headline small, on surface | Title large, on surface, in the top bar |
| Supporting text | Body medium, on surface variant | Body medium, below the top bar |
| Content | Any components, 16 px below the text | Any components, below the top bar |
| Actions | Text buttons, right-aligned, 8 px apart, 24 px below the content | One text button at the right of the top bar |
| Close button | None: the user dismisses by clicking the scrim or pressing Escape | 48 px close icon button at the left of the top bar |
| Scrim | Scrim colour at 32 % opacity | Not visible |

Sources: Jetpack Compose `DialogTokens` (v0_210) and the M3 dialogs specification.

## 3. How it works

- `Dialog.show()` opens the Dialog through Anvil's own `alert()`, with no Anvil title and no Anvil buttons. Anvil's own focus handling, Escape key, backdrop and stacking of several open dialogs therefore apply unchanged.
- `show()` passes the Role `m3x-dialog` (or `m3x-dialog-full-screen`) to `alert()`. Anvil puts that Role on its dialog window as the class `anvil-role-m3x-dialog`. `dialog.css` uses that class to remove the window's own frame and to set the M3 widths. Anvil's other alerts keep their look.
- When the Dialog appears, it gives the newest Anvil backdrop the class `m3x-dialog-scrim`, which sets the M3 scrim colour and opacity.
- `close(value)` raises Anvil's `x-close-alert` event, which closes the alert. `show()` then returns `value`. A dismissed Dialog returns `None`.
- If the Dialog sits inside a form, `show()` opens the whole form, so a Dialog can be designed in the Anvil designer inside its own form.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `headline` | string | `''` | The headline. Hidden when empty. |
| `supporting_text` | string | `''` | The text below the headline. Hidden when empty. |
| `icon` | icon | `''` | An `mi:` icon above the headline. Basic dialogs only. |
| `full_screen` | boolean | `False` | Shows the full-screen dialog. |
| `dismissible` | boolean | `True` | The user can dismiss the Dialog by clicking the scrim or pressing Escape. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Methods:

| Name | Meaning |
|---|---|
| `show()` | Opens the Dialog and waits. Returns the value passed to `close()`, or `None` if dismissed. |
| `close(value=None)` | Closes the Dialog. |
| `add_action(text, value=None, appearance="text", **properties)` | Adds a Button to the actions. Clicking it closes the Dialog and `show()` returns `value`. Returns the Button. |
| `add_component(component, slot="dialog-content-slot")` | Adds a component to the content. `slot="dialog-actions-slot"` adds it to the actions. |

Events: `show`, `hide`.

Slots: `dialog-content-slot` (content), `dialog-actions-slot` (actions).

## 5. Use

```python
dialog = m3.Dialog(icon="mi:delete", headline="Delete 3 files?",
                   supporting_text="The files move to the bin.")
dialog.add_action("Cancel", value=False)
dialog.add_action("Delete", value=True)
if dialog.show():
    delete_files()
```

## 6. Rules

- A Dialog that is already on the page (not inside an alert) cannot be opened with `show()`. Create it in code, or in its own form.
- Basic dialogs hold at most two or three actions. Use a full-screen dialog for a form with several fields on phones.
- A Dialog with `dismissible=False` must have an action that closes it.
