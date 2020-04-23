"""Module to manipulate general screen tasks."""

## Constants
# General
KX_TEXFACE_MATERIAL = 0
KX_BLENDER_MULTITEX_MATERIAL = 1
KX_BLENDER_GLSL_MATERIAL = 2
VSYNC_OFF = 1
VSYNC_ON = 0
VSYNC_ADAPTIVE = 2
LEFT_EYE = 0
RIGHT_EYE = 1

# HDR
HDR_NONE = 0
HDR_HALF_FLOAT = 1
HDR_FULL_FLOAT = 2

# Mipmap
RAS_MIPMAP_NONE = 0
RAS_MIPMAP_NEAREST = 1
RAS_MIPMAP_LINEAR = 2

## Functions
def getWindowWidth():
	"""Gets the width of the window (in pixels)

	Return type:
	integer"""
	return 0
	
def getWindowHeight():
	"""Gets the height of the window (in pixels)

	Return type:
	integer"""
	return 0
	
def setWindowSize(width, height):
	"""Set the width and height of the window (in pixels). This also works for fullscreen applications.

	Note: Only works in the standalone player, not the Blender-embedded player.

	Parameters:
	width (integer) - width in pixels
	height (integer) - height in pixels"""
	pass
	
def setFullscreen(enable):
	"""Set whether or not the window should be fullscreen.

	Note: Only works in the standalone player, not the Blender-embedded player.

	Parameters:
	enable (bool) - True to set full screen, False to set windowed."""
	pass
	
def getFullscreen():
	"""Returns whether or not the window is fullscreen.

	Note: Only works in the standalone player, not the Blender-embedded player; there it always returns False.

	Return type:
	bool"""
	return False
	
def getDisplayDimensions():
	"""Get the display dimensions, in pixels, of the display (e.g., the monitor). Can return the size of the entire view, so the combination of all monitors; for example, (3840, 1080) for two side-by-side 1080p monitors.

	Return type:
	tuple (width, height)"""
	return (0,0)
	
def makeScreenshot(filename):
	"""Writes an image file with the current displayed frame.

	The image is written to ‘filename'. The path may be absolute (eg. /home/foo/image) or relative when started with // (eg. //image). Note that absolute paths are not portable between platforms. If the filename contains a #, it will be replaced by an incremental index so that screenshots can be taken multiple times without overwriting the previous ones (eg. image-#).

	Settings for the image are taken from the render settings (file format and respective settings, gamma and colospace conversion, etc). The image resolution matches the framebuffer, meaning, the window size and aspect ratio. When running from the standalone player, instead of the embedded player, only PNG files are supported. Additional color conversions are also not supported.

	Parameters:
	filename (string) - path and name of the file to write"""
	pass
	
def enableVisibility(visible):
	"""Deprecated; doesn't do anything."""
	pass
	
def showMouse(visible):
	"""Enables or disables the operating system mouse cursor.

	Parameters:
	visible (boolean)"""
	pass
	
def setMousePosition(x, y):
	"""Sets the mouse cursor position.

	Parameters:
	x (integer) - X-coordinate in screen pixel coordinates.
	y (integer) - Y-coordinate in screen pixel coordinates."""
	pass
	
def setBackgroundColor(rgba):
	"""Deprecated and no longer functional. Use bge.types.KX_WorldInfo.backgroundColor() instead."""
	pass
	
def setEyeSeparation(eyesep):
	"""Sets the eye separation for stereo mode. Usually Focal Length/30 provides a confortable value.

	Parameters:
	eyesep (float) - The distance between the left and right eye."""
	pass
	
def getEyeSeparation():
	"""Gets the current eye separation for stereo mode.

	Return type:
	float"""
	return True
	
def setFocalLength(focallength):
	"""Sets the focal length for stereo mode. It uses the current camera focal length as initial value.

	Parameters:
	focallength (float) - The focal length."""
	pass
	
def getFocalLength():
	"""Gets the current focal length for stereo mode.

	Return type:
	float"""
	return 0.0
	
def getStereoEye():
	"""Gets the current stereoscopy eye being rendered. This function is mainly used in a bge.types.KX_Scene.pre_draw callback function to customize the camera projection matrices for each stereoscopic eye.

	Return type:
	LEFT_EYE, RIGHT_EYE"""
	pass
	
def setMaterialMode(mode):
	"""Set the material mode to use for OpenGL rendering.

	Parameters:
	mode (KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL) - material mode

	Note: Changes will only affect newly created scenes."""
	pass
	
def getMaterialMode(mode):
	"""Get the material mode to use for OpenGL rendering.

	Return type:
	KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL"""
	pass
	
def setGLSLMaterialSetting(setting, enable):
	"""Enables or disables a GLSL material setting.

	Parameters:
	setting (string (lights, shaders, shadows, ramps, nodes, extra_textures))
	enable (boolean)"""
	pass
	
def getGLSLMaterialSetting(setting):
	"""Get the state of a GLSL material setting.

	Parameters:
	setting (string (lights, shaders, shadows, ramps, nodes, extra_textures)) -

	Return type:
	boolean"""
	return True
	
def setAnisotropicFiltering(level):
	"""Set the anisotropic filtering level for textures.

	Parameters:
	level (integer (must be one of 1, 2, 4, 8, 16)) - The new anisotropic filtering level to use

	Note: Changing this value can cause all textures to be recreated, which can be slow."""
	pass
	
def getAnisotropicFiltering():
	"""Get the anisotropic filtering level used for textures.

	Return type:
	integer (one of 1, 2, 4, 8, 16)"""
	return 16
	
def setMipmapping(value):
	"""Change how to use mipmapping.

	Note: Changing this value can cause all textures to be recreated, which can be slow."""
	pass
	
def getMipmapping():
	"""Get the current mipmapping setting.

	Return type:
	RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR"""
	pass
	
def drawLine(fromVec, toVec, color):
	"""Draw a line in the 3D scene.

	Parameters:
	fromVec (list [x, y, z]) - the origin of the line
	toVec (list [x, y, z]) - the end of the line
	color (list [r, g, b]) - the color of the line"""
	pass
	
def enableMotionBlur(factor):
	"""Enable the motion blur effect.

	Parameters:
	factor (float [0.0 - 1.0]) - the ammount of motion blur to display."""
	pass
	
def disableMotionBlur():
	"""Disable the motion blur effect."""
	pass
	
def showFramerate(enable):
	"""Show or hide the framerate.

	Parameters:
	enable (boolean)"""
	pass
	
def showProfile(enable):
	"""Show or hide the profile.

	Parameters:
	enable (boolean)"""
	pass
	
def showProperties(enable):
	"""Show or hide the debug properties.

	Parameters:
	enable (boolean)"""
	pass
	
def autoDebugList(enable):
	"""Enable or disable auto adding debug properties to the debug list.

	Parameters:
	enable (boolean)"""
	pass
	
def clearDebugList():
	"""Clears the debug property list."""
	pass
	
def setVsync(value):
	"""Set the vsync value

	Parameters:
	value (integer) - One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE"""
	pass
	
def getVsync():
	"""Get the current vsync value

	Return type:
	One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE"""
	pass

