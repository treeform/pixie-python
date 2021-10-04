from ctypes import *
import os, sys

dir = os.path.dirname(sys.modules["pixie"].__file__)
if sys.platform == "win32":
  libName = "pixie.dll"
elif sys.platform == "darwin":
  libName = "libpixie.dylib"
else:
  libName = "libpixie.so"
dll = cdll.LoadLibrary(os.path.join(dir, libName))

class PixieError(Exception):
    pass

DEFAULT_MITER_LIMIT = 4.0

AUTO_LINE_HEIGHT = -1.0

FileFormat = c_byte
FF_PNG = 0
FF_BMP = 1
FF_JPG = 2
FF_GIF = 3

BlendMode = c_byte
BM_NORMAL = 0
BM_DARKEN = 1
BM_MULTIPLY = 2
BM_COLOR_BURN = 3
BM_LIGHTEN = 4
BM_SCREEN = 5
BM_COLOR_DODGE = 6
BM_OVERLAY = 7
BM_SOFT_LIGHT = 8
BM_HARD_LIGHT = 9
BM_DIFFERENCE = 10
BM_EXCLUSION = 11
BM_HUE = 12
BM_SATURATION = 13
BM_COLOR = 14
BM_LUMINOSITY = 15
BM_MASK = 16
BM_OVERWRITE = 17
BM_SUBTRACT_MASK = 18
BM_EXCLUDE_MASK = 19

PaintKind = c_byte
PK_SOLID = 0
PK_IMAGE = 1
PK_IMAGE_TILED = 2
PK_GRADIENT_LINEAR = 3
PK_GRADIENT_RADIAL = 4
PK_GRADIENT_ANGULAR = 5

WindingRule = c_byte
WR_NON_ZERO = 0
WR_EVEN_ODD = 1

LineCap = c_byte
LC_BUTT = 0
LC_ROUND = 1
LC_SQUARE = 2

LineJoin = c_byte
LJ_MITER = 0
LJ_ROUND = 1
LJ_BEVEL = 2

HorizontalAlignment = c_byte
HA_LEFT = 0
HA_CENTER = 1
HA_RIGHT = 2

VerticalAlignment = c_byte
VA_TOP = 0
VA_MIDDLE = 1
VA_BOTTOM = 2

TextCase = c_byte
TC_NORMAL = 0
TC_UPPER = 1
TC_LOWER = 2
TC_TITLE = 3

def check_error():
    result = dll.pixie_check_error()
    return result

def take_error():
    result = dll.pixie_take_error().decode("utf8")
    return result

class Vector2(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float)
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y

class Matrix3(Structure):
    _fields_ = [
        ("values", c_float * 9)
    ]

    def __init__(self):
        tmp = dll.pixie_matrix_3()
        self.values = tmp.values

    def __eq__(self, obj):
        return self.values[0] == obj.values[0] and self.values[1] == obj.values[1] and self.values[2] == obj.values[2] and self.values[3] == obj.values[3] and self.values[4] == obj.values[4] and self.values[5] == obj.values[5] and self.values[6] == obj.values[6] and self.values[7] == obj.values[7] and self.values[8] == obj.values[8]

    def __mul__(self, b):
        result = dll.pixie_matrix_3_mul(self, b)
        return result

class Rect(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("w", c_float),
        ("h", c_float)
    ]

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y and self.w == obj.w and self.h == obj.h

class Color(Structure):
    _fields_ = [
        ("r", c_float),
        ("g", c_float),
        ("b", c_float),
        ("a", c_float)
    ]

    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __eq__(self, obj):
        return self.r == obj.r and self.g == obj.g and self.b == obj.b and self.a == obj.a

class ColorStop(Structure):
    _fields_ = [
        ("color", Color),
        ("position", c_float)
    ]

    def __init__(self, color, position):
        self.color = color
        self.position = position

    def __eq__(self, obj):
        return self.color == obj.color and self.position == obj.position

class TextMetrics(Structure):
    _fields_ = [
        ("width", c_float)
    ]

    def __init__(self, width):
        self.width = width

    def __eq__(self, obj):
        return self.width == obj.width

class SeqFloat32(Structure):
    _fields_ = [("ref", c_ulonglong)]

    def __bool__(self):
        return self.ref != None

    def __eq__(self, obj):
        return self.ref == obj.ref

    def __del__(self):
        dll.pixie_seq_float_32_unref(self)

    def __init__(self):
        self.ref = dll.pixie_new_seq_float_32()

    def __len__(self):
        return dll.pixie_seq_float_32_len(self)

    def __getitem__(self, index):
        return dll.pixie_seq_float_32_get(self, index)

    def __setitem__(self, index, value):
        dll.pixie_seq_float_32_set(self, index, value)

    def __delitem__(self, index):
        dll.pixie_seq_float_32_delete(self, index)

    def append(self, value):
        dll.pixie_seq_float_32_add(self, value)

    def clear(self):
        dll.pixie_seq_float_32_clear(self)

class SeqSpan(Structure):
    _fields_ = [("ref", c_ulonglong)]

    def __bool__(self):
        return self.ref != None

    def __eq__(self, obj):
        return self.ref == obj.ref

    def __del__(self):
        dll.pixie_seq_span_unref(self)

    def __init__(self):
        self.ref = dll.pixie_new_seq_span()

    def __len__(self):
        return dll.pixie_seq_span_len(self)

    def __getitem__(self, index):
        return dll.pixie_seq_span_get(self, index)

    def __setitem__(self, index, value):
        dll.pixie_seq_span_set(self, index, value)

    def __delitem__(self, index):
        dll.pixie_seq_span_delete(self, index)

    def append(self, value):
        dll.pixie_seq_span_add(self, value)

    def clear(self):
        dll.pixie_seq_span_clear(self)

    def typeset(self, bounds = None, h_align = HA_LEFT, v_align = VA_TOP, wrap = True):
        """
        Lays out the character glyphs and returns the arrangement.
        Optional parameters:
        bounds: width determines wrapping and hAlign, height for vAlign
        hAlign: horizontal alignment of the text
        vAlign: vertical alignment of the text
        wrap: enable/disable text wrapping
        """
        if bounds is None:
            bounds = Vector2(0, 0)
        result = dll.pixie_seq_span_typeset(self, bounds, h_align, v_align, wrap)
        return result

    def compute_bounds(self):
        """
        Computes the width and height of the spans in pixels.
        """
        result = dll.pixie_seq_span_compute_bounds(self)
        return result

class Image(Structure):
    _fields_ = [("ref", c_ulonglong)]

    def __bool__(self):
        return self.ref != None

    def __eq__(self, obj):
        return self.ref == obj.ref

    def __del__(self):
        dll.pixie_image_unref(self)

    def __init__(self, width, height):
        result = dll.pixie_new_image(width, height)
        if check_error():
            raise PixieError(take_error())
        self.ref = result

    @property
    def width(self):
        return dll.pixie_image_get_width(self)

    @width.setter
    def width(self, width):
        dll.pixie_image_set_width(self, width)

    @property
    def height(self):
        return dll.pixie_image_get_height(self)

    @height.setter
    def height(self, height):
        dll.pixie_image_set_height(self, height)

    def write_file(self, file_path):
        """
        Writes an image to a file.
        """
        dll.pixie_image_write_file(self, file_path.encode("utf8"))
        if check_error():
            raise PixieError(take_error())

    def copy(self):
        """
        Copies the image data into a new image.
        """
        result = dll.pixie_image_copy(self)
        if check_error():
            raise PixieError(take_error())
        return result

    def get_color(self, x, y):
        """
        Gets a color at (x, y) or returns transparent black if outside of bounds.
        """
        result = dll.pixie_image_get_color(self, x, y)
        return result

    def set_color(self, x, y, color):
        """
        Sets a color at (x, y) or does nothing if outside of bounds.
        """
        dll.pixie_image_set_color(self, x, y, color)

    def fill(self, color):
        """
        Fills the image with the parameter color.
        """
        dll.pixie_image_fill(self, color)

    def flip_horizontal(self):
        """
        Flips the image around the Y axis.
        """
        dll.pixie_image_flip_horizontal(self)

    def flip_vertical(self):
        """
        Flips the image around the X axis.
        """
        dll.pixie_image_flip_vertical(self)

    def sub_image(self, x, y, w, h):
        """
        Gets a sub image from this image.
        """
        result = dll.pixie_image_sub_image(self, x, y, w, h)
        if check_error():
            raise PixieError(take_error())
        return result

    def minify_by_2(self, power = 1):
        """
        Scales the image down by an integer scale.
        """
        result = dll.pixie_image_minify_by_2(self, power)
        if check_error():
            raise PixieError(take_error())
        return result

    def magnify_by_2(self, power = 1):
        """
        Scales image up by 2 ^ power.
        """
        result = dll.pixie_image_magnify_by_2(self, power)
        if check_error():
            raise PixieError(take_error())
        return result

    def apply_opacity(self, opacity):
        """
        Multiplies alpha of the image by opacity.
        """
        dll.pixie_image_apply_opacity(self, opacity)

    def invert(self):
        """
        Inverts all of the colors and alpha.
        """
        dll.pixie_image_invert(self)

    def blur(self, radius, out_of_bounds = None):
        """
        Applies Gaussian blur to the image given a radius.
        """
        if out_of_bounds is None:
            out_of_bounds = Color(0, 0, 0, 0)
        dll.pixie_image_blur(self, radius, out_of_bounds)
        if check_error():
            raise PixieError(take_error())

    def new_mask(self):
        """
        Returns a new mask using the alpha values of the parameter image.
        """
        result = dll.pixie_image_new_mask(self)
        if check_error():
            raise PixieError(take_error())
        return result

    def resize(self, width, height):
        """
        Resize an image to a given height and width.
        """
        result = dll.pixie_image_resize(self, width, height)
        if check_error():
            raise PixieError(take_error())
        return result

    def shadow(self, offset, spread, blur, color):
        """
        Create a shadow of the image with the offset, spread and blur.
        """
        result = dll.pixie_image_shadow(self, offset, spread, blur, color)
        if check_error():
            raise PixieError(take_error())
        return result

    def super_image(self, x, y, w, h):
        """
        Either cuts a sub image or returns a super image with padded transparency.
        """
        result = dll.pixie_image_super_image(self, x, y, w, h)
        if check_error():
            raise PixieError(take_error())
        return result

    def draw(self, b, transform = None, blend_mode = BM_NORMAL):
        """
        Draws one image onto another using matrix with color blending.
        """
        if transform is None:
            transform = Matrix3()
        dll.pixie_image_draw(self, b, transform, blend_mode)
        if check_error():
            raise PixieError(take_error())

    def mask_draw(self, mask, transform = None, blend_mode = BM_MASK):
        """
        Draws a mask onto an image using a matrix with color blending.
        """
        if transform is None:
            transform = Matrix3()
        dll.pixie_image_mask_draw(self, mask, transform, blend_mode)
        if check_error():
            raise PixieError(take_error())

    def fill_gradient(self, paint):
        """
        Fills with the Paint gradient.
        """
        dll.pixie_image_fill_gradient(self, paint)
        if check_error():
            raise PixieError(take_error())

    def fill_text(self, font, text, transform = None, bounds = None, h_align = HA_LEFT, v_align = VA_TOP):
        """
        Typesets and fills the text. Optional parameters:
        transform: translation or matrix to apply
        bounds: width determines wrapping and hAlign, height for vAlign
        hAlign: horizontal alignment of the text
        vAlign: vertical alignment of the text
        """
        if transform is None:
            transform = Matrix3()
        if bounds is None:
            bounds = Vector2(0, 0)
        dll.pixie_image_fill_text(self, font, text.encode("utf8"), transform, bounds, h_align, v_align)
        if check_error():
            raise PixieError(take_error())

    def arrangement_fill_text(self, arrangement, transform = None):
        """
        Fills the text arrangement.
        """
        if transform is None:
            transform = Matrix3()
        dll.pixie_image_arrangement_fill_text(self, arrangement, transform)
        if check_error():
            raise PixieError(take_error())

    def stroke_text(self, font, text, transform = None, stroke_width = 1.0, bounds = None, h_align = HA_LEFT, v_align = VA_TOP, line_cap = LC_BUTT, line_join = LJ_MITER, miter_limit = DEFAULT_MITER_LIMIT, dashes = None):
        """
        Typesets and strokes the text. Optional parameters:
        transform: translation or matrix to apply
        bounds: width determines wrapping and hAlign, height for vAlign
        hAlign: horizontal alignment of the text
        vAlign: vertical alignment of the text
        lineCap: stroke line cap shape
        lineJoin: stroke line join shape
        """
        if transform is None:
            transform = Matrix3()
        if bounds is None:
            bounds = Vector2(0, 0)
        if dashes is None:
            dashes = SeqFloat32()
        dll.pixie_image_stroke_text(self, font, text.encode("utf8"), transform, stroke_width, bounds, h_align, v_align, line_cap, line_join, miter_limit, dashes)
        if check_error():
            raise PixieError(take_error())

    def arrangement_stroke_text(self, arrangement, transform = None, stroke_width = 1.0, line_cap = LC_BUTT, line_join = LJ_MITER, miter_limit = DEFAULT_MITER_LIMIT, dashes = None):
        """
        Strokes the text arrangement.
        """
        if transform is None:
            transform = Matrix3()
        if dashes is None:
            dashes = SeqFloat32()
        dll.pixie_image_arrangement_stroke_text(self, arrangement, transform, stroke_width, line_cap, line_join, miter_limit, dashes)
        if check_error():
            raise PixieError(take_error())

    def fill_path(self, path, paint, transform = None, winding_rule = WR_NON_ZERO):
        """
        Fills a path.
        """
        if transform is None:
            transform = Matrix3()
        dll.pixie_image_fill_path(self, path, paint, transform, winding_rule)
        if check_error():
            raise PixieError(take_error())

    def stroke_path(self, path, paint, transform = None, stroke_width = 1.0, line_cap = LC_BUTT, line_join = LJ_MITER, miter_limit = DEFAULT_MITER_LIMIT, dashes = None):
        """
        Strokes a path.
        """
        if transform is None:
            transform = Matrix3()
        if dashes is None:
            dashes = SeqFloat32()
        dll.pixie_image_stroke_path(self, path, paint, transform, stroke_width, line_cap, line_join, miter_limit, dashes)
        if check_error():
            raise PixieError(take_error())

    def new_context(self):
        """
        Create a new Context that will draw to the parameter image.
        """
        result = dll.pixie_image_new_context(self)
        return result

