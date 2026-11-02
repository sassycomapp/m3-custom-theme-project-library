# Base inventory: Anvil Material 3 Theme v1.2.6

Source: git tag `upstream-v1.2.6` (commit `e7eb485c`), as imported at Step 1 (`base-v1.2.6`). Generated from the files in the tag; do not edit by hand. Regenerate when the base changes.

## 1. Summary

- Components with a `form_template.yaml`: 26
- Layouts: 2
- Component CSS files in `theme/assets/anvil-m3/`: 14
- Colour scheme: 46 named colours in `theme/parameters.yaml`; 45 CSS variables, all of the form `--anvil-m3-*`, defined in `theme/assets/theme.css`
- Roles in `theme/parameters.yaml`: 1 (`data-grid-header`)
- Typography, shape, elevation, state-layer and motion tokens as CSS variables: **none**. Colour is the only token category.
- Dark mode: **none**. One colour scheme only.

## 2. Components

Properties are listed as `name` (type, default, options). Events are listed by name; the default event is marked with `*`.

### 2.1 `_Components.Avatar`

- File: `client_code/_Components/Avatar/form_template.yaml`; container component: no
- Events: none
- Properties (18): `user_name` (string); `image` (uri); `size` (number, default 40); `fallback_icon` (icon, default 'mi:person'); `background_color` (color); `text_color` (color); `align` (enum, default 'left', options left/center/right); `appearance` (enum, default 'filled', options filled/tonal/outlined); `margin` (margin, default ['', '', '', '']); `visible` (boolean, default True); `role` (themeRole); `tooltip` (string); `fallback_icon_color` (color); `border` (string); `tag` (object); `font_size` (number); `fallback_icon_size` (number); `font_family` (string)

### 2.2 `_Components.AvatarMenu`

- File: `client_code/_Components/AvatarMenu/form_template.yaml`; container component: yes
- Events: `click`*
- Properties (21): `menu_background_color` (color); `menu_border` (string); `visible` (boolean, default True); `appearance` (enum, default 'filled', options filled/tonal/outlined); `tooltip` (string); `enabled` (boolean, default True); `user_name` (string); `avatar_border` (string); `avatar_background_color` (color); `avatar_text_color` (color); `fallback_icon` (icon, default 'mi:person'); `avatar_font_size` (number); `fallback_icon_color` (color); `fallback_icon_size` (number); `margin` (margin); `align` (enum, default 'left', options left/center/right); `avatar_font_family` (string); `role` (themeRole); `menu_items` (object); `image` (uri); `tag` (object)

### 2.3 `_Components.Button`

- File: `client_code/_Components/Button/form_template.yaml`; container component: no
- Events: `click`*, `show`, `hide`
- Properties (21): `enabled` (boolean, default True); `tag` (object); `role` (themeRole); `align` (enum, default 'left', options left/center/right/full); `visible` (boolean, default True); `appearance` (enum, default 'filled', options filled/elevated/tonal/outlined/text); `text` (string); `text_color` (color); `font_family` (string); `font_size` (number); `underline` (boolean, default False); `italic` (boolean, default False); `bold` (boolean, default True); `icon` (icon); `icon_color` (color); `icon_size` (number); `icon_align` (enum, default 'left', options left/right); `spacing` (spacing); `background_color` (color); `border` (string); `tooltip` (string)

### 2.4 `_Components.ButtonMenu`

- File: `client_code/_Components/ButtonMenu/form_template.yaml`; container component: yes
- Events: `click`*, `show`, `hide`
- Properties (24): `text` (string); `role` (themeRole); `tag` (object); `appearance` (enum, default 'elevated', options elevated/filled/tonal/outlined); `enabled` (boolean, default True); `visible` (boolean, default True); `tooltip` (string); `bold` (boolean, default True); `italic` (boolean, default False); `underline` (boolean, default False); `button_background_color` (color); `button_text_color` (color); `button_border` (string); `button_font_size` (number); `icon_color` (color); `icon_size` (number); `icon_align` (enum, default 'left', options left/right); `icon` (icon); `spacing` (spacing); `button_font_family` (string); `menu_background_color` (color); `menu_border` (string); `align` (enum, default 'left', options left/center/right/full); `menu_items` (object)

### 2.5 `_Components.Card.CardContentContainer`

