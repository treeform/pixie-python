import pixie

image = pixie.Image(200, 200)
image.fill(pixie.Color(1, 1, 1, 1))

paint = pixie.Paint(pixie.PK_SOLID)
paint.color = pixie.Color(1, 0, 0, 1)

ctx = image.new_context()
ctx.fill_style = paint

ctx.fill_rect(50, 50, 100, 100)

image.write_file("examples/square.png")