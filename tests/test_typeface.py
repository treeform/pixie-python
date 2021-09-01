import pixie

def test_fields():
    typeface = pixie.read_typeface("tests/fonts/Roboto-Regular_1.ttf")
    assert typeface.file_path == "tests/fonts/Roboto-Regular_1.ttf"

def test_procs():
    typeface = pixie.read_typeface("tests/fonts/Roboto-Regular_1.ttf")
    assert typeface.ascent() == 1900
    assert typeface.descent() == -500
    assert typeface.line_gap() == 0
    assert typeface.line_height() == 2400
    assert typeface.get_glyph_path(50) is not None
    assert typeface.get_advance(32) == 507
    assert typeface.get_kerning_adjustment(84, 101) == -99 # Te
    assert typeface.new_font() is not None
