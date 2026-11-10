# Badge

Component `m3.Badge` (`client_code/_Components/Badge/`), CSS `theme/assets/m3x/badge.css`, tokens `--m3x-badge-*` in `theme/assets/m3x/tokens.css`.

## 1. What it is

A Badge marks new or unread items. M3 defines two sizes:

- **Small**: a 6 px dot, meaning "something new", without a number.
- **Large**: a 16 px pill holding a count, such as the number of unread messages.

## 2. Anatomy (M3 specification)

| Part | Value |
|---|---|
| Small badge | 6 px circle, Error colour |
| Large badge | 16 px high, at least 16 px wide, fully rounded, Error colour, 4 px padding at the sides |
| Label | Label small, On Error |
| Long counts | Counts above the maximum show as the maximum with a plus, such as "999+" |

Sources: Jetpack Compose `BadgeTokens` (v0_103) and the Compose `Badge` layout.

## 3. How it works

- With no `count`, the Badge is the small dot. With a `count`, it is the large pill showing the count.
- The Badge sits in line with other components, for example after a Text in a FlowPanel. The navigation components that show badges on their icons use the same `m3x-badge` CSS classes.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `count` | number | `None` | The number shown. `None` shows the small dot. |
| `max_count` | number | `999` | Counts above this show as the number with a plus. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Events: `show`, `hide`.

## 5. Use

```python
self.inbox_row.add_component(m3.Text(text="Inbox"))
self.inbox_row.add_component(m3.Badge(count=unread_count))
```