- File: `client_code/_Components/Card/CardContentContainer/form_template.yaml`; container component: yes
- Events: `show`*, `hide`
- Properties (1): `margin` (margin, default ['16', '16', '16', '16'])

### 2.6 `_Components.Card`

- File: `client_code/_Components/Card/form_template.yaml`; container component: yes
- Events: `show`*, `hide`
- Properties (10): `visible` (boolean, default True); `role` (themeRole); `tag` (object); `align` (enum, default 'left', options left/center/right/full); `appearance` (enum, default 'elevated', options elevated/filled/outlined); `spacing` (spacing); `background_color` (color); `tooltip` (string); `border` (string); `orientation` (enum, default 'column', options column/row)

### 2.7 `_Components.Checkbox`

- File: `client_code/_Components/Checkbox/form_template.yaml`; container component: no
- Events: `change`*, `show`, `hide`
- Properties (20): `checked` (boolean, default False); `role` (themeRole); `tag` (object); `enabled` (boolean, default True); `error` (boolean, default False); `text` (string); `allow_indeterminate` (boolean, default False); `visible` (boolean, default True); `underline` (boolean, default False); `italic` (boolean, default False); `font_size` (number); `bold` (boolean, default False); `border` (string); `font_family` (string); `checkbox_color` (color); `text_color` (color); `background_color` (color); `align` (enum, default 'left', options left/center/right); `spacing` (spacing); `tooltip` (string)

### 2.8 `_Components.CircularProgressIndicator`

- File: `client_code/_Components/CircularProgressIndicator/form_template.yaml`; container component: no
- Events: `show`*, `hide`
- Properties (9): `visible` (boolean, default True); `role` (themeRole); `tag` (object); `type` (enum, default 'indeterminate', options determinate/indeterminate); `progress` (number, default 0); `align` (enum, default 'left', options left/center/right); `margin` (margin); `tooltip` (string); `color` (color)

### 2.9 `_Components.Divider`

- File: `client_code/_Components/Divider/form_template.yaml`; container component: no
- Events: `show`*, `hide`
- Properties (5): `type` (enum, default 'full_width', options full_width/inset); `visible` (boolean, default True); `role` (themeRole); `color` (color); `margin` (margin)

### 2.10 `_Components.DropdownMenu`

- File: `client_code/_Components/DropdownMenu/form_template.yaml`; container component: yes
- Events: `change`*, `show`, `hide`
- Properties (41): `background_color` (color); `label_bold` (boolean, default False); `tag` (object); `enabled` (boolean, default True); `label_font_family` (string); `label_font_size` (number); `label_color` (color); `label_italic` (boolean, default False); `role` (themeRole); `align` (enum, default 'left', options left/center/right/full); `items` (text[], default []); `placeholder` (string); `appearance` (enum, default 'filled', options filled/outlined); `selected_value` (object); `label_underline` (boolean, default False); `visible` (boolean, default True); `label` (string); `items_bold` (boolean, default False); `items_italic` (boolean, default False); `items_underline` (boolean, default False); `items_text_color` (color); `menu_background_color` (color); `items_font_family` (string); `items_font_size` (number); `allow_none` (boolean, default False); `selected_italic` (boolean, default False); `selected_bold` (boolean, default False); `selected_underline` (boolean, default False); `selected_font_family` (string); `selected_font_size` (number); `selected_text_color` (color); `margin` (margin); `error` (boolean, default False); `icon` (icon); `icon_color` (color); `tooltip` (string); `supporting_text` (string); `supporting_text_color` (color); `supporting_text_font_size` (number); `supporting_text_font_family` (string); `border_color` (color)

### 2.11 `_Components.FileLoader`

- File: `client_code/_Components/FileLoader/form_template.yaml`; container component: no
- Events: `change`*, `focus`, `lost_focus`, `show`, `hide`
- Properties (25): `file` (object); `tag` (object); `file_types` (string); `files` (object); `multiple` (boolean, default False); `show_state` (boolean, default False); `text` (string, default 'File upload'); `role` (themeRole); `icon` (icon, default 'mi:file_upload'); `enabled` (boolean, default True); `visible` (boolean, default True); `text_color` (color); `icon_color` (color); `background_color` (color); `underline` (boolean, default False); `italic` (boolean, default False); `bold` (boolean, default False); `font_family` (string); `font_size` (number); `icon_size` (number); `align` (enum, default 'left', options left/center/right/full); `border` (string); `spacing` (spacing); `tooltip` (string); `appearance` (enum, default 'text', options text/elevated/filled/tonal/outlined)