class Mask(Structure):
    _fields_ = [("ref", c_ulonglong)]

    def __bool__(self):
        return self.ref != None

    def __eq__(self, obj):
        return self.ref == obj.ref

    def __del__(self):
        dll.pixie_mask_unref(self)

    def __init__(self, width, height):
        result = dll.pixie_new_mask(width, height)
        if check_error():
            raise PixieError(take_error())
        self.ref = result

    @property
    def width(self):
        return dll.pixie_mask_get_width(self)

    @width.setter
    def width(self, width):
        dll.pixie_mask_set_width(self, width)

    @property
    def height(self):
        return dll.pixie_mask_get_height(self)

    @height.setter
    def height(self, height):
        dll.pixie_mask_set_height(self, height)

    def write_file(self, file_path):
        """
        Writes a mask to a file.
        """
        dll.pixie_mask_write_file(self, file_path.encode("utf8"))
        if check_error():
            raise PixieError(take_error())

    def copy(self):
        """
        Copies the image data into a new image.
        """
        result = dll.pixie_mask_copy(self)
        if check_error():
            raise PixieError(take_error())
        return result

    def get_value(self, x, y):
        """
        Gets a value at (x, y) or returns transparent black if outside of bounds.
        """
        result = dll.pixie_mask_get_value(self, x, y)
        return result

    def set_value(self, x, y, value):
        """
        Sets a value at (x, y) or does nothing if outside of bounds.
        """
        dll.pixie_mask_set_value(self, x, y, value)

    def fill(self, value):
        """
        Fills the mask with the parameter value.
        """
        dll.pixie_mask_fill(self, value)

    def minify_by_2(self, power = 1):
        """
        Scales the mask down by an integer scale.
        """
        result = dll.pixie_mask_minify_by_2(self, power)
        if check_error():
            raise PixieError(take_error())
        return result

    def magnify_by_2(self, power = 1):
        """
        Scales mask up by 2 ^ power.
        """
        result = dll.pixie_mask_magnify_by_2(self, power)
        if check_error():
            raise PixieError(take_error())
        return result

    def spread(self, spread):
        """
        Grows the mask by spread.
        """
        dll.pixie_mask_spread(self, spread)
        if check_error():
            raise PixieError(take_error())

    def ceil(self):
        """
        A value of 0 stays 0. Anything else turns into 255.
        """
        dll.pixie_mask_ceil(self)

    def new_image(self):
        result = dll.pixie_mask_new_image(self)
        if check_error():
            raise PixieError(take_error())
        return result

    def apply_opacity(self, opacity):
        """
        Multiplies alpha of the image by opacity.
        """
        dll.pixie_mask_apply_opacity(self, opacity)

    def invert(self):
        """
        Inverts all of the colors and alpha.
        """
        dll.pixie_mask_invert(self)

    def blur(self, radius, out_of_bounds = 0):
        """
        Applies Gaussian blur to the image given a radius.
        """
        dll.pixie_mask_blur(self, radius, out_of_bounds)
        if check_error():
            raise PixieError(take_error())

    def draw(self, b, transform = None, blend_mode = BM_MASK):
        """
        Draws a mask onto a mask using a matrix with color blending.
        """
        if transform is None:
            transform = Matrix3()
        dll.pixie_mask_draw(self, b, transform, blend_mode)
        if check_error():
            raise PixieError(take_error())

    def image_draw(self, image, transform = None, blend_mode = BM_MASK):
        """
        Draws a image onto a mask using a matrix with color blending.
        """
        if transform is None:
            transform = Matrix3()
        dll.pixie_mask_image_draw(self, image, transform, blend_mode)
        if check_error():
            raise PixieError(take_error())

    def fill_text(self, font, text, transform = None, bounds = None, h_align = HA_LEFT, v_align = VA_TOP):
        """
        Typesets and fills the text. Optional parameters:
        transform: translation or matrix to apply
        bounds: width determines wrapping and hAlign, height for vAlign
        hAlign: horizontal alignment of the text
        vAlign: vertical alignment of the text
        """
        if transform is None:
            transform = Matrix3()
        if bounds is None:
            bounds = Vector2(0, 0)
        dll.pixie_mask_fill_text(self, font, text.encode("utf8"), transform, bounds, h_align, v_align)
        if check_error():
            raise PixieError(take_error())

    def arrangement_fill_text(self, arrangement, transform = None):
        """
        Fills the text arrangement.
        """
        if transform is None:
            transform = Matrix3()
        dll.pixie_mask_arrangement_fill_text(self, arrangement, transform)
        if check_error():
            raise PixieError(take_error())

    def stroke_text(self, font, text, transform = None, stroke_width = 1.0, bounds = None, h_align = HA_LEFT, v_align = VA_TOP, line_cap = LC_BUTT, line_join = LJ_MITER, miter_limit = DEFAULT_MITER_LIMIT, dashes = None):
        """
        Typesets and strokes the text. Optional parameters:
        transform: translation or matrix to apply
        bounds: width determines wrapping and hAlign, height for vAlign
        hAlign: horizontal alignment of the text
        vAlign: vertical alignment of the text
        lineCap: stroke line cap shape
        lineJoin: stroke line join shape
        """
        if transform is None:
            transform = Matrix3()
        if bounds is None:
            bounds = Vector2(0, 0)
        if dashes is None:
            dashes = SeqFloat32()
        dll.pixie_mask_stroke_text(self, font, text.encode("utf8"), transform, stroke_width, bounds, h_align, v_align, line_cap, line_join, miter_limit, dashes)
        if check_error():
            raise PixieError(take_error())

    def arrangement_stroke_text(self, arrangement, transform = None, stroke_width = 1.0, line_cap = LC_BUTT, line_join = LJ_MITER, miter_limit = DEFAULT_MITER_LIMIT, dashes = None):
        """
        Strokes the text arrangement.
        """
        if transform is None:
            transform = Matrix3()
        if dashes is None:
            dashes = SeqFloat32()
        dll.pixie_mask_arrangement_stroke_text(self, arrangement, transform, stroke_width, line_cap, line_join, miter_limit, dashes)
        if check_error():
            raise PixieError(take_error())

    def fill_path(self, path, transform = None, winding_rule = WR_NON_ZERO, blend_mode = BM_NORMAL):
        """
        Fills a path.
        """
        if transform is None:
            transform = Matrix3()
        dll.pixie_mask_fill_path(self, path, transform, winding_rule, blend_mode)
        if check_error():
            raise PixieError(take_error())

    def stroke_path(self, path, transform = None, stroke_width = 1.0, line_cap = LC_BUTT, line_join = LJ_MITER, miter_limit = DEFAULT_MITER_LIMIT, dashes = None, blend_mode = BM_NORMAL):
        """
        Strokes a path.
        """
        if transform is None:
            transform = Matrix3()
        if dashes is None:
            dashes = SeqFloat32()
        dll.pixie_mask_stroke_path(self, path, transform, stroke_width, line_cap, line_join, miter_limit, dashes, blend_mode)
        if check_error():
            raise PixieError(take_error())

