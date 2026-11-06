# DatePicker

Component `m3.DatePicker` (`client_code/_Components/DatePicker/`), shared field code `client_code/_utils/m3x_picker.py`, CSS `theme/assets/m3x/date-picker.css`, tokens `--m3x-date-picker-*` in `theme/assets/m3x/tokens.css`. Gap C11.

## 1. What it is

A date picker lets the user enter a date. It is an M3 text field with a calendar icon at its end. The user either types the date into the field, or clicks the icon and chooses the date in a calendar dialog (the M3 modal date picker). The calendar dialog can also switch to typing.

## 2. Anatomy (M3 specification)

| Part | Value |
|---|---|
| Field | The base theme's TextBox, filled or outlined, with a 24 px calendar icon at its end |
| Dialog container | Surface Container High, corner extra large (28 px): the m3x Dialog |
| Supporting text | "Select date", Label large, On Surface Variant |
| Headline | The chosen date, such as "Wed, 18 Nov", Headline large, On Surface Variant, with an edit icon button that switches to typing |
| Month and year | A Label large button, such as "November 2026", that opens the year list; previous and next month icon buttons |
| Weekdays | One letter each, Body large, On Surface |
| Days | 40 px circles, Body large, On Surface. Today: 1 px Primary outline and Primary text. Selected: Primary with On Primary. Outside the allowed range: On Surface at 38 % |
| Years | 72 × 36 px pills, three to a row, Body large. Selected: Primary with On Primary |
| Actions | "Cancel" and "OK" text buttons |
| States | Hover and pressed layers in the content colour. Focus ring: 3 px Secondary, 2 px outside |

Sources: Jetpack Compose `DatePickerModalTokens` and the M3 date pickers specification.

## 3. How it works

- The field shows the date in `format` (by default `%d/%m/%Y`, as in 18/11/2026). Its placeholder is an example: today's date in that format, such as "e.g. 18/11/2026". An example is clear for every format, including formats with month names.
- A typed date is read when the user presses Enter or leaves the field. A date that cannot be read, or that lies outside `min_date` and `max_date`, puts the field into its error state and keeps the last good date. The message gives the example and, when limits are set, the allowed range, such as "Enter a date like 06 Nov 2026. Choose from 06 Nov 2026 to 05 Jan 2027." An empty field sets the date to None.
- The calendar opens on the chosen date, or on today. The previous and next month arrows move one month per click; held down, they keep moving, one month every 120 ms after a 400 ms pause. An arrow is disabled when the month it leads to has no allowed day. For large jumps, the month and year button opens the year list. Choosing a day selects it; "OK" confirms the choice and raises `change`; "Cancel", Escape or a click outside closes the dialog without a change.
- In the calendar, the arrow keys move one day or one week, Page Up and Page Down move one month, and Enter chooses the focused day. Today carries `aria-current="date"` and the selected day `aria-selected="true"`.
- The year list runs from `min_date` to `max_date`, or from 1900 to 2100 when they are not set. Choosing a year keeps the shown month inside the allowed range.
- In typing mode, an empty field is not an error; a typed date is checked as in the field.
- The month and day names are English. The week starts on Monday or Sunday (`week_starts_on`).

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `date` | datetime.date | `None` | The chosen date. |
| `label` | string | `'Date'` | The field label. |
| `format` | string | `'%d/%m/%Y'` | How the date is written: `%d`, `%m`, `%b`, `%B`, `%Y`, `%y`. |
| `min_date` | datetime.date | `None` | The earliest date allowed. |
| `max_date` | datetime.date | `None` | The latest date allowed. |
| `week_starts_on` | enum | `monday` | `monday` or `sunday`. |
| `appearance` | enum | `outlined` | `filled` or `outlined`. |
| `supporting_text` | string | `''` | Help text below the field. |
| `enabled` | boolean | `True` | Standard. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Events: `change` (default), `show`, `hide`.