### 2.12 `_Components.Heading`

- File: `client_code/_Components/Heading/form_template.yaml`; container component: no
- Events: `show`*, `hide`
- Properties (21): `style` (enum, default 'headline', options display/headline/title); `scale` (enum, default 'medium', options small/medium/large); `font_size` (number); `tag` (object); `role` (themeRole); `font_family` (string); `bold` (boolean, default False); `italic` (boolean, default False); `text` (string); `underline` (boolean, default False); `visible` (boolean, default True); `icon` (icon); `text_color` (color); `background_color` (color); `border` (string); `align` (enum, default 'left', options left/center/right/justify); `icon_size` (number); `icon_color` (color); `spacing` (spacing); `tooltip` (string); `line_height` (string)

### 2.13 `_Components.IconButton`

- File: `client_code/_Components/IconButton/form_template.yaml`; container component: no
- Events: `click`*, `show`, `hide`
- Properties (12): `appearance` (enum, default 'standard', options standard/filled/tonal/outlined); `tag` (object); `icon` (icon, default 'mi:star'); `enabled` (boolean, default True); `role` (themeRole); `visible` (boolean, default True); `border` (string); `background_color` (color); `icon_color` (color); `align` (enum, default 'left', options left/center/right); `tooltip` (string); `margin` (margin)

### 2.14 `_Components.IconButtonMenu`

- File: `client_code/_Components/IconButtonMenu/form_template.yaml`; container component: yes
- Events: `click`*
- Properties (15): `visible` (boolean, default True); `menu_border` (string); `menu_background_color` (color); `appearance` (enum, default 'standard', options standard/filled/tonal/outlined); `tooltip` (string); `enabled` (boolean, default True); `button_border` (string); `button_background_color` (color); `icon` (icon, default 'mi:star'); `icon_color` (color); `margin` (margin); `align` (enum, default 'left', options left/center/right); `role` (string); `menu_items` (object); `tag` (object)

### 2.15 `_Components.LinearProgressIndicator`

- File: `client_code/_Components/LinearProgressIndicator/form_template.yaml`; container component: no
- Events: `show`*, `hide`
- Properties (9): `visible` (boolean, default True); `role` (themeRole); `tag` (object); `type` (enum, default 'indeterminate', options determinate/indeterminate); `progress` (number, default 0); `margin` (margin); `tooltip` (string); `progress_color` (color); `track_color` (color)

### 2.16 `_Components.Link`

- File: `client_code/_Components/Link/form_template.yaml`; container component: yes
- Events: `click`*, `show`, `hide`
- Properties (18): `text` (string); `role` (themeRole); `url` (string); `align` (enum, default 'left', options left/center/right); `bold` (boolean, default False); `italic` (boolean, default False); `font_family` (string); `font_size` (number); `icon` (icon); `underline` (boolean, default True); `visible` (boolean, default True); `text_color` (color); `icon_color` (color); `icon_size` (number, default 24); `border` (string); `spacing` (spacing); `tooltip` (string); `background_color` (color)

### 2.17 `_Components.Menu`

- File: `client_code/_Components/Menu/form_template.yaml`; container component: yes
- Events: none
- Properties (2): `visible` (boolean, default True); `background_color` (color)

### 2.18 `_Components.MenuItem`

- File: `client_code/_Components/MenuItem/form_template.yaml`; container component: no
- Events: `click`*
- Properties (22): `leading_icon` (icon); `text` (string); `tag` (object); `trailing_icon` (icon); `trailing_text` (string); `add_icon_space` (boolean, default False); `enabled` (boolean, default True); `bold` (boolean, default False); `font_family` (string); `font_size` (number); `text_color` (color); `italic` (boolean, default False); `underline` (boolean, default False); `background_color` (color); `visible` (boolean, default True); `leading_icon_size` (number); `trailing_icon_size` (number); `leading_icon_color` (color); `trailing_icon_color` (color); `role` (string); `spacing` (spacing); `tooltip` (string)

### 2.19 `_Components.NavigationLink`

