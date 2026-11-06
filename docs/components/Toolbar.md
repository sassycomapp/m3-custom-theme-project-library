# Toolbar

Component `m3.Toolbar` (`client_code/_Components/Toolbar/`), CSS `theme/assets/m3x/toolbar.css`, tokens `--m3x-toolbar-*` in `theme/assets/m3x/tokens.css`. Gap C17; also covers the bottom app bar part of C7.

## 1. What it is

A toolbar holds a small set of actions, usually icon buttons, for the current page. M3 Expressive defines two variants:

- **Floating toolbar**: a fully rounded bar that floats over the content, horizontal or vertical, with an optional floating action button (FAB) beside it.
- **Docked toolbar**: a full-width bar along the bottom of the screen. M3 Expressive uses it in place of the bottom app bar.

Each comes in two colour styles: **standard** (a quiet surface colour) and **vibrant** (the primary container colour, for more emphasis).

## 2. Anatomy (M3 specification)

| Part | Value |
|---|---|
| Floating bar | 64 px high (64 px wide when vertical), fully rounded, 8 px space at each end, 4 px between items |
| Floating elevation | None; level 1 when a FAB sits beside it |
| FAB | 8 px from the floating bar. Suggested colours: Primary Container with a standard toolbar, Tertiary Container with a vibrant one (set on the FAB's `appearance`) |
| Docked bar | 64 px high, full width, square corners, 16 px space at each end, items spread evenly with at least 4 px between them, no elevation |
| Standard colours | Container Surface Container; icons On Surface |
| Vibrant colours | Container Primary Container; icons On Primary Container; a selected toggle icon button gets a Surface Container circle with an On Surface icon |
| Pinned position | Docked: along the bottom edge of the window. Floating: 16 px above the bottom centre, or 16 px in from the right edge when vertical |
| Hide on scroll | The pinned toolbar slides away after the user scrolls down 40 px and returns after 40 px back up, in 300 ms (emphasized); no motion when the device asks for reduced motion |

Sources: Jetpack Compose `FloatingToolbarTokens`, `DockedToolbarTokens`, `FloatingToolbarDefaults` and `BottomAppBarDefaults`, and the M3 toolbars specification.

## 3. How it works

- The developer adds IconButtons, ToggleIconButtons or other buttons to the toolbar. A FloatingActionButton goes in the `toolbar-fab-slot`: beside a floating toolbar (to its right, or below it when vertical), or at the end of a docked toolbar.
- With `pin_to_screen` False, the toolbar sits in the page flow like any other component. With `pin_to_screen` True, it is fixed to the window. A pinned docked toolbar covers the bottom 64 px of the window, so the page needs that much space at its end.
- `hide_on_scroll` works only on a pinned toolbar. It reacts to scrolling of the page or of any scrolling container on it, apart from the toolbar itself.
- In the Anvil designer the toolbar is always drawn in place, even when pinned, so components can be dropped into it.
- The bar has the ARIA role `toolbar`, with `aria-orientation` and the name in `label`.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `variant` | enum | `'floating'` | `floating` or `docked`. |
| `color_style` | enum | `'standard'` | `standard` or `vibrant`. |
| `vertical` | boolean | `False` | True: a floating toolbar is a vertical column. Docked toolbars are always horizontal. |
| `pin_to_screen` | boolean | `False` | True: the toolbar is fixed to the window. |
| `hide_on_scroll` | boolean | `False` | True: a pinned toolbar slides away while the user scrolls down. |
| `label` | string | `'Toolbar'` | The toolbar's name for screen readers. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Events: `show`, `hide`.

Slots: `toolbar-slot` (default), `toolbar-fab-slot`.

Toolbox: Navigation section.

## 5. Usage

```python
bar = m3.Toolbar(color_style="vibrant", pin_to_screen=True, hide_on_scroll=True)
bar.add_component(m3.IconButton(icon="mi:undo"))
bar.add_component(m3.IconButton(icon="mi:redo"))
bar.add_component(m3.FloatingActionButton(icon="mi:add",
                                          appearance="tertiary_container"),
                  slot="toolbar-fab-slot")
```
