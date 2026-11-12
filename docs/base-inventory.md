---
title: "base-inventory"
---
# m3-custom-theme: component inventory

Every component the theme offers in the Anvil toolbox, and its two layouts, with each property, the events it raises and the slots a layout offers. This file and `component-inventory.yaml` are generated from the theme's component definitions by `tools/build_inventory.py`, so they always match the theme. A component the theme adds also has its own specification in `docs/components/`, named in its entry.

A property marked writeback can be bound with `writeback:<property>` in a form template.

## `m3.Layouts.NavigationDrawerLayout`

Specification: this file.

Slots: `app_bar_links`, `app_bar_title`, `content`, `navigation`, `sidesheet`.

Events: none.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `navigation_drawer_color` | color |  |  |  | The color of the Navigation Drawer on Forms using this Layout. |
| `background_color` | string |  |  |  | The background color of Forms using this Layout. |
| `text_color` | string |  |  |  | The default color of the text on Forms using this Layout. |
| `show_sidesheet` | boolean |  | False |  | If True, the sidesheet will be shown on Forms using this Layout. |
| `content_padding` | padding |  | 8, 8, 8, 8 |  | The padding (pixels) around the content of the page |

## `m3.Layouts.NavigationRailLayout`

Specification: this file.

Slots: `content`, `navigation`, `sidesheet`, `slot_2`, `slot_4`.

Events: none.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `navigation_rail_collapse_to` | enum | bottom_app_bar, modal_navigation_drawer | bottom_app_bar |  | The way the side navigation will collapse on mobile. |
| `navigation_rail_color` | color |  |  |  |  |
| `background_color` | color |  |  |  | The background color of Forms using this Layout. |
| `text_color` | color |  |  |  | Default color of the text on Forms using this layout |
| `show_sidesheet` | boolean |  | True |  |  |
| `navigation_rail_vertical_align` | enum | top, center, bottom | top |  | The vertical position of the content in the navigation rail. |
| `rail_style` | enum | standard, expressive | standard |  | m3x: standard (the base 80 px rail) or expressive (the M3 Expressive rail: 96 px wide, with a menu button that expands it to 220 px with full labels). Phone widths keep the base behaviour. |
| `rail_adaptive` | boolean |  | False |  | m3x: If True, an expressive rail expands by itself on large and extra-large windows (1200 px and wider) and collapses on smaller ones. The menu button still switches it until the window changes size class. |
| `rail_expanded` | boolean |  | False |  | m3x: If True, an expressive rail starts expanded. The menu button at the top of the rail switches it. |
| `content_padding` | padding |  | 8, 8, 8, 8 |  | The padding (pixels) around the content of the page |

## `m3._Components.Avatar`

Specification: this file.

Events: none.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `user_name` | string |  |  |  | The name of the associated user. If no image is provided, the avatar will display initials generated from the user_name. |
| `image` | uri |  |  |  | The image to display on the component. |
| `size` | number |  | 40 |  | Dimensions (in pixels) of the component's height and width |
| `fallback_icon` | icon |  | mi:person |  | The icon to display if no image or name is provided. |
| `background_color` | color |  |  |  | Background color of the component if no image is provided |
| `text_color` | color |  |  |  | Color of the initials displayed on the component if no image is provided |
| `align` | enum | left, center, right | left |  | The position of this component in the available space. |
| `appearance` | enum | filled, tonal, outlined | filled |  | A predefined style for this component. |
| `margin` | margin |  | , , ,  |  | The margin (pixels) of the component. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `fallback_icon_color` | color |  |  |  | The colour of the icon displayed on this component. |
| `border` | string |  |  |  | The border of this component. Can take any valid CSS border value. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `font_size` | number |  |  |  | The font size of the initials displayed on this component. |
| `fallback_icon_size` | number |  |  |  | The size (pixels) of the icon on this component |
| `font_family` | string |  |  |  | The font family to use for the initials on this component. |

## `m3._Components.AvatarMenu`

Specification: this file.

Events: `click`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `menu_background_color` | color |  |  |  | The color of the background of the Menu |
| `menu_border` | string |  |  |  | The border of the Menu. Can take any valid CSS border value. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `appearance` | enum | filled, tonal, outlined | filled |  | A predefined style for this component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `user_name` | string |  |  |  | The name of the associated user. If no image is provided, the avatar will display initials generated from the user_name. |
| `avatar_border` | string |  |  |  | The border of the Avatar in this component. Can take any valid CSS border value. |
| `avatar_background_color` | color |  |  |  | Background color of the Avatar in this component if no image is provided |
| `avatar_text_color` | color |  |  |  | Color of the initials displayed on the Avatar if no image is provided |
| `fallback_icon` | icon |  | mi:person |  | The icon to display on the Avatar if no image or user_name is provided. |
| `avatar_font_size` | number |  |  |  | The font size of the initials displayed on the Avatar |
| `fallback_icon_color` | color |  |  |  | The colour of the icon displayed on the Avatar |
| `fallback_icon_size` | number |  |  |  | The size (pixels) of the icon on the Avatar |
| `margin` | margin |  |  |  | The margin (pixels) of the component. |
| `align` | enum | left, center, right | left |  | The position of this component in the available space. |
| `avatar_font_family` | string |  |  |  | The font family to use for the initials on the Avatar |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles |
| `menu_items` | object |  |  |  | A list of components to be added to the menu |
| `image` | uri |  |  |  | The image to display on the component. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.Badge`

Specification: `Badge.md`.

Events: `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `count` | number |  |  |  | The number shown. Leave empty for a small dot without a number. |
| `max_count` | number |  | 999 |  | Counts above this number show as the number with a plus, for example 999+. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.BottomSheet`

Specification: `BottomSheet.md`.

Events: `opened`, `closed`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `modal` | boolean |  | True |  | If True, a scrim covers the page while the sheet is open and the page cannot be used. If False, the page stays usable (standard sheet). |
| `dismissible` | boolean |  | True |  | If True, the user can close the sheet by dragging it down, tapping the scrim, tapping the drag handle or pressing Escape. |
| `show_drag_handle` | boolean |  | True |  | If True, a drag handle is shown at the top of the sheet. |
| `label` | string |  | Sheet |  | A name for the sheet that screen readers announce. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.Button`

Specification: `Button.md`.

