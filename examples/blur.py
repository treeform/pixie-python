import pixie

trees = pixie.read_image("examples/data/trees.png")

path = pixie.Path()
path.polygon(100, 100, 70, 6)

mask = pixie.Mask(200, 200)
mask.fill_path(path)

blur = trees.copy()
blur.blur(20)
blur.mask_draw(mask)

image = pixie.Image(200, 200)
image.fill(pixie.Color(1, 1, 1, 1))

image.draw(trees)
image.draw(blur)

image.write_file("examples/blur.png")
