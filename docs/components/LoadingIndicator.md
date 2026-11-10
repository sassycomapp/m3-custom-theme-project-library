# LoadingIndicator

Component `m3.LoadingIndicator` (`client_code/_Components/LoadingIndicator/`), shapes `client_code/_utils/m3x_loading.py`, CSS `theme/assets/m3x/loading-indicator.css`, tokens `--m3x-loading-indicator-*` in `theme/assets/m3x/tokens.css`.

## 1. What it is

The loading indicator is new in M3 Expressive. It shows that something is loading when the wait is short and its length is unknown, for example while a page or a list refreshes. It is a filled shape that keeps changing from one rounded shape into the next while it turns. For waits that can show how far they have got, use a progress indicator instead.

M3 defines two forms:

- **Plain**: the shape alone, in the Primary colour.
- **Contained**: the shape inside a round Primary Container background, for use on top of other content.

## 2. Anatomy (M3 Expressive specification)

| Part | Value |
|---|---|
| Size | 48 px |
| Active shape | 38 px, Primary (plain) or On Primary Container (contained) |
| Container (contained only) | 48 px circle, Primary Container |
| Shapes, in order | Soft burst, 9-sided cookie, pentagon, pill, sunny, 4-sided cookie, oval |
| Morph | One shape every 650 ms, each morph turning the shape a further quarter turn |
| Rotation | The whole indicator turns once every 4666 ms |

Sources: Jetpack Compose `LoadingIndicatorTokens` and the Compose `LoadingIndicator` (its shape sequence and timings).

## 3. How it works

- Each of the seven shapes is drawn with the same number of points round its centre, so the browser can morph one shape smoothly into the next with SVG animation. No JavaScript library is needed.
- One loop passes four times through the seven shapes: 28 quarter turns, which is seven whole turns. The loop therefore restarts without a visible jump.
- Each morph eases in and out, close to the spring Compose uses.
- With the device's reduced-motion setting on, the indicator shows the first shape, still.
- The indicator is announced to screen readers as a progress bar named by `label`.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `contained` | boolean | `False` | The shape sits in a round Primary Container background. |
| `label` | string | `'Loading'` | The screen-reader name. |
| `align` | enum | `left` | `left`, `center` or `right`. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Events: `show`, `hide`.
