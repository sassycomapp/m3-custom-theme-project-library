# BottomSheet

Component `m3.BottomSheet` (`client_code/_Components/BottomSheet/`), CSS `theme/assets/m3x/bottom-sheet.css`, tokens `--m3x-bottom-sheet-*` in `theme/assets/m3x/tokens.css`. Gap C15.

## 1. What it is

A bottom sheet is a surface that slides up from the bottom of the screen and holds extra content or actions, such as a list of sharing options. M3 defines two kinds:

- **Modal bottom sheet**: a scrim covers the page, and the page cannot be used until the sheet closes.
- **Standard bottom sheet**: no scrim; the page above the sheet stays usable.

## 2. Anatomy (M3 specification)

| Part | Value |
|---|---|
| Container | Surface Container Low, corner extra large (28 px) at the top, elevation level 1 |
| Width | The full window width, up to 640 px; centred on wider windows |
| Height | As tall as its content, up to the window height less 72 px; taller content scrolls inside the sheet |
| Drag handle | A 32 x 4 px fully rounded bar, On Surface Variant, centred in a 48 px touch target (22 px above and below the bar) |
| Scrim | Scrim colour at 32 % opacity, modal sheet only |
| Content | 16 px padding at the sides and 24 px at the bottom |
| Motion | Slides up in 400 ms (emphasized decelerate) and down in 200 ms (emphasized accelerate); no motion when the device asks for reduced motion |

Sources: Jetpack Compose `SheetBottomTokens`, `ScrimTokens` and `BottomSheetDefaults`, and the M3 bottom sheets specification.

## 3. How it works

- The developer places a BottomSheet on a form in the designer and drops components into it. In the designer the sheet is drawn in place. At run time it takes no space on the page until `open()` is called.
- While open, the sheet is drawn on the page body, outside Anvil's containers, which would otherwise cut it off (lesson 19). On `close()`, and when the form is removed from the page, it returns to its place.
- With `dismissible` True, the user closes the sheet by dragging the handle down by a quarter of the sheet's height or flicking it down, by tapping the handle, by tapping the scrim, or with the Escape key. A shorter drag lets the sheet spring back. With `dismissible` False, only the app's own `close()` call closes it.
- A modal sheet takes the keyboard focus when it opens, keeps the Tab key inside the sheet, stops the page from scrolling behind it, and gives the focus back to the element that had it when it closes. It is announced as a dialog with the name in `label`.
- `opened` is raised when the sheet opens; `closed` is raised when it closes, however it was closed.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `modal` | boolean | `True` | True: modal sheet with a scrim. False: standard sheet. |
| `dismissible` | boolean | `True` | True: the user can close the sheet. |
| `show_drag_handle` | boolean | `True` | True: the drag handle is shown. |
| `label` | string | `'Sheet'` | The sheet's name for screen readers. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Methods: `open()`, `close()`. Read-only attribute: `is_open`.

Events: `opened` (default), `closed`, `show`, `hide`.

Slot: `bottom-sheet-content-slot`.

Toolbox: Containers section.

## 5. Usage

```python
def share_button_click(self, **event_args):
    self.share_sheet.open()

def copy_link_item_click(self, **event_args):
    self.share_sheet.close()
```
