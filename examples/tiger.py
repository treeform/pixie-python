from os import access
import pixie

image = pixie.Image(200, 200)
image.fill(pixie.Color(1, 1, 1, 1))

tiger = pixie.read_image("examples/data/tiger.svg")

image.draw(
    tiger,
    pixie.translate(100, 100) *
    pixie.scale(0.2, 0.2) *
    pixie.translate(-450, -450)
)

image.write_file("examples/tiger.png")
