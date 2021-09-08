import pixie

image = pixie.Image(200, 200)
image.fill(pixie.Color(1, 1, 1, 1))

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

image.write_file("examples/masking.png")
