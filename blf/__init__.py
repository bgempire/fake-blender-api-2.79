"""Font Drawing (blf)

This module provides access to blenders text drawing functions."""

# Constants
CLIPPING = 2
KERNING_DEFAULT = 8
ROTATION = 1
SHADOW = 4
WORD_WRAP = 128


def aspect(fontid, aspect):
    # type: (int, float) -> None
    """Set the aspect for drawing text. 

    Args:
        fontid: The id of the typeface as returned by blf.load(), for default font use 0.
        aspect: The aspect ratio for text drawing to use."""

    pass


def blur(fontid, radius):
    # type: (int, int) -> None
    """Set the blur radius for drawing text.

    Args:
        fontid (int): The id of the typeface as returned by blf.load(), for default font use 0.
        radius (int): The radius for blurring text (in pixels)."""

    pass


def clipping(fontid, xmin, ymin, xmax, ymax):
    # type: (int, float, float, float, float) -> None
    """Set the clipping, enable/disable using CLIPPING.

    Args:
        fontid (int): The id of the typeface as returned by blf.load(), for default font use 0.
        xmin (float): Clip the drawing area by these bounds.
        ymin (float): Clip the drawing area by these bounds.
        xmax (float): Clip the drawing area by these bounds.
        ymax (float): Clip the drawing area by these bounds."""

    pass


def dimensions(fontid, text):
    # type: (int, str) -> tuple[float]
    """Return the width and height of the text.

    Args:
        fontid: The id of the typeface as returned by blf.load(), for default font use 0.
        text: the text to draw.

    Returns:
        tuple[float]: the width and height of the text."""

    pass


def disable(fontid, option):
    # type: (int, int) -> None
    """Disable option.

    Args:
        fontid: The id of the typeface as returned by blf.load(), for default font use 0.
        option: One of ROTATION, CLIPPING, SHADOW or KERNING_DEFAULT."""

    pass


def draw(fontid, text):
    # type: (int, str) -> None
    """Draw text in the current context.

    fontid: The id of the typeface as returned by blf.load(), for default font use 0.
    text: the text to draw."""

    pass


def enable(fontid, option):
    # type: (int, int) -> None
    """Enable option.

    fontid: The id of the typeface as returned by blf.load(), for default font use 0.
    option: One of ROTATION, CLIPPING, SHADOW or KERNING_DEFAULT."""

    pass


def load(filename):
    # type: (str) -> int
    """Load a new font.

    Args:
        filename: the filename of the font.

    Returns:
        The new font's fontid or -1 if there was an error."""

    pass


def position(fontid, x, y, z):
    # type: (int, float, float, float) -> None
    """Set the position for drawing text.

    Args:
        fontid: The id of the typeface as returned by blf.load(), for default font use 0.
        x: X axis position to draw the text.
        y: Y axis position to draw the text.
        z: Z axis position to draw the text."""

    pass


def rotation(fontid, angle):
    # type: (int, float) -> None
    """Set the text rotation angle, enable/disable using ROTATION.

    Args:
        fontid: The id of the typeface as returned by blf.load(), for default font use 0.
        angle: The angle for text drawing to use."""

    pass


def shadow(fontid, level, r, g, b, a):
    # type: (int, int, float, float, float, float) -> None
    """Shadow options, enable/disable using SHADOW .

    Args:
        fontid: The id of the typeface as returned by blf.load(), for default font use 0.
        level: The blur level, can be 3, 5 or 0.
        r: Shadow color (red channel 0.0 - 1.0).
        g: Shadow color (green channel 0.0 - 1.0).
        b: Shadow color (blue channel 0.0 - 1.0).
        a: Shadow color (alpha channel 0.0 - 1.0)."""

    pass


def shadow_offset(fontid, x, y):
    # type: (int, float, float) -> None
    """Set the offset for shadow text.

    Args:
        fontid: The id of the typeface as returned by blf.load(), for default font use 0.
        x: Vertical shadow offset value in pixels.
        y: Horizontal shadow offset value in pixels."""

    pass


def size(fontid, size, dpi):
    # type: (int, int, int) -> None
    """Set the size and dpi for drawing text.

    Args:
        fontid (int): The id of the typeface as returned by blf.load(), for default font use 0.
        size (int): Point size of the font.
        dpi (int): dots per inch value to use for drawing."""

    pass


def unload(filename):
    # type: (str) -> None
    """Unload an existing font.

    Args:
        filename (str): the filename of the font."""

    pass


def word_wrap(fontid, wrap_width):
    # type: (int, int) -> None
    """Set the wrap width, enable/disable using WORD_WRAP.

    Args:
        fontid (int): The id of the typeface as returned by blf.load(), for default font use 0.
        wrap_width (int): The width (in pixels) to wrap words at."""

    pass
