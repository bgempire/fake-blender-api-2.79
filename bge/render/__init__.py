"""Rasterizer (bge.render)

Module to manipulate general screen tasks."""

# Constants
# General
KX_TEXFACE_MATERIAL = 0  # type: int
"""Materials as defined by the texture face settings. See bge.render.getMaterialMode() and bge.render.setMaterialMode()."""

KX_BLENDER_MULTITEX_MATERIAL = 1  # type: int
"""Materials approximating blender materials with multitexturing. See bge.render.getMaterialMode() and bge.render.setMaterialMode()."""

KX_BLENDER_GLSL_MATERIAL = 2  # type: int
"""Materials approximating blender materials with GLSL. See bge.render.getMaterialMode() and bge.render.setMaterialMode()."""

VSYNC_OFF = 1  # type: int
"""Disables vsync. See bge.render.getVsync() and bge.render.setVsync()."""

VSYNC_ON = 0  # type: int
"""Enables vsync. See bge.render.getVsync() and bge.render.setVsync()."""

VSYNC_ADAPTIVE = 2  # type: int
"""Enables adaptive vsync if supported. Adaptive vsync enables vsync if the framerate is above the monitors refresh rate. Otherwise, vsync is diabled if the framerate is too low. See bge.render.getVsync() and bge.render.setVsync()."""

LEFT_EYE = 0  # type: int
"""Left eye being used during stereoscopic rendering."""

RIGHT_EYE = 1  # type: int
"""Right eye being used during stereoscopic rendering."""

RAS_OFS_RENDER_BUFFER = 1  # type: int
"""The pixel buffer for offscreen render is a RenderBuffer. Argument to offScreenCreate()."""

RAS_OFS_RENDER_TEXTURE = 2  # type: int
"""The pixel buffer for offscreen render is a Texture. Argument to offScreenCreate()."""


# HDR
HDR_NONE = 0  # type: int
"""Use 8 bit per channel image format."""

HDR_HALF_FLOAT = 1  # type: int
"""Use 16 bit float per channel image format."""

HDR_FULL_FLOAT = 2  # type: int
"""Use 32 bit float per channel image format."""


# Mipmap
RAS_MIPMAP_NONE = 0  # type: int
"""Disables mipmaps. See bge.render.getMipmapping() and bge.render.setMipmapping()."""

RAS_MIPMAP_NEAREST = 1  # type: int
"""Nearest mipmaps. See bge.render.getMipmapping() and bge.render.setMipmapping()."""

RAS_MIPMAP_LINEAR = 2  # type: int
"""Linear mipmaps. See bge.render.getMipmapping() and bge.render.setMipmapping()."""


# Functions
def getWindowWidth():
    # type: () -> int
    """Gets the width of the window (in pixels).

    Returns:
        Window width in pixels."""

    pass


def getWindowHeight():
    # type: () -> int
    """Gets the height of the window (in pixels).

    Returns:
        Window height in pixels."""

    pass


def setWindowSize(width, height):
    # type: (int, int) -> None
    """Set the width and height of the window (in pixels). This also works for fullscreen applications.

    Note:
        - Only works in the standalone player, not the Blender-embedded player.

    Args:
        width: width in pixels
        height: height in pixels"""

    pass


def setFullscreen(enable):
    # type: (bool) -> None
    """Set whether or not the window should be fullscreen.

    Note:
        - Only works in the standalone player, not the Blender-embedded player.

    Args:
        enable: True to set full screen, False to set windowed."""

    pass


def getFullscreen():
    # type: () -> bool
    """Returns whether or not the window is fullscreen.

    Note:
        - Only works in the standalone player, not the Blender-embedded player; there it always returns False.

    Returns:
        If game is in fullscreen mode."""

    pass


def getDisplayDimensions():
    # type: () -> tuple[int, int]
    """Get the display dimensions, in pixels, of the display (e.g., the monitor). Can return the size of the entire
    view, so the combination of all monitors; for example, (3840, 1080) for two side-by-side 1080p monitors.

    Returns:
        Display dimensions in pixels of the display."""

    pass


def makeScreenshot(filename):
    # type: (str) -> None
    """Writes an image file with the current displayed frame. The image is written to 'filename'. The path may be
    absolute (eg. /home/foo/image) or relative when started with // (eg. //image). Note that absolute paths are not
    portable between platforms. If the filename contains a #, it will be replaced by an incremental index so that
    screenshots can be taken multiple times without overwriting the previous ones (eg. image-#).

    Settings for the image are taken from the render settings (file format and respective settings, gamma and
    colospace conversion, etc). The image resolution matches the framebuffer, meaning, the window size and aspect
    ratio. When running from the standalone player, instead of the embedded player, only PNG files are supported.
    Additional color conversions are also not supported.

    Args:
        filename: path and name of the file to write"""

    pass


def enableVisibility(visible):
    # type: (bool) -> None
    """Deprecated; doesn't do anything."""

    pass


def showMouse(visible):
    # type: (bool) -> None
    """Enables or disables the operating system mouse cursor.

    Args:
        visible: Whether show mouse cursor. """

    pass


