import pixie

image = pixie.Image(200, 200)
image.fill(pixie.Color(1, 1, 1, 1))

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

image.write_file("examples/shadow.png")