class Paint(Structure):
    _fields_ = [("ref", c_ulonglong)]

    def __bool__(self):
        return self.ref != None

    def __eq__(self, obj):
        return self.ref == obj.ref

    def __del__(self):
        dll.pixie_paint_unref(self)

    def __init__(self, kind):
        result = dll.pixie_new_paint(kind)
        self.ref = result

    @property
    def kind(self):
        return dll.pixie_paint_get_kind(self)

    @kind.setter
    def kind(self, kind):
        dll.pixie_paint_set_kind(self, kind)

    @property
    def blend_mode(self):
        return dll.pixie_paint_get_blend_mode(self)

    @blend_mode.setter
    def blend_mode(self, blend_mode):
        dll.pixie_paint_set_blend_mode(self, blend_mode)

    @property
    def opacity(self):
        return dll.pixie_paint_get_opacity(self)

    @opacity.setter
    def opacity(self, opacity):
        dll.pixie_paint_set_opacity(self, opacity)

    @property
    def color(self):
        return dll.pixie_paint_get_color(self)

    @color.setter
    def color(self, color):
        dll.pixie_paint_set_color(self, color)

    @property
    def image(self):
        return dll.pixie_paint_get_image(self)

    @image.setter
    def image(self, image):
        dll.pixie_paint_set_image(self, image)

    @property
    def image_mat(self):
        return dll.pixie_paint_get_image_mat(self)

    @image_mat.setter
    def image_mat(self, image_mat):
        dll.pixie_paint_set_image_mat(self, image_mat)

    class PaintGradientHandlePositions:

        def __init__(self, paint):
            self.paint = paint

        def __len__(self):
            return dll.pixie_paint_gradient_handle_positions_len(self.paint)

        def __getitem__(self, index):
            return dll.pixie_paint_gradient_handle_positions_get(self.paint, index)

        def __setitem__(self, index, value):
            dll.pixie_paint_gradient_handle_positions_set(self.paint, index, value)

        def __delitem__(self, index):
            dll.pixie_paint_gradient_handle_positions_delete(self.paint, index)

        def append(self, value):
            dll.pixie_paint_gradient_handle_positions_add(self.paint, value)

        def clear(self):
            dll.pixie_paint_gradient_handle_positions_clear(self.paint)

    @property
    def gradient_handle_positions(self):
        return self.PaintGradientHandlePositions(self)

    class PaintGradientStops:

        def __init__(self, paint):
            self.paint = paint

        def __len__(self):
            return dll.pixie_paint_gradient_stops_len(self.paint)

        def __getitem__(self, index):
            return dll.pixie_paint_gradient_stops_get(self.paint, index)

        def __setitem__(self, index, value):
            dll.pixie_paint_gradient_stops_set(self.paint, index, value)

        def __delitem__(self, index):
            dll.pixie_paint_gradient_stops_delete(self.paint, index)

        def append(self, value):
            dll.pixie_paint_gradient_stops_add(self.paint, value)

        def clear(self):
            dll.pixie_paint_gradient_stops_clear(self.paint)

    @property
    def gradient_stops(self):
        return self.PaintGradientStops(self)

    def new_paint(self):
        """
        Create a new Paint with the same properties.
        """
        result = dll.pixie_paint_new_paint(self)
        return result

class Path(Structure):
    _fields_ = [("ref", c_ulonglong)]

    def __bool__(self):
        return self.ref != None

    def __eq__(self, obj):
        return self.ref == obj.ref

    def __del__(self):
        dll.pixie_path_unref(self)

    def __init__(self):
        result = dll.pixie_new_path()
        self.ref = result

    def transform(self, mat):
        """
        Apply a matrix transform to a path.
        """
        dll.pixie_path_transform(self, mat)

    def add_path(self, other):
        """
        Adds a path to the current path.
        """
        dll.pixie_path_add_path(self, other)

    def close_path(self):
        """
        Attempts to add a straight line from the current point to the start of
        the current sub-path. If the shape has already been closed or has only
        one point, this function does nothing.
        """
        dll.pixie_path_close_path(self)

    def compute_bounds(self, transform = None):
        """
        Compute the bounds of the path.
        """
        if transform is None:
            transform = Matrix3()
        result = dll.pixie_path_compute_bounds(self, transform)
        if check_error():
            raise PixieError(take_error())
        return result

    def fill_overlaps(self, test, transform = None, winding_rule = WR_NON_ZERO):
        """
        Returns whether or not the specified point is contained in the current path.
        """
        if transform is None:
            transform = Matrix3()
        result = dll.pixie_path_fill_overlaps(self, test, transform, winding_rule)
        if check_error():
            raise PixieError(take_error())
        return result

    def stroke_overlaps(self, test, transform = None, stroke_width = 1.0, line_cap = LC_BUTT, line_join = LJ_MITER, miter_limit = DEFAULT_MITER_LIMIT, dashes = None):
        """
        Returns whether or not the specified point is inside the area contained
        by the stroking of a path.
        """
        if transform is None:
            transform = Matrix3()
        if dashes is None:
            dashes = SeqFloat32()
        result = dll.pixie_path_stroke_overlaps(self, test, transform, stroke_width, line_cap, line_join, miter_limit, dashes)
        if check_error():
            raise PixieError(take_error())
        return result

    def move_to(self, x, y):
        """
        Begins a new sub-path at the point (x, y).
        """
        dll.pixie_path_move_to(self, x, y)

    def line_to(self, x, y):
        """
        Adds a straight line to the current sub-path by connecting the sub-path's
        last point to the specified (x, y) coordinates.
        """
        dll.pixie_path_line_to(self, x, y)

    def bezier_curve_to(self, x_1, y_1, x_2, y_2, x_3, y_3):
        """
        Adds a cubic Bézier curve to the current sub-path. It requires three
        points: the first two are control points and the third one is the end
        point. The starting point is the latest point in the current path,
        which can be changed using moveTo() before creating the Bézier curve.
        """
        dll.pixie_path_bezier_curve_to(self, x_1, y_1, x_2, y_2, x_3, y_3)

    def quadratic_curve_to(self, x_1, y_1, x_2, y_2):
        """
        Adds a quadratic Bézier curve to the current sub-path. It requires two
        points: the first one is a control point and the second one is the end
        point. The starting point is the latest point in the current path,
        which can be changed using moveTo() before creating the quadratic
        Bézier curve.
        """
        dll.pixie_path_quadratic_curve_to(self, x_1, y_1, x_2, y_2)

    def elliptical_arc_to(self, rx, ry, x_axis_rotation, large_arc_flag, sweep_flag, x, y):
        """
        Adds an elliptical arc to the current sub-path, using the given radius
        ratios, sweep flags, and end position.
        """
        dll.pixie_path_elliptical_arc_to(self, rx, ry, x_axis_rotation, large_arc_flag, sweep_flag, x, y)

    def arc(self, x, y, r, a_0, a_1, ccw = False):
        """
        Adds a circular arc to the current sub-path.
        """
        dll.pixie_path_arc(self, x, y, r, a_0, a_1, ccw)
        if check_error():
            raise PixieError(take_error())

    def arc_to(self, x_1, y_1, x_2, y_2, r):
        """
        Adds a circular arc using the given control points and radius.
        Commonly used for making rounded corners.
        """
        dll.pixie_path_arc_to(self, x_1, y_1, x_2, y_2, r)
        if check_error():
            raise PixieError(take_error())

    def rect(self, x, y, w, h, clockwise = True):
        """
        Adds a rectangle.
        Clockwise param can be used to subtract a rect from a path when using
        even-odd winding rule.
        """
        dll.pixie_path_rect(self, x, y, w, h, clockwise)

    def rounded_rect(self, x, y, w, h, nw, ne, se, sw, clockwise = True):
        """
        Adds a rounded rectangle.
        Clockwise param can be used to subtract a rect from a path when using
        even-odd winding rule.
        """
        dll.pixie_path_rounded_rect(self, x, y, w, h, nw, ne, se, sw, clockwise)

    def ellipse(self, cx, cy, rx, ry):
        """
        Adds a ellipse.
        """
        dll.pixie_path_ellipse(self, cx, cy, rx, ry)

    def circle(self, cx, cy, r):
        """
        Adds a circle.
        """
        dll.pixie_path_circle(self, cx, cy, r)

    def polygon(self, x, y, size, sides):
        """
        Adds an n-sided regular polygon at (x, y) with the parameter size.
        """
        dll.pixie_path_polygon(self, x, y, size, sides)

class Typeface(Structure):
    _fields_ = [("ref", c_ulonglong)]

    def __bool__(self):
        return self.ref != None

    def __eq__(self, obj):
        return self.ref == obj.ref

    def __del__(self):
        dll.pixie_typeface_unref(self)

    @property
    def file_path(self):
        return dll.pixie_typeface_get_file_path(self).decode("utf8")

    @file_path.setter
    def file_path(self, file_path):
        dll.pixie_typeface_set_file_path(self, file_path.encode("utf8"))

    def ascent(self):
        """
        The font ascender value in font units.
        """
        result = dll.pixie_typeface_ascent(self)
        return result

    def descent(self):
        """
        The font descender value in font units.
        """
        result = dll.pixie_typeface_descent(self)
        return result

    def line_gap(self):
        """
        The font line gap value in font units.
        """
        result = dll.pixie_typeface_line_gap(self)
        return result

    def line_height(self):
        """
        The default line height in font units.
        """
        result = dll.pixie_typeface_line_height(self)
        return result

    def has_glyph(self, rune):
        """
        Returns if there is a glyph for this rune.
        """
        result = dll.pixie_typeface_has_glyph(self, rune)
        return result

    def get_glyph_path(self, rune):
        """
        The glyph path for the rune.
        """
        result = dll.pixie_typeface_get_glyph_path(self, rune)
        if check_error():
            raise PixieError(take_error())
        return result

    def get_advance(self, rune):
        """
        The advance for the rune in pixels.
        """
        result = dll.pixie_typeface_get_advance(self, rune)
        return result

    def get_kerning_adjustment(self, left, right):
        """
        The kerning adjustment for the rune pair, in pixels.
        """
        result = dll.pixie_typeface_get_kerning_adjustment(self, left, right)
        return result

    def new_font(self):
        result = dll.pixie_typeface_new_font(self)
        return result