def setMousePosition(x, y):
    # type: (int, int) -> None
    """Sets the mouse cursor position.

    Args:
        x: X-coordinate in screen pixel coordinates.
        y: Y-coordinate in screen pixel coordinates."""

    pass


def setBackgroundColor(rgba):
    # type: (tuple[float]) -> None
    """Deprecated and no longer functional. Use bge.types.KX_WorldInfo.backgroundColor() instead."""

    pass


def setEyeSeparation(eyesep):
    # type: (float) -> None
    """Sets the eye separation for stereo mode. Usually Focal Length/30 provides a confortable value.

    Args:
        eyesep: The distance between the left and right eye."""

    pass


def getEyeSeparation():
    # type: () -> int
    """Gets the current eye separation for stereo mode.

    Returns:
        Current eye separation for stereo mode."""

    pass


def setFocalLength(focallength):
    # type: (float) -> None
    """Sets the focal length for stereo mode. It uses the current camera focal length as initial value.

    Args:
        focallength: The focal length."""

    pass


def getFocalLength():
    # type: () -> float
    """Gets the current focal length for stereo mode.

    Returns:
        Current focal length for stereo mode."""

    pass


def getStereoEye():
    # type: () -> int
    """Gets the current stereoscopy eye being rendered. This function is mainly used in a bge.types.KX_Scene.pre_draw
    callback function to customize the camera projection matrices for each stereoscopic eye.

    Returns:
        Current stereoscopy eye being rendered."""

    pass


def setMaterialMode(mode):
    # type: (int) -> None
    """Set the material mode to use for OpenGL rendering. The parameter mode can be one of the following constants:

    - KX_TEXFACE_MATERIAL
    - KX_BLENDER_MULTITEX_MATERIAL
    - KX_BLENDER_GLSL_MATERIAL

    Args:
        mode: material mode

    Note:
        - Changes will only affect newly created scenes."""

    pass


def getMaterialMode():
    # type: () -> int
    """Get the material mode to use for OpenGL rendering.

    Returns:
        Material mode to use for OpenGL rendering. One of KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL or KX_BLENDER_GLSL_MATERIAL"""

    pass


def setGLSLMaterialSetting(setting, enable):
    # type: (str, bool) -> None
    """Enables or disables a GLSL material setting. The parameter setting can be one of the following strings:

    - shaders
    - shadows
    - ramps
    - nodes
    - extra_textures

    Args:
        setting: Name of the setting.
        enable: If enable the setting."""

    pass


def getGLSLMaterialSetting(setting):
    # type: (str) -> None
    """Get the state of a GLSL material setting.

    Args:
        setting: Name of the setting.

    Returns:
        State of the passed GLSL material setting."""

    pass


def setAnisotropicFiltering(level):
    # type: (int) -> None
    """Set the anisotropic filtering level for textures. The parameter level must be one of the integers:
    (1, 2, 4, 8, 16).

    Args:
        level: The new anisotropic filtering level to use.

    Note:
        - Changing this value can cause all textures to be recreated, which can be slow."""

    pass


def getAnisotropicFiltering():
    # type: () -> int
    """Get the anisotropic filtering level used for textures.

    Returns:
        Anisotropic filtering level. One of (1, 2, 4, 8, 16)."""

    pass


def setMipmapping(value):
    # type: (int) -> None
    """Change how to use mipmapping.

    Note:
        - Changing this value can cause all textures to be recreated, which can be slow."""

    pass


def getMipmapping():
    # type: () -> int
    """Get the current mipmapping setting.

    Returns:
        Current mipmapping setting. One of RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR."""

    pass


def drawLine(fromVec, toVec, color):
    # type: (tuple[float], tuple[float], tuple[float]) -> None
    """Draw a line in the 3D scene.

    Args:
        fromVec: the origin of the line
        toVec: the end of the line
        color: the color of the line"""

    pass


def enableMotionBlur(factor):
    # type: (float) -> None
    """Enable the motion blur effect.

    Args:
        factor: The ammount of motion blur to display. Allows from 0.0 to 1.0."""

    pass


def disableMotionBlur():
    # type: () -> None
    """Disable the motion blur effect."""

    pass


def showFramerate(enable):
    # type: (bool) -> None
    """Show or hide the framerate.

    Args:
        enable: If show or hide the framerate."""

    pass


def showProfile(enable):
    # type: (bool) -> None
    """Show or hide the profile.

    Args:
        enable: If show or hide the profile."""

    pass


def showProperties(enable):
    # type: (bool) -> None
    """Show or hide the debug properties.

    Args:
        enable: If show or hide the debug properties."""

    pass


def autoDebugList(enable):
    # type: (bool) -> None
    """Enable or disable auto adding debug properties to the debug list.

    Args:
        enable: If enable auto adding debug properties to the debug list."""

    pass


def clearDebugList():
    # type: () -> None
    """Clears the debug property list."""
    pass


def setVsync(value):
    # type: (int) -> None
    """Set the vsync value.

    Args:
        value: Vsync value. One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE."""

    pass


def getVsync():
    # type: () -> int
    """Get the current vsync value.

    Returns:
        Current vsync value. One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE."""

    pass
