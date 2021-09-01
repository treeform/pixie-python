import pixie

def test_fields():
    context = pixie.Context(100, 100)
    assert context.image is not None
    fill = pixie.Paint(pixie.PK_SOLID)
    fill.color = pixie.Color(1, 0, 0, 1)
    context.fill_style = fill
    assert context.fill_style == fill
    stroke = pixie.Paint(pixie.PK_SOLID)
    stroke.color = pixie.Color(0, 1, 1, 1)
    context.stroke = stroke
    assert context.stroke == stroke
    context.global_alpha = 0.5
    assert context.global_alpha == 0.5
    context.line_width = 2
    assert context.line_width == 2
    context.miter_limit = 2
    assert context.miter_limit == 2
    context.line_cap = pixie.LC_ROUND
    assert context.line_cap == pixie.LC_ROUND
    context.line_join = pixie.LJ_BEVEL
    assert context.line_join == pixie.LJ_BEVEL
    context.font = "tests/fonts/Roboto-Regular_1.ttf"
    assert context.font == "tests/fonts/Roboto-Regular_1.ttf"
    context.font_size = 18
    assert context.font_size == 18
    context.text_align = pixie.HA_CENTER
    assert context.text_align == pixie.HA_CENTER

def test_save_restore():
    context = pixie.Context(100, 100)
    paint1 = pixie.Paint(pixie.PK_SOLID)
    paint1.color = pixie.Color(1, 0, 0, 1)
    context.fill_style = paint1
    context.save()
    paint2 = pixie.Paint(pixie.PK_SOLID)
    paint2.color = pixie.Color(1, 1, 0, 1)
    context.fill_style = paint2
    context.restore()
    context.fill_style == paint1

def test_transform():
    context = pixie.Context(100, 100)
    context.get_transform() == pixie.Matrix3()
    mat3 = pixie.Matrix3()
    mat3.b = 1
    context.set_transform(mat3)
    context.get_transform().b == 1
    mat3.a = 0
    mat3.b = 0
    mat3.e = 0
    mat3.i = 0
    context.transform(mat3) # All 0 matrix
    assert context.get_transform() == mat3
    context.reset_transform()
    context.get_transform() == pixie.Matrix3()
    context.translate(10, 20)
    assert context.get_transform().g == 10
    assert context.get_transform().h == 20
    context.scale(2, 2)
    assert context.get_transform().a == 2
    context.reset_transform()
    context.rotate(180)
    assert context.get_transform().a != 1

def test_fill():
    context = pixie.Context(100, 100)
    paint = pixie.Paint(pixie.PK_SOLID)
    paint.color = pixie.Color(1, 0, 0, 1)
    context.fill_style = paint
    context.begin_path()
    context.rect(0, 0, 100, 100)
    context.fill()
    assert context.image.get_color(10, 10) == paint.color

def test_stroke():
    context = pixie.Context(100, 100)
    paint = pixie.Paint(pixie.PK_SOLID)
    paint.color = pixie.Color(1, 0, 0, 1)
    context.stroke_style = paint
    context.line_width = 10
    context.begin_path()
    context.rect(0, 0, 100, 100)
    context.stroke()
    assert context.image.get_color(0, 0) == paint.color
    assert context.image.get_color(50, 50) == pixie.Color(0, 0, 0, 0)

def test_clip():
    context = pixie.Context(100, 100)
    paint = pixie.Paint(pixie.PK_SOLID)
    paint.color = pixie.Color(1, 0, 0, 1)
    context.fill_style = paint
    context.begin_path()
    context.rect(0, 0, 50, 50)
    context.clip()
    context.begin_path()
    context.rect(0, 0, 100, 100)
    context.fill()
    assert context.image.get_color(10, 10) == paint.color
    assert context.image.get_color(60, 60) == pixie.Color(0, 0, 0, 0)

def test_paths():
    context = pixie.Context(100, 100)
    context.begin_path()
    context.move_to(0, 0)
    context.line_to(0, 0)
    context.bezier_curve_to(0, 0, 0, 0, 0, 0)
    context.quadratic_curve_to(0, 0, 0, 0)
    context.arc(0, 0, 0, 0, 0)
    context.arc_to(0, 0, 0, 0, 0)
    context.rect(0, 0, 0, 0)
    context.rounded_rect(0, 0, 0, 0, 0, 0, 0, 0)
    context.ellipse(0, 0, 0, 0)
    context.circle(0, 0, 0)
    context.polygon(0, 0, 0, 0)
    context.close_path()
    assert not context.is_point_in_path(1, 1)
    assert not context.is_point_in_stroke(1, 1)

def test_text():
    context = pixie.Context(100, 100)
    context.font = "tests/fonts/Roboto-Regular_1.ttf"

    # metrics = context.measure_text("Hello world")
    # assert metrics.width == 61

    context.fill_text("test", 0, 0)
    context.stroke_text("text", 0, 0)
