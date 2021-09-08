import pixie

image = pixie.Image(200, 200)
image.fill(pixie.Color(1, 1, 1, 1))

paint = pixie.Paint(pixie.PK_SOLID)
paint.color = pixie.Color(0, 1, 0, 1)

ctx = image.new_context()
ctx.fill_style = paint
ctx.rounded_rect(50, 50, 100, 100, 25, 25, 25, 25)
ctx.fill()

image.write_file("examples/rounded_rectangle.png")
