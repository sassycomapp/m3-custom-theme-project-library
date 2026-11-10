# SearchBar

Component `m3.SearchBar` (`client_code/_Components/SearchBar/`), CSS `theme/assets/m3x/search.css`, tokens `--m3x-search-*` in `theme/assets/m3x/tokens.css`.

## 1. What it is

Search lets the user find content by typing. M3 defines two parts:

- **Search bar**: a pill-shaped field with a search icon, a placeholder such as "Search recipes", and optional elements at its end, such as the user's avatar.
- **Search view**: the list of suggestions that opens below the bar while the user types. On wide screens it drops down from the bar (docked): it is drawn on the page body, outside Anvil's containers, placed under the bar at the bar's width, and reaches down to 16 px above the bottom of the window. A handle in its bottom right corner lets the user drag it shorter or taller. Changing the window between wide and phone width closes the view. On screens narrower than 600 px it fills the screen (full screen), with a back arrow to close it.

## 2. Anatomy (M3 specification)

| Part | Value |
|---|---|
| Bar | Surface Container High, 56 px high, fully rounded; leading search icon On Surface; text Body large, On Surface; placeholder On Surface Variant |
| Clear button | A 48 px close icon button, shown while the bar holds text |
| Trailing slot | Components at the end of the bar, such as an Avatar or IconButton |
| Docked view | Surface Container High, corner extra large (28 px) at the bottom; the bar's bottom corners square off; a 1 px Outline divider between bar and view; elevation level 3 |
| Full-screen view | Fills the screen below a 72 px header holding a back arrow, the input and the clear button |
| Suggestions | 56 px rows with a search icon and the suggestion in Body large; the highlighted row has an 8 % On Surface layer |

Sources: Jetpack Compose `SearchBarTokens` and `SearchViewTokens`, and the M3 search specification.

## 3. How it works

- The view opens when the bar gets focus and closes on Escape, the back arrow, a click outside, or a search.
- The view lists the `suggestions` that contain the typed text, ignoring capital letters, up to `max_suggestions`. With an empty bar it lists the first suggestions.
- The Up and Down arrow keys move through the suggestions; Enter searches for the highlighted suggestion, or for the typed text. A click on a suggestion searches for it.
- A search fills the bar with the query, closes the view and raises `search` with the argument `query`. Typing raises `change`, so an app can replace `suggestions` with results from its own data as the user types.
- The input is an ARIA combobox linked to the view (a listbox), and the highlighted suggestion is announced through `aria-activedescendant`.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `text` | string | `''` | The text in the bar. |
| `placeholder` | string | `'Search'` | The text shown in the empty bar, and its screen-reader name. |
| `suggestions` | text[] | empty | The suggestions offered while typing. |
| `max_suggestions` | number | `8` | The largest number of suggestions shown. |
| `enabled` | boolean | `True` | Standard. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Events: `search` (default, with `query`), `change`, `show`, `hide`. Method: `focus()`.

Slot: `search-trailing-slot`.