class Font(Structure):
    _fields_ = [("ref", c_ulonglong)]

    def __bool__(self):
        return self.ref != None

    def __eq__(self, obj):
        return self.ref == obj.ref

    def __del__(self):
        dll.pixie_font_unref(self)

    @property
    def typeface(self):
        return dll.pixie_font_get_typeface(self)

    @typeface.setter
    def typeface(self, typeface):
        dll.pixie_font_set_typeface(self, typeface)

    @property
    def size(self):
        return dll.pixie_font_get_size(self)

    @size.setter
    def size(self, size):
        dll.pixie_font_set_size(self, size)

    @property
    def line_height(self):
        return dll.pixie_font_get_line_height(self)

    @line_height.setter
    def line_height(self, line_height):
        dll.pixie_font_set_line_height(self, line_height)

    class FontPaints:

        def __init__(self, font):
            self.font = font

        def __len__(self):
            return dll.pixie_font_paints_len(self.font)

        def __getitem__(self, index):
            return dll.pixie_font_paints_get(self.font, index)

        def __setitem__(self, index, value):
            dll.pixie_font_paints_set(self.font, index, value)

        def __delitem__(self, index):
            dll.pixie_font_paints_delete(self.font, index)

        def append(self, value):
            dll.pixie_font_paints_add(self.font, value)

        def clear(self):
            dll.pixie_font_paints_clear(self.font)

    @property
    def paints(self):
        return self.FontPaints(self)

    @property
    def text_case(self):
        return dll.pixie_font_get_text_case(self)

    @text_case.setter
    def text_case(self, text_case):
        dll.pixie_font_set_text_case(self, text_case)

    @property
    def underline(self):
        return dll.pixie_font_get_underline(self)

    @underline.setter
    def underline(self, underline):
        dll.pixie_font_set_underline(self, underline)

    @property
    def strikethrough(self):
        return dll.pixie_font_get_strikethrough(self)

    @strikethrough.setter
    def strikethrough(self, strikethrough):
        dll.pixie_font_set_strikethrough(self, strikethrough)

    @property
    def no_kerning_adjustments(self):
        return dll.pixie_font_get_no_kerning_adjustments(self)

    @no_kerning_adjustments.setter
    def no_kerning_adjustments(self, no_kerning_adjustments):
        dll.pixie_font_set_no_kerning_adjustments(self, no_kerning_adjustments)

    def scale(self):
        """
        The scale factor to transform font units into pixels.
        """
        result = dll.pixie_font_scale(self)
        return result

    def default_line_height(self):
        """
        The default line height in pixels for the current font size.
        """
        result = dll.pixie_font_default_line_height(self)
        return result

    def typeset(self, text, bounds = None, h_align = HA_LEFT, v_align = VA_TOP, wrap = True):
        """
        Lays out the character glyphs and returns the arrangement.
        Optional parameters:
        bounds: width determines wrapping and hAlign, height for vAlign
        hAlign: horizontal alignment of the text
        vAlign: vertical alignment of the text
        wrap: enable/disable text wrapping
        """
        if bounds is None:
            bounds = Vector2(0, 0)
        result = dll.pixie_font_typeset(self, text.encode("utf8"), bounds, h_align, v_align, wrap)
        return result

    def compute_bounds(self, text):
        """
        Computes the width and height of the text in pixels.
        """
        result = dll.pixie_font_compute_bounds(self, text.encode("utf8"))
        return result

class Span(Structure):
    _fields_ = [("ref", c_ulonglong)]

    def __bool__(self):
        return self.ref != None

    def __eq__(self, obj):
        return self.ref == obj.ref

    def __del__(self):
        dll.pixie_span_unref(self)

    def __init__(self, text, font):
        result = dll.pixie_new_span(text.encode("utf8"), font)
        self.ref = result

    @property
    def text(self):
        return dll.pixie_span_get_text(self).decode("utf8")

    @text.setter
    def text(self, text):
        dll.pixie_span_set_text(self, text.encode("utf8"))

    @property
    def font(self):
        return dll.pixie_span_get_font(self)

    @font.setter
    def font(self, font):
        dll.pixie_span_set_font(self, font)

class Arrangement(Structure):
    _fields_ = [("ref", c_ulonglong)]

    def __bool__(self):
        return self.ref != None

    def __eq__(self, obj):
        return self.ref == obj.ref

    def __del__(self):
        dll.pixie_arrangement_unref(self)

    def compute_bounds(self):
        """
        Computes the width and height of the arrangement in pixels.
        """
        result = dll.pixie_arrangement_compute_bounds(self)
        return result

