import pixie

image = pixie.Image(200, 200)
image.fill(pixie.Color(1, 1, 1, 1))

paint = pixie.Paint(pixie.SOLID_PAINT)
paint.color = pixie.parse_color("#FF5C00")

ctx = image.new_context()
ctx.stroke_style = paint
ctx.line_width = 10

ctx.stroke_segment(25, 25, 175, 175)

image.write_file("examples/line.png")
