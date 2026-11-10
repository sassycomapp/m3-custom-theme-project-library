# m3-custom-theme: usage guide

m3-custom-theme is a complete Material 3 (M3) theme for Anvil apps, including the M3 Expressive components and styles. It is built on Anvil's Material 3 Theme v1.2.6 and keeps its package name, `m3`. An app switches to it by changing one dependency; its forms, components and code stay as they are.

This guide says how to add the theme to an app, how to choose colours, menu style and motion, which components exist, and where each one is specified. Each component's full specification is in `docs/components/` in this repository.

## 1. Add the theme to an app

The theme takes the place of Anvil's Material 3 Theme. An app never uses both.

1. Open the app in the Anvil editor.
2. Open **Settings**, then **Dependencies**.
3. If the app lists Anvil's Material 3 Theme, remove it.
4. Add a dependency on the **m3-custom-theme** app (`UGGJBAZUZ74XZ7VU`), and choose the branch **master**.
5. Run the app. Every `m3` component, layout and import works unchanged, because the package name is the same.

A new app starts from a blank Anvil app with the same dependency.

## 2. Colours: palette and light or dark mode

The theme has eight palettes, each with a light and a dark scheme: `default`, `professional_blue`, `warm_coral`, `calm_teal`, `sophisticated_purple`, `sky_blue`, `forest_green` and `desert_rose`. The colour preset chosen in Anvil's Theme editor sets the app's starting palette and mode; there is one preset per palette and mode. A new app starts on `professional_blue` light.

An app can change them at start-up, for example from a per-client setting, and can offer them to the user:

```python
from m3._utils import m3x_theming

m3x_theming.apply_saved()                 # Once at start-up: the browser's last choice, or the preset.
m3x_theming.set_palette("calm_teal")      # One of m3x_theming.PALETTES.
m3x_theming.set_mode("dark")              # "light", "dark" or "system" (follow the device).
```

A choice made with `set_palette` or `set_mode` is remembered in the browser and wins over the preset. `get_palette()`, `get_mode()` and `is_dark()` read the current state.

## 3. Menu style

One setting chooses the look of every menu in the app (button, icon button, avatar and dropdown menus):

```python
m3x_theming.set_menu_style("standard")    # "baseline" (default), "standard" or "vibrant".
```

`baseline` is the classic M3 menu. `standard` and `vibrant` are the M3 Expressive menus. A `MenuItem` with `selected=True` shows as the current choice; a DropdownMenu marks its current value by itself. See `docs/components/Menu.md`.

## 4. Motion

Components move with the M3 Expressive springs. One setting chooses the motion scheme for the whole app:

```python
from m3._utils import m3x_motion

m3x_motion.set_scheme("standard")         # "expressive" (default, lively) or "standard" (calm).
```

When the device asks for reduced motion, the theme removes its motion. `m3x_motion.animate(node, keyframes, "spatial-fast")` runs an app's own animation with the same springs. See `docs/components/Motion.md`.

## 5. Window sizes and adaptive layouts

M3 adapts to the window's width in five size classes: compact (under 600 px), medium (600 to 839), expanded (840 to 1199), large (1200 to 1599) and extra-large (1600 and wider).

```python
from m3._utils import m3x_adaptive

m3x_adaptive.width_class()                 # "compact", "medium", "expanded", "large" or "extra_large".
m3x_adaptive.on_change(lambda name: ...)   # Called when the window moves to another class.
```

`PaneLayout` gives the M3 list-detail and supporting-pane layouts, which show one pane at a time on narrow windows and two side by side from 840 px. See `docs/components/PaneLayout.md`.

## 6. Navigation layouts

The two layouts are Anvil's own, with additions:

| Layout | Additions |
|---|---|
| `NavigationRailLayout` | `rail_style="expressive"`: the M3 Expressive rail, 96 px wide with a menu button that expands it to 220 px with full labels. `rail_expanded` sets its state; `rail_adaptive=True` expands it by itself on windows 1200 px and wider. See `docs/components/NavigationRail.md`. |
| `NavigationDrawerLayout` | Unchanged. |

