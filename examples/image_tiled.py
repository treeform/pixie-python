import pixie

image = pixie.Image(200, 200)
image.fill(pixie.Color(1, 1, 1, 1))

path = pixie.Path()
path.polygon(100, 100, 70, 8)

paint = pixie.Paint(pixie.PK_IMAGE_TILED)
paint.image = pixie.read_image("examples/data/baboon.png")
paint.image_mat = pixie.scale(0.08, 0.08)

image.fill_path(path, paint)

image.write_file("examples/image_tiled.png")
