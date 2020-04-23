"""The bge.texture module allows you to manipulate textures during the game.

Several sources for texture are possible: video files, image files, video capture, memory buffer, camera render or a mix of that.

The video and image files can be loaded from the internet using an URL instead of a file name.

In addition, you can apply filters on the images before sending them to the GPU, allowing video effect: blue screen, color band, gray, normal map."""

from .. import render

## Constants
# FFmpeg Video and Image Status
SOURCE_ERROR = -1
SOURCE_EMPTY = 0
SOURCE_READY = 1
SOURCE_PLAYING = 2
SOURCE_STOPPED = 3

# Image Blending Modes
IMB_BLEND_MIX = 0
IMB_BLEND_ADD = 1
IMB_BLEND_SUB = 2
IMB_BLEND_MUL = 3
IMB_BLEND_LIGHTEN = 4
IMB_BLEND_DARKEN = 5
IMB_BLEND_ERASE_ALPHA = 6
IMB_BLEND_ADD_ALPHA = 7
IMB_BLEND_OVERLAY = 8
IMB_BLEND_HARDLIGHT = 9
IMB_BLEND_COLORBURN = 10
IMB_BLEND_LINEARBURN = 11
IMB_BLEND_COLORDODGE = 12
IMB_BLEND_SCREEN = 13
IMB_BLEND_SOFTLIGHT = 14
IMB_BLEND_PINLIGHT = 15
IMB_BLEND_VIVIDLIGHT = 16
IMB_BLEND_LINEARLIGHT = 17
IMB_BLEND_DIFFERENCE = 18
IMB_BLEND_EXCLUSION = 19
IMB_BLEND_HUE = 20
IMB_BLEND_SATURATION = 21
IMB_BLEND_LUMINOSITY = 22
IMB_BLEND_COLOR = 23
IMB_BLEND_COPY = 1000
IMB_BLEND_COPY_RGB = 1001
IMB_BLEND_COPY_ALPHA = 1002

## Functions
def getLastError():
	"""Last error that occurred in a bge.texture function.

	Returns:	
	The description of the last error occurred in a bge.texture function.

	Return type:
	str"""
	return "str"
	
def imageToArray(image, mode):
	"""Returns a Buffer corresponding to the current image stored in a texture source object.

	Parameters:
	image - Image source object of type ...
	VideoFFmpeg
	ImageFFmpeg
	ImageBuff
	ImageMirror
	ImageMix
	ImageRender
	ImageViewport

	mode (str) - Optional argument representing the pixel format.
	You can use the characters R, G, B for the 3 color channels, A for the alpha channel, 0 to force a fixed 0 color channel and 1 to force a fixed 255 color channel.

	Examples:
	"BGR" will return 3 bytes per pixel with the Blue, Green and Red channels in that order.
	"RGB1" will return 4 bytes per pixel with the Red, Green, Blue channels in that order and the alpha channel forced to 255.

	A special mode "F" allows to return the image as an array of float. This mode should only be used to retrieve the depth buffer of the class:ImageViewport and ImageRender objects. The default mode is "RGBA".

	Returns:	
	An object representing the image as one dimensional array of bytes of size (pixel_size*width*height), line by line starting from the bottom of the image. The pixel size and format is determined by the mode parameter. For mode ‘F', the array is a one dimensional array of float of size (width*height).

	Return type:
	Buffer"""
	return None
	
def materialID(object, name):
	"""Returns a numeric value that can be used in Texture to create a dynamic texture.

	The value corresponds to an internal material number that uses the texture identified by name. name is a string representing a texture name with IM prefix if you want to identify the texture directly. This method works for basic tex face and for material, provided the material has a texture channel using that particular texture in first position of the texture stack. name can also have MA prefix if you want to identify the texture by material. In that case the material must have a texture channel in first position.

	If the object has no material that matches name, it generates a runtime error. Use try/except to catch the exception.

	Ex: bge.texture.materialID(obj, 'IMvideo.png')

	Parameters:
	object (KX_GameObject) - The game object that uses the texture you want to make dynamic.
	name (str) - Name of the texture/material you want to make dynamic.

	Returns:	
	The internal material number.

	Return type:
	int"""
	return 0
	