class Context(Structure):
    _fields_ = [("ref", c_ulonglong)]

    def __bool__(self):
        return self.ref != None

    def __eq__(self, obj):
        return self.ref == obj.ref

    def __del__(self):
        dll.pixie_context_unref(self)

    def __init__(self, width, height):
        result = dll.pixie_new_context(width, height)
        if check_error():
            raise PixieError(take_error())
        self.ref = result

    @property
    def image(self):
        return dll.pixie_context_get_image(self)

    @image.setter
    def image(self, image):
        dll.pixie_context_set_image(self, image)

    @property
    def fill_style(self):
        return dll.pixie_context_get_fill_style(self)

    @fill_style.setter
    def fill_style(self, fill_style):
        dll.pixie_context_set_fill_style(self, fill_style)

    @property
    def stroke_style(self):
        return dll.pixie_context_get_stroke_style(self)

    @stroke_style.setter
    def stroke_style(self, stroke_style):
        dll.pixie_context_set_stroke_style(self, stroke_style)

    @property
    def global_alpha(self):
        return dll.pixie_context_get_global_alpha(self)

    @global_alpha.setter
    def global_alpha(self, global_alpha):
        dll.pixie_context_set_global_alpha(self, global_alpha)

    @property
    def line_width(self):
        return dll.pixie_context_get_line_width(self)

    @line_width.setter
    def line_width(self, line_width):
        dll.pixie_context_set_line_width(self, line_width)

    @property
    def miter_limit(self):
        return dll.pixie_context_get_miter_limit(self)

    @miter_limit.setter
    def miter_limit(self, miter_limit):
        dll.pixie_context_set_miter_limit(self, miter_limit)

    @property
    def line_cap(self):
        return dll.pixie_context_get_line_cap(self)

    @line_cap.setter
    def line_cap(self, line_cap):
        dll.pixie_context_set_line_cap(self, line_cap)

    @property
    def line_join(self):
        return dll.pixie_context_get_line_join(self)

    @line_join.setter
    def line_join(self, line_join):
        dll.pixie_context_set_line_join(self, line_join)

    @property
    def font(self):
        return dll.pixie_context_get_font(self).decode("utf8")

    @font.setter
    def font(self, font):
        dll.pixie_context_set_font(self, font.encode("utf8"))

    @property
    def font_size(self):
        return dll.pixie_context_get_font_size(self)

    @font_size.setter
    def font_size(self, font_size):
        dll.pixie_context_set_font_size(self, font_size)

    @property
    def text_align(self):
        return dll.pixie_context_get_text_align(self)

    @text_align.setter
    def text_align(self, text_align):
        dll.pixie_context_set_text_align(self, text_align)

    def save(self):
        """
        Saves the entire state of the context by pushing the current state onto
        a stack.
        """
        dll.pixie_context_save(self)
        if check_error():
            raise PixieError(take_error())

    def save_layer(self):
        """
        Saves the entire state of the context by pushing the current state onto
        a stack and allocates a new image layer for subsequent drawing. Calling
        restore blends the current layer image onto the prior layer or root image.
        """
        dll.pixie_context_save_layer(self)
        if check_error():
            raise PixieError(take_error())

    def restore(self):
        """
        Restores the most recently saved context state by popping the top entry
        in the drawing state stack. If there is no saved state, this method does
        nothing.
        """
        dll.pixie_context_restore(self)
        if check_error():
            raise PixieError(take_error())

    def begin_path(self):
        """
        Starts a new path by emptying the list of sub-paths.
        """
        dll.pixie_context_begin_path(self)

    def close_path(self):
        """
        Attempts to add a straight line from the current point to the start of
        the current sub-path. If the shape has already been closed or has only
        one point, this function does nothing.
        """
        dll.pixie_context_close_path(self)

    def fill(self, winding_rule = WR_NON_ZERO):
        """
        Fills the current path with the current fillStyle.
        """
        dll.pixie_context_fill(self, winding_rule)
        if check_error():
            raise PixieError(take_error())

    def path_fill(self, path, winding_rule = WR_NON_ZERO):
        """
        Fills the path with the current fillStyle.
        """
        dll.pixie_context_path_fill(self, path, winding_rule)
        if check_error():
            raise PixieError(take_error())

    def clip(self, winding_rule = WR_NON_ZERO):
        """
        Turns the current path into the current clipping region. The previous
        clipping region, if any, is intersected with the current or given path
        to create the new clipping region.
        """
        dll.pixie_context_clip(self, winding_rule)
        if check_error():
            raise PixieError(take_error())

    def path_clip(self, path, winding_rule = WR_NON_ZERO):
        """
        Turns the path into the current clipping region. The previous clipping
        region, if any, is intersected with the current or given path to create
        the new clipping region.
        """
        dll.pixie_context_path_clip(self, path, winding_rule)
        if check_error():
            raise PixieError(take_error())

    def stroke(self):
        """
        Strokes (outlines) the current or given path with the current strokeStyle.
        """
        dll.pixie_context_stroke(self)
        if check_error():
            raise PixieError(take_error())

    def path_stroke(self, path):
        """
        Strokes (outlines) the current or given path with the current strokeStyle.
        """
        dll.pixie_context_path_stroke(self, path)
        if check_error():
            raise PixieError(take_error())

    def measure_text(self, text):
        """
        Returns a TextMetrics object that contains information about the measured
        text (such as its width, for example).
        """
        result = dll.pixie_context_measure_text(self, text.encode("utf8"))
        if check_error():
            raise PixieError(take_error())
        return result

    def get_transform(self):
        """
        Retrieves the current transform matrix being applied to the context.
        """
        result = dll.pixie_context_get_transform(self)
        return result

    def set_transform(self, transform):
        """
        Overrides the transform matrix being applied to the context.
        """
        dll.pixie_context_set_transform(self, transform)

    def transform(self, transform):
        """
        Multiplies the current transform with the matrix described by the
        arguments of this method.
        """
        dll.pixie_context_transform(self, transform)

    def reset_transform(self):
        """
        Resets the current transform to the identity matrix.
        """
        dll.pixie_context_reset_transform(self)

    def draw_image(self, image, dx, dy):
        """
        Draws a source image onto the destination image.
        """
        dll.pixie_context_draw_image(self, image, dx, dy)
        if check_error():
            raise PixieError(take_error())

    def draw_image_2(self, image, dx, dy, d_width, d_height):
        dll.pixie_context_draw_image_2(self, image, dx, dy, d_width, d_height)
        if check_error():
            raise PixieError(take_error())

    def draw_image_3(self, image, sx, sy, s_width, s_height, dx, dy, d_width, d_height):
        dll.pixie_context_draw_image_3(self, image, sx, sy, s_width, s_height, dx, dy, d_width, d_height)
        if check_error():
            raise PixieError(take_error())

    def move_to(self, x, y):
        """
        Begins a new sub-path at the point (x, y).
        """
        dll.pixie_context_move_to(self, x, y)

    def line_to(self, x, y):
        """
        Adds a straight line to the current sub-path by connecting the sub-path's
        last point to the specified (x, y) coordinates.
        """
        dll.pixie_context_line_to(self, x, y)

    def bezier_curve_to(self, cp_1x, cp_1y, cp_2x, cp_2y, x, y):
        """
        Adds a cubic Bézier curve to the current sub-path. It requires three
        points: the first two are control points and the third one is the end
        point. The starting point is the latest point in the current path,
        which can be changed using moveTo() before creating the Bézier curve.
        """
        dll.pixie_context_bezier_curve_to(self, cp_1x, cp_1y, cp_2x, cp_2y, x, y)

    def quadratic_curve_to(self, cpx, cpy, x, y):
        """
        Adds a quadratic Bézier curve to the current sub-path. It requires two
        points: the first one is a control point and the second one is the end
        point. The starting point is the latest point in the current path,
        which can be changed using moveTo() before creating the quadratic
        Bézier curve.
        """
        dll.pixie_context_quadratic_curve_to(self, cpx, cpy, x, y)

    def arc(self, x, y, r, a_0, a_1, ccw = False):
        """
        Draws a circular arc.
        """
        dll.pixie_context_arc(self, x, y, r, a_0, a_1, ccw)
        if check_error():
            raise PixieError(take_error())

    def arc_to(self, x_1, y_1, x_2, y_2, radius):
        """
        Draws a circular arc using the given control points and radius.
        """
        dll.pixie_context_arc_to(self, x_1, y_1, x_2, y_2, radius)
        if check_error():
            raise PixieError(take_error())

    def rect(self, x, y, width, height):
        """
        Adds a rectangle to the current path.
        """
        dll.pixie_context_rect(self, x, y, width, height)

    def rounded_rect(self, x, y, w, h, nw, ne, se, sw):
        """
        Adds a rounded rectangle to the current path.
        """
        dll.pixie_context_rounded_rect(self, x, y, w, h, nw, ne, se, sw)

    def ellipse(self, x, y, rx, ry):
        """
        Adds an ellipse to the current sub-path.
        """
        dll.pixie_context_ellipse(self, x, y, rx, ry)

    def circle(self, cx, cy, r):
        """
        Adds a circle to the current path.
        """
        dll.pixie_context_circle(self, cx, cy, r)

    def polygon(self, x, y, size, sides):
        """
        Adds an n-sided regular polygon at (x, y) of size to the current path.
        """
        dll.pixie_context_polygon(self, x, y, size, sides)

    def clear_rect(self, x, y, width, height):
        """
        Erases the pixels in a rectangular area.
        """
        dll.pixie_context_clear_rect(self, x, y, width, height)
        if check_error():
            raise PixieError(take_error())

    def fill_rect(self, x, y, width, height):
        """
        Draws a rectangle that is filled according to the current fillStyle.
        """
        dll.pixie_context_fill_rect(self, x, y, width, height)
        if check_error():
            raise PixieError(take_error())

    def stroke_rect(self, x, y, width, height):
        """
        Draws a rectangle that is stroked (outlined) according to the current
        strokeStyle and other context settings.
        """
        dll.pixie_context_stroke_rect(self, x, y, width, height)
        if check_error():
            raise PixieError(take_error())

    def stroke_segment(self, ax, ay, bx, by):
        """
        Strokes a segment (draws a line from ax, ay to bx, by) according
        to the current strokeStyle and other context settings.
        """
        dll.pixie_context_stroke_segment(self, ax, ay, bx, by)
        if check_error():
            raise PixieError(take_error())

    def fill_text(self, text, x, y):
        """
        Draws the outlines of the characters of a text string at the specified
        coordinates.
        """
        dll.pixie_context_fill_text(self, text.encode("utf8"), x, y)
        if check_error():
            raise PixieError(take_error())

    def stroke_text(self, text, x, y):
        """
        Draws the outlines of the characters of a text string at the specified
        coordinates.
        """
        dll.pixie_context_stroke_text(self, text.encode("utf8"), x, y)
        if check_error():
            raise PixieError(take_error())

    def translate(self, x, y):
        """
        Adds a translation transformation to the current matrix.
        """
        dll.pixie_context_translate(self, x, y)

    def scale(self, x, y):
        """
        Adds a scaling transformation to the context units horizontally and/or
        vertically.
        """
        dll.pixie_context_scale(self, x, y)

    def rotate(self, angle):
        """
        Adds a rotation to the transformation matrix.
        """
        dll.pixie_context_rotate(self, angle)

    def is_point_in_path(self, x, y, winding_rule = WR_NON_ZERO):
        """
        Returns whether or not the specified point is contained in the current path.
        """
        result = dll.pixie_context_is_point_in_path(self, x, y, winding_rule)
        if check_error():
            raise PixieError(take_error())
        return result

    def path_is_point_in_path(self, path, x, y, winding_rule = WR_NON_ZERO):
        """
        Returns whether or not the specified point is contained in the current path.
        """
        result = dll.pixie_context_path_is_point_in_path(self, path, x, y, winding_rule)
        if check_error():
            raise PixieError(take_error())
        return result

    def is_point_in_stroke(self, x, y):
        """
        Returns whether or not the specified point is inside the area contained
        by the stroking of a path.
        """
        result = dll.pixie_context_is_point_in_stroke(self, x, y)
        if check_error():
            raise PixieError(take_error())
        return result

    def path_is_point_in_stroke(self, path, x, y):
        """
        Returns whether or not the specified point is inside the area contained
        by the stroking of a path.
        """
        result = dll.pixie_context_path_is_point_in_stroke(self, path, x, y)
        if check_error():
            raise PixieError(take_error())
        return result

def read_image(file_path):
    """
    Loads an image from a file.
    """
    result = dll.pixie_read_image(file_path.encode("utf8"))
    if check_error():
        raise PixieError(take_error())
    return result

def read_mask(file_path):
    """
    Loads a mask from a file.
    """
    result = dll.pixie_read_mask(file_path.encode("utf8"))
    if check_error():
        raise PixieError(take_error())
    return result

def read_typeface(file_path):
    """
    Loads a typeface from a file.
    """
    result = dll.pixie_read_typeface(file_path.encode("utf8"))
    if check_error():
        raise PixieError(take_error())
    return result

def read_font(file_path):
    """
    Loads a font from a file.
    """
    result = dll.pixie_read_font(file_path.encode("utf8"))
    if check_error():
        raise PixieError(take_error())
    return result

def parse_path(path):
    """
    Converts a SVG style path string into seq of commands.
    """
    result = dll.pixie_parse_path(path.encode("utf8"))
    if check_error():
        raise PixieError(take_error())
    return result

def miter_limit_to_angle(limit):
    """
    Converts miter-limit-ratio to miter-limit-angle.
    """
    result = dll.pixie_miter_limit_to_angle(limit)
    return result

def angle_to_miter_limit(angle):
    """
    Converts miter-limit-angle to miter-limit-ratio.
    """
    result = dll.pixie_angle_to_miter_limit(angle)
    return result

def parse_color(s):
    result = dll.pixie_parse_color(s.encode("utf8"))
    if check_error():
        raise PixieError(take_error())
    return result

def translate(x, y):
    result = dll.pixie_translate(x, y)
    return result

def rotate(angle):
    result = dll.pixie_rotate(angle)
    return result

def scale(x, y):
    result = dll.pixie_scale(x, y)
    return result

def inverse(m):
    result = dll.pixie_inverse(m)
    return result

dll.pixie_check_error.argtypes = []
dll.pixie_check_error.restype = c_bool

dll.pixie_take_error.argtypes = []
dll.pixie_take_error.restype = c_char_p

dll.pixie_matrix_3.argtypes = []
dll.pixie_matrix_3.restype = Matrix3

dll.pixie_matrix_3_mul.argtypes = [Matrix3, Matrix3]
dll.pixie_matrix_3_mul.restype = Matrix3

dll.pixie_seq_float_32_unref.argtypes = [SeqFloat32]
dll.pixie_seq_float_32_unref.restype = None

dll.pixie_new_seq_float_32.argtypes = []
dll.pixie_new_seq_float_32.restype = c_ulonglong

dll.pixie_seq_float_32_len.argtypes = [SeqFloat32]
dll.pixie_seq_float_32_len.restype = c_longlong

dll.pixie_seq_float_32_get.argtypes = [SeqFloat32, c_longlong]
dll.pixie_seq_float_32_get.restype = c_float

dll.pixie_seq_float_32_set.argtypes = [SeqFloat32, c_longlong, c_float]
dll.pixie_seq_float_32_set.restype = None

dll.pixie_seq_float_32_delete.argtypes = [SeqFloat32, c_longlong]
dll.pixie_seq_float_32_delete.restype = None

dll.pixie_seq_float_32_add.argtypes = [SeqFloat32, c_float]
dll.pixie_seq_float_32_add.restype = None

dll.pixie_seq_float_32_clear.argtypes = [SeqFloat32]
dll.pixie_seq_float_32_clear.restype = None

dll.pixie_seq_span_unref.argtypes = [SeqSpan]
dll.pixie_seq_span_unref.restype = None

dll.pixie_new_seq_span.argtypes = []
dll.pixie_new_seq_span.restype = c_ulonglong

dll.pixie_seq_span_len.argtypes = [SeqSpan]
dll.pixie_seq_span_len.restype = c_longlong

dll.pixie_seq_span_get.argtypes = [SeqSpan, c_longlong]
dll.pixie_seq_span_get.restype = Span

dll.pixie_seq_span_set.argtypes = [SeqSpan, c_longlong, Span]
dll.pixie_seq_span_set.restype = None

