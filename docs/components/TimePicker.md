# TimePicker

Component `m3.TimePicker` (`client_code/_Components/TimePicker/`), shared field code `client_code/_utils/m3x_picker.py`, CSS `theme/assets/m3x/time-picker.css`, tokens `--m3x-time-picker-*` in `theme/assets/m3x/tokens.css`.

## 1. What it is

A time picker lets the user enter a time. It is an M3 text field with a clock icon at its end. The user either types the time into the field, or clicks the icon and chooses the time on a clock dial in a dialog. The dialog can also switch to typing the hour and minute.

## 2. Anatomy (M3 specification)

| Part | Value |
|---|---|
| Field | The base theme's TextBox, filled or outlined, with a 24 px clock icon at its end |
| Dialog container | Surface Container High, corner extra large (28 px): the m3x Dialog |
| Supporting text | "Select time", Label medium, On Surface Variant |
| Hour and minute boxes | 96 × 80 px (114 px wide with the 24-hour clock), corner small (8 px), Display large. Selected: Primary Container with On Primary Container. Not selected: Surface Container Highest with On Surface |
| AM and PM (12-hour clock) | A 52 × 80 px box split in two, 1 px Outline, Title medium. Selected: Tertiary Container with On Tertiary Container |
| Dial | A 256 px circle, Surface Container Highest; labels Body large, On Surface |
| Dial selector | A 2 px Primary hand from an 8 px Primary centre to a 48 px Primary circle; the label under it in On Primary |
| 24-hour hours | 00 to 11 on the outer ring, 12 to 23 on the inner ring |
| Mode button | A keyboard icon button at the bottom left that switches to typing; a clock icon switches back |
| Actions | "Cancel" and "OK" text buttons |

Sources: Jetpack Compose `TimePickerTokens` and the Compose `TimePicker` dial layout (outer ring radius 101 px, inner ring 69 px), and the M3 time pickers specification.

## 3. How it works

- The field shows the time as 14:30 (24-hour clock, the default) or 2:30 PM (12-hour clock). Its placeholder is an example in the same form, such as "e.g. 14:30". Typing accepts forms such as 14:30, 1430, 9.15 and 2:30 pm.
- A typed time is read when the user presses Enter or leaves the field. A time that cannot be read puts the field into its error state and keeps the last good time. An empty field sets the time to None.
- In the dialog, the user clicks or drags on the dial. Choosing the hour moves on to the minutes, as M3 sets. Clicking an hour or minute box chooses which one the dial sets. The dial also takes the arrow keys.
- In typing mode the hour and minute boxes become text inputs; a value out of range turns the box's outline to the Error colour.
- "OK" confirms the choice and raises `change`; "Cancel", Escape or a click outside closes the dialog without a change.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `time` | datetime.time | `None` | The chosen time, to the minute. |
| `label` | string | `'Time'` | The field label. |
| `format_24h` | boolean | `True` | 24-hour clock; `False` for the 12-hour clock with AM and PM. |
| `appearance` | enum | `outlined` | `filled` or `outlined`. |
| `supporting_text` | string | `''` | Help text below the field. |
| `enabled` | boolean | `True` | Standard. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Events: `change` (default), `show`, `hide`.
