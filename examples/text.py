import pixie

font = pixie.read_font("examples/data/Roboto-Regular_1.ttf")
font.size = 20

text = "Typesetting is the arrangement and composition of text in graphic design and publishing in both digital and traditional medias."

image = pixie.Image(200, 200)
image.fill(pixie.Color(1, 1, 1, 1))

image.fill_text(
    font,
    text,
    bounds = pixie.Vector2(180, 180),
    transform = pixie.translate(10, 10)
)

image.write_file("examples/text.png")