- File: `client_code/_Components/NavigationLink/form_template.yaml`; container component: no
- Events: `click`*, `show`, `hide`
- Properties (21): `url` (string); `tag` (object); `text` (string, default 'Label'); `selected` (boolean, default False); `role` (themeRole); `badge` (boolean, default False); `badge_count` (number); `text_color` (color); `font_size` (string); `font_family` (string); `icon_color` (color); `icon_size` (string); `icon` (icon, default 'mi:star'); `navigate_to` (form); `spacing` (spacing); `tooltip` (string); `visible` (boolean, default True); `italic` (boolean, default False); `underline` (boolean, default False); `bold` (boolean, default False); `background_color` (color)

### 2.20 `_Components.RadioButton`

- File: `client_code/_Components/RadioButton/form_template.yaml`; container component: no
- Events: `select`*, `show`, `hide`
- Properties (20): `selected` (boolean, default False); `role` (themeRole); `enabled` (boolean, default True); `text` (string); `value` (string); `tag` (object); `align` (enum, default 'left', options left/center/right); `background_color` (color); `bold` (boolean, default False); `border` (string); `font_family` (string); `font_size` (number); `text_color` (color); `italic` (boolean, default False); `underline` (boolean, default False); `visible` (boolean, default True); `spacing` (spacing); `tooltip` (string); `radio_color` (color); `group` (object)

### 2.21 `_Components.RadioGroupPanel`

- File: `client_code/_Components/RadioGroupPanel/form_template.yaml`; container component: yes
- Events: `change`*, `hide`, `show`
- Properties (1): `selected_value` (object)

### 2.22 `_Components.SidesheetContent`

- File: `client_code/_Components/SidesheetContent/form_template.yaml`; container component: yes
- Events: none
- Properties (0): none

### 2.23 `_Components.Slider`

- File: `client_code/_Components/Slider/form_template.yaml`; container component: no
- Events: `change`*, `change_end`, `show`, `hide`
- Properties (17): `value` (number); `show_label` (boolean, default False); `role` (themeRole); `enabled` (boolean, default True); `progress_color` (color); `track_color` (color); `thumb_color` (color); `label_color` (color); `tag` (object); `label_text_color` (color); `min` (number, default 0); `max` (number, default 10); `step` (number); `margin` (margin, default ['', '', '', '']); `show_markers` (boolean, default False); `tooltip` (string); `visible` (boolean, default True)

### 2.24 `_Components.Switch`

- File: `client_code/_Components/Switch/form_template.yaml`; container component: no
- Events: `change`*, `show`, `hide`
- Properties (15): `selected_icon` (icon); `selected` (boolean, default False); `unselected_icon` (icon); `unselected_background_color` (color); `selected_background_color` (color); `unselected_thumb_color` (color); `selected_thumb_color` (color); `unselected_outline_color` (color); `role` (themeRole); `tag` (object); `enabled` (boolean, default True); `align` (enum, default 'left', options left/center/right); `margin` (margin, default ['', '', '', '']); `visible` (boolean, default True); `tooltip` (string)

### 2.25 `_Components.Text`

- File: `client_code/_Components/Text/form_template.yaml`; container component: no
- Events: `show`*, `hide`
- Properties (21): `style` (enum, default 'body', options body/label); `scale` (enum, default 'medium', options small/medium/large); `align` (enum, default 'left', options left/center/right/justify); `background_color` (color); `bold` (boolean, default False); `border` (string); `font_family` (string); `font_size` (number); `text_color` (color); `role` (themeRole); `icon` (icon); `italic` (boolean, default False); `tag` (object); `text` (string); `underline` (boolean, default False); `visible` (boolean, default True); `icon_size` (number); `icon_color` (color); `spacing` (spacing); `tooltip` (string); `line_height` (string)

### 2.26 `_Components.TextInput`

- File: `client_code/_Components/TextInput/form_template.yaml`; container component: no
- Events: `change`*, `show`, `hide`, `focus`, `lost_focus`
- Properties (30): `label` (string); `placeholder` (string); `supporting_text` (string); `character_limit` (number, default 0); `role` (themeRole); `align` (enum, default 'left', options left/center/right); `appearance` (enum, default 'filled', options filled/outlined); `visible` (boolean, default True); `tag` (object); `label_color` (color); `label_bold` (boolean, default False); `label_italic` (boolean, default False); `label_underline` (boolean, default False); `label_font_size` (number); `label_font_family` (string); `display_bold` (boolean, default False); `display_italic` (boolean, default False); `display_underline` (boolean, default False); `display_font_family` (string); `display_text_color` (color); `display_font_size` (number); `enabled` (boolean, default True); `error` (boolean, default False); `margin` (margin); `background_color` (color); `tooltip` (string); `border_color` (color); `subcontent_color` (color); `subcontent_font_family` (string); `subcontent_font_size` (number)