def setLogFile(filename):
	"""Sets the name of a text file in which runtime error messages will be written, in addition to the printing of the messages on the Python console. Only the runtime errors specific to the VideoTexture module are written in that file, ordinary runtime time errors are not written.

	Parameters:
	filename (str) - Name of the error log file.

	Returns:	-1 if the parameter name is invalid (not of type string), else 0.

	Return type:
	int"""
	return 0

## Filter Classes
class FilterBGR24:
	"""Source filter BGR24."""
	pass

class FilterBlueScreen:
	"""Filter for Blue Screen. The RGB channels of the color are left unchanged, while the output alpha is obtained as follows:
	
	if the square of the euclidian distance between the RGB color and the filter's reference color is smaller than the filter's lower limit, the output alpha is set to 0;
	if that square is bigger than the filter's upper limit, the output alpha is set to 255;
	otherwise the output alpha is linarly extrapoled between 0 and 255 in the interval of the limits."""
	
	def __init__(self):
		self.color = (0,0,255)
		self.limits = (64,64)
		self.previous = None

class FilterColor:
	"""Filter for color calculations. The output color is obtained by multiplying the reduced 4x4 matrix with the input color and adding the remaining column to the result."""
	
	def __init__(self):
		self.matrix = ((256, 0, 0, 0, 0), (0, 256, 0, 0, 0), (0, 0, 256, 0, 0), (0, 0, 0, 256, 0))
		self.previous = None

class FilterGray:
	"""Filter for gray scale effect. Proportions of R, G and B contributions in the output gray scale are 28:151:77."""
	
	def __init__(self):
		self.previous = None

class FilterLevel:
	"""Filter for levels calculations. Each output color component is obtained as follows:

	- if it is smaller than its corresponding min value, it is set to 0;
	- if it is bigger than its corresponding max value, it is set to 255;
	- Otherwise it is linearly extrapoled between 0 and 255 in the (min, max) interval."""
	
	def __init__(self):
		self.levels = ((0, 255), (0, 255), (0, 255), (0, 255))
		self.previous = None

class FilterNormal:
	"""Normal map filter."""
	
	def __init__(self):
		self.colorIdx = 0
		self.depth = 4.0
		self.previous = None

class FilterRGB24:
	"""Returns a new input filter object to be used with ImageBuff object when the image passed to the ImageBuff.load() function has the 3-bytes pixel format BGR."""
	pass

class FilterRGB32:
	"""Source filter RGBA32."""
	pass

## Video Classes
class VideoFFmpeg:
	"""FFmpeg video source.

	Parameters:	
	file (str) - Path to the video to load; if capture >= 0 on Windows, this parameter will not be used.
	capture (int) - Capture device number; if >= 0, the corresponding webcam will be used. (optional)
	rate (float) - Capture rate. (optional, used only if capture >= 0)
	width (int) - Capture width. (optional, used only if capture >= 0)
	height (int) - Capture height. (optional, used only if capture >= 0)"""
	
	def __init__(self, file, capture=-1, rate=25.0, width=0, height=0):
		self.status = 0
		self.range = (0.0,0.0)
		self.repeat = 0
		self.framerate = 0.0
		self.valid = True
		self.image = None
		self.size = (0,0)
		self.scale = True
		self.flip = True
		self.filter = None
		self.preseek = 0
		self.deinterlace = True
	
	# Functions
	def play():
		"""Play (restart) video.

		Returns:
		Whether the video was ready or stopped.

		Return type:
		bool"""
		return True
		
	def pause():
		"""Pause video.

		Returns:
		Whether the video was playing.

		Return type:
		bool"""
		return True
		
	def stop():
		"""Stop video (play will replay it from start).

		Returns:	
		Whether the video was playing.

		Return type:
		bool"""
		return True
		
	def refresh(buffer=None, format="RGBA", timestamp=-1.0):
		"""Refresh video - get its status.

		Value:
		see FFmpeg Video and Image Status.

		Return type:
		int"""
		return 0