Both layouts hold a side sheet, checked against the M3 specification (`docs/components/SideSheet.md`).

## 7. Components

Every component sits in the Anvil toolbox and can be created in code from `m3.components`:

```python
import m3.components as m3

button = m3.Button(text="Save", size="medium", shape="square")
```

Components from Anvil's theme, with M3 Expressive additions where M3 adds them:

| Component | Additions | Specification |
|---|---|---|
| Button | `size` (xsmall to xlarge), `shape` (round or square), `toggle`, `selected` | `Button.md` |
| IconButton, ToggleIconButton | `size`, `button_width` (narrow, default, wide), `shape` | `IconButton.md` |
| Slider | `size` (small to xlarge) | `Slider.md` |
| LinearProgressIndicator, CircularProgressIndicator | `wavy` | `WavyProgress.md` |
| MenuItem | `selected` | `Menu.md` |
| Card, InteractiveCard | Checked against M3; enabled by default | `Card.md` |
| Avatar, AvatarMenu, ButtonMenu, IconButtonMenu, Checkbox, RadioButton, RadioGroupPanel, Switch, TextBox, TextArea, DropdownMenu, FileLoader, Heading, Text, Link, Divider, NavigationLink, SidesheetContent, CardContentContainer | Unchanged | Anvil's documentation |

Components added by this theme:

| Component | What it is | Specification |
|---|---|---|
| Badge | A small dot, or a count, marking new or unread items | `Badge.md` |
| BottomSheet | A panel that slides up from the bottom, modal or standard | `BottomSheet.md` |
| ButtonGroup | Connected or standard groups of buttons, single or multiple choice | `ButtonGroup.md` |
| Carousel | A row of pictures in five M3 layouts; `images` takes asset paths | `Carousel.md` |
| Chip | Assist, filter, input and suggestion chips | `Chip.md` |
| DatePicker | A date field: typed, or chosen in a calendar dialog | `DatePicker.md` |
| Dialog | Basic and full-screen dialogs | `Dialog.md` |
| FabMenu | A floating action button that opens a stack of actions | `FabMenu.md` |
| FloatingActionButton | The main action on a screen; an extended FAB also shows a label | `FloatingActionButton.md` |
| ListItem | One row of a list: headline, supporting text, and leading and trailing elements | `ListItem.md` |
| LoadingIndicator | The M3 Expressive shape-changing loading indicator, plain or contained | `LoadingIndicator.md` |
| NavigationBar | The bottom navigation bar | `NavigationBar.md` |
| PaneLayout | List-detail and supporting-pane layouts | `PaneLayout.md` |
| RichTooltip | A tooltip with a heading, text and an action (Python object) | `RichTooltip.md` |
| SearchBar | A search bar with a suggestion view | `SearchBar.md` |
| Snackbar | A brief message at the bottom of the screen (Python object) | `Snackbar.md` |
| SplitButton | A main action joined to a menu of related actions | `SplitButton.md` |
| Tabs | Primary and secondary tabs | `Tabs.md` |
| TimePicker | A time field: typed, or chosen on a clock dial in a dialog | `TimePicker.md` |
| Toolbar | Floating and docked toolbars | `Toolbar.md` |
| TopAppBar | Small (title can be centred), medium flexible and large flexible top app bars | `TopAppBar.md` |

## 8. Design tokens

All colours, type sizes, shapes, elevations, state layers, motion and spacing come from CSS variables named `--m3x-*`, defined in `theme/assets/m3x/tokens.css` and taken from Google's Jetpack Compose Material 3 token files. A Role or custom CSS in an app uses the same variables, so it follows the palette and the light or dark mode. The demo form (`Form1` in the theme app) shows every token.

## 9. Versions

The theme has one version, on its `master` branch. Every change to the theme is released there, so an app that depends on `master` always has the current theme.
