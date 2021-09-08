import pixie

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

image = pixie.Image(200, 200)
image.fill(pixie.Color(1, 1, 1, 1))
image.fill_path(path, paint)

image.write_file("examples/heart.png")
