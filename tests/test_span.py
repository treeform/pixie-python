import pixie

def test_fields():
    font = pixie.read_font("tests/fonts/Roboto-Regular_1.ttf")
    span = pixie.Span("a", font)
    assert span.text == "a"
    assert span.font == font

def test_procs():
    font = pixie.read_font("tests/fonts/Roboto-Regular_1.ttf")
    span = pixie.Span("typeset", font)
    spans = pixie.SeqSpan()
    spans.append(span)
    assert spans.typeset() is not None
    assert spans.layout_bounds() == pixie.Vector2(39, 14)
