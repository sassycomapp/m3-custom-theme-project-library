# Gap list: base v1.2.6 compared with the full M3 / M3 Expressive set

Companion to `docs/base-inventory.md`. The foundation findings in Section 1 come from the base files. The component list in Sections 2 and 3 comes from the M3 component catalogue as known at the end of June 2026. It is not read from m3.material.io (the site cannot be read automatically). Confirm it by saving the page https://m3.material.io/components into this repo as `m3-components-page.htm`; any component on that page that is missing below is added to Section 2 before Step 5 ends.

## 1. Foundation gaps (found in the base files)

| # | Gap | Evidence in v1.2.6 |
|---|---|---|
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

| # | Component | In base? | Note |
|---|---|---|---|
| C1 | Dialogs | No | The base only restyles Anvil's own modal in `theme.css`. A proper component is needed. |
| C2 | Chips (assist, filter, input, suggestion) | No | |
| C3 | Tabs (primary, secondary) | No | |
| C4 | Snackbar | No | |
| C5 | FAB and extended FAB | No | Expressive update applies. |
| C6 | Lists and list items | No | Expressive refresh applies. |
| C7 | Top app bar as a component | Partly | It exists only as styling inside the two navigation layouts. |
| C8 | Navigation bar (bottom) | No | Expressive update applies. |
| C9 | Button groups and segmented button | No | Button groups are new in Expressive and replace the segmented button. |
| C10 | Badges | No | |

Priority 2:

| # | Component | In base? | Note |
|---|---|---|---|
| C11 | Date picker | No | The base toolbox offers Anvil's standard DatePicker. |
| C12 | Time picker | No | |
| C13 | Tooltips (plain, rich) | Partly | `Button` has a `tooltip` property. No rich tooltip. |
| C14 | Search (search bar, search view) | No | |
| C15 | Bottom sheets | No | |
| C16 | Loading indicator | No | New in Expressive. |
| C17 | Toolbars (docked, floating) | No | New in Expressive. |
| C18 | Split button | No | New in Expressive. |
| C19 | FAB menu | No | New in Expressive. |

Priority 3:

| # | Component | In base? | Note |
|---|---|---|---|
| C20 | Carousel | No | |
| C21 | Bottom app bar | No | |

## 3. Existing components that need an Expressive update

These exist in the base. Each needs its M3 Expressive spec checked, and a variant added where the spec changed. Done through the Component Build Loop (4.1 of `m3-custom-theme.md`), without changing the existing behaviour (rule 5.3).

| # | Component | Expected update |
|---|---|---|
| E1 | `Button` | Sizes, round and square shapes, toggle behaviour. |
| E2 | `IconButton`, `ToggleIconButton` | Sizes, shapes, shape change when selected. |
| E3 | `LinearProgressIndicator`, `CircularProgressIndicator` | Wavy variants. |
| E4 | `Slider` | Expressive sizes and handle styles. |
| E5 | Navigation layouts (`NavigationDrawerLayout`, `NavigationRailLayout`) | Expressive rail, and adaptive behaviour at all window size classes (F7). |
| E6 | `Menu`, `DropdownMenu`, `MenuItem` | Refreshed Expressive menu guidance. |
| E7 | `Card`, `InteractiveCard` | Check against the current spec during Step 7. |

## 4. Not planned

Components in the base that are not M3 components (`Avatar`, `AvatarMenu`, `FileLoader`, `Heading`, `Text`, `Link`, `NavigationLink`, `SidesheetContent`, `RadioGroupPanel`) stay as they are. They are carried over unchanged.
