import pixie

def test_basic_fields():
    paint = pixie.Paint(pixie.SOLID_PAINT)
    assert paint.kind == pixie.SOLID_PAINT
    paint.kind = pixie.IMAGE_PAINT
    assert paint.kind == pixie.IMAGE_PAINT
    paint.blend_mode = pixie.MULTIPLY_BLEND
    assert paint.blend_mode == pixie.MULTIPLY_BLEND
    paint.opacity = 0.5
    assert paint.opacity == 0.5
    paint.color = pixie.Color(1, 0, 0, 1)
    assert paint.color == pixie.Color(1, 0, 0, 1)
    paint.image = pixie.Image(100, 100)
    assert paint.image.width == 100
    assert paint.image.height == 100
    paint.image_mat = pixie.Matrix3()
    assert paint.image_mat == pixie.Matrix3()

    paint2 = paint.new_paint()
    assert paint2 != paint

def test_seq_fields():
    paint = pixie.Paint(pixie.LINEAR_GRADIENT_PAINT)

    paint.gradient_handle_positions.append(pixie.Vector2(100, 100))
    paint.gradient_handle_positions.append(pixie.Vector2(200, 200))
    del(paint.gradient_handle_positions[0])
    assert paint.gradient_handle_positions[0] == pixie.Vector2(200, 200)
    assert len(paint.gradient_handle_positions) == 1
    paint.gradient_handle_positions.clear()
    assert len(paint.gradient_handle_positions) == 0

    paint.gradient_stops.append(pixie.ColorStop(pixie.Color(1, 1, 1, 1), 0.5))
    paint.gradient_stops.append(pixie.ColorStop(pixie.Color(1, 0, 0, 1), 0.5))
    del(paint.gradient_stops[0])
    assert paint.gradient_stops[0] == pixie.ColorStop(pixie.Color(1, 0, 0, 1), 0.5)
    assert len(paint.gradient_stops) == 1
    paint.gradient_stops.clear()
    assert len(paint.gradient_stops) == 0
