import pixie

def test_error():
    try:
        mask = pixie.Mask(-100, -100)
    except:
        return
    assert False # Should go into except block and return

def test_basic():
    mask = pixie.Mask(100, 100)
    assert mask.width == 100
    assert mask.height == 100
    mask.set_value(50, 25, 100)
    assert mask.get_value(50, 25) == 100
    mask.fill(127)
    assert mask.get_value(50, 25) == 127
    mask.write_file("tests/masks/127.png")
    copy = mask.copy()
    copy.fill(255)
    copy.write_file("tests/masks/255.png")

def test_minify_by_2():
    mask = pixie.Mask(400, 400)
    mask.fill(255)
    mask = mask.minify_by_2(2)
    mask.write_file("tests/masks/minified.png")

def test_paths():
    path = pixie.Path()
    path.rect(25, 25, 50, 50)

    fill = pixie.Mask(100, 100)
    fill.fill_path(path)
    fill.write_file("tests/masks/fill1.png")

    stroke = pixie.Mask(100, 100)
    stroke.stroke_path(path, stroke_width=10)
    stroke.write_file("tests/masks/stroke1.png")

def test_spread():
    path = pixie.Path()
    path.rect(25, 25, 50, 50)

    mask = pixie.Mask(100, 100)
    mask.fill_path(path)

    mask.spread(10)
    mask.write_file("tests/masks/spread.png")

def test_ceil():
    mask = pixie.Mask(100, 100)
    mask.fill(127)
    mask.ceil()
    assert mask.get_value(10, 10) == 255

def test_new_image():
    mask = pixie.Mask(100, 100)
    mask.fill(255)

    image = mask.new_image()
    assert image.width == 100
    assert image.height == 100
    assert image.get_color(5, 50).a == 1

def test_apply_opacity():
    mask = pixie.Mask(100, 100)
    mask.fill(255)

    mask.apply_opacity(0.6)
    assert mask.get_value(10, 10) == 153

def test_invert():
    mask = pixie.Mask(100, 100)
    assert mask.get_value(30, 30) == 0
    mask.invert()
    assert mask.get_value(30, 30) == 255

def test_blur():
    path = pixie.Path()
    path.rect(25, 25, 50, 50)

    mask = pixie.Mask(100, 100)
    mask.fill_path(path)

    mask.blur(10)
    mask.write_file("tests/masks/blur.png")

def test_draw():
    a = pixie.Mask(100, 100)
    a_path = pixie.Path()
    a_path.rect(25, 25, 50, 50)
    a.fill_path(a_path)

    b = pixie.Mask(100, 100)
    b_path = pixie.Path()
    b_path.rect(0, 0, 100, 50)
    b.fill_path(b_path)

    a.draw(b)
    a.write_file("tests/masks/draw.png")

def test_draw_image():
    mask = pixie.Mask(100, 100)
    mask_path = pixie.Path()
    mask_path.rect(25, 25, 50, 50)
    mask.fill_path(mask_path)

    image = pixie.Image(100, 100)
    image_path = pixie.Path()
    image_path.rect(0, 0, 100, 30)
    image_paint = pixie.Paint(pixie.PK_SOLID)
    image_paint.color = pixie.Color(1, 1, 1, 1)
    image.fill_path(image_path, image_paint)

    mask.image_draw(image)
    mask.write_file("tests/masks/image_draw.png")

def test_text():
    font = pixie.read_font("tests/fonts/Roboto-Regular_1.ttf")
    font.size = 72

    fill = pixie.Mask(100, 100)
    fill.fill_text(font, "fill")

    fill.write_file("tests/masks/fill_text.png")

    stroke = pixie.Mask(100, 100)
    stroke.stroke_text(font, "fill", stroke_width=3)

    stroke.write_file("tests/masks/stroke_text.png")