class VideoDeckLink:
	"""Image source from an external video stream captured with a DeckLink video card from Black Magic Design. Before this source can be used, a DeckLink hardware device must be installed, it can be a PCIe card or a USB device, and the ‘Desktop Video’ software package (version 10.4 or above must be installed) on the host as described in the DeckLink documentation. If in addition you have a recent nVideo Quadro card, you can benefit from the ‘GPUDirect’ technology to push the captured video frame very efficiently to the GPU. For this you need to install the ‘DeckLink SDK’ version 10.4 or above and copy the ‘dvp.dll’ runtime library to Blender’s installation directory or to any other place where Blender can load a DLL from.
	
	Parameters:
	format (str) – string describing the video format to be captured.
	capture (int) – Card number from which the input video must be captured."""
	
	def __init__(self, format, capture=0):
		self.status = 0
		self.framerate = 0.0
		self.valid = False
		self.image = None
		self.size = (0,0)
		self.scale = False
		self.flip = False
		self.filter = None
		
	def play():
		"""Kick-off the capture after creation of the object.
		
		Returns:
		True if the capture could be started, False otherwise.
		
		Return type:
		bool"""
		return True
		
	def pause():
		"""Temporary stops the capture. Use play() to restart it.
		
		Returns:
		True if the capture could be paused, False otherwise.
		
		Return type:
		bool"""
		return True
		
	def pause():
		"""Stops the capture.
		
		Returns:
		True if the capture could be stopped, False otherwise.
		
		Return type:
		bool"""
		return True

## Image Classes
class ImageFFmpeg:
	"""FFmpeg image source.

	Parameters:
	file (str) - Path to the image to load."""
	
	def __init__(self, file):
		self.status = 0
		self.valid = True
		self.image = None
		self.size = (0,0)
		self.scale = True
		self.flip = True
		self.filter = None
		
	def refresh():
		"""Refresh image, i.e. load it.

		Value:
		see FFmpeg Video and Image Status.

		Return type:
		int"""
		return 0
		
	def reload():
		"""Reload image, i.e. reopen it.

		Parameters:
		newname (str) - Path to a new image. (optional)"""
		pass

	pass

class ImageBuff:
	"""Image source from image buffer.

	Parameters:
	width (int) - Width of the image.
	height (int) - Height of the image.
	color (int in [0, 255]) - Value to initialize RGB channels with. The initialized buffer will have all pixels set to (color, color, color, 255). (optional)
	scale (bool) - Image uses scaling. (optional)"""

	def __init__(self, width, height, color=0, scale=False):
		self.filter = None
		self.flip = True
		self.image = None
		self.scale = True
		self.size = (0,0)
		self.valid = True
	
	def load(imageBuffer, width, height):
		"""Load image from buffer.

		Parameters:
		imageBuffer (Buffer or Python object implementing the buffer protocol (f.ex. bytes)) - Buffer to load the image from.
		width (int) - Width of the image to load.
		height (int) - Height of the image to load."""
		pass
		
	def plot(imageBuffer, width, height, positionX, positionY, mode=IMB_BLEND_COPY):
		"""Update image buffer.

		Parameters:
		imageBuffer (Buffer, ImageBuff or Python object implementing the buffer protocol (f.ex. bytes)) - Buffer to load the new data from.
		width (int) - Width of the data to load.
		height (int) - Height of the data to load.
		positionX (int) - Left boundary of the region to be drawn on.
		positionY (int) - Upper boundary of the region to be drawn on.
		mode (int) - Drawing mode, see Image Blending Modes."""
		pass

	pass