## 3. Layouts

### `Layouts.NavigationDrawerLayout`

- Events: none
- Properties (5): `navigation_drawer_color` (color); `background_color` (string); `text_color` (string); `show_sidesheet` (boolean, default False); `content_padding` (padding, default ['8', '8', '8', '8'])

### `Layouts.NavigationRailLayout`

- Events: none
- Properties (7): `navigation_rail_collapse_to` (enum, default 'bottom_app_bar', options bottom_app_bar/modal_navigation_drawer); `navigation_rail_color` (color); `background_color` (color); `text_color` (color); `show_sidesheet` (boolean, default True); `navigation_rail_vertical_align` (enum, default 'top', options top/center/bottom); `content_padding` (padding, default ['8', '8', '8', '8'])

## 4. Components defined in Python modules (no own `form_template.yaml`)

- `client_code/_Components/InteractiveCard.py`
- `client_code/_Components/ToggleIconButton.py`
- `client_code/_Components/MenuMixin.py`

## 5. Exports in `client_code/components/__init__.py`

`Avatar`, `AvatarMenu`, `Button`, `ButtonMenu`, `Card`, `CardContentContainer`, `Checkbox`, `CircularProgressIndicator`, `Divider`, `DropdownMenu`, `FileLoader`, `Heading`, `IconButton`, `IconButtonMenu`, `InteractiveCard`, `LinearProgressIndicator`, `Link`, `MenuItem`, `NavigationLink`, `RadioButton`, `RadioGroup`, `RadioGroupPanel`, `SidesheetContent`, `Slider`, `Switch`, `Text`, `TextArea`, `TextBox`, `ToggleIconButton`

## 6. Standard Anvil components replaced by M3 versions (`client_code/InitModule.py`)

Registered through `pluggable_ui.provide("m3", ...)`: `anvil.TextBoxWithLabel` and `anvil.TextBox` → `TextBox`; `anvil.Button` → `Button` (aligned centre); `anvil.CheckBox` → `Checkbox`; `anvil.alerts.FooterButton` → `Button`.

## 7. Shared helpers

`client_code/_utils/properties.py`: `ComponentTag`, `theme_color_to_css`, `property_with_callback`, `property_without_callback`, `color_property`, `style_property`, `innerHTML_property`, `innerText_property`, `href_property`, `checked_property`, `enabled_property`, `name_property`, `value_property`, `underline_property`, `italic_property`, `bold_property`, `custom_bold_property`, `font_size_property`, `font_family_property`, `border_property`, `margin_property`, `spacing_property`, `padding_property`, `role_property`, `tooltip_property`, `anvil_prop`, `inline_editing`.
`client_code/_utils/fui.py`: `auto_update`, `size_middleware` (floating-ui positioning).

## 8. CSS

`theme/assets/theme.css` imports the component files below, then defines the colour variables, the page structure (`.anvil-m3-structure`, top app bar, navigation drawer, navigation rail, content area) and the Anvil modal dialog styling. Layout breakpoints in `theme.css` are 600 px, 780 px and 980 px.

| File | Lines |
|---|---|
| `theme/assets/anvil-m3/avatar.css` | 107 |
| `theme/assets/anvil-m3/button.css` | 95 |
| `theme/assets/anvil-m3/card.css` | 92 |
| `theme/assets/anvil-m3/checkbox.css` | 156 |
| `theme/assets/anvil-m3/fileloader.css` | 97 |
| `theme/assets/anvil-m3/iconbutton.css` | 99 |
| `theme/assets/anvil-m3/menu.css` | 159 |
| `theme/assets/anvil-m3/navigation-link.css` | 311 |
| `theme/assets/anvil-m3/progress-indicator.css` | 62 |
| `theme/assets/anvil-m3/radiobutton.css` | 99 |
| `theme/assets/anvil-m3/slider.css` | 166 |
| `theme/assets/anvil-m3/switch.css` | 146 |
| `theme/assets/anvil-m3/text-inputs.css` | 208 |
| `theme/assets/anvil-m3/text.css` | 165 |

