# Tabs

Component `m3.Tabs` (`client_code/_Components/Tabs/`), CSS `theme/assets/m3x/tabs.css`, tokens `--m3x-tabs-*` in `theme/assets/m3x/tokens.css`. Gap C3.

## 1. What it is

Tabs organise content into views at the same level, such as "Overview", "Specifications" and "Reviews" of one product. One tab is selected at a time. M3 defines two types:

- **Primary tabs** sit at the top of a page, below the top app bar, and switch the page's main views.
- **Secondary tabs** sit inside a part of a page and switch the content of that part.

Either type is fixed (the tabs share the width equally) or scrollable (the tabs keep their natural width and the row scrolls sideways).

## 2. Anatomy (M3 specification)

| Part | Value |
|---|---|
| Container | Surface, 48 px high (64 px when the tabs have icons), a 1 px Surface Variant divider at the bottom |
| Label | Title small. Selected: Primary (primary tabs) or On Surface (secondary tabs). Not selected: On Surface Variant |
| Icon (optional) | 24 px, above the label, same colours as the label |
| Active indicator, primary tabs | 3 px high, Primary, as wide as the label (at least 24 px), rounded top corners |
| Active indicator, secondary tabs | 2 px high, Primary, the full width of the tab |
| States | Hover, focus and pressed layers in the label colour. Focus ring: 3 px Secondary, inside the tab |

Sources: Jetpack Compose `PrimaryNavigationTabTokens` and `SecondaryNavigationTabTokens` (v0_162), and the M3 tabs specification.

## 3. How it works

- The Tabs component draws the row of tabs. The app shows the content of the selected tab, normally by making one of several panels visible in the `change` event. This keeps the content in ordinary Anvil containers that the designer can edit.
- The tabs follow the ARIA tabs pattern: the row is a `tablist`, each tab is a `tab` with `aria-selected`, and only the selected tab is in the keyboard's Tab order. The Left and Right arrow keys, Home and End move the selection.
- Selecting a tab that is partly out of view in a scrollable row scrolls it into view.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `items` | text[] | `Tab 1`, `Tab 2`, `Tab 3` | The label of each tab. |
| `icons` | text[] | empty | Optional `mi:` icons, one per tab, in the same order. |
| `selected_index` | number | `0` | The position of the selected tab, counting from 0. |
| `selected_text` | string (read only) | | The label of the selected tab. |
| `type` | enum | `primary` | `primary` or `secondary`. |
| `scrollable` | boolean | `False` | Natural widths and sideways scrolling. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Events: `change` (default), `show`, `hide`.

## 5. Use

```python
def tabs_1_change(self, **event_args):
    for i, panel in enumerate([self.overview_panel, self.specs_panel, self.reviews_panel]):
        panel.visible = i == self.tabs_1.selected_index
```
