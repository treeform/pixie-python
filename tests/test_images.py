import pixie

def test_error():
    try:
        image = pixie.Image(-100, -100)
    except:
        return
    assert False # Should go into except block and return

def test_basic():
    image = pixie.Image(100, 100)
    assert image.width == 100
    assert image.height == 100
    assert image.wh() == pixie.Vector2(100, 100)
    image.set_color(50, 25, pixie.Color(1, 1, 0, 1))
    assert image.get_color(50, 25) == pixie.Color(1, 1, 0, 1)
    image.fill(pixie.Color(1, 0, 0, 1))
    assert image.get_color(50, 25) == pixie.Color(1, 0, 0, 1)
    image.write_file("tests/images/red.png")
    copy = image.copy()
    copy.fill(pixie.Color(0, 0, 1, 1))
    copy.write_file("tests/images/blue.png")

def test_flips():
    image = pixie.Image(100, 100)
    path = pixie.parse_path("M 10,30 A 20,20 0,0,1 50,30 A 20,20 0,0,1 90,30 Q 90,60 50,90 Q 10,60 10,30 z")
    path.polygon(50, 50, 20, 5)
    paint = pixie.Paint(pixie.PK_SOLID)
    paint.color = pixie.Color(1, 0, 0, 1)
    image.fill_path(path, paint)
    image.flip_vertical()
    image.write_file("tests/images/flip_vertical.png")
    path2 = pixie.Path()
    path2.rect(0, 0, 10, 100)
    image.fill_path(path2, paint)
    image.flip_horizontal()
    image.write_file("tests/images/flip_horizontal.png")

def test_subsuper():
    image = pixie.Image(100, 100)
    path = pixie.Path()
    path.rounded_rect(10, 10, 80, 80, 10, 10, 10, 10)
    paint = pixie.Paint(pixie.PK_SOLID)
    paint.color = pixie.Color(1, 1, 1, 1)
    image.fill_path(path, paint)
    image.sub_image(0, 0, 20, 20).write_file("tests/images/sub_image.png")
    image.super_image(-10, -10, 120, 120).write_file("tests/images/super_image.png")

def test_minify_by_2():
    image = pixie.Image(400, 400)
    image.fill(pixie.Color(0, 0, 1, 1))
    image = image.minify_by_2(2)
    image.write_file("tests/images/minified.png")

def test_magnify_by_2():
    image = pixie.Image(25, 25)
    image.fill(pixie.Color(0, 1, 0, 1))
    image = image.magnify_by_2(2)
    image.write_file("tests/images/magnified.png")

def test_paths():
    path = pixie.Path()
    path.rect(25, 25, 50, 50)

    paint = pixie.Paint(pixie.PK_SOLID)
    paint.color = pixie.Color(1, 0, 1, 1)

    fill = pixie.Image(100, 100)
    fill.fill_path(path, paint)
    fill.write_file("tests/images/fill1.png")

    stroke = pixie.Image(100, 100)
    stroke.stroke_path(path, paint, stroke_width=10)
    stroke.write_file("tests/images/stroke1.png")

def test_new_mask():
    image = pixie.Image(100, 100)
    image.fill(pixie.Color(1, 1, 1, 1))

    mask = image.new_mask()
    assert mask.wh() == pixie.Vector2(100, 100)
    assert mask.get_value(5, 50) == 255

def test_apply_opacity():
    image = pixie.Image(100, 100)
    image.fill(pixie.Color(1, 1, 1, 1))

    image.apply_opacity(0.6)
    assert image.get_color(10, 10) == pixie.Color(1, 1, 1, 0.6)

def test_invert():
    image = pixie.Image(100, 100)
    assert image.get_color(30, 30) == pixie.Color(0, 0, 0, 0)
    image.invert()
    assert image.get_color(30, 30) == pixie.Color(1, 1, 1, 1)

def test_blur():
    path = pixie.Path()
    path.rect(25, 25, 50, 50)

    paint = pixie.Paint(pixie.PK_SOLID)
    paint.color = pixie.Color(1, 1, 0, 1)

    image = pixie.Image(100, 100)
    image.fill_path(path, paint)

    image.blur(10)
    image.write_file("tests/images/blur.png")

def test_draw():
    a = pixie.Image(100, 100)
    a_path = pixie.Path()
    a_path.rect(25, 25, 50, 50)
    a_paint = pixie.Paint(pixie.PK_SOLID)
    a_paint.color = pixie.Color(1, 1, 0, 0.5)
    a.fill_path(a_path, a_paint)

    b = pixie.Image(100, 100)
    b_path = pixie.Path()
    b_path.rect(0, 0, 100, 50)
    b_paint = pixie.Paint(pixie.PK_SOLID)
    b_paint.color = pixie.Color(1, 0, 1, 0.5)
    b.fill_path(b_path, b_paint)

    a.draw(b)
    a.write_file("tests/images/draw.png")

def test_draw_mask():
    image = pixie.Image(100, 100)
    image_path = pixie.Path()
    image_path.rect(0, 0, 100, 30)
    image_paint = pixie.Paint(pixie.PK_SOLID)
    image_paint.color = pixie.Color(1, 1, 1, 1)
    image.fill_path(image_path, image_paint)

    mask = pixie.Mask(100, 100)
    mask_path = pixie.Path()
    mask_path.rect(25, 25, 50, 50)
    mask.fill_path(mask_path)

    image.mask_draw(mask)
    image.write_file("tests/images/mask_draw.png")

def test_shadow():
    image = pixie.Image(100, 100)
    path = pixie.Path()
    path.rounded_rect(20, 20, 60, 60, 10, 10, 10, 10)
    paint = pixie.Paint(pixie.PK_SOLID)
    paint.color = pixie.Color(1, 1, 1, 1)
    image.fill_path(path, paint)
    shadow = image.shadow(pixie.Vector2(0, 0), 2, 4, pixie.Color(0, 0, 0, 1))
    shadow.write_file("tests/images/shadow.png")

def test_text():
    font = pixie.read_font("tests/fonts/Roboto-Regular_1.ttf")
    font.size = 72

    fill = pixie.Image(100, 100)
    fill.fill_text(font, "fill")

    fill.write_file("tests/images/fill_text.png")

    stroke = pixie.Image(100, 100)
    stroke.stroke_text(font, "fill", stroke_width=3)

    stroke.write_file("tests/images/stroke_text.png")

def test_fill_gradient():
    paint = pixie.Paint(pixie.PK_GRADIENT_LINEAR)
    paint.gradient_handle_positions.append(pixie.Vector2(0, 50))
    paint.gradient_handle_positions.append(pixie.Vector2(100, 50))
    paint.gradient_stops.append(pixie.ColorStop(pixie.Color(1, 0, 0, 1), 0))
    paint.gradient_stops.append(pixie.ColorStop(pixie.Color(1, 0, 0, 0.15625), 1.0))

    image = pixie.Image(100, 100)
    image.fill_gradient(paint)
    image.write_file("tests/images/fill_gradient.png")

def test_new_context():
    image = pixie.Image(100, 100)
    context = image.new_context()
    assert context.image == image