Events: `click`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `align` | enum | left, center, right, full | left |  | The position of this component in the available space. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `appearance` | enum | filled, elevated, tonal, outlined, text | filled |  | A predefined style for this component. |
| `text` | string |  |  |  | The text displayed on this component. |
| `size` | enum | standard, xsmall, small, medium, large, xlarge | standard |  | m3x: standard (the base button), or an M3 Expressive size: xsmall (32 px), small (40 px), medium (56 px), large (96 px) or xlarge (136 px). |
| `shape` | enum | round, square | round |  | m3x: round (fully rounded ends) or square (rounded corners). |
| `toggle` | boolean |  | False |  | m3x: If True, the button is a toggle button: a click switches selected, and the colours and shape change when selected. |
| `selected` | boolean |  | False |  | m3x: If True, a toggle button is shown as selected. |
| `text_color` | color |  |  |  | The colour of the text on the component. |
| `font_family` | string |  |  |  | The font family to use for this component. |
| `font_size` | number |  |  |  | The font size of the text displayed on this component. |
| `underline` | boolean |  | False |  | If True, this component’s text will be underlined. |
| `italic` | boolean |  | False |  | If True, this component’s text will be italic. |
| `bold` | boolean |  | True |  | If True, this component’s text will be bold. |
| `icon` | icon |  |  |  | The icon to display on this component. |
| `icon_color` | color |  |  |  | The colour of the icon displayed on this component. |
| `icon_size` | number |  |  |  | The size (pixels) of the icon displayed on this component. |
| `icon_align` | enum | left, right | left |  | The position of the icon on this component. |
| `spacing` | spacing |  |  |  | The margin and padding (pixels) of the component. |
| `background_color` | color |  |  |  | The colour of the background of this component. |
| `border` | string |  |  |  | The border of this component. Can take any valid CSS border value. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |

## `m3._Components.ButtonGroup`

Specification: `ButtonGroup.md`.

Events: `change`, `click`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `items` | text[] |  | Day, Week, Month |  | The label of each button, one per line. |
| `icons` | text[] |  |  |  | Optional: one icon per button, in the same order as the items, one per line, for example mi:list. |
| `type` | enum | connected, standard | connected |  | connected: the buttons are joined into one bar, for choosing between options. standard: the buttons stand apart, for related actions. |
| `selection` | enum | none, single, multiple | single |  | none: the buttons are actions. single: exactly one button is selected. multiple: any number of buttons can be selected. |
| `selected_index` | number |  |  | yes (change) | The position of the selected button, counting from 0 (single selection; empty selects the first button). With multiple selection, the first selected button. |
| `selected_indices` | object |  |  |  | The positions of all selected buttons, as a list (multiple selection). |
| `appearance` | enum | filled, tonal, outlined | filled |  | The colours of the buttons: filled, tonal or outlined. |
| `full_width` | boolean |  | False |  | If True, the group fills the width of its container and the buttons share it equally. |
| `enabled` | boolean |  | True |  | If True, the buttons can be clicked. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.ButtonMenu`

Specification: this file.

Events: `click`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `text` | string |  |  |  | The text displayed on the Button. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `appearance` | enum | elevated, filled, tonal, outlined | elevated |  | A predefined style for the Button. |
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `bold` | boolean |  | True |  | If True, the Button's text will be bold. |
| `italic` | boolean |  | False |  | If True, the Button’s text will be italic. |
| `underline` | boolean |  | False |  | If True, the Button’s text will be underlined. |
| `button_background_color` | color |  |  |  | Color of the background of the Button. |
| `button_text_color` | color |  |  |  | Color of the text on the Button. |
| `button_border` | string |  |  |  | The border of the Button. Can take any valid CSS border value. |
| `button_font_size` | number |  |  |  | Font size of text displayed on the Button. |
| `icon_color` | color |  |  |  | The colour of the icon displayed on the Button. |
| `icon_size` | number |  |  |  | The size (pixels) of the icon displayed on the Button. |
| `icon_align` | enum | left, right | left |  | The position of the icon on the Button. |
| `icon` | icon |  |  |  | The icon to display on the Button. |
| `spacing` | spacing |  |  |  | The spacing (pixels) of the button. |
| `button_font_family` | string |  |  |  | The font family to use for the Button |
| `menu_background_color` | color |  |  |  | The color of the background of the Menu |
| `menu_border` | string |  |  |  | The border of the Menu. Can take any valid CSS border value. |
| `align` | enum | left, center, right, full | left |  | The position of this component in the available space. |
| `menu_items` | object |  |  |  | A list of components to be added to the menu |

## `m3._Components.Card`

Specification: `Card.md`.

Events: `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `align` | enum | left, center, right, full | left |  | The position of this component in the available space. |
| `appearance` | enum | elevated, filled, outlined | elevated |  | A predefined style for this component. |
| `spacing` | spacing |  |  |  | The margin and padding (pixels) of the component. |
| `background_color` | color |  |  |  | The colour of the background of this component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `border` | string |  |  |  | The border of this component. Can take any valid CSS border value. |
| `orientation` | enum | column, row | column |  | The orientation of the content in this Card |

## `m3._Components.Card.CardContentContainer`

Specification: this file.

Events: `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `margin` | margin |  | 16, 16, 16, 16 |  | The margin (pixels) of this component |

## `m3._Components.Carousel`

Specification: `Carousel.md`.

Events: `item_click`, `change`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `layout` | enum | multi_browse, hero, center_hero, uncontained, full_width | multi_browse |  | multi_browse: large, medium and small items. hero: one large and one small item. center_hero: one large item between two small ones. uncontained: items of one size that scroll freely. full_width: one item at a time, the full width. |
| `images` | text[] |  |  |  | Pictures to show, one per line: an asset path such as _/theme/photo.jpg (a file uploaded to Assets), or a web address. Each becomes an item, cropped to fill it. |
| `item_width` | number |  | 186 |  | The width in pixels that large items aim for (multi_browse), or that every item has (uncontained). |
| `item_height` | number |  | 220 |  | The height of the items in pixels. |
| `index` | number |  | 0 |  | The position of the first large item (from 0). Set it to move the carousel. |
| `label` | string |  | Carousel |  | A name for the carousel that screen readers announce. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.Checkbox`

Specification: this file.

