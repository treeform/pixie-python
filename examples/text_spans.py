import pixie

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

image = pixie.Image(200, 200)
image.fill(pixie.Color(1, 1, 1, 1))

image.arrangement_fill_text(
    spans.typeset(bounds = pixie.Vector2(180, 180)),
    transform = pixie.translate(10, 10)
)

image.write_file("examples/text_spans.png")
