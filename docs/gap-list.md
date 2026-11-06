# Gap list: base v1.2.6 compared with the full M3 / M3 Expressive set

Companion to `docs/base-inventory.md`. The foundation findings in Section 1 come from the base files. The component list in Sections 2 and 3 was checked against the saved page `Components – Material Design 3.htm` (2 Nov 2026). That page lists 36 component pages, plus an "All buttons" overview. The base covers 13 of them in full (buttons, cards, checkbox, divider, icon buttons, menus, navigation drawer, navigation rail, progress indicators, radio button, sliders, switch, text fields). Three are covered in part: app bars (C7), side sheets (E8) and tooltips (C13). The other 20 are missing and are in Section 2. The check found no component missing from this list.

## 1. Foundation gaps (found in the base files)

| # | Gap | Evidence in v1.2.6 |
|---|---|---|---|
| F1 | No dark mode | One colour scheme. No `prefers-color-scheme` rule anywhere in `theme.css` or `anvil-m3/*.css`. |
| F2 | Only colour tokens exist | `theme.css` defines 45 `--anvil-m3-*` variables, all colours. No typography, shape, elevation, state-layer or motion variables. |
| F3 | Hardcoded shape values | Component CSS uses literal radii such as `4px`, `16px`, `100px`, `50%`. |
| F4 | No motion system | 33 `transition` lines with literal values. No easing tokens, no spring tokens. |
| F5 | No reduced-motion support | No `prefers-reduced-motion` rule anywhere. |
| F6 | `!important` used heavily | 59 occurrences across `theme.css` and `anvil-m3/*.css`. |
| F7 | Breakpoints differ from M3 window size classes | `theme.css` uses 600 / 780 / 980 px. M3 defines compact, medium, expanded, large and extra-large classes at 600 / 840 / 1200 / 1600 px. |
| F8 | One Role only | `data-grid-header`. No Roles for typography or surface levels. |
| F9 | Fonts load from a CDN | `head_html` loads Poppins, Roboto and Material Symbols from Google Fonts. Kept as is for now (decision 7). |

## 2. Missing components, in build priority order

Priority 1 (core components every business app needs):

| # | Component | In base? | Note | Status |
|---|---|---|---|---|
| C1 | Dialogs | No | The base only restyles Anvil's own modal in `theme.css`. A proper component is needed. | Built: `Dialog` |
| C2 | Chips (assist, filter, input, suggestion) | No | | Built: `Chip` |
| C3 | Tabs (primary, secondary) | No | | Built: `Tabs` |
| C4 | Snackbar | No | | Built: `Snackbar` |
| C5 | FAB and extended FAB | No | Expressive update applies. | Built: `FloatingActionButton` |
| C6 | Lists and list items | No | Expressive refresh applies. | Built: `ListItem` |
| C7 | App bars (top, bottom, search app bar) | Partly | The top app bar exists only as styling inside the two navigation layouts. On m3.material.io, bottom and search app bars are part of the App bars page. | Top app bar built: `TopAppBar`. The bottom app bar is the docked `Toolbar` (C17), which M3 Expressive uses in its place; the search app bar is `SearchBar` (C14). |
| C8 | Navigation bar (bottom) | No | Expressive update applies. | Built: `NavigationBar` |
| C9 | Button groups and segmented buttons | No | Both have pages on m3.material.io. Button groups are new in Expressive and replace the segmented button, so button groups are built first. | Built: `ButtonGroup` (connected and standard) |
| C10 | Badges | No | | Built: `Badge` |

Priority 2:

| # | Component | In base? | Note | Status |
|---|---|---|---|---|
| C11 | Date picker | No | The base toolbox offers Anvil's standard DatePicker. | Built: `DatePicker` |
| C12 | Time picker | No | | Built: `TimePicker` |
| C13 | Tooltips (plain, rich) | Partly | `Button` has a `tooltip` property. No rich tooltip. | Built: plain tooltip is the base `tooltip` property; rich tooltip is `RichTooltip` |
| C14 | Search (search bar, search view) | No | | Built: `SearchBar` (search bar with docked and full-screen search view) |
| C15 | Bottom sheets | No | | Built: `BottomSheet` (modal and standard) |
| C16 | Loading indicator | No | New in Expressive. | Built: `LoadingIndicator` |
| C17 | Toolbars (docked, floating) | No | New in Expressive. | Built: `Toolbar` (floating and docked, standard and vibrant) |
| C18 | Split button | No | New in Expressive. | Built: `SplitButton` |
| C19 | FAB menu | No | New in Expressive. | Built: `FabMenu` |

Priority 3:

| # | Component | In base? | Note | Status |
|---|---|---|---|---|
| C20 | Carousel | No | | Built: `Carousel` (multi-browse, hero, center-aligned hero, uncontained, full width) |
| C21 | (merged into C7) | | The Bottom app bar is part of the App bars page. | |

## 3. Existing components that need an Expressive update

These exist in the base. Each needs its M3 Expressive spec checked, and a variant added where the spec changed. Done through the Component Build Loop (4.1 of `m3-custom-theme.md`), without changing the existing behaviour (rule 5.3).

| # | Component | Expected update | Status |
|---|---|---|---|
| E1 | `Button` | Sizes, round and square shapes, toggle behaviour. | Built: `size`, `shape`, `toggle`, `selected` |
| E2 | `IconButton`, `ToggleIconButton` | Sizes, shapes, shape change when selected. | Built: `size`, `button_width`, `shape` |
| E3 | `LinearProgressIndicator`, `CircularProgressIndicator` | Wavy variants. | Built: `wavy` property |
| E4 | `Slider` | Expressive sizes and handle styles. | Built: `size`; the base handle already has the Expressive style |
| E5 | Navigation layouts (`NavigationDrawerLayout`, `NavigationRailLayout`) | Expressive rail, and adaptive behaviour at all window size classes (F7). | To build |
| E6 | `Menu`, `DropdownMenu`, `MenuItem` | Refreshed Expressive menu guidance. | To build |
| E7 | `Card`, `InteractiveCard` | Check against the current spec during Step 6. | To build |
| E8 | `SidesheetContent` | The base has the content container for side sheets inside the layouts. Check against the side sheets spec. | To build |

## 4. Not planned

Components in the base that are not M3 components (`Avatar`, `AvatarMenu`, `FileLoader`, `Heading`, `Text`, `Link`, `NavigationLink`, `SidesheetContent`, `RadioGroupPanel`) stay as they are. They are carried over unchanged.
