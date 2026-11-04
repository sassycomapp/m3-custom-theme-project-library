# Chip

Component `m3.Chip` (`client_code/_Components/Chip/`), CSS `theme/assets/m3x/chip.css`, tokens `--m3x-chip-*` in `theme/assets/m3x/tokens.css`. Gap C2.

## 1. What it is

A Chip is a small, compact element that stands for an action, a choice, a piece of entered information or a suggestion. M3 defines four types, and one component covers all four through its `type` property:

- **assist**: a smart action related to the content, such as "Add to calendar".
- **filter**: a choice the user switches on and off, such as a category in a list of filters.
- **input**: a piece of information the user entered, such as a person added to an email. It usually has a remove icon.
- **suggestion**: a suggested reply or search term.

## 2. Anatomy (M3 specification)

| Part | Value |
|---|---|
| Container | 32 px high, corner small (8 px), 1 px Outline Variant outline |
| Elevated container (assist, filter, suggestion) | Surface Container Low, no outline, elevation level 1 (level 2 on hover) |
| Selected container (filter, input) | Secondary Container, no outline |
| Label | Label large. Assist: On Surface. Filter, input, suggestion: On Surface Variant. Selected: On Secondary Container |
| Leading icon | 18 px. Assist, filter, suggestion: Primary. Input: On Surface Variant (Primary when selected). A selected filter Chip without its own icon shows a check mark |
| Remove icon | 18 px close icon after the label, On Surface Variant |
| Padding | 16 px at each end, 8 px beside an icon, 8 px between icon and label |
| States | Hover, focus and pressed layers in the label colour. Focus ring: 3 px Secondary, 2 px outside |
| Disabled | Label and icons On Surface at 38 %. Outline, and elevated or selected containers, On Surface at 12 %. No shadow |
| Touch target | 48 px high |

Sources: Jetpack Compose `AssistChipTokens`, `FilterChipTokens`, `InputChipTokens` and `SuggestionChipTokens` (7_0_1), and the M3 chips specification.

## 3. How it works

- The Chip is two buttons inside one container: the main button (icon and label) and the remove button. The remove button is a separate button, so it can be reached by keyboard and does not also trigger the main button.
- Clicking a filter or input Chip switches `selected` and raises `change`, then raises `click`. Clicking an assist or suggestion Chip raises `click` only.
- Clicking the remove icon raises `remove`. The Chip does not remove itself: the app decides, normally with `chip.remove_from_parent()`.
- A disabled Chip raises no events.
- The type class (`m3x-chip-assist` and so on) sets three colour variables. Every other rule in `chip.css` reads only those three variables, so each state works the same way for every type.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `text` | string | `'Chip'` | The label. |
| `type` | enum | `assist` | `assist`, `filter`, `input` or `suggestion`. |
| `selected` | boolean | `False` | Selected state. Filter and input Chips only. |
| `leading_icon` | icon | `''` | An `mi:` icon before the label. |
| `elevated` | boolean | `False` | Shadow instead of outline. Assist, filter and suggestion Chips only. |
| `removable` | boolean | `False` | Shows the remove icon. Meant for input Chips. |
| `enabled` | boolean | `True` | Standard. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tooltip` | string | `''` | Standard. |
| `tag` | object | | Standard. |

Events: `click` (default), `change`, `remove`, `show`, `hide`.

## 5. Use

```python
for name in ("Vegan", "Gluten free", "Halal"):
    chip = m3.Chip(text=name, type="filter")
    chip.add_event_handler("change", self.update_menu)
    self.filters_panel.add_component(chip)
```

Place a set of Chips in a FlowPanel, which wraps them onto new lines and spaces them evenly.