Events: `change`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `checked` | boolean |  | False | yes (change) | Whether or not the checkbox is checked. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `error` | boolean |  | False |  | Whether or not the checkbox is in an error state. |
| `text` | string |  |  |  | The text displayed on this component. |
| `allow_indeterminate` | boolean |  | False |  | Support an indeterminate state. The indeterminate state can only be set in code by setting checked=None. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `underline` | boolean |  | False |  | If True, this component’s text will be underlined. |
| `italic` | boolean |  | False |  | If True, this component’s text will be italic. |
| `font_size` | number |  |  |  | The font size of the text displayed on this component. |
| `bold` | boolean |  | False |  | If True, this component’s text will be bold. |
| `border` | string |  |  |  | The border of this component. Can take any valid CSS border value. |
| `font_family` | string |  |  |  | The font family to use for this component. |
| `checkbox_color` | color |  |  |  | The color of the checkbox. |
| `text_color` | color |  |  |  | The colour of the text on the component. |
| `background_color` | color |  |  |  | The colour of the background of this component. |
| `align` | enum | left, center, right | left |  | The position of this component in the available space. |
| `spacing` | spacing |  |  |  | The margin and padding (pixels) of the component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |

## `m3._Components.Chip`

Specification: `Chip.md`.

Events: `click`, `change`, `remove`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `text` | string |  | Chip |  | The text displayed on the Chip. |
| `type` | enum | assist, filter, input, suggestion | assist |  | The kind of Chip: assist (a smart action), filter (a toggled choice), input (a piece of entered information) or suggestion (a suggested reply or search). |
| `selected` | boolean |  | False | yes (change) | If True, a filter or input Chip is selected. |
| `leading_icon` | icon |  |  |  | An icon shown before the text. |
| `elevated` | boolean |  | False |  | If True, an assist, filter or suggestion Chip is raised with a shadow instead of an outline. |
| `removable` | boolean |  | False |  | If True, the Chip shows a remove icon, which raises the remove event. Meant for input Chips. |
| `enabled` | boolean |  | True |  | If True, the Chip can be clicked. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.CircularProgressIndicator`

Specification: this file.

Events: `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `type` | enum | determinate, indeterminate | indeterminate |  | Display a determinate or indeterminate progress indicator. Use determinate to set the progress with the progress property. Use indeterminate to express an unspecified amount of wait time. |
| `progress` | number |  | 0 |  | The percentage of progress for the determinate type indicator. This property is irrelevant for the indeterminate type. |
| `wavy` | boolean |  | False |  | If True, the indicator is drawn as an M3 Expressive wave. |
| `align` | enum | left, center, right | left |  | The position of this component in the available space. |
| `margin` | margin |  |  |  | The margin (pixels) of the component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `color` | color |  |  |  | The color of this component. |

## `m3._Components.DatePicker`

Specification: `DatePicker.md`.

Events: `change`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `date` | object |  |  | yes (change) | The chosen date, as a datetime.date. None when empty. |
| `label` | string |  | Date |  | The label of the field. |
| `format` | string |  | %d/%m/%Y |  | How the date is written in the field, using %d (day), %m (month number), %b (short month name), %B (month name), %Y (year) and %y (two-digit year). |
| `min_date` | object |  |  |  | The earliest date that can be chosen, as a datetime.date. None for no limit. |
| `max_date` | object |  |  |  | The latest date that can be chosen, as a datetime.date. None for no limit. |
| `week_starts_on` | enum | monday, sunday | monday |  | The first day of the week in the calendar. |
| `appearance` | enum | filled, outlined | outlined |  | The look of the field. |
| `supporting_text` | string |  |  |  | A line of help text below the field. |
| `enabled` | boolean |  | True |  | If True, the date can be changed. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.Dialog`

Specification: `Dialog.md`.

Events: `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `headline` | string |  |  |  | The headline (title) of the Dialog. |
| `supporting_text` | string |  |  |  | The supporting text below the headline. |
| `icon` | icon |  |  |  | An icon shown above the headline. Basic dialogs only. |
| `full_screen` | boolean |  | False |  | If True, the Dialog fills the whole screen, with a close button and the actions in a top bar. |
| `dismissible` | boolean |  | True |  | If True, the user can dismiss the Dialog by clicking outside it or pressing Escape. show() then returns None. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.Divider`

Specification: this file.

Events: `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `type` | enum | full_width, inset | full_width |  | Display the Divider across the full width of the container or inset. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `color` | color |  |  |  | The colour of this component. |
| `margin` | margin |  |  |  | The margin (pixels) of the component. |

## `m3._Components.DropdownMenu`

Specification: this file.

Events: `change`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `background_color` | color |  |  |  | The colour of the background of this component. |
| `label_bold` | boolean |  | False |  | If True, the label text will be bold |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `label_font_family` | string |  |  |  | The font family to use for this component's label |
| `label_font_size` | number |  |  |  | The height of text displayed on this component's label in pixels |
| `label_color` | color |  |  |  | The colour of the label text on the component. |
| `label_italic` | boolean |  | False |  | If True, the label text will be italic |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `align` | enum | left, center, right, full | left |  | The position of this component in the available space. |
| `items` | text[] |  |  |  | The items to display in the menu |
| `placeholder` | string |  |  |  | The text to be displayed when the selected_value is None |
| `appearance` | enum | filled, outlined | filled |  | A predefined style for this component. |
| `selected_value` | object |  |  | yes (change) | The value of the currently selected item. Can only be set at runtime. |
| `label_underline` | boolean |  | False |  | If True, the label text will be underlined |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `label` | string |  |  |  | Label text associated with the component. Usually the prompt. |
| `items_bold` | boolean |  | False |  | If True, the menu items will be bold |
| `items_italic` | boolean |  | False |  | If True, the menu items will be italic |
| `items_underline` | boolean |  | False |  | If True, the menu items will be underlined |
| `items_text_color` | color |  |  |  | The colour of the menu items' text |
| `menu_background_color` | color |  |  |  | The background colour of the menu |
| `items_font_family` | string |  |  |  | The font family to use for the menu items |
| `items_font_size` | number |  |  |  | The font size of the menu items |
| `allow_none` | boolean |  | False |  | If True, a placeholder item is added to the menu with value None |
| `selected_italic` | boolean |  | False |  | If True and there is a selected item, the displayed text is in italic. |
| `selected_bold` | boolean |  | False |  | If True and there is a selected item, the displayed text is bold |
| `selected_underline` | boolean |  | False |  | If True and there is a selected item, the displayed text is underlined |
| `selected_font_family` | string |  |  |  | The font-family of the displayed text if there is a selected item |
| `selected_font_size` | number |  |  |  | The font size (pixels) of the displayed text if there is a selected item |
| `selected_text_color` | color |  |  |  | The colour of the displayed text if there is a selected item |
| `margin` | margin |  |  |  | The margin (pixels) of the component. |
| `error` | boolean |  | False |  | If True, this component is in an error state. |
| `icon` | icon |  |  |  | The leading icon to display on this component. |
| `icon_color` | color |  |  |  | The colour of the leading icon |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component |
| `supporting_text` | string |  |  |  | The supporting text displayed underneath this component |
| `supporting_text_color` | color |  |  |  | The colour of the supporting text underneath this component |
| `supporting_text_font_size` | number |  |  |  | The font size of the supporting text displayed underneath this component |
| `supporting_text_font_family` | string |  |  |  | The font family to use for the supporting text underneath this component |
| `border_color` | color |  |  |  |  |

