import pixie

def test_fields():
    font = pixie.read_font("tests/fonts/Roboto-Regular_1.ttf")
    assert font.typeface is not None
    font.size = 24
    assert font.size == 24
    font.line_height = 100
    assert font.line_height == 100
    font.text_case = pixie.UPPER_CASE
    assert font.text_case == pixie.UPPER_CASE
    font.underline = True
    assert font.underline
    font.strikethrough = True
    assert font.strikethrough
    font.no_kerning_adjustment = True
    assert font.no_kerning_adjustment
    paint = pixie.Paint(pixie.SOLID_PAINT)
    paint.color = pixie.Color(1, 1, 0, 1)
    font.paint = paint
    assert font.paint.color == paint.color

def test_paints():
    font = pixie.read_font("tests/fonts/Roboto-Regular_1.ttf")
    paint1 = pixie.Paint(pixie.SOLID_PAINT)
    paint2 = pixie.Paint(pixie.LINEAR_GRADIENT_PAINT)
    font.paints[0] = paint1
    font.paints.append(paint2)
    assert len(font.paints) == 2
    del(font.paints[0])
    assert font.paints[0].ref == paint2.ref
    assert len(font.paints) == 1
    font.paints.clear()
    assert len(font.paints) == 0

def test_procs():
    font = pixie.read_font("tests/fonts/Roboto-Regular_1.ttf")
    assert font.scale() == 0.005859375
    assert font.default_line_height() == 14
    arrangement = font.typeset("typeset")
    assert arrangement is not None
    assert font.layout_bounds("typeset") == pixie.Vector2(39, 14)
