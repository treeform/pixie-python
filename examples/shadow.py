import pixie

polygon_image = pixie.Image(200, 200)

paint = pixie.Paint(pixie.PK_SOLID)
paint.color = pixie.Color(1, 1, 1, 1)

ctx = polygon_image.new_context()
ctx.fill_style = paint
ctx.polygon(100, 100, 70, 8)
ctx.fill()

shadow = polygon_image.shadow(
    offset = pixie.Vector2(2, 2),
    spread = 2,
    blur = 10,
    color = pixie.Color(0, 0, 0, 0.78125)
)

image = pixie.Image(200, 200)
image.fill(pixie.Color(1, 1, 1, 1))

image.draw(shadow)
image.draw(polygon_image)

image.write_file("examples/shadow.png")