## `m3._Components.FabMenu`

Specification: `FabMenu.md`.

Events: `item_click`, `opened`, `closed`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `icon` | icon |  | mi:add |  | The icon on the button while the menu is closed. |
| `items` | text[] |  |  |  | The actions in the menu, one per line, from top to bottom. |
| `item_icons` | text[] |  |  |  | Optional: one icon per action, such as mi:mail, one per line in the same order as items. |
| `color` | enum | primary, secondary, tertiary | primary |  | The colour set: the button is X Container while closed and X while open; the actions are X Container. |
| `size` | enum | regular, medium, large | regular |  | The size of the button while the menu is closed. It is always 56 px while open. |
| `floating` | boolean |  | False |  | If True, the button floats in the bottom right corner of the window. |
| `label` | string |  | Actions |  | A name for the button and its menu that screen readers announce. |
| `enabled` | boolean |  | True |  | If True, the button can be clicked. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.FileLoader`

Specification: this file.

Events: `change`, `focus`, `lost_focus`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `file` | object |  |  |  | The currently selected file (or the first, if multiple files are selected). This is a Media object. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `file_types` | string |  |  |  | Specify what type of file to upload. Can accept a MIME type (eg "image/png" or "image/*"), an extension (eg ".png") or a comma-separated set of them (eg ".png,.jpg,.jpeg") |
| `files` | object |  |  |  | A list of currently selected files. Each file is a Media object. |
| `multiple` | boolean |  | False |  | If True, this FileLoader can load multiple files at the same time |
| `show_state` | boolean |  | False |  | If True, display a message indicating the number of selected files. |
| `text` | string |  | File upload |  | The text displayed on this component. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `icon` | icon |  | mi:file_upload |  |  |
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `text_color` | color |  |  |  | The colour of the text on the component. |
| `icon_color` | color |  |  |  | The colour of the icon displayed on this component. |
| `background_color` | color |  |  |  | The colour of the background of this component. |
| `underline` | boolean |  | False |  | If True, this component’s text will be underlined. |
| `italic` | boolean |  | False |  | If True, this component’s text will be italic. |
| `bold` | boolean |  | False |  | If True, this component’s text will be bold. |
| `font_family` | string |  |  |  | The font family to use for this component. |
| `font_size` | number |  |  |  | The font size of the text displayed on this component. |
| `icon_size` | number |  |  |  | The size (pixels) of the icon displayed on this component. |
| `align` | enum | left, center, right, full | left |  | The position of this component in the available space. |
| `border` | string |  |  |  | The border of this component. Can take any valid CSS border value. |
| `spacing` | spacing |  |  |  | The margin and padding (pixels) of the component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `appearance` | enum | text, elevated, filled, tonal, outlined | text |  | A predefined style for this component. |

## `m3._Components.FloatingActionButton`

Specification: `FloatingActionButton.md`.

Events: `click`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `icon` | icon |  | mi:add |  | The icon on the button. |
| `text` | string |  |  |  | A label after the icon. With a label, the button is an extended FAB. |
| `size` | enum | regular, medium, large | regular |  | The size: regular (56 px), medium (80 px) or large (96 px). |
| `appearance` | enum | primary_container, secondary_container, tertiary_container, primary, secondary, tertiary | primary_container |  | The colour: the three container colours are tonal, the three plain colours are filled and stronger. |
| `floating` | boolean |  | False |  | If True, the button floats in the bottom right corner of the window, above the page. |
| `tooltip` | string |  |  |  | A description of the action for screen readers. Needed when the button has no label. |
| `enabled` | boolean |  | True |  | If True, the button can be clicked. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.Heading`

Specification: this file.

Events: `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `style` | enum | display, headline, title | headline |  | Role of the heading component: display, headline or title |
| `scale` | enum | small, medium, large | medium |  | Size of the heading component |
| `font_size` | number |  |  |  | The font size of the text displayed on this component. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `font_family` | string |  |  |  | The font family to use for this component. |
| `bold` | boolean |  | False |  | If True, this component’s text will be bold. |
| `italic` | boolean |  | False |  | If True, this component’s text will be italic. |
| `text` | string |  |  |  | The text displayed on this component. |
| `underline` | boolean |  | False |  | If True, this component’s text will be underlined. |
| `visible` | boolean |  | True |  | If True |
| `icon` | icon |  |  |  | The icon to display on this component. |
| `text_color` | color |  |  |  | The colour of the text on the component. |
| `background_color` | color |  |  |  | The background colour of this component. |
| `border` | string |  |  |  | The border of this component. Can take any valid CSS border value. |
| `align` | enum | left, center, right, justify | left |  | The position of this component in the available space. |
| `icon_size` | number |  |  |  | The size (pixels) of the icon displayed on this component. |
| `icon_color` | color |  |  |  | The colour of the icon displayed on this component. |
| `spacing` | spacing |  |  |  | The margin and padding (pixels) of the component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `line_height` | string |  |  |  | The line height of the component |

## `m3._Components.IconButton`

Specification: `IconButton.md`.

Events: `click`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `appearance` | enum | standard, filled, tonal, outlined | standard |  | A predefined style for this component. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `size` | enum | standard, xsmall, small, medium, large, xlarge | standard |  | m3x: standard (the base icon button), or an M3 Expressive size: xsmall (32 px), small (40 px), medium (56 px), large (96 px) or xlarge (136 px). |
| `button_width` | enum | narrow, default, wide | default |  | m3x: narrow, default or wide: the space beside the icon, for Expressive sizes. |
| `shape` | enum | round, square | round |  | m3x: round (a circle or pill) or square (rounded corners). A selected ToggleIconButton switches to the other shape. |
| `icon` | icon |  | mi:star |  | Icon to display on button |
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `border` | string |  |  |  | Custom border of this component. Can take any valid CSS border value. |
| `background_color` | color |  |  |  | The colour of the background of this component. |
| `icon_color` | color |  |  |  | The colour of the icon displayed on this component. |
| `align` | enum | left, center, right | left |  | The position of this component in the available space. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `margin` | margin |  |  |  | The margin (pixels) of the component. |

## `m3._Components.IconButtonMenu`

Specification: this file.

Events: `click`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `menu_border` | string |  |  |  | The border of the menu. Can take any valid CSS border value. |
| `menu_background_color` | color |  |  |  | The color of the background of the menu. |
| `appearance` | enum | standard, filled, tonal, outlined | standard |  | A predefined style for this component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `button_border` | string |  |  |  | The border of the IconButton. Can take any valid CSS border value. |
| `button_background_color` | color |  |  |  | Color of the background of the IconButton. |
| `icon` | icon |  | mi:star |  | The icon to display on the IconButton. |
| `icon_color` | color |  |  |  | The color of the icon displayed on the IconButton. |
| `margin` | margin |  |  |  | The margin (pixels) of the button. |
| `align` | enum | left, center, right | left |  | The position of this component in the available space. |
| `role` | string |  |  |  |  |
| `menu_items` | object |  |  |  | A list of components to be added to the menu |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.InteractiveCard`

