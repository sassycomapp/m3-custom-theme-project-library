# TopAppBar

Component `m3.TopAppBar` (`client_code/_Components/TopAppBar/`), CSS `theme/assets/m3x/top-app-bar.css`, tokens `--m3x-top-app-bar-*` in `theme/assets/m3x/tokens.css`. The M3 bottom app bar is the docked toolbar (`Toolbar.md`), and the search app bar is part of the SearchBar (`SearchBar.md`).

## 1. What it is

A top app bar sits at the top of a screen. It shows the title of the page, an optional navigation icon at the start (a menu or a back arrow), and actions at the end, such as "Search". M3 Expressive defines three sizes:

- **Small**: the title sits in the bar. The title can be centred.
- **Medium flexible** and **large flexible**: the navigation icon and actions sit in the top row, and a larger title sits on its own row below them, for the top of a page.

Each size can have a subtitle below the title.

## 2. Anatomy (M3 Expressive specification)

| Part | Small | Medium | Large |
|---|---|---|---|
| Height | 64 px | 112 px (136 px with subtitle) | 120 px (152 px with subtitle) |
| Title | Title large | Headline medium | Display small |
| Subtitle | Label medium | Label large | Title medium |

| Part | Value |
|---|---|
| Container | Surface; Surface Container while the page is scrolled |
| Title and subtitle | On Surface and On Surface Variant, one line each |
| Navigation icon | A 48 px icon button with a 24 px On Surface icon, 4 px from the start edge |
| Actions | Icon buttons, 4 px from the end edge |
| Title padding | 16 px from the start edge |

Sources: Jetpack Compose `AppBarTokens`, `AppBarSmallTokens`, `AppBarMediumFlexibleTokens` and `AppBarLargeFlexibleTokens` (14_0_0), and the M3 app bars specification.

## 3. How it works

- The TopAppBar is a container: components added to it (in code with `add_component`, or by dropping them on it in the designer) go into the actions slot at the end of the bar. Use IconButtons.
- The navigation icon raises the `navigation_click` event. The app opens its menu or goes back.
- With `sticky` set to `True`, the bar stays at the top of the window while the page scrolls, and takes the Surface Container colour while the page is scrolled away from the top. The bar listens to the scrolling of the page while it is on screen.
- The base theme's navigation layouts keep their own top app bar. The TopAppBar component is for pages that do not use those layouts, and for sections inside a page.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `title` | string | `'Title'` | The title of the page. |
| `subtitle` | string | `''` | A smaller line below the title. |
| `size` | enum | `small` | `small`, `medium` or `large`. |
| `centered` | boolean | `False` | Centres the title of a small bar. |
| `navigation_icon` | icon | `''` | An `mi:` icon button at the start, such as `mi:menu` or `mi:arrow_back`. |
| `navigation_label` | string | `''` | The screen-reader name of the navigation icon, such as "Open menu". |
| `sticky` | boolean | `True` | Stays at the top of the window and changes colour while the page is scrolled. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Events: `navigation_click` (default), `show`, `hide`.

Slot: `top-app-bar-actions-slot`.
