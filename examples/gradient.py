import pixie

image = pixie.Image(200, 200)
image.fill(pixie.Color(1, 1, 1, 1))

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

image.write_file("examples/gradient.png")