Specification: this file.

Events: `click`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `align` | enum | left, center, right, full | left |  | The position of this component in the available space. |
| `appearance` | enum | elevated, filled, outlined | elevated |  | A predefined style for this component. |
| `spacing` | spacing |  |  |  | The margin and padding (pixels) of the component. |
| `background_color` | color |  |  |  | The colour of the background of this component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `border` | string |  |  |  | The border of this component. Can take any valid CSS border value. |
| `orientation` | enum | column, row | column |  | The orientation of the content in this Card |

## `m3._Components.LinearProgressIndicator`

Specification: this file.

Events: `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `type` | enum | determinate, indeterminate | indeterminate |  | Display a determinate or indeterminate progress indicator. Use determinate to set the progress with the progress property. Use indeterminate to express an unspecified amount of wait time. |
| `progress` | number |  | 0 |  | The percentage of progress for the determinate type indicator. This property is irrelevant for the indeterminate type. |
| `wavy` | boolean |  | False |  | If True, the indicator is drawn as an M3 Expressive wave. |
| `margin` | margin |  |  |  | The margin (pixels) of the component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `progress_color` | color |  |  |  | The color of the progress bar. |
| `track_color` | color |  |  |  | The color of the track |

## `m3._Components.Link`

Specification: this file.

Events: `click`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `text` | string |  |  |  | The text displayed on this component. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `url` | string |  |  |  | The target URL of the link. Can be set to a URL string or to a Media object. |
| `align` | enum | left, center, right | left |  | The position of this component in the available space. |
| `bold` | boolean |  | False |  | If True, this component’s text will be bold. |
| `italic` | boolean |  | False |  | If True, this component’s text will be italic. |
| `font_family` | string |  |  |  | The font family to use for this component. |
| `font_size` | number |  |  |  | The font size of the text displayed on this component. |
| `icon` | icon |  |  |  |  |
| `underline` | boolean |  | True |  | If True, this component’s text will be underlined. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `text_color` | color |  |  |  | The colour of the text on the component. |
| `icon_color` | color |  |  |  | The colour of the icon displayed on this component. |
| `icon_size` | number |  | 24 |  | The size (pixels) of the icon displayed on this component. |
| `border` | string |  |  |  | The border of this component. Can take any valid CSS border value. |
| `spacing` | spacing |  |  |  | The margin and padding (pixels) of the component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `background_color` | color |  |  |  | The color of the background of this component |

## `m3._Components.ListItem`

Specification: `ListItem.md`.

Events: `click`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `headline` | string |  | List item |  | The main text of the item. |
| `supporting_text` | string |  |  |  | A second line of text below the headline. |
| `overline` | string |  |  |  | A small line of text above the headline. |
| `three_line` | boolean |  | False |  | If True, the supporting text may take two lines and the item is 88 px high. |
| `leading_icon` | icon |  |  |  | An icon at the start of the item. |
| `leading_avatar_text` | string |  |  |  | Text (usually initials) shown in a round avatar at the start of the item. |
| `leading_image` | uri |  |  |  | An image shown at the start of the item. |
| `trailing_text` | string |  |  |  | A short text at the end of the item, such as a time or a count. |
| `trailing_icon` | icon |  |  |  | An icon at the end of the item. |
| `clickable` | boolean |  | False |  | If True, the item reacts to the mouse and keyboard and raises the click event. |
| `selected` | boolean |  | False |  | If True, the item is shown as selected. |
| `enabled` | boolean |  | True |  | If True, a clickable item can be clicked. |
| `divider` | boolean |  | False |  | If True, a thin line is drawn under the item. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.LoadingIndicator`

Specification: `LoadingIndicator.md`.

Events: `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `contained` | boolean |  | False |  | If True, the shape sits in a round coloured container, for use on top of other content. |
| `label` | string |  | Loading |  | The name of the indicator for screen readers. |
| `align` | enum | left, center, right | left |  | The position of this component in the available space. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.MenuItem`

Specification: this file.

Events: `click`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `selected` | boolean |  | False |  | m3x: If True, the item is shown as selected, for example the current choice. Its colours follow the app menu style (m3x_theming.set_menu_style). |
| `leading_icon` | icon |  |  |  | The leading icon to display on this component. |
| `text` | string |  |  |  | The main text displayed on this component |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `trailing_icon` | icon |  |  |  | The trailing icon to display on this component. |
| `trailing_text` | string |  |  |  | The text to be displayed on the right side of the component. Will be to the left of the trailing icon if both exist. |
| `add_icon_space` | boolean |  | False |  | If True, add a space where the leading_icon would be so that this MenuItem is aligned with MenuItems with leading_icons. |
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `bold` | boolean |  | False |  | If True, the main text will be bold. |
| `font_family` | string |  |  |  | The font family to use for the main text. |
| `font_size` | number |  |  |  | The font size of the text displayed on this component. |
| `text_color` | color |  |  |  | The colour of the text on the component. |
| `italic` | boolean |  | False |  | If True, the main text will be italic. |
| `underline` | boolean |  | False |  | If True, the main text will be underlined. |
| `background_color` | color |  |  |  | The colour of the background of this component. |
| `visible` | boolean |  | True |  | If True, this component will be displayed |
| `leading_icon_size` | number |  |  |  | The size (pixels) of the leading icon displayed on this component |
| `trailing_icon_size` | number |  |  |  | The size (pixels) of the trailing icon displayed on this component |
| `leading_icon_color` | color |  |  |  | The colour of the leading icon displayed on this component |
| `trailing_icon_color` | color |  |  |  | The colour of the trailing icon displayed on this component |
| `role` | string |  |  |  | A style for this component defined in CSS and added to Roles. |
| `spacing` | spacing |  |  |  | The margin and padding (pixels) of the component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |

