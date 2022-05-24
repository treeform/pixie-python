import pixie

def test():
    path = pixie.Path()
    path.move_to(0, 0)
    path.line_to(0, 0)
    path.bezier_curve_to(0, 0, 0, 0, 0, 0)
    path.quadratic_curve_to(0, 0, 0, 0)
    path.elliptical_arc_to(0, 0, 0, True, True, 0, 0)
    path.arc(0, 0, 0, 0, 0)
    path.arc_to(0, 0, 0, 0, 0)
    path.rect(0, 0, 0, 0)
    path.rounded_rect(0, 0, 0, 0, 0, 0, 0, 0)
    path.ellipse(0, 0, 0, 0)
    path.circle(0, 0, 0)
    path.polygon(0, 0, 0, 3)
    path.transform(pixie.Matrix3())
    path.add_path(pixie.Path())
    path.close_path()
    assert path.compute_bounds() == pixie.Rect(0, 0, 0, 0)
    assert not path.fill_overlaps(pixie.Vector2(1, 1))
    assert not path.stroke_overlaps(pixie.Vector2(1, 1))
