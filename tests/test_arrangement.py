import pixie

def test_procs():
    font = pixie.read_font("tests/fonts/Roboto-Regular_1.ttf")
    span = pixie.Span("typeset", font)
    spans = pixie.SeqSpan()
    spans.append(span)
    arrangement = spans.typeset()
    assert arrangement.compute_bounds() == pixie.Vector2(39, 14)
