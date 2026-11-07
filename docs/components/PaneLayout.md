# PaneLayout and window size classes

Component `m3.PaneLayout` (`client_code/_Components/PaneLayout/`), CSS `theme/assets/m3x/pane-layout.css`, token `--m3x-panes-spacer`. Module `client_code/_utils/m3x_adaptive.py`. Step 9.

## 1. What it is

M3 adapts layouts to the window's width, in five window size classes. `m3x_adaptive` reports the class in use. `PaneLayout` provides the two M3 canonical layouts that change with it:

- **List-detail**: a list and the chosen item's detail. Compact and medium windows show one pane at a time; wider windows show both.
- **Supporting pane**: main content with a supporting pane. Compact and medium windows stack the supporting pane below; wider windows put it beside the main content.

The Expressive rail can also adapt (`NavigationRailLayout.rail_adaptive`, see `NavigationRail.md`).

## 2. Window size classes (M3 specification)

| Class | Width | Panes |
|---|---|---|
| compact | under 600 px | one |
| medium | 600 to 839 px | one |
| expanded | 840 to 1199 px | two |
| large | 1200 to 1599 px | two |
| extra_large | 1600 px and up | two |

## 3. Anatomy

| Part | Value |
|---|---|
| Space between panes | 24 px |
| Fixed pane | 360 px (`fixed_pane_width`): the list in list-detail, the supporting pane in supporting |
| Flexible pane | The rest of the width |

The window margins belong to the page layout (`content_padding` in the navigation layouts), so PaneLayout adds none.

## 4. How it works

- The panes switch with CSS media queries at 840 px, so they change at once while the window is resized.
- In list-detail, `show_secondary` chooses the pane on narrow windows. The app sets it to True when an item is chosen, and shows its own back button while `is_single_pane` is True.
- `width_class_change` is raised whenever the window moves to another class.
- `m3x_adaptive` watches the class boundaries with `matchMedia` and writes the class to the page's root element as `data-m3x-window`.
- The designer shows both panes side by side with dashed outlines, so components can go in either.

## 5. API

PaneLayout properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `layout` | enum | `'list_detail'` | `list_detail` or `supporting`. |
| `show_secondary` | boolean | `False` | List-detail on narrow windows: True shows the detail pane. |
| `fixed_pane_width` | number | `360` | The fixed pane's width on wide windows. |
| `visible`, `role`, `tag` | | | Standard. |

Read-only attribute: `is_single_pane`. Events: `width_class_change` (with `width_class`), `show`, `hide`. Slots: `pane-primary`, `pane-secondary`. Toolbox: Containers section.

`m3x_adaptive`: `CLASSES`, `width_class(width=None)`, `is_single_pane()`, `on_change(callback)` (returns a function that stops the calls).

## 6. Usage

```python
def message_list_item_click(self, sender, **event_args):
    self.show_message(sender.tag)
    self.pane_layout_1.show_secondary = True
    self.back_button.visible = self.pane_layout_1.is_single_pane
```