dll.pixie_seq_span_delete.argtypes = [SeqSpan, c_longlong]
dll.pixie_seq_span_delete.restype = None

dll.pixie_seq_span_add.argtypes = [SeqSpan, Span]
dll.pixie_seq_span_add.restype = None

dll.pixie_seq_span_clear.argtypes = [SeqSpan]
dll.pixie_seq_span_clear.restype = None

dll.pixie_seq_span_typeset.argtypes = [SeqSpan, Vector2, HorizontalAlignment, VerticalAlignment, c_bool]
dll.pixie_seq_span_typeset.restype = Arrangement

dll.pixie_seq_span_compute_bounds.argtypes = [SeqSpan]
dll.pixie_seq_span_compute_bounds.restype = Vector2

dll.pixie_image_unref.argtypes = [Image]
dll.pixie_image_unref.restype = None

dll.pixie_new_image.argtypes = [c_longlong, c_longlong]
dll.pixie_new_image.restype = c_ulonglong

dll.pixie_image_get_width.argtypes = [Image]
dll.pixie_image_get_width.restype = c_longlong

dll.pixie_image_set_width.argtypes = [Image, c_longlong]
dll.pixie_image_set_width.restype = None

dll.pixie_image_get_height.argtypes = [Image]
dll.pixie_image_get_height.restype = c_longlong

dll.pixie_image_set_height.argtypes = [Image, c_longlong]
dll.pixie_image_set_height.restype = None

dll.pixie_image_write_file.argtypes = [Image, c_char_p]
dll.pixie_image_write_file.restype = None

dll.pixie_image_copy.argtypes = [Image]
dll.pixie_image_copy.restype = Image

dll.pixie_image_get_color.argtypes = [Image, c_longlong, c_longlong]
dll.pixie_image_get_color.restype = Color

dll.pixie_image_set_color.argtypes = [Image, c_longlong, c_longlong, Color]
dll.pixie_image_set_color.restype = None

dll.pixie_image_fill.argtypes = [Image, Color]
dll.pixie_image_fill.restype = None

dll.pixie_image_flip_horizontal.argtypes = [Image]
dll.pixie_image_flip_horizontal.restype = None

dll.pixie_image_flip_vertical.argtypes = [Image]
dll.pixie_image_flip_vertical.restype = None

dll.pixie_image_sub_image.argtypes = [Image, c_longlong, c_longlong, c_longlong, c_longlong]
dll.pixie_image_sub_image.restype = Image

dll.pixie_image_minify_by_2.argtypes = [Image, c_longlong]
dll.pixie_image_minify_by_2.restype = Image

dll.pixie_image_magnify_by_2.argtypes = [Image, c_longlong]
dll.pixie_image_magnify_by_2.restype = Image

dll.pixie_image_apply_opacity.argtypes = [Image, c_float]
dll.pixie_image_apply_opacity.restype = None

dll.pixie_image_invert.argtypes = [Image]
dll.pixie_image_invert.restype = None

dll.pixie_image_blur.argtypes = [Image, c_float, Color]
dll.pixie_image_blur.restype = None

dll.pixie_image_new_mask.argtypes = [Image]
dll.pixie_image_new_mask.restype = Mask

dll.pixie_image_resize.argtypes = [Image, c_longlong, c_longlong]
dll.pixie_image_resize.restype = Image

dll.pixie_image_shadow.argtypes = [Image, Vector2, c_float, c_float, Color]
dll.pixie_image_shadow.restype = Image

dll.pixie_image_super_image.argtypes = [Image, c_longlong, c_longlong, c_longlong, c_longlong]
dll.pixie_image_super_image.restype = Image

dll.pixie_image_draw.argtypes = [Image, Image, Matrix3, BlendMode]
dll.pixie_image_draw.restype = None

dll.pixie_image_mask_draw.argtypes = [Image, Mask, Matrix3, BlendMode]
dll.pixie_image_mask_draw.restype = None

dll.pixie_image_fill_gradient.argtypes = [Image, Paint]
dll.pixie_image_fill_gradient.restype = None

dll.pixie_image_fill_text.argtypes = [Image, Font, c_char_p, Matrix3, Vector2, HorizontalAlignment, VerticalAlignment]
dll.pixie_image_fill_text.restype = None

dll.pixie_image_arrangement_fill_text.argtypes = [Image, Arrangement, Matrix3]
dll.pixie_image_arrangement_fill_text.restype = None

dll.pixie_image_stroke_text.argtypes = [Image, Font, c_char_p, Matrix3, c_float, Vector2, HorizontalAlignment, VerticalAlignment, LineCap, LineJoin, c_float, SeqFloat32]
dll.pixie_image_stroke_text.restype = None

dll.pixie_image_arrangement_stroke_text.argtypes = [Image, Arrangement, Matrix3, c_float, LineCap, LineJoin, c_float, SeqFloat32]
dll.pixie_image_arrangement_stroke_text.restype = None

dll.pixie_image_fill_path.argtypes = [Image, Path, Paint, Matrix3, WindingRule]
dll.pixie_image_fill_path.restype = None

dll.pixie_image_stroke_path.argtypes = [Image, Path, Paint, Matrix3, c_float, LineCap, LineJoin, c_float, SeqFloat32]
dll.pixie_image_stroke_path.restype = None

dll.pixie_image_new_context.argtypes = [Image]
dll.pixie_image_new_context.restype = Context

dll.pixie_mask_unref.argtypes = [Mask]
dll.pixie_mask_unref.restype = None

dll.pixie_new_mask.argtypes = [c_longlong, c_longlong]
dll.pixie_new_mask.restype = c_ulonglong

dll.pixie_mask_get_width.argtypes = [Mask]
dll.pixie_mask_get_width.restype = c_longlong

dll.pixie_mask_set_width.argtypes = [Mask, c_longlong]
dll.pixie_mask_set_width.restype = None

dll.pixie_mask_get_height.argtypes = [Mask]
dll.pixie_mask_get_height.restype = c_longlong

dll.pixie_mask_set_height.argtypes = [Mask, c_longlong]
dll.pixie_mask_set_height.restype = None

dll.pixie_mask_write_file.argtypes = [Mask, c_char_p]
dll.pixie_mask_write_file.restype = None

dll.pixie_mask_copy.argtypes = [Mask]
dll.pixie_mask_copy.restype = Mask

dll.pixie_mask_get_value.argtypes = [Mask, c_longlong, c_longlong]
dll.pixie_mask_get_value.restype = c_ubyte

dll.pixie_mask_set_value.argtypes = [Mask, c_longlong, c_longlong, c_ubyte]
dll.pixie_mask_set_value.restype = None

dll.pixie_mask_fill.argtypes = [Mask, c_ubyte]
dll.pixie_mask_fill.restype = None

dll.pixie_mask_minify_by_2.argtypes = [Mask, c_longlong]
dll.pixie_mask_minify_by_2.restype = Mask

dll.pixie_mask_magnify_by_2.argtypes = [Mask, c_longlong]
dll.pixie_mask_magnify_by_2.restype = Mask

dll.pixie_mask_spread.argtypes = [Mask, c_float]
dll.pixie_mask_spread.restype = None

dll.pixie_mask_ceil.argtypes = [Mask]
dll.pixie_mask_ceil.restype = None

dll.pixie_mask_new_image.argtypes = [Mask]
dll.pixie_mask_new_image.restype = Image

dll.pixie_mask_apply_opacity.argtypes = [Mask, c_float]
dll.pixie_mask_apply_opacity.restype = None

dll.pixie_mask_invert.argtypes = [Mask]
dll.pixie_mask_invert.restype = None

dll.pixie_mask_blur.argtypes = [Mask, c_float, c_ubyte]
dll.pixie_mask_blur.restype = None

dll.pixie_mask_draw.argtypes = [Mask, Mask, Matrix3, BlendMode]
dll.pixie_mask_draw.restype = None

dll.pixie_mask_image_draw.argtypes = [Mask, Image, Matrix3, BlendMode]
dll.pixie_mask_image_draw.restype = None

dll.pixie_mask_fill_text.argtypes = [Mask, Font, c_char_p, Matrix3, Vector2, HorizontalAlignment, VerticalAlignment]
dll.pixie_mask_fill_text.restype = None

dll.pixie_mask_arrangement_fill_text.argtypes = [Mask, Arrangement, Matrix3]
dll.pixie_mask_arrangement_fill_text.restype = None

dll.pixie_mask_stroke_text.argtypes = [Mask, Font, c_char_p, Matrix3, c_float, Vector2, HorizontalAlignment, VerticalAlignment, LineCap, LineJoin, c_float, SeqFloat32]
dll.pixie_mask_stroke_text.restype = None

dll.pixie_mask_arrangement_stroke_text.argtypes = [Mask, Arrangement, Matrix3, c_float, LineCap, LineJoin, c_float, SeqFloat32]
dll.pixie_mask_arrangement_stroke_text.restype = None

dll.pixie_mask_fill_path.argtypes = [Mask, Path, Matrix3, WindingRule, BlendMode]
dll.pixie_mask_fill_path.restype = None

dll.pixie_mask_stroke_path.argtypes = [Mask, Path, Matrix3, c_float, LineCap, LineJoin, c_float, SeqFloat32, BlendMode]
dll.pixie_mask_stroke_path.restype = None

dll.pixie_paint_unref.argtypes = [Paint]
dll.pixie_paint_unref.restype = None

dll.pixie_new_paint.argtypes = [PaintKind]
dll.pixie_new_paint.restype = c_ulonglong

dll.pixie_paint_get_kind.argtypes = [Paint]
dll.pixie_paint_get_kind.restype = PaintKind

dll.pixie_paint_set_kind.argtypes = [Paint, PaintKind]
dll.pixie_paint_set_kind.restype = None

dll.pixie_paint_get_blend_mode.argtypes = [Paint]
dll.pixie_paint_get_blend_mode.restype = BlendMode

dll.pixie_paint_set_blend_mode.argtypes = [Paint, BlendMode]
dll.pixie_paint_set_blend_mode.restype = None

dll.pixie_paint_get_opacity.argtypes = [Paint]
dll.pixie_paint_get_opacity.restype = c_float

dll.pixie_paint_set_opacity.argtypes = [Paint, c_float]
dll.pixie_paint_set_opacity.restype = None

dll.pixie_paint_get_color.argtypes = [Paint]
dll.pixie_paint_get_color.restype = Color

dll.pixie_paint_set_color.argtypes = [Paint, Color]
dll.pixie_paint_set_color.restype = None

dll.pixie_paint_get_image.argtypes = [Paint]
dll.pixie_paint_get_image.restype = Image

