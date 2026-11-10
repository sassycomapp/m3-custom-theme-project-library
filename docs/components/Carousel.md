# Carousel

Component `m3.Carousel` (`client_code/_Components/Carousel/`), CSS `theme/assets/m3x/carousel.css`, tokens `--m3x-carousel-*` in `theme/assets/m3x/tokens.css`.

## 1. What it is

A carousel shows a row of items, usually images, that the user moves through. Each component added to the carousel, such as an Image or a Card holding one, becomes one item. M3 defines these layouts:

- **Multi-browse**: large items in front, then a medium item and a small item that hint at what comes next. Suits browsing many items.
- **Hero**: one large item and one small item. Suits showcasing.
- **Center-aligned hero**: one large item between two small items.
- **Uncontained**: items of one width in a row that scrolls freely; the edge cuts the last item.
- **Full width**: one item at a time, filling the width inside the same 16 px padding as the other layouts (the M3 full-screen layout, horizontal).

## 2. Anatomy (M3 specification)

| Part | Value |
|---|---|
| Item | Corner extra large (28 px), content cropped to the item and centred; Surface Container Highest behind the content |
| Spacing | 8 px between items; 16 px padding at each end of contained layouts (none at the end of uncontained) |
| Small item | 56 px wide; 40 px in carousels narrower than 360 px |
| Multi-browse | Large items as close as possible to `item_width` (default 186 px); the medium item half a large one (never less than a small one); together they fill the width exactly |
| Hero | Large item fills the width less one small item and a gap |
| Center-aligned hero | Large item fills the width less two small items and two gaps |
| Moving | Items change width smoothly in 300 ms (emphasized); no motion when the device asks for reduced motion |
| At the end | The arrangement turns round so the last item is large: small, medium, then large items |

Sources: Jetpack Compose `CarouselDefaults` and `Carousel` (Compose has no carousel token file), and the M3 carousel specification.

## 3. How it works

- Pictures are added in one of two ways. The simplest is the `images` property: one picture per line, as an asset path such as `_/theme/photo.jpg` (a file uploaded to the app's Assets) or a web address; from code the list may also hold Media objects. The carousel makes an Image item for each. Alternatively, any component added to the carousel becomes an item.
- Every Image item, however it was added, is set to `zoom_to_fill`: the picture is scaled, keeping its proportions, until it covers the item, and the overflow is cropped evenly from both sides. Pictures are never stretched. Anvil Images fill their item whatever their own height setting.
- Recommended pictures: landscape JPG or WebP for photos, PNG for graphics; about 800 x 600 px for multi-browse and uncontained, about 1600 x 900 px for the hero and full-width layouts; the subject near the centre; files under about 300 KB.
- `index` is the position of the first large item (the large item itself in the hero layouts). Changing it, or the user moving the carousel, raises `change`.
- The user moves a contained carousel by dragging or swiping 48 px per item, by scrolling sideways with a trackpad or with Shift and the mouse wheel, or with the Left, Right, Home and End keys while the carousel has the keyboard focus. Up and down scrolling stays with the page.
- An uncontained carousel scrolls freely with the same inputs.
- A click on an item raises `item_click` with `index` and `component`. The click that ends a drag does not.
- The carousel re-arranges itself whenever its width changes.
- The carousel is a region with `aria-roledescription="carousel"` and the name in `label`; each item is a group described as a slide, named "n of total"; hidden items are hidden from screen readers.
- The gap, padding and small widths are read from the `--m3x-carousel-*` tokens.

## 4. API

Properties:

| Name | Type | Default | Meaning |
|---|---|---|---|
| `images` | text[] | empty | Pictures to show, one per line (asset paths or web addresses). |
| `layout` | enum | `'multi_browse'` | `multi_browse`, `hero`, `center_hero`, `uncontained` or `full_width`. |
| `item_width` | number | `186` | The width large items aim for (multi-browse), or every item's width (uncontained). |
| `item_height` | number | `220` | The items' height in pixels. |
| `index` | number | `0` | The position of the first large item. |
| `label` | string | `'Carousel'` | The name screen readers announce. |
| `visible` | boolean | `True` | Standard. |
| `role` | themeRole | `''` | Standard. |
| `tag` | object | | Standard. |

Methods: `next()`, `previous()`.

Events: `item_click` (default, with `index` and `component`), `change` (with `index`), `show`, `hide`.

Slot: `carousel-slot`.

Toolbox: Containers section.

## 5. Usage

In the designer: set the carousel's `images` property to `_/theme/photo1.jpg`, `_/theme/photo2.jpg` and so on, one per line.

In code:

```python
self.carousel_1.images = [row["photo"] for row in app_tables.photos.search()]
```