`theme/assets/anvil-m3/floating-ui/` holds `core@1.6.7.js` and `dom@1.6.10.js`, loaded from `head_html` in `anvil.yaml`.

## 9. Colour scheme (`theme/parameters.yaml`)

46 colours, name (light value): `Primary` (#6750A4), `Primary Container` (#EADDFF), `On Primary` (#FFFFFF), `On Primary Container` (#21005E), `Secondary` (#625B71), `Secondary Container` (#E8DEF8), `On Secondary` (#FFFFFF), `On Secondary Container` (#1D192B), `Tertiary` (#7D5260), `Tertiary Container` (#FFD8E4), `On Tertiary` (#FFFFFF), `On Tertiary Container` (#370B1E), `Error` (#B3261E), `Background` (#FFFBFE), `Surface` (#FFFBFE), `On Background` (#1C1B1F), `On Surface` (#1C1B1F), `Surface Variant` (#E7E0EC), `On Surface Variant` (#49454E), `Outline` (#79747E), `On Disabled` (rgba(29, 27, 32, 0.38)), `Disabled Container` (rgba(29, 27, 32, 0.12)), `Light Overlay 1` (rgba(255, 255, 255, 0.08)), `Light Overlay 2` (rgba(255, 255, 255, 0.12)), `Dark Overlay 1` (rgba(29, 25, 43, 0.08)), `Dark Overlay 2` (rgba(29, 25, 43, 0.12)), `Primary Overlay 1` (rgba(103, 80, 164, 0.05)), `Primary Overlay 2` (rgba(103, 80, 164, 0.08)), `Primary Overlay 3` (rgba(103, 80, 164, 0.12)), `Outline Variant` (#C4C7C5), `On Error` (#FFFFFF), `Surface Container Low` (#F7F2FA), `Surface Container High` (#ECE6F0), `Surface Container Highest` (#E6E0E9), `Disabled Container 2` (rgba(29, 27, 32, 0.04)), `Error Overlay 1` (rgba(179, 38, 30, 0.08)), `Error Overlay 2` (rgba(179, 38, 30, 0.12)), `Dark Overlay 3` (rgba(29, 25, 43, 0.16)), `On Error Container` (#410E0B), `Surface Container` (#F3EDF7), `Inverse Surface` (#322F35), `Inverse On Surface` (#F5EFF7), `On Surface Variant Overlay 1` (rgba(73,69,79, 0.08)), `On Surface Variant Overlay 2` (rgba(73,69,79, 0.12)), `Inverse On Surface Overlay 1` (rgba(245,239,247, 0.08)), `Inverse On Surface Overlay 2` (rgba(245,239,247, 0.12)).

## 10. Designer toolbox sections (`anvil.yaml`)

- **Common Components**: Button, Text, Link, Checkbox, TextBox, Card
- **Typography**: Text, Heading, Link, RichText
- **Buttons**: Button, IconButton, ToggleIconButton
- **Display**: Avatar, Card, InteractiveCard, CardContentContainer, SidesheetContent, Divider
- **Form Input**: Checkbox, RadioButton, TextBox, TextArea, DropdownMenu, Switch, FileLoader, Slider, DatePicker, RadioGroupPanel
- **Navigation**: NavigationLink
- **Menus**: ButtonMenu, IconButtonMenu, AvatarMenu, MenuItem
- **Feedback**: LinearProgressIndicator, CircularProgressIndicator
- **Integrations**: Plot, YouTube Video, Google Map, Canvas
- **Containers**: ColumnPanel, FlowPanel, Repeating Panel, DataRowPanel, LinearPanel, GridPanel, XYPanel, Data Grid
- **Other**: Image, Spacer, Timer

## 11. Other base configuration

- `anvil.yaml`: `package_name: m3`; `code_prelude` adds `import m3.components as m3` to every form; `client_init_module: InitModule`; `head_html` loads Poppins, Roboto and Material Symbols Outlined from Google Fonts, plus floating-ui.
- `.ruff.toml`: lint rules `E`, `F`, `I001`.
- `CHANGELOG.md` and `CONTRIBUTING.md` exist. Upstream contributions require signing Anvil's CLA; we do not contribute upstream, so this does not apply.