## `m3._Components.NavigationBar`

Specification: `NavigationBar.md`.

Events: `change`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `items` | text[] |  | Home, Search, Profile |  | The label of each destination, one per line. Use three to five destinations. |
| `icons` | text[] |  | mi:home, mi:search, mi:person |  | One icon per destination, in the same order as the items, one per line, for example mi:home. |
| `selected_index` | number |  | 0 |  | The position of the selected destination, counting from 0. |
| `badges` | object |  |  |  | Optional: one badge per destination, as a list. None means no badge, 0 means a small dot, a number shows that number. For example [None, 3, 0]. |
| `fixed` | boolean |  | False |  | If True, the bar is fixed to the bottom edge of the window. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.NavigationLink`

Specification: this file.

Events: `click`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `url` | string |  |  |  | The target URL of the link |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `text` | string |  | Label |  | The text displayed on this component. |
| `selected` | boolean |  | False |  | If True, the component is in the selected state. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `badge` | boolean |  | False |  | If True, display a notification badge on the icon. |
| `badge_count` | number |  |  |  | The number to display on the badge |
| `text_color` | color |  |  |  | The colour of the text on the component. |
| `font_size` | string |  |  |  | The font size of the text displayed on this component. |
| `font_family` | string |  |  |  | The font family to use for this component. |
| `icon_color` | color |  |  |  | The colour of the icon displayed on this component. |
| `icon_size` | string |  |  |  | The size (pixels) of the icon displayed on this component. |
| `icon` | icon |  | mi:star |  | The icon to display on this component. |
| `navigate_to` | form |  |  |  | The Form to navigate to when the link is clicked |
| `spacing` | spacing |  |  |  | The margin and padding (pixels) of the component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `italic` | boolean |  | False |  | If True, this component’s text will be italic. |
| `underline` | boolean |  | False |  | If True, this component’s text will be underlined. |
| `bold` | boolean |  | False |  | If True, this component’s text will be bold. |
| `background_color` | color |  |  |  | The color of the background of this component |

## `m3._Components.PaneLayout`

Specification: `PaneLayout.md`.

Events: `width_class_change`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `layout` | enum | list_detail, supporting | list_detail |  | list_detail: a list (primary pane) and the chosen item's detail (secondary pane); on narrow windows one pane at a time. supporting: main content (primary pane) with a supporting pane; on narrow windows the supporting pane goes below. |
| `show_secondary` | boolean |  | False |  | list_detail on narrow windows: if True the secondary (detail) pane is shown, otherwise the primary (list) pane. Wide windows show both. |
| `fixed_pane_width` | number |  | 360 |  | The width in pixels of the fixed pane on wide windows: the list in list_detail, the supporting pane in supporting. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.RadioButton`

Specification: this file.

Events: `select`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `selected` | boolean |  | False |  | If True, the component is in the selected state. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `text` | string |  |  |  | The text displayed on this component. |
| `value` | string |  |  |  | The value of the group when this radio button is selected |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `align` | enum | left, center, right | left |  | The position of this component in the available space. |
| `background_color` | color |  |  |  | The colour of the background of this component. |
| `bold` | boolean |  | False |  | If True, this component’s text will be bold. |
| `border` | string |  |  |  | The border of this component. Can take any valid CSS border value. |
| `font_family` | string |  |  |  | The font family to use for this component. |
| `font_size` | number |  |  |  | The font size of the text displayed on this component. |
| `text_color` | color |  |  |  | The colour of the text on the component. |
| `italic` | boolean |  | False |  | If True, this component’s text will be italic. |
| `underline` | boolean |  | False |  | If True, this component’s text will be underlined. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `spacing` | spacing |  |  |  | The margin and padding (pixels) of the component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `radio_color` | color |  |  |  | The color of the radio button. |
| `group` | object |  |  |  | This button's RadioGroup. No more than one RadioButton in any RadioGroup can be selected at a time. If this radio button is placed inside a RadioGroupPanel, by default this property will refer to that RadioGroupPanel. If this radio button has no enclosing RadioGroupPanel, by default this property will refer to to a global RadioGroup containing all radio buttons that don't have an enclosing RadioGroupPanel. You can override this default by manually setting this property to a RadioGroup object. |

## `m3._Components.RadioGroupPanel`

Specification: this file.

Events: `change`, `hide`, `show`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `selected_value` | object |  |  | yes | Value property of the selected RadioButton |

## `m3._Components.SearchBar`

Specification: `SearchBar.md`.

Events: `search`, `change`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `text` | string |  |  | yes (change) | The text in the search bar. |
| `placeholder` | string |  | Search |  | The text shown in the empty search bar. |
| `suggestions` | text[] |  |  |  | Suggestions shown below the bar while the user types, one per line. The list shows the suggestions that contain the typed text. |
| `max_suggestions` | number |  | 8 |  | The largest number of suggestions shown at once. |
| `enabled` | boolean |  | True |  | If True, the user can type in the search bar. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.SidesheetContent`

Specification: this file.

Events: none.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|

## `m3._Components.Slider`

Specification: `Slider.md`.

Events: `change`, `change_end`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `size` | enum | standard, small, medium, large, xlarge | standard |  | m3x: standard (the base slider, M3 Expressive extra small: 16 px track), or an Expressive size: small (24 px track), medium (40 px), large (56 px) or xlarge (96 px). |
| `value` | number |  |  | yes (change_end) | The value of the slider |
| `show_label` | boolean |  | False |  | Display a label above the thumb |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `progress_color` | color |  |  |  | The colour of the progress bar. |
| `track_color` | color |  |  |  | The colour of the track. |
| `thumb_color` | color |  |  |  | The colour of the Slider thumb. |
| `label_color` | color |  |  |  | The colour of the background of the label. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `label_text_color` | color |  |  |  | The colour of the text of the label. |
| `min` | number |  | 0 |  | The minimum value of the Slider. |
| `max` | number |  | 10 |  | The maximum value of the Slider. |
| `step` | number |  |  |  | The stepping interval for the Slider |
| `margin` | margin |  | , , ,  |  | The margin (pixels) of the component. |
| `show_markers` | boolean |  | False |  | If True, display discrete markers on the track. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |

## `m3._Components.SplitButton`

Specification: `SplitButton.md`.

Events: `click`, `item_click`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `text` | string |  | Save |  | The label of the main action. |
| `icon` | icon |  |  |  | An optional icon before the label. |
| `menu_items` | text[] |  |  |  | The options in the menu that the arrow opens, one per line. |
| `appearance` | enum | filled, tonal, elevated, outlined | filled |  | The colours of the button. |
| `size` | enum | xsmall, small, medium, large, xlarge | small |  | The size of the button. |
| `enabled` | boolean |  | True |  | If True, the button can be clicked. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.Switch`