class ImageMirror:
	"""Image source from mirror.

	Parameters:
	scene (KX_Scene) - Scene in which the image has to be taken.
	observer (KX_GameObject) - Reference object for the mirror (the object from which the mirror has to be looked at, for example a camera).
	mirror (KX_GameObject) - Object holding the mirror.
	material (int) - ID of the mirror's material to be used for mirroring. (optional)"""
	
	def __init__(self, scene, observer, mirror, material=0, width=0, height=0, samples=0, hdr=render.HDR_NONE):
		self.alpha = True
		self.background = [0,0,0,0]
		self.capsize = (0,0)
		self.clip = 0.0
		self.filter = None
		self.flip = True
		self.image = None
		self.scale = True
		self.size = (0,0)
		self.valid = True
		self.whole = True
		
	def refresh(buffer=None, format="RGBA"):
		"""Refresh image - invalidate its current content."""
		pass

	pass

class ImageMix:
	"""Image mixer."""
	
	def __init__(self):
		self.filter = None
		self.flip = True
		self.image = None
		self.scale = True
		self.size = (0,0)
		self.valid = True
		
	def getSource(id):
		"""Get image source.

		Parameters:
		id (str) - Identifier of the source to get.

		Returns:	
		Image source.

		Return type:
		one of...
		VideoFFmpeg
		ImageFFmpeg
		ImageBuff
		ImageMirror
		ImageMix
		ImageRender
		ImageViewport"""
		pass
		
	def getWeight(id):
		"""Get image source weight.

		Parameters:
		id (str) - Identifier of the source.

		Returns:	
		Weight of the source.

		Return type:
		int"""
		return 0
		
	def refresh(buffer=None, format="RGBA"):
		"""Refresh image - invalidate its current content."""
		pass
		
	def setSource(id, image):
		"""Set image source - all sources must have the same size.

		Parameters:
		id (str) - Identifier of the source to set.
		image -
		Image source of type...
		VideoFFmpeg
		ImageFFmpeg
		ImageBuff
		ImageMirror
		ImageMix
		ImageRender
		ImageViewport"""
		pass
		
	def setWeight(id, weight):
		"""Set image source weight - the sum of the weights should be 256 to get full color intensity in the output.

		Parameters:
		id (str) - Identifier of the source.
		weight (int) - Weight of the source."""
		pass

	pass

class ImageRender:
	"""Image source from render.

	Parameters:
	scene (KX_Scene) - Scene in which the image has to be taken.
	camera (KX_Camera) - Camera from which the image has to be taken."""
	
	def __init__(self, scene, camera, width, height, samples, hdr):
		self.alpha = True
		self.horizon = [0,0,0,0]
		self.zenith = [0,0,0,0]
		self.background = [0,0,0,0]
		self.updateShadow = True
		self.colorBindCode = 0
		self.capsize = (0,0)
		self.filter = None
		self.flip = True
		self.image = None
		self.scale = True
		self.size = (0,0)
		self.valid = True
		self.whole = True
		self.depth = True
		self.zbuff = True
		
	def render():
		"""Render the scene but do not extract the pixels yet. The function returns as soon as the render commands have been send to the GPU. The render will proceed asynchronously in the GPU while the host can perform other tasks. To complete the render, you can either call refresh() directly of refresh the texture of which this object is the source. This method is useful to implement asynchronous render for optimal performance: call render() on frame n and refresh() on frame n+1 to give as much as time as possible to the GPU to render the frame while the game engine can perform other tasks.

		Returns:
		True if the render was initiated, False if the render cannot be performed (e.g. the camera is active)
		
		Return type:
		bool"""
		return True
		
	def refresh(buffer, format="RGBA"):
		"""Refresh video - render and optionally copy the image to an external buffer then invalidate its current content. The render may have been started earlier with the render() method, in which case this function simply waits for the render operations to complete. When called without argument, the pixels are not extracted but the render is guaranteed to be completed when the function returns. This only makes sense with offscreen render on texture target (see bge.render.offScreenCreate()).
		
		Parameters:
		buffer (any buffer type of sufficient size) – An object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown. The transfer to the buffer is optimal if no processing of the image is needed. This is the case if flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False and no filter is set.
		format (str) – An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
		
		Returns:
		True if the render is complete, False if the render cannot be performed (e.g. the camera is active)
		
		Return type:
		bool"""
		return True

	pass

