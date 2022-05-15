"""Application Data (bge.app)

Module to access application values that remain unchanged during runtime."""

# Variables
version = (2, 7, 9)  # type: tuple[int, int, int]
"""The Blender/BGE version as a tuple of 3 ints, eg. (2, 75, 1).

Note:
    - Version tuples can be compared simply with (in)equality symbols; for example, (2, 74, 5) <= (2, 75, 0) returns True (lexical order)."""

version_string = "2.79 (sub 1)"  # type: str
"""The Blender/BGE version formatted as a string, eg. “2.75 (sub 1)”."""

version_char = "2.79"  # type: str
"""The Blender/BGE version character (for minor releases)."""

has_texture_ffmpeg = True  # type: bool
"""True if the BGE has been built with FFmpeg support, enabling use of ImageFFmpeg and VideoFFmpeg."""

has_joystick = True  # type: bool
"""True if the BGE has been built with joystick support."""

has_physics = True  # type: bool
"""True if the BGE has been built with physics support."""

# UPBGE
upbge_version = (0, 2, 4)  # type: tuple[int, int, int]
"""The UPBGE version as a tuple of 3 ints, eg. (0, 2, 3).

Note:
    - Version tuples can be compared simply with (in)equality symbols; for example, (0, 2, 2) <= (0, 2, 3) returns True (lexical order)."""

upbge_version_string = "0.2 (sub 4)"  # type: str
"""The UPBGE version formatted as a string, eg. “0.2 (sub 3)”."""