Specification: this file.

Events: `change`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `selected_icon` | icon |  |  |  | Optional icon to appear on the Switch when toggled on. |
| `selected` | boolean |  | False | yes (change) | If True, this component is toggled on. |
| `unselected_icon` | icon |  |  |  | Optional icon on the Switch when toggled off. |
| `unselected_background_color` | color |  |  |  | The background colour of the component when toggled off. |
| `selected_background_color` | color |  |  |  | The background colour of the component when toggled on. |
| `unselected_thumb_color` | color |  |  |  | The colour of the Switch thumb when toggled off. |
| `selected_thumb_color` | color |  |  |  | The colour of the Switch thumb when toggled on. |
| `unselected_outline_color` | color |  |  |  | The colour of the outline of the Switch when toggled off. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `align` | enum | left, center, right | left |  | The position of this component in the available space. |
| `margin` | margin |  | , , ,  |  | The margin (pixels) of the component. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |

## `m3._Components.Tabs`

Specification: `Tabs.md`.

Events: `change`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `items` | text[] |  | Tab 1, Tab 2, Tab 3 |  | The label of each tab, one per line. |
| `icons` | text[] |  |  |  | Optional: one icon per tab, in the same order as the items, one per line, for example mi:home. Leave empty for tabs without icons. |
| `selected_index` | number |  | 0 | yes (change) | The position of the selected tab, counting from 0. |
| `type` | enum | primary, secondary | primary |  | primary tabs sit at the top of a page and switch its main views. secondary tabs sit inside a part of a page and switch its content. |
| `scrollable` | boolean |  | False |  | If True, tabs keep their natural width and the row scrolls sideways. If False, the tabs share the width equally. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.Text`

Specification: this file.

Events: `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `style` | enum | body, label | body |  | Role of the text component: body or label |
| `scale` | enum | small, medium, large | medium |  | Size of the text component |
| `align` | enum | left, center, right, justify | left |  | The position of this component in the available space. |
| `background_color` | color |  |  |  | The background colour of this component. |
| `bold` | boolean |  | False |  | If True, this component’s text will be bold. |
| `border` | string |  |  |  | The border of this component. Can take any valid CSS border value. |
| `font_family` | string |  |  |  | The font family to use for this component. |
| `font_size` | number |  |  |  | The font size of the text displayed on this component. |
| `text_color` | color |  |  |  | The colour of the text on the component. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles |
| `icon` | icon |  |  |  | The icon to display on this component. |
| `italic` | boolean |  | False |  | If True, this component’s text will be italic. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `text` | string |  |  |  | The text displayed on this component. |
| `underline` | boolean |  | False |  | If True, this component’s text will be underlined. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `icon_size` | number |  |  |  | The size (pixels) of the icon displayed on this component. |
| `icon_color` | color |  |  |  | The colour of the icon displayed on this component. |
| `spacing` | spacing |  |  |  | The margin and padding (pixels) of the component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `line_height` | string |  |  |  | The line height of the component |

## `m3._Components.TextInput.TextArea`

Specification: this file.

Events: `change`, `show`, `hide`, `focus`, `lost_focus`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `text` | string |  | None | yes | The input text displayed on this component |
| `height` | number |  |  |  | The initial height of this TextArea |
| `label` | string |  |  |  | The label text of the component. |
| `placeholder` | string |  |  |  | The text to be displayed when the component is empty. |
| `supporting_text` | string |  |  |  | The supporting text displayed underneath this component |
| `character_limit` | number |  | 0 |  | The max number of characters a user can enter into this component. The limit is displayed below the component. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles |
| `align` | enum | left, center, right | left |  | The position of this component in the available space. |
| `appearance` | enum | filled, outlined | filled |  | A predefined style for this component. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `label_color` | color |  |  |  | The colour of the label text on the component. |
| `label_bold` | boolean |  | False |  | If True, the label text will be bold. |
| `label_italic` | boolean |  | False |  | If True, the label text will be italic. |
| `label_underline` | boolean |  | False |  | If True, the label text will be underlined. |
| `label_font_size` | number |  |  |  | The font size of the label text on this component. |
| `label_font_family` | string |  |  |  | The font family to use for the label on this component. |
| `display_bold` | boolean |  | False |  | If True, the input and placeholder text will be bold. |
| `display_italic` | boolean |  | False |  | If True, the input and placeholder text will be italic. |
| `display_underline` | boolean |  | False |  | If True, the input and placeholder text will be underlined. |
| `display_font_family` | string |  |  |  | The font family to use for the input and placeholder text. |
| `display_text_color` | color |  |  |  | The colour of the input text displayed on this component. |
| `display_font_size` | number |  |  |  | The font size of the input and placeholder text. |
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `error` | boolean |  | False |  | If True, this component is in an error state. |
| `margin` | margin |  |  |  | The margin (pixels) of this component. |
| `background_color` | color |  |  |  | The colour of the background of this component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `border_color` | color |  |  |  | The colour of the border of this component. |
| `subcontent_color` | color |  |  |  | The colour of the supporting text and the character limit underneath this component. |
| `subcontent_font_family` | string |  |  |  | The font family of the supporting text and the character limit displayed underneath this component. |
| `subcontent_font_size` | number |  |  |  | The font size of the supporting text and character limit displayed underneath this component. |

## `m3._Components.TextInput.TextBox`

Specification: this file.