dll.pixie_paint_set_image.argtypes = [Paint, Image]
dll.pixie_paint_set_image.restype = None

dll.pixie_paint_get_image_mat.argtypes = [Paint]
dll.pixie_paint_get_image_mat.restype = Matrix3

dll.pixie_paint_set_image_mat.argtypes = [Paint, Matrix3]
dll.pixie_paint_set_image_mat.restype = None

dll.pixie_paint_gradient_handle_positions_len.argtypes = [Paint]
dll.pixie_paint_gradient_handle_positions_len.restype = c_longlong

dll.pixie_paint_gradient_handle_positions_get.argtypes = [Paint, c_longlong]
dll.pixie_paint_gradient_handle_positions_get.restype = Vector2

dll.pixie_paint_gradient_handle_positions_set.argtypes = [Paint, c_longlong, Vector2]
dll.pixie_paint_gradient_handle_positions_set.restype = None

dll.pixie_paint_gradient_handle_positions_delete.argtypes = [Paint, c_longlong]
dll.pixie_paint_gradient_handle_positions_delete.restype = None

dll.pixie_paint_gradient_handle_positions_add.argtypes = [Paint, Vector2]
dll.pixie_paint_gradient_handle_positions_add.restype = None

dll.pixie_paint_gradient_handle_positions_clear.argtypes = [Paint]
dll.pixie_paint_gradient_handle_positions_clear.restype = None

dll.pixie_paint_gradient_stops_len.argtypes = [Paint]
dll.pixie_paint_gradient_stops_len.restype = c_longlong

dll.pixie_paint_gradient_stops_get.argtypes = [Paint, c_longlong]
dll.pixie_paint_gradient_stops_get.restype = ColorStop

dll.pixie_paint_gradient_stops_set.argtypes = [Paint, c_longlong, ColorStop]
dll.pixie_paint_gradient_stops_set.restype = None

dll.pixie_paint_gradient_stops_delete.argtypes = [Paint, c_longlong]
dll.pixie_paint_gradient_stops_delete.restype = None

dll.pixie_paint_gradient_stops_add.argtypes = [Paint, ColorStop]
dll.pixie_paint_gradient_stops_add.restype = None

dll.pixie_paint_gradient_stops_clear.argtypes = [Paint]
dll.pixie_paint_gradient_stops_clear.restype = None

dll.pixie_paint_new_paint.argtypes = [Paint]
dll.pixie_paint_new_paint.restype = Paint

dll.pixie_path_unref.argtypes = [Path]
dll.pixie_path_unref.restype = None

dll.pixie_new_path.argtypes = []
dll.pixie_new_path.restype = c_ulonglong

dll.pixie_path_transform.argtypes = [Path, Matrix3]
dll.pixie_path_transform.restype = None

dll.pixie_path_add_path.argtypes = [Path, Path]
dll.pixie_path_add_path.restype = None

dll.pixie_path_close_path.argtypes = [Path]
dll.pixie_path_close_path.restype = None

dll.pixie_path_compute_bounds.argtypes = [Path, Matrix3]
dll.pixie_path_compute_bounds.restype = Rect

dll.pixie_path_fill_overlaps.argtypes = [Path, Vector2, Matrix3, WindingRule]
dll.pixie_path_fill_overlaps.restype = c_bool

dll.pixie_path_stroke_overlaps.argtypes = [Path, Vector2, Matrix3, c_float, LineCap, LineJoin, c_float, SeqFloat32]
dll.pixie_path_stroke_overlaps.restype = c_bool

dll.pixie_path_move_to.argtypes = [Path, c_float, c_float]
dll.pixie_path_move_to.restype = None

dll.pixie_path_line_to.argtypes = [Path, c_float, c_float]
dll.pixie_path_line_to.restype = None

dll.pixie_path_bezier_curve_to.argtypes = [Path, c_float, c_float, c_float, c_float, c_float, c_float]
dll.pixie_path_bezier_curve_to.restype = None

dll.pixie_path_quadratic_curve_to.argtypes = [Path, c_float, c_float, c_float, c_float]
dll.pixie_path_quadratic_curve_to.restype = None

dll.pixie_path_elliptical_arc_to.argtypes = [Path, c_float, c_float, c_float, c_bool, c_bool, c_float, c_float]
dll.pixie_path_elliptical_arc_to.restype = None

dll.pixie_path_arc.argtypes = [Path, c_float, c_float, c_float, c_float, c_float, c_bool]
dll.pixie_path_arc.restype = None

dll.pixie_path_arc_to.argtypes = [Path, c_float, c_float, c_float, c_float, c_float]
dll.pixie_path_arc_to.restype = None

dll.pixie_path_rect.argtypes = [Path, c_float, c_float, c_float, c_float, c_bool]
dll.pixie_path_rect.restype = None

dll.pixie_path_rounded_rect.argtypes = [Path, c_float, c_float, c_float, c_float, c_float, c_float, c_float, c_float, c_bool]
dll.pixie_path_rounded_rect.restype = None

dll.pixie_path_ellipse.argtypes = [Path, c_float, c_float, c_float, c_float]
dll.pixie_path_ellipse.restype = None

dll.pixie_path_circle.argtypes = [Path, c_float, c_float, c_float]
dll.pixie_path_circle.restype = None

dll.pixie_path_polygon.argtypes = [Path, c_float, c_float, c_float, c_longlong]
dll.pixie_path_polygon.restype = None

dll.pixie_typeface_unref.argtypes = [Typeface]
dll.pixie_typeface_unref.restype = None

dll.pixie_typeface_get_file_path.argtypes = [Typeface]
dll.pixie_typeface_get_file_path.restype = c_char_p

dll.pixie_typeface_set_file_path.argtypes = [Typeface, c_char_p]
dll.pixie_typeface_set_file_path.restype = None

dll.pixie_typeface_ascent.argtypes = [Typeface]
dll.pixie_typeface_ascent.restype = c_float

dll.pixie_typeface_descent.argtypes = [Typeface]
dll.pixie_typeface_descent.restype = c_float

dll.pixie_typeface_line_gap.argtypes = [Typeface]
dll.pixie_typeface_line_gap.restype = c_float

dll.pixie_typeface_line_height.argtypes = [Typeface]
dll.pixie_typeface_line_height.restype = c_float

dll.pixie_typeface_has_glyph.argtypes = [Typeface, c_int]
dll.pixie_typeface_has_glyph.restype = c_bool

dll.pixie_typeface_get_glyph_path.argtypes = [Typeface, c_int]
dll.pixie_typeface_get_glyph_path.restype = Path

dll.pixie_typeface_get_advance.argtypes = [Typeface, c_int]
dll.pixie_typeface_get_advance.restype = c_float

dll.pixie_typeface_get_kerning_adjustment.argtypes = [Typeface, c_int, c_int]
dll.pixie_typeface_get_kerning_adjustment.restype = c_float

dll.pixie_typeface_new_font.argtypes = [Typeface]
dll.pixie_typeface_new_font.restype = Font

dll.pixie_font_unref.argtypes = [Font]
dll.pixie_font_unref.restype = None

dll.pixie_font_get_typeface.argtypes = [Font]
dll.pixie_font_get_typeface.restype = Typeface

dll.pixie_font_set_typeface.argtypes = [Font, Typeface]
dll.pixie_font_set_typeface.restype = None

dll.pixie_font_get_size.argtypes = [Font]
dll.pixie_font_get_size.restype = c_float

dll.pixie_font_set_size.argtypes = [Font, c_float]
dll.pixie_font_set_size.restype = None

dll.pixie_font_get_line_height.argtypes = [Font]
dll.pixie_font_get_line_height.restype = c_float

dll.pixie_font_set_line_height.argtypes = [Font, c_float]
dll.pixie_font_set_line_height.restype = None

dll.pixie_font_paints_len.argtypes = [Font]
dll.pixie_font_paints_len.restype = c_longlong

dll.pixie_font_paints_get.argtypes = [Font, c_longlong]
dll.pixie_font_paints_get.restype = Paint

dll.pixie_font_paints_set.argtypes = [Font, c_longlong, Paint]
dll.pixie_font_paints_set.restype = None

dll.pixie_font_paints_delete.argtypes = [Font, c_longlong]
dll.pixie_font_paints_delete.restype = None

dll.pixie_font_paints_add.argtypes = [Font, Paint]
dll.pixie_font_paints_add.restype = None

dll.pixie_font_paints_clear.argtypes = [Font]
dll.pixie_font_paints_clear.restype = None

dll.pixie_font_get_text_case.argtypes = [Font]
dll.pixie_font_get_text_case.restype = TextCase

dll.pixie_font_set_text_case.argtypes = [Font, TextCase]
dll.pixie_font_set_text_case.restype = None

dll.pixie_font_get_underline.argtypes = [Font]
dll.pixie_font_get_underline.restype = c_bool

dll.pixie_font_set_underline.argtypes = [Font, c_bool]
dll.pixie_font_set_underline.restype = None

dll.pixie_font_get_strikethrough.argtypes = [Font]
dll.pixie_font_get_strikethrough.restype = c_bool

dll.pixie_font_set_strikethrough.argtypes = [Font, c_bool]
dll.pixie_font_set_strikethrough.restype = None

dll.pixie_font_get_no_kerning_adjustments.argtypes = [Font]
dll.pixie_font_get_no_kerning_adjustments.restype = c_bool

dll.pixie_font_set_no_kerning_adjustments.argtypes = [Font, c_bool]
dll.pixie_font_set_no_kerning_adjustments.restype = None

dll.pixie_font_scale.argtypes = [Font]
dll.pixie_font_scale.restype = c_float

dll.pixie_font_default_line_height.argtypes = [Font]
dll.pixie_font_default_line_height.restype = c_float

dll.pixie_font_typeset.argtypes = [Font, c_char_p, Vector2, HorizontalAlignment, VerticalAlignment, c_bool]
dll.pixie_font_typeset.restype = Arrangement

dll.pixie_font_compute_bounds.argtypes = [Font, c_char_p]
dll.pixie_font_compute_bounds.restype = Vector2

dll.pixie_span_unref.argtypes = [Span]
dll.pixie_span_unref.restype = None

dll.pixie_new_span.argtypes = [c_char_p, Font]
dll.pixie_new_span.restype = c_ulonglong

dll.pixie_span_get_text.argtypes = [Span]
dll.pixie_span_get_text.restype = c_char_p

dll.pixie_span_set_text.argtypes = [Span, c_char_p]
dll.pixie_span_set_text.restype = None