class ImageViewport:
	
	def __init__(self):
		self.alpha = True
		self.capsize = (0,0)
		self.filter = None
		self.flip = True
		self.image = None
		self.position = (0,0)
		self.scale = True
		self.size = (0,0)
		self.valid = True
		self.whole = True
		self.depth = True
		self.zbuff = True
		
	def refresh(buffer=None, format="RGBA"):
		"""Refresh video - copy the viewport to an external buffer (optional) then invalidate its current content.
		
		Parameters:
		buffer (any buffer type) – An optional object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown. The transfer to the buffer is optimal if no processing of the image is needed. This is the case if flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False and no filter is set.
		format (str) – An optional image format specifier for the image that will be copied to the buffer. Only valid values are “RGBA” or "BGRA" """
		pass

	pass

## Texture Classes
class Texture:
	"""Texture object.

	Parameters:	
	gameObj (KX_GameObject) – Game object to be created a video texture on.
	materialID (int) – Material ID default, 0 is the first material. (optional)
	textureID (int) – Texture index in case of multi-texture channel, 0 = first channel by default. In case of UV texture, this parameter should always be 0. (optional)
	textureObj (Texture) – Reference to another Texture object with shared bindId which he user might want to reuse the texture. If this argument is used, you should not create any source on this texture and there is no need to refresh it either: the other Texture object will provide the texture for both materials/textures.(optional)"""
	
	def __init__(self, gameObj, materialID=0, textureID=0, textureObj=None):
		self.bindId = 0
		self.mipmap = True
		self.source = None
	
	def close():
		"""Close dynamic texture and restore original."""
		pass
		
	def refresh(refresh_source, timestamp=-1.0):
		"""Refresh texture from source.

		Parameters:
		refresh_source (bool) - Whether to also refresh the image source of the texture.
		ts (float) - If the texture controls a VideoFFmpeg object: timestamp (in seconds from the start of the movie) of the frame to be loaded; this can be used for video-sound synchonization by passing time to it. (optional)"""
		pass

	pass


class DeckLink:
	"""Certain DeckLink devices can be used to playback video: the host sends video frames regularly for immediate or scheduled playback. The video feed is outputted on HDMI or SDI interfaces. This class supports the immediate playback mode: it has a source attribute that is assigned one of the source object in the bge.texture module. Refreshing the DeckLink object causes the image source to be computed and sent to the DeckLink device for immediate transmission on the output interfaces. Keying is supported: it allows to composite the frame with an input video feed that transits through the DeckLink card.

	Parameters:
	cardIdx (int) – Number of the card to be used for output (0=first card). It should be noted that DeckLink devices are usually half duplex: they can either be used for capture or playback but not both at the same time.
	format (str) – String representing the display mode of the output feed."""
	
	def __init__(self, cardIdx=0, format=""):
		source = None
		right = None
		keying = False
		level = 0
		extend = False
		
	def close():
		"""Close the DeckLink device and release all resources. After calling this method, the object cannot be reactivated, it must be destroyed and a new DeckLink object created from fresh to restart the output."""
		pass
		
	def refresh(refresh_source, ts):
		"""This method must be called frequently to update the output frame in the DeckLink device.

		Parameters:
		refresh_source (bool) – True if the source objects image buffer should be invalidated after being used to compute the output frame. This triggers the recomputing of the source image on next refresh, which is normally the desired effect. False if the image source buffer should stay valid and reused on next refresh. Note that the DeckLink device stores the output frame and replays until a new frame is sent from the host. Thus, it is not necessary to refresh the DeckLink object if it is known that the image source has not changed.
		ts (float) – The timestamp value passed to the image source object to compute the image. If unspecified, the BGE clock is used."""
		pass