Events: `trailing_icon_click`, `pressed_enter`, `change`, `show`, `hide`, `focus`, `lost_focus`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `text` | string |  | None | yes | The text displayed on this component. |
| `leading_icon` | icon |  | None |  | The leading icon to display on this component. |
| `trailing_icon` | icon |  | None |  | The trailing icon to display on this component. |
| `type` | enum | text, number, email, tel, url | text |  | The type of data that the user can enter into this box. |
| `hide_text` | boolean |  | False |  | If True, display stars instead of text when the user types input into this component. |
| `leading_icon_color` | color |  |  |  | The colour of the leading icon. |
| `trailing_icon_color` | color |  |  |  | The colour of the trailing icon. |
| `label` | string |  |  |  | The label text of the component. |
| `placeholder` | string |  |  |  | The text to be displayed when the component is empty. |
| `supporting_text` | string |  |  |  | The supporting text displayed underneath this component |
| `character_limit` | number |  | 0 |  | The max number of characters a user can enter into this component. The limit is displayed below the component. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles |
| `align` | enum | left, center, right | left |  | The position of this component in the available space. |
| `appearance` | enum | filled, outlined | filled |  | A predefined style for this component. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `label_color` | color |  |  |  | The colour of the label text on the component. |
| `label_bold` | boolean |  | False |  | If True, the label text will be bold. |
| `label_italic` | boolean |  | False |  | If True, the label text will be italic. |
| `label_underline` | boolean |  | False |  | If True, the label text will be underlined. |
| `label_font_size` | number |  |  |  | The font size of the label text on this component. |
| `label_font_family` | string |  |  |  | The font family to use for the label on this component. |
| `display_bold` | boolean |  | False |  | If True, the input and placeholder text will be bold. |
| `display_italic` | boolean |  | False |  | If True, the input and placeholder text will be italic. |
| `display_underline` | boolean |  | False |  | If True, the input and placeholder text will be underlined. |
| `display_font_family` | string |  |  |  | The font family to use for the input and placeholder text. |
| `display_text_color` | color |  |  |  | The colour of the input text displayed on this component. |
| `display_font_size` | number |  |  |  | The font size of the input and placeholder text. |
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `error` | boolean |  | False |  | If True, this component is in an error state. |
| `margin` | margin |  |  |  | The margin (pixels) of this component. |
| `background_color` | color |  |  |  | The colour of the background of this component. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `border_color` | color |  |  |  | The colour of the border of this component. |
| `subcontent_color` | color |  |  |  | The colour of the supporting text and the character limit underneath this component. |
| `subcontent_font_family` | string |  |  |  | The font family of the supporting text and the character limit displayed underneath this component. |
| `subcontent_font_size` | number |  |  |  | The font size of the supporting text and character limit displayed underneath this component. |

## `m3._Components.TimePicker`

Specification: `TimePicker.md`.

Events: `change`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `time` | object |  |  | yes (change) | The chosen time, as a datetime.time. None when empty. |
| `label` | string |  | Time |  | The label of the field. |
| `format_24h` | boolean |  | True |  | If True, the time uses the 24-hour clock (14:30). If False, the 12-hour clock with AM and PM (2:30 PM). |
| `appearance` | enum | filled, outlined | outlined |  | The look of the field. |
| `supporting_text` | string |  |  |  | A line of help text below the field. |
| `enabled` | boolean |  | True |  | If True, the time can be changed. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.ToggleIconButton`

Specification: this file.

Events: `click`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |
| `selected` | boolean |  | False |  | If True, the component is in the selected state |
| `selected_border` | string |  |  |  | The border style when the component is in the selected state. Accepts any valid CSS border value. |
| `selected_background_color` | color |  |  |  | The background color when the component is in the selected state. |
| `selected_icon_color` | color |  |  |  | The icon color when the component is in the selected state. |
| `appearance` | enum | standard, filled, tonal, outlined | standard |  | A predefined style for this component. |
| `size` | enum | standard, xsmall, small, medium, large, xlarge | standard |  | m3x: standard (the base icon button), or an M3 Expressive size: xsmall (32 px), small (40 px), medium (56 px), large (96 px) or xlarge (136 px). |
| `button_width` | enum | narrow, default, wide | default |  | m3x: narrow, default or wide: the space beside the icon, for Expressive sizes. |
| `shape` | enum | round, square | round |  | m3x: round (a circle or pill) or square (rounded corners). A selected ToggleIconButton switches to the other shape. |
| `icon` | icon |  | mi:star |  | Icon to display on button |
| `enabled` | boolean |  | True |  | If True, this component allows user interaction. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `border` | string |  |  |  | Custom border of this component. Can take any valid CSS border value. |
| `background_color` | color |  |  |  | The colour of the background of this component. |
| `icon_color` | color |  |  |  | The colour of the icon displayed on this component. |
| `align` | enum | left, center, right | left |  | The position of this component in the available space. |
| `tooltip` | string |  |  |  | The text to display when the mouse is hovered over this component. |
| `margin` | margin |  |  |  | The margin (pixels) of the component. |

## `m3._Components.Toolbar`

Specification: `Toolbar.md`.

Events: `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `variant` | enum | floating, docked | floating |  | floating: a rounded bar that floats over the content. docked: a full-width bar along the bottom (replaces the bottom app bar). |
| `color_style` | enum | standard, vibrant | standard |  | standard: a quiet surface colour. vibrant: the primary container colour, for more emphasis. |
| `vertical` | boolean |  | False |  | If True, a floating toolbar is a vertical column. Docked toolbars are always horizontal. |
| `pin_to_screen` | boolean |  | False |  | If True, the toolbar is fixed to the window: a docked toolbar along the bottom edge; a floating toolbar 16 px above the bottom centre, or 16 px from the right edge when vertical. |
| `hide_on_scroll` | boolean |  | False |  | If True, a toolbar pinned to the screen slides away while the user scrolls down and comes back when the user scrolls up. |
| `label` | string |  | Toolbar |  | A name for the toolbar that screen readers announce. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

## `m3._Components.TopAppBar`

Specification: `TopAppBar.md`.

Events: `navigation_click`, `show`, `hide`.

| Property | Type | Options | Default | Writeback | Description |
|---|---|---|---|---|---|
| `title` | string |  | Title |  | The title of the page. |
| `subtitle` | string |  |  |  | A smaller line of text below the title. |
| `size` | enum | small, medium, large | small |  | small: the title sits in the bar. medium and large: a larger title sits below the bar, for the top of a page. |
| `centered` | boolean |  | False |  | If True, the title of a small bar is centred. |
| `navigation_icon` | icon |  |  |  | An icon button at the start of the bar, such as mi:menu or mi:arrow_back. It raises the navigation_click event. |
| `navigation_label` | string |  |  |  | The name of the navigation icon for screen readers, such as Open menu or Back. |
| `sticky` | boolean |  | True |  | If True, the bar stays at the top of the window when the page scrolls, and takes a slightly darker colour while the page is scrolled. |
| `visible` | boolean |  | True |  | If True, the component will be displayed. |
| `role` | themeRole |  |  |  | A style for this component defined in CSS and added to Roles. |
| `tag` | object |  |  |  | Use this property to store any extra data for the component. |

*Generated file: change the theme, then run the generator.*
