# Pixie - A full-featured 2D graphics library for Python

[Pixie](https://github.com/treeform/pixie) is a 2D graphics library similar to [Cairo](https://www.cairographics.org/) and [Skia](https://skia.org).

![Github Actions](https://github.com/treeform/pixie-python/workflows/Github%20Actions/badge.svg)

`pip install pixie-python`

Features:
* Typesetting and rasterizing text, including styled rich text via spans.
* Drawing paths, shapes and curves with even-odd and non-zero windings.
* Pixel-perfect AA quality.
* Supported file formats are PNG, BMP, JPG, SVG + more in development.
* Strokes with joins and caps.
* Shadows, glows and blurs.
* Complex masking: Subtract, Intersect, Exclude.
* Complex blends: Darken, Multiply, Color Dodge, Hue, Luminosity... etc.
* Many operations are SIMD accelerated.

### Image file formats

Format        | Read          | Write         |
------------- | ------------- | ------------- |
PNG           | ✅           | ✅            |
JPEG          | ✅           |               |
BMP           | ✅           | ✅            |
GIF           | ✅           |               |
SVG           | ✅           |               |

### Font file formats

Format        | Read
------------- | -------------
TTF           | ✅
OTF           | ✅
SVG           | ✅

### Joins and caps

Supported Caps:
  * Butt
  * Round
  * Square

Supported Joins:
  * Miter (with miter angle limit)
  * Bevel
  * Round

### Blending & masking

Supported Blend Modes:
  * Normal
  * Darken
  * Multiply
  * ColorBurn
  * Lighten
  * Screen
  * Color Dodge
  * Overlay
  * Soft Light
  * Hard Light
  * Difference
  * Exclusion
  * Hue
  * Saturation
  * Color
  * Luminosity

Supported Mask Modes:
  * Mask
  * Overwrite
  * Subtract Mask
  * Intersect Mask
  * Exclude Mask

### SVG style paths:

Format        | Supported     | Description           |
------------- | ------------- | --------------------- |
M m           | ✅            | move to               |
L l           | ✅            | line to               |
h h           | ✅            | horizontal line to    |
V v           | ✅            | vertical line to      |
C c S s       | ✅            | cublic to             |
Q q T t       | ✅            | quadratic to          |
A a           | ✅            | arc to                |
z             | ✅            | close path            |

## Testing

`pytest`

## Examples

`git clone https://github.com/treeform/pixie-python` to run examples.

### Text
python [examples/text.py](examples/text.py)
```py
font = pixie.read_font("examples/data/Roboto-Regular_1.ttf")
font.size = 20

text = "Typesetting is the arrangement and composition of text in graphic design and publishing in both digital and traditional medias."

image.fill_text(
    font,
    text,
    bounds = pixie.Vector2(180, 180),
    transform = pixie.translate(10, 10)
)
```
![example output](examples/text.png)

### Text spans
python [examples/text_spans.py](examples/text_spans.py)
```py
typeface = pixie.read_typeface("examples/data/Ubuntu-Regular_1.ttf")

def make_font(typeface, size, color):
    font = typeface.new_font()
    font.size = size
    font.paints[0].color = color
    return font

spans = pixie.SeqSpan()
spans.append(pixie.Span(
    "verb [with object] ",
    make_font(typeface, 12, pixie.Color(0.78125, 0.78125, 0.78125, 1))
))
spans.append(pixie.Span(
    "strallow\n",
    make_font(typeface, 36, pixie.Color(0, 0, 0, 1))
))
spans.append(pixie.Span(
    "\nstral·low\n",
    make_font(typeface, 13, pixie.Color(0, 0.5, 0.953125, 1))
))
spans.append(pixie.Span(
    "\n1. free (something) from restrictive restrictions \"the regulations are intended to strallow changes in public policy\" ",
    make_font(typeface, 14, pixie.Color(0.3125, 0.3125, 0.3125, 1))
))

image.arrangement_fill_text(
    spans.typeset(bounds = pixie.Vector2(180, 180)),
    transform = pixie.translate(10, 10)
)
```
![example output](examples/text_spans.png)

### Square
python [examples/square.py](examples/square.py)
```py
paint = pixie.Paint(pixie.PK_SOLID)
paint.color = pixie.Color(1, 0, 0, 1)

ctx = image.new_context()
ctx.fill_style = paint

ctx.fill_rect(50, 50, 100, 100)
```
![example output](examples/square.png)

### Line
python [examples/line.py](examples/line.py)
```py
paint = pixie.Paint(pixie.PK_SOLID)
paint.color = pixie.parse_color("#FF5C00")

ctx = image.new_context()
ctx.stroke_style = paint
ctx.line_width = 10

ctx.stroke_segment(25, 25, 175, 175)
```
![example output](examples/line.png)

### Rounded rectangle
python [examples/rounded_rectangle.py](examples/rounded_rectangle.py)
```py
paint = pixie.Paint(pixie.PK_SOLID)
paint.color = pixie.Color(0, 1, 0, 1)

ctx = image.new_context()
ctx.fill_style = paint
ctx.rounded_rect(50, 50, 100, 100, 25, 25, 25, 25)
ctx.fill()
```
![example output](examples/rounded_rectangle.png)

### Heart
python [examples/heart.py](examples/heart.py)
```py
path = pixie.parse_path(
    """
    M 20 60
    A 40 40 90 0 1 100 60
    A 40 40 90 0 1 180 60
    Q 180 120 100 180
    Q 20 120 20 60
    z
    """
)

paint = pixie.Paint(pixie.PK_SOLID)
paint.color = pixie.parse_color("#FC427B")

image.fill_path(path, paint)
```
![example output](examples/heart.png)

### Masking
python [examples/masking.py](examples/masking.py)
```py
lines = pixie.Image(200, 200)
lines.fill(pixie.parse_color("#FC427B"))

paint = pixie.Paint(pixie.PK_SOLID)
paint.color = pixie.parse_color("#F8D1DD")

ctx = lines.new_context()
ctx.stroke_style = paint
ctx.line_width = 30

ctx.stroke_segment(25, 25, 175, 175)
ctx.stroke_segment(25, 175, 175, 25)

path = pixie.parse_path(
    """
    M 20 60
    A 40 40 90 0 1 100 60
    A 40 40 90 0 1 180 60
    Q 180 120 100 180
    Q 20 120 20 60
    z
    """
)

mask = pixie.Mask(200, 200)
mask.fill_path(path)

lines.mask_draw(mask)
image.draw(lines)
```
![example output](examples/masking.png)

### Gradient
python [examples/gradient.py](examples/gradient.py)
```py
paint = pixie.Paint(pixie.PK_GRADIENT_RADIAL)

paint.gradient_handle_positions.append(pixie.Vector2(100, 100))
paint.gradient_handle_positions.append(pixie.Vector2(200, 100))
paint.gradient_handle_positions.append(pixie.Vector2(100, 200))

paint.gradient_stops.append(pixie.ColorStop(pixie.Color(1, 0, 0, 1), 0))
paint.gradient_stops.append(pixie.ColorStop(pixie.Color(1, 0, 0, 0.15625), 1))

path = pixie.parse_path(
    """
    M 20 60
    A 40 40 90 0 1 100 60
    A 40 40 90 0 1 180 60
    Q 180 120 100 180
    Q 20 120 20 60
    z
    """
)

image.fill_path(path, paint)
```
![example output](examples/gradient.png)

### Image tiled
python [examples/image_tiled.py](examples/image_tiled.py)
```py
path = pixie.Path()
path.polygon(100, 100, 70, 8)

paint = pixie.Paint(pixie.PK_IMAGE_TILED)
paint.image = pixie.read_image("examples/data/baboon.png")
paint.image_mat = pixie.scale(0.08, 0.08)

image.fill_path(path, paint)
```
![example output](examples/image_tiled.png)

### Shadow
python [examples/shadow.py](examples/shadow.py)
```py
path = pixie.Path()
path.polygon(100, 100, 70, sides = 8)

paint = pixie.Paint(pixie.PK_SOLID)
paint.color = pixie.Color(1, 1, 1, 1)

polygon_image = pixie.Image(200, 200)
polygon_image.fill_path(path, paint)

shadow = polygon_image.shadow(
    offset = pixie.Vector2(2, 2),
    spread = 2,
    blur = 10,
    color = pixie.Color(0, 0, 0, 0.78125)
)

image.draw(shadow)
image.draw(polygon_image)
```
![example output](examples/shadow.png)

### Blur
python [examples/blur.py](examples/blur.py)
```py
trees = pixie.read_image("examples/data/trees.png")

path = pixie.Path()
path.polygon(100, 100, 70, 6)

mask = pixie.Mask(200, 200)
mask.fill_path(path)

blur = trees.copy()
blur.blur(20)
blur.mask_draw(mask)

image.draw(trees)
image.draw(blur)
```
![example output](examples/blur.png)

### Tiger
python [examples/tiger.py](examples/tiger.py)
```py
tiger = pixie.read_image("examples/data/tiger.svg")

image.draw(
    tiger,
    pixie.translate(100, 100) *
    pixie.scale(0.2, 0.2) *
    pixie.translate(-450, -450)
)
```
![example output](examples/tiger.png)