dll.pixie_span_get_font.argtypes = [Span]
dll.pixie_span_get_font.restype = Font

dll.pixie_span_set_font.argtypes = [Span, Font]
dll.pixie_span_set_font.restype = None

dll.pixie_arrangement_unref.argtypes = [Arrangement]
dll.pixie_arrangement_unref.restype = None

dll.pixie_arrangement_compute_bounds.argtypes = [Arrangement]
dll.pixie_arrangement_compute_bounds.restype = Vector2

dll.pixie_context_unref.argtypes = [Context]
dll.pixie_context_unref.restype = None

dll.pixie_new_context.argtypes = [c_longlong, c_longlong]
dll.pixie_new_context.restype = c_ulonglong

dll.pixie_context_get_image.argtypes = [Context]
dll.pixie_context_get_image.restype = Image

dll.pixie_context_set_image.argtypes = [Context, Image]
dll.pixie_context_set_image.restype = None

dll.pixie_context_get_fill_style.argtypes = [Context]
dll.pixie_context_get_fill_style.restype = Paint

dll.pixie_context_set_fill_style.argtypes = [Context, Paint]
dll.pixie_context_set_fill_style.restype = None

dll.pixie_context_get_stroke_style.argtypes = [Context]
dll.pixie_context_get_stroke_style.restype = Paint

dll.pixie_context_set_stroke_style.argtypes = [Context, Paint]
dll.pixie_context_set_stroke_style.restype = None

dll.pixie_context_get_global_alpha.argtypes = [Context]
dll.pixie_context_get_global_alpha.restype = c_float

dll.pixie_context_set_global_alpha.argtypes = [Context, c_float]
dll.pixie_context_set_global_alpha.restype = None

dll.pixie_context_get_line_width.argtypes = [Context]
dll.pixie_context_get_line_width.restype = c_float

dll.pixie_context_set_line_width.argtypes = [Context, c_float]
dll.pixie_context_set_line_width.restype = None

dll.pixie_context_get_miter_limit.argtypes = [Context]
dll.pixie_context_get_miter_limit.restype = c_float

dll.pixie_context_set_miter_limit.argtypes = [Context, c_float]
dll.pixie_context_set_miter_limit.restype = None

dll.pixie_context_get_line_cap.argtypes = [Context]
dll.pixie_context_get_line_cap.restype = LineCap

dll.pixie_context_set_line_cap.argtypes = [Context, LineCap]
dll.pixie_context_set_line_cap.restype = None

dll.pixie_context_get_line_join.argtypes = [Context]
dll.pixie_context_get_line_join.restype = LineJoin

dll.pixie_context_set_line_join.argtypes = [Context, LineJoin]
dll.pixie_context_set_line_join.restype = None

dll.pixie_context_get_font.argtypes = [Context]
dll.pixie_context_get_font.restype = c_char_p

dll.pixie_context_set_font.argtypes = [Context, c_char_p]
dll.pixie_context_set_font.restype = None

dll.pixie_context_get_font_size.argtypes = [Context]
dll.pixie_context_get_font_size.restype = c_float

dll.pixie_context_set_font_size.argtypes = [Context, c_float]
dll.pixie_context_set_font_size.restype = None

dll.pixie_context_get_text_align.argtypes = [Context]
dll.pixie_context_get_text_align.restype = HorizontalAlignment

dll.pixie_context_set_text_align.argtypes = [Context, HorizontalAlignment]
dll.pixie_context_set_text_align.restype = None

dll.pixie_context_save.argtypes = [Context]
dll.pixie_context_save.restype = None

dll.pixie_context_save_layer.argtypes = [Context]
dll.pixie_context_save_layer.restype = None

dll.pixie_context_restore.argtypes = [Context]
dll.pixie_context_restore.restype = None

dll.pixie_context_begin_path.argtypes = [Context]
dll.pixie_context_begin_path.restype = None

dll.pixie_context_close_path.argtypes = [Context]
dll.pixie_context_close_path.restype = None

dll.pixie_context_fill.argtypes = [Context, WindingRule]
dll.pixie_context_fill.restype = None

dll.pixie_context_path_fill.argtypes = [Context, Path, WindingRule]
dll.pixie_context_path_fill.restype = None

dll.pixie_context_clip.argtypes = [Context, WindingRule]
dll.pixie_context_clip.restype = None

dll.pixie_context_path_clip.argtypes = [Context, Path, WindingRule]
dll.pixie_context_path_clip.restype = None

dll.pixie_context_stroke.argtypes = [Context]
dll.pixie_context_stroke.restype = None

dll.pixie_context_path_stroke.argtypes = [Context, Path]
dll.pixie_context_path_stroke.restype = None

dll.pixie_context_measure_text.argtypes = [Context, c_char_p]
dll.pixie_context_measure_text.restype = TextMetrics

dll.pixie_context_get_transform.argtypes = [Context]
dll.pixie_context_get_transform.restype = Matrix3

dll.pixie_context_set_transform.argtypes = [Context, Matrix3]
dll.pixie_context_set_transform.restype = None

dll.pixie_context_transform.argtypes = [Context, Matrix3]
dll.pixie_context_transform.restype = None

dll.pixie_context_reset_transform.argtypes = [Context]
dll.pixie_context_reset_transform.restype = None

dll.pixie_context_draw_image.argtypes = [Context, Image, c_float, c_float]
dll.pixie_context_draw_image.restype = None

dll.pixie_context_draw_image_2.argtypes = [Context, Image, c_float, c_float, c_float, c_float]
dll.pixie_context_draw_image_2.restype = None

dll.pixie_context_draw_image_3.argtypes = [Context, Image, c_float, c_float, c_float, c_float, c_float, c_float, c_float, c_float]
dll.pixie_context_draw_image_3.restype = None

dll.pixie_context_move_to.argtypes = [Context, c_float, c_float]
dll.pixie_context_move_to.restype = None

dll.pixie_context_line_to.argtypes = [Context, c_float, c_float]
dll.pixie_context_line_to.restype = None

dll.pixie_context_bezier_curve_to.argtypes = [Context, c_float, c_float, c_float, c_float, c_float, c_float]
dll.pixie_context_bezier_curve_to.restype = None

dll.pixie_context_quadratic_curve_to.argtypes = [Context, c_float, c_float, c_float, c_float]
dll.pixie_context_quadratic_curve_to.restype = None

dll.pixie_context_arc.argtypes = [Context, c_float, c_float, c_float, c_float, c_float, c_bool]
dll.pixie_context_arc.restype = None

dll.pixie_context_arc_to.argtypes = [Context, c_float, c_float, c_float, c_float, c_float]
dll.pixie_context_arc_to.restype = None

dll.pixie_context_rect.argtypes = [Context, c_float, c_float, c_float, c_float]
dll.pixie_context_rect.restype = None

dll.pixie_context_rounded_rect.argtypes = [Context, c_float, c_float, c_float, c_float, c_float, c_float, c_float, c_float]
dll.pixie_context_rounded_rect.restype = None

dll.pixie_context_ellipse.argtypes = [Context, c_float, c_float, c_float, c_float]
dll.pixie_context_ellipse.restype = None

dll.pixie_context_circle.argtypes = [Context, c_float, c_float, c_float]
dll.pixie_context_circle.restype = None

dll.pixie_context_polygon.argtypes = [Context, c_float, c_float, c_float, c_longlong]
dll.pixie_context_polygon.restype = None

dll.pixie_context_clear_rect.argtypes = [Context, c_float, c_float, c_float, c_float]
dll.pixie_context_clear_rect.restype = None

dll.pixie_context_fill_rect.argtypes = [Context, c_float, c_float, c_float, c_float]
dll.pixie_context_fill_rect.restype = None

dll.pixie_context_stroke_rect.argtypes = [Context, c_float, c_float, c_float, c_float]
dll.pixie_context_stroke_rect.restype = None

dll.pixie_context_stroke_segment.argtypes = [Context, c_float, c_float, c_float, c_float]
dll.pixie_context_stroke_segment.restype = None

dll.pixie_context_fill_text.argtypes = [Context, c_char_p, c_float, c_float]
dll.pixie_context_fill_text.restype = None

dll.pixie_context_stroke_text.argtypes = [Context, c_char_p, c_float, c_float]
dll.pixie_context_stroke_text.restype = None

dll.pixie_context_translate.argtypes = [Context, c_float, c_float]
dll.pixie_context_translate.restype = None

dll.pixie_context_scale.argtypes = [Context, c_float, c_float]
dll.pixie_context_scale.restype = None

dll.pixie_context_rotate.argtypes = [Context, c_float]
dll.pixie_context_rotate.restype = None

dll.pixie_context_is_point_in_path.argtypes = [Context, c_float, c_float, WindingRule]
dll.pixie_context_is_point_in_path.restype = c_bool

dll.pixie_context_path_is_point_in_path.argtypes = [Context, Path, c_float, c_float, WindingRule]
dll.pixie_context_path_is_point_in_path.restype = c_bool

dll.pixie_context_is_point_in_stroke.argtypes = [Context, c_float, c_float]
dll.pixie_context_is_point_in_stroke.restype = c_bool

dll.pixie_context_path_is_point_in_stroke.argtypes = [Context, Path, c_float, c_float]
dll.pixie_context_path_is_point_in_stroke.restype = c_bool

dll.pixie_read_image.argtypes = [c_char_p]
dll.pixie_read_image.restype = Image

dll.pixie_read_mask.argtypes = [c_char_p]
dll.pixie_read_mask.restype = Mask

dll.pixie_read_typeface.argtypes = [c_char_p]
dll.pixie_read_typeface.restype = Typeface

dll.pixie_read_font.argtypes = [c_char_p]
dll.pixie_read_font.restype = Font

dll.pixie_parse_path.argtypes = [c_char_p]
dll.pixie_parse_path.restype = Path

dll.pixie_miter_limit_to_angle.argtypes = [c_float]
dll.pixie_miter_limit_to_angle.restype = c_float

dll.pixie_angle_to_miter_limit.argtypes = [c_float]
dll.pixie_angle_to_miter_limit.restype = c_float

dll.pixie_parse_color.argtypes = [c_char_p]
dll.pixie_parse_color.restype = Color

dll.pixie_translate.argtypes = [c_float, c_float]
dll.pixie_translate.restype = Matrix3

dll.pixie_rotate.argtypes = [c_float]
dll.pixie_rotate.restype = Matrix3

dll.pixie_scale.argtypes = [c_float, c_float]
dll.pixie_scale.restype = Matrix3

dll.pixie_inverse.argtypes = [Matrix3]
dll.pixie_inverse.restype = Matrix3

