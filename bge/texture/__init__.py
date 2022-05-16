"""The bge.texture module allows you to manipulate textures during the game.

Several sources for texture are possible: video files, image files, video capture, memory buffer, camera render or a mix of that.

The video and image files can be loaded from the internet using an URL instead of a file name.

In addition, you can apply filters on the images before sending them to the GPU, allowing video effect: blue screen, color band, gray, normal map."""

from .. import render as _render
from .. import types as _types
from ... import bgl as _bgl


# Constants
# FFmpeg Video and Image Status
SOURCE_ERROR = -1  # type: int
"""See FFmpeg Video and Image classes status attributes."""

SOURCE_EMPTY = 0  # type: int
"""See FFmpeg Video and Image classes status attributes."""

SOURCE_READY = 1  # type: int
"""See FFmpeg Video and Image classes status attributes."""

SOURCE_PLAYING = 2  # type: int
"""See FFmpeg Video and Image classes status attributes."""

SOURCE_STOPPED = 3  # type: int
"""See FFmpeg Video and Image classes status attributes."""


# Image Blending Modes
IMB_BLEND_MIX = 0  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_ADD = 1  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_SUB = 2  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_MUL = 3  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_LIGHTEN = 4  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_DARKEN = 5  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_ERASE_ALPHA = 6  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_ADD_ALPHA = 7  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_OVERLAY = 8  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_HARDLIGHT = 9  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_COLORBURN = 10  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_LINEARBURN = 11  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_COLORDODGE = 12  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_SCREEN = 13  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_SOFTLIGHT = 14  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_PINLIGHT = 15  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_VIVIDLIGHT = 16  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_LINEARLIGHT = 17  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_DIFFERENCE = 18  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_EXCLUSION = 19  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_HUE = 20  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_SATURATION = 21  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_LUMINOSITY = 22  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_COLOR = 23  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_COPY = 1000  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_COPY_RGB = 1001  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""

IMB_BLEND_COPY_ALPHA = 1002  # type: int
"""See Wikipedia's Blend Modes for reference: https://en.wikipedia.org/wiki/Blend_modes"""


# Video Classes
class VideoFFmpeg:

    def __init__(self, file, capture=-1, rate=25.0, width=0, height=0):
        # type: (str, int, float, int, int) -> None
        """FFmpeg video source.

        Args:
            file (str): Path to the video to load; if capture >= 0 on Windows, this parameter will not be used.
            capture (int): Capture device number; if >= 0, the corresponding webcam will be used. (optional)
            rate (float): Capture rate. (optional, used only if capture >= 0)
            width (int): Capture width. (optional, used only if capture >= 0)
            height (int): Capture height. (optional, used only if capture >= 0)"""

        self.status = 0  # type: int
        """Video status. (readonly)"""

        self.range = (0.0, 0.0)  # type: tuple[float, float]
        """Replay range."""

        self.repeat = 0  # type: int
        """Repeat count, -1 for infinite repeat."""

        self.framerate = 0.0  # type: float
        """Frame rate."""

        self.valid = True  # type: bool
        """Tells if an image is available. (readonly)"""

        self.image = None  # type: _bgl.Buffer
        """Image data. (readonly)"""

        self.size = (0, 0)  # type: tuple[int, int]
        """Image size. (readonly)"""

        self.scale = True  # type: bool
        """Fast scale of image (near neighbour)."""

        self.flip = True  # type: bool
        """Flip image vertically."""

        self.filter = None  # type: FilterBGR24 | FilterBlueScreen | FilterColor | FilterGray | FilterLevel | FilterNormal | FilterRGB24 | FilterRGBA32
        """Pixel filter."""

        self.preseek = 0  # type: int
        """Number of frames of preseek."""

        self.deinterlace = True  # type: bool
        """Deinterlace image."""

    # Functions
    def play(self):
        # type: () -> bool
        """Play (restart) video.

        Returns:
            bool: Whether the video was ready or stopped."""

        pass

    def pause(self):
        # type: () -> bool
        """Pause video.

        Returns:
            bool: Whether the video was playing."""

        pass

    def stop(self):
        # type: () -> bool
        """Stop video (play will replay it from start).

        Returns:
            bool: Whether the video was playing."""

        pass

    def refresh(self, buffer=None, format="RGBA", timestamp=-1.0):
        # type: (_bgl.Buffer, str, float) -> bool
        """Refresh video - get its status.

        Args:
            buffer (any buffer type): An optional object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown.
            format (str): An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
            timestamp (float): An optional timestamp (in seconds from the start of the movie) of the frame to be copied to the buffer.

        Returns:
            int: see FFmpeg Video and Image Status."""

        pass


class VideoDeckLink:

    def __init__(self, format, capture=0):
        # type: (str, int) -> None
        """Image source from an external video stream captured with a DeckLink video card from Black Magic Design. Before this source can be used, a DeckLink hardware device must be installed, it can be a PCIe card or a USB device, and the 'Desktop Video' software package (version 10.4 or above must be installed) on the host as described in the DeckLink documentation. If in addition you have a recent nVideo Quadro card, you can benefit from the 'GPUDirect' technology to push the captured video frame very efficiently to the GPU. For this you need to install the 'DeckLink SDK' version 10.4 or above and copy the 'dvp.dll' runtime library to Blender's installation directory or to any other place where Blender can load a DLL from.

        Args:
            format (str): string describing the video format to be captured.
            capture (int): Card number from which the input video must be captured."""

        self.status = 0  # type: int
        """Status of the capture: 1=ready to use, 2=capturing, 3=stopped"""

        self.framerate = 0.0  # type: float
        """Capture frame rate as computed from the video format."""

        self.valid = False  # type: bool
        """Tells if the image attribute can be used to retrieve the image. Always False in this implementation (the image is not available at python level)."""

        self.image = None  # type: None
        """The image data. Always None in this implementation."""

        self.size = (0, 0)  # type: tuple[int, int]
        """The size of the frame in pixel. Stereo frames have double the height of the video frame, i.e. 3D is delivered to the GPU as a single image in top-bottom order, left eye on top."""

        self.scale = None  # type: None
        """Not used in this object."""

        self.flip = None  # type: None
        """Not used in this object."""

        self.filter = None  # type: None
        """Not used in this object."""

    def play(self):
        # type: () -> bool
        """Kick-off the capture after creation of the object.

        Returns:
            bool: True if the capture could be started, False otherwise."""

        pass

    def pause(self):
        # type: () -> bool
        """Temporary stops the capture. Use play() to restart it.

        Returns:
            bool: True if the capture could be paused, False otherwise."""

        pass

    def pause(self):
        # type: () -> bool
        """Stops the capture.

        Returns:
            bool: True if the capture could be stopped, False otherwise."""

        pass


# Image Classes
class ImageFFmpeg:

    def __init__(self, file):
        """FFmpeg image source.

        Args:
            file (str): Path to the image to load."""

        self.status = 0  # type: int
        """Image status. (readonly)"""

        self.valid = True  # type: bool
        """Tells if an image is available. (readonly)"""

        self.image = None  # type: _bgl.Buffer
        """Image data. (readonly)"""

        self.size = (0, 0)  # type: tuple[int, int]
        """Image size. (readonly)"""

        self.scale = True  # type: bool
        """Fast scale of image (near neighbour)."""

        self.flip = True  # type: bool
        """Flip image vertically."""

        self.filter = None  # type: FilterBGR24 | FilterBlueScreen | FilterColor | FilterGray | FilterLevel | FilterNormal | FilterRGB24 | FilterRGBA32
        """Pixel filter."""

    def refresh(self, buffer=None, format="RGBA"):
        # type: (_bgl.Buffer, str) -> bool
        """Refresh image, get its status and optionally copy the frame to an external buffer.

        Args:
            buffer (any buffer type): An optional object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown.
            format (str): An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"

        Value:
            int: see FFmpeg Video and Image Status."""

        pass

    def reload(self, newname=None):
        # type: (str) -> None
        """Reload image, i.e. reopen it.

        Args:
            newname (str): Path to a new image. (optional)"""

        pass


class ImageBuff:

    def __init__(self, width, height, color=0, scale=False):
        # type: (int, int, int, bool) -> None
        """Image source from image buffer.

        Args:
            width (int): Width of the image.
            height (int): Height of the image.
            color (int in [0, 255]): Value to initialize RGB channels with. The initialized buffer will have all pixels set to (color, color, color, 255). (optional)
            scale (bool): Image uses scaling. (optional)"""

        self.filter = None  # type: FilterBGR24 | FilterBlueScreen | FilterColor | FilterGray | FilterLevel | FilterNormal | FilterRGB24 | FilterRGBA32
        """Pixel filter."""

        self.flip = True  # type: bool
        """Flip image vertically."""

        self.image = None  # type: _bgl.Buffer
        """Image data. (readonly)"""

        self.scale = True  # type: bool
        """Fast scale of image (near neighbour)."""

        self.size = (0, 0)  # type: tuple[int, int]
        """Image size. (readonly)"""

        self.valid = True  # type: bool
        """Tells if an image is available. (readonly)"""

    def load(self, imageBuffer, width, height):
        # type: (_bgl.Buffer, int, int) -> None
        """Load image from buffer.

        Args:
            imageBuffer (Buffer or Python object implementing the buffer protocol (f.ex. bytes)): Buffer to load the image from.
            width (int): Width of the image to load.
            height (int): Height of the image to load."""

        pass

    def plot(self, imageBuffer, width, height, positionX, positionY, mode=IMB_BLEND_COPY):
        # type: (_bgl.Buffer, int, int, int, int, int) -> None
        """Update image buffer.

        Args:
            imageBuffer (Buffer, ImageBuff or Python object implementing the buffer protocol (f.ex. bytes)): Buffer to load the new data from.
            width (int): Width of the data to load.
            height (int): Height of the data to load.
            positionX (int): Left boundary of the region to be drawn on.
            positionY (int): Upper boundary of the region to be drawn on.
            mode (int): Drawing mode, see Image Blending Modes."""

        pass


class ImageMirror:

    def __init__(self, scene, observer, mirror, material=0, width=0, height=0, samples=0, hdr=_render.HDR_NONE):
    # type: (_types.KX_Scene, _types.KX_GameObject, _types.KX_GameObject, int, int, int, int, int) -> None
        """Image source from mirror.

        Args:
            scene (KX_Scene): Scene in which the image has to be taken.
            observer (KX_GameObject): Reference object for the mirror (the object from which the mirror has to be looked at, for example a camera).
            mirror (KX_GameObject): Object holding the mirror.
            material (int): ID of the mirror's material to be used for mirroring. (optional)"""

        self.alpha = True  # type: bool
        """Use alpha in texture."""

        self.background = [0, 0, 0, 0]  # type: list[int]
        """Background color."""

        self.capsize = (0, 0)  # type: tuple[int, int]
        """Size of render area."""

        self.clip = 0.0  # type: float
        """Clipping distance."""

        self.filter = None  # type: FilterBGR24 | FilterBlueScreen | FilterColor | FilterGray | FilterLevel | FilterNormal | FilterRGB24 | FilterRGBA32
        """Pixel filter."""

        self.flip = True  # type: bool
        """Flip image vertically."""

        self.image = None  # type: _bgl.Buffer
        """Image data. (readonly)"""

        self.scale = True  # type: bool
        """Fast scale of image (near neighbour)."""

        self.size = (0, 0)  # type: tuple[int, int]
        """Image size. (readonly)"""

        self.valid = True  # type: bool
        """Tells if an image is available. (readonly)"""

        self.whole = True  # type: bool
        """Use whole viewport to render."""

    def refresh(self, buffer=None, format="RGBA"):
        # type: (_bgl.Buffer, str) -> bool
        """Refresh image - render and copy the image to an external buffer (optional) then invalidate its current content.

        Args:
            buffer (any buffer type): An optional object that implements the buffer protocol. If specified, the image is rendered and copied to the buffer, which must be big enough or an exception is thrown.
            format (str): An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA" """

        pass


class ImageMix:

    def __init__(self):
        # type: () -> None
        """Image mixer."""

        self.filter = None  # type: FilterBGR24 | FilterBlueScreen | FilterColor | FilterGray | FilterLevel | FilterNormal | FilterRGB24 | FilterRGBA32
        """Pixel filter."""

        self.flip = True  # type: bool
        """Flip image vertically."""

        self.image = None  # type: _bgl.Buffer
        """Image data. (readonly)"""

        self.scale = True  # type: bool
        """Fast scale of image (near neighbour)."""

        self.size = (0, 0)  # type: tuple[int, int]
        """Image size. (readonly)"""

        self.valid = True  # type: bool
        """Tells if an image is available. (readonly)"""

    def getSource(self, id):
        # type: (str) -> VideoFFmpeg | ImageFFmpeg | ImageBuff | ImageMirror | ImageMix | ImageRender | ImageViewport
        """Get image source.

        Args:
            id (str): Identifier of the source to get.

        Returns:
            Image source."""

        pass

    def getWeight(self, id):
        # type: (str) -> int
        """Get image source weight.

        Args:
            id (str): Identifier of the source.

        Returns:
            int: Weight of the source."""

        pass

    def refresh(self, buffer=None, format="RGBA"):
        # type: (_bgl.Buffer, str) -> None
        """Refresh image - calculate and copy the image to an external buffer (optional) then invalidate its current content.

        Args:
            buffer (any buffer type): An optional object that implements the buffer protocol. If specified, the image is calculated and copied to the buffer, which must be big enough or an exception is thrown.
            format (str): An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA" """

        pass

    def setSource(self, id, image):
        # type: (str, VideoFFmpeg | ImageFFmpeg | ImageBuff | ImageMirror | ImageMix | ImageRender | ImageViewport) -> None
        """Set image source - all sources must have the same size.

        Args:
            id (str): Identifier of the source to set.
            image: Image source."""

        pass

    def setWeight(self, id, weight):
        # type: (str, int) -> None
        """Set image source weight - the sum of the weights should be 256 to get full color intensity in the output.

        Args:
            id (str): Identifier of the source.
            weight (int): Weight of the source."""

        pass


class ImageRender:

    def __init__(self, scene, camera, width=None, height=None, samples=None, hdr=None):
    # type: (_types.KX_Scene, _types.KX_Camera, int, int, int, int) -> None
        """Image source from render.

        Args:
            scene (KX_Scene): Scene in which the image has to be taken.
            camera (KX_Camera): Camera from which the image has to be taken.
            width (integer): Off-screen render buffer width (optional).
            height (integer): Off-screen render buffer height (optional).
            samples (integer): Off-screen render buffer samples (optional).
            hdr (One of these constants): Off-screen image format (optional)."""

        self.alpha = True  # type: bool
        """Use alpha in texture."""

        self.horizon = [0, 0, 0, 0]  # type: list[int]
        """Horizon color."""

        self.zenith = [0, 0, 0, 0]  # type: list[int]
        """Zenith color."""

        self.background = [0, 0, 0, 0]  # type: list[int]
        """Background color."""

        self.updateShadow = True  # type: bool
        """Choose to force shadow buffer update if there is a gap beetween image rendered and shadows."""

        self.colorBindCode = 0  # type: int
        """Off-screen color texture bind code."""

        self.capsize = (0, 0)  # type: tuple[int, int]
        """Size of render area."""

        self.filter = None  # type: FilterBGR24 | FilterBlueScreen | FilterColor | FilterGray | FilterLevel | FilterNormal | FilterRGB24 | FilterRGBA32
        """Pixel filter."""

        self.flip = True  # type: bool
        """Flip image vertically."""

        self.image = None  # type: _bgl.Buffer
        """Image data. (readonly)"""

        self.scale = True  # type: bool
        """Fast scale of image (near neighbour)."""

        self.size = (0, 0)  # type: tuple[int, int]
        """Image size. (readonly)"""

        self.valid = True  # type: bool
        """Tells if an image is available. (readonly)"""

        self.whole = True  # type: bool
        """Use whole viewport to render."""

        self.depth = True  # type: bool
        """Use depth component of render as array of float - not suitable for texture source, should only be used with bge.texture.imageToArray(mode='F')."""

        self.zbuff = True  # type: bool
        """Use depth component of render as grayscale color - suitable for texture source."""

    def render(self):
        # type: () -> bool
        """Render the scene but do not extract the pixels yet. The function returns as soon as the render commands have been send to the GPU. The render will proceed asynchronously in the GPU while the host can perform other tasks. To complete the render, you can either call refresh() directly of refresh the texture of which this object is the source. This method is useful to implement asynchronous render for optimal performance: call render() on frame n and refresh() on frame n+1 to give as much as time as possible to the GPU to render the frame while the game engine can perform other tasks.

        Returns:
            bool: True if the render was initiated, False if the render cannot be performed (e.g. the camera is active)"""

        pass

    def refresh(self, buffer, format="RGBA"):
        # type: (_bgl.Buffer, str) -> bool
        """Refresh video - render and optionally copy the image to an external buffer then invalidate its current content. The render may have been started earlier with the render() method, in which case this function simply waits for the render operations to complete. When called without argument, the pixels are not extracted but the render is guaranteed to be completed when the function returns. This only makes sense with offscreen render on texture target (see bge.render.offScreenCreate()).

        Args:
            buffer (any buffer type of sufficient size): An object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown. The transfer to the buffer is optimal if no processing of the image is needed. This is the case if flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False and no filter is set.
            format (str): An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"

        Returns:
            bool: True if the render is complete, False if the render cannot be performed (e.g. the camera is active)"""

        pass


class ImageViewport:

    def __init__(self):
        """Image source from viewport."""

        self.alpha = True  # type: bool
        """Use alpha in texture."""

        self.capsize = (0, 0)  # type: tuple[int, int]
        """Size of viewport area being captured."""

        self.filter = None  # type: FilterBGR24 | FilterBlueScreen | FilterColor | FilterGray | FilterLevel | FilterNormal | FilterRGB24 | FilterRGBA32
        """Pixel filter."""

        self.flip = True  # type: bool
        """Flip image vertically."""

        self.image = None  # type: _bgl.Buffer
        """Image data. (readonly)"""

        self.position = (0, 0)  # type: tuple[int, int]
        """Upper left corner of the captured area."""

        self.scale = True  # type: bool
        """Fast scale of image (near neighbour)."""

        self.size = (0, 0)  # type: tuple[int, int]
        """Image size. (readonly)"""

        self.valid = True  # type: bool
        """Tells if an image is available. (readonly)"""

        self.whole = True  # type: bool
        """Use whole viewport to capture."""

        self.depth = True  # type: bool
        """Use depth component of viewport as array of float - not suitable for texture source, should only be used with bge.texture.imageToArray(mode='F')."""

        self.zbuff = True  # type: bool
        """Use depth component of viewport as grayscale color - suitable for texture source."""

    def refresh(self, buffer=None, format="RGBA"):
        # type: (_bgl.Buffer, str) -> None
        """Refresh video - copy the viewport to an external buffer (optional) then invalidate its current content.

        Args:
            buffer (any buffer type): An optional object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown. The transfer to the buffer is optimal if no processing of the image is needed. This is the case if flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False and no filter is set.
            format (str): An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA" """

        pass


# Texture Classes
class Texture:

    def __init__(self, gameObj, materialID=0, textureID=0, textureObj=None):
        # type: (_types.KX_GameObject, int, int, Texture) -> None
        """Texture object.

        Args:
            gameObj (KX_GameObject): Game object to be created a video texture on.
            materialID (int): Material ID default, 0 is the first material. (optional)
            textureID (int): Texture index in case of multi-texture channel, 0 = first channel by default. In case of UV texture, this parameter should always be 0. (optional)
            textureObj (Texture): Reference to another Texture object with shared bindId which he user might want to reuse the texture. If this argument is used, you should not create any source on this texture and there is no need to refresh it either: the other Texture object will provide the texture for both materials/textures.(optional)"""

        self.bindId = 0  # type: int
        """OpenGL Bind Name. (readonly)"""

        self.mipmap = True  # type: bool
        """Mipmap texture."""

        self.source = None  # type: VideoFFmpeg | ImageFFmpeg | ImageBuff | ImageMirror | ImageMix | ImageRender | ImageViewport
        """Source of texture."""

    def close(self):
        # type: () -> None
        """Close dynamic texture and restore original."""

        pass

    def refresh(self, refresh_source, timestamp=-1.0):
        # type: (bool, float) -> None
        """Refresh texture from source.

        Args:
            refresh_source (bool): Whether to also refresh the image source of the texture.
            timestamp (float): If the texture controls a VideoFFmpeg object, the timestamp (in seconds from the start of the movie) of the frame to be loaded; this can be used for video-sound synchonization by passing time to it. (optional)"""

        pass


class DeckLink:

    def __init__(self, cardIdx=0, format=""):
        # type: (int, str) -> None
        """Certain DeckLink devices can be used to playback video: the host sends video frames regularly for immediate or scheduled playback. The video feed is outputted on HDMI or SDI interfaces. This class supports the immediate playback mode: it has a source attribute that is assigned one of the source object in the bge.texture module. Refreshing the DeckLink object causes the image source to be computed and sent to the DeckLink device for immediate transmission on the output interfaces. Keying is supported: it allows to composite the frame with an input video feed that transits through the DeckLink card.

        Args:
            cardIdx (int): Number of the card to be used for output (0=first card). It should be noted that DeckLink devices are usually half duplex: they can either be used for capture or playback but not both at the same time.
            format (str): String representing the display mode of the output feed."""

        source = None  # type: VideoFFmpeg | ImageFFmpeg | ImageBuff | ImageMirror | ImageMix | ImageRender | ImageViewport
        """This attribute must be set to one of the image source. If the image size does not fit exactly the frame size, the extend attribute determines what to do.

        For best performance, the source image should match exactly the size of the output frame. A further optimization is achieved if the image source object is ImageViewport or ImageRender set for whole viewport, flip disabled and no filter: the GL frame buffer is copied directly to the image buffer and directly from there to the DeckLink card (hence no buffer to buffer copy inside VideoTexture)."""

        right = None  # type: VideoFFmpeg | ImageFFmpeg | ImageBuff | ImageMirror | ImageMix | ImageRender | ImageViewport
        """If the video format is stereo 3D, this attribute should be set to an image source object that will produce the right eye images. If the goal is to render the BGE scene in 3D, it can be achieved with 2 cameras, one for each eye, used by 2 ImageRender with an offscreen render buffer that is just the size of the video frame."""

        keying = False  # type: bool
        """Specify if keying is enabled. False (default): the output frame is sent unmodified on the output interface (in that case no input video is required). True: the output frame is mixed with the input video, using the alpha channel to blend the two images and the combination is sent on the output interface."""

        level = 0  # type: int
        """If keying is enabled, sets the keying level from 0 to 255. This value is a global alpha value that multiplies the alpha channel of the image source. Use 255 (the default) to keep the alpha channel unmodified, 0 to make the output frame totally transparent."""

        extend = False  # type: bool
        """Determines how the image source should be mapped if the size does not fit the video frame size. * False (the default): map the image pixel by pixel. If the image size is smaller than the frame size, extra space around the image is filled with 0-alpha black. If it is larger, the image is cropped to fit the frame size. * True: the image is scaled by the nearest neighbor algorithm to fit the frame size. The scaling is fast but poor quality. For best results, always adjust the image source to match the size of the output video."""

    def close(self):
        # type: () -> None
        """Close the DeckLink device and release all resources. After calling this method, the object cannot be reactivated, it must be destroyed and a new DeckLink object created from fresh to restart the output."""

        pass

    def refresh(self, refresh_source, ts):
        # type: (bool, float) -> None
        """This method must be called frequently to update the output frame in the DeckLink device.

        Args:
            refresh_source (bool): True if the source objects image buffer should be invalidated after being used to compute the output frame. This triggers the recomputing of the source image on next refresh, which is normally the desired effect. False if the image source buffer should stay valid and reused on next refresh. Note that the DeckLink device stores the output frame and replays until a new frame is sent from the host. Thus, it is not necessary to refresh the DeckLink object if it is known that the image source has not changed.
            ts (float): The timestamp value passed to the image source object to compute the image. If unspecified, the BGE clock is used."""

        pass


# Filter Classes
class FilterBGR24:
    """Source filter BGR24."""

    pass


class FilterBlueScreen:

    def __init__(self):
        # type: () -> None
        """Filter for Blue Screen. The RGB channels of the color are left unchanged, while the output alpha is obtained as follows:

        - if the square of the euclidian distance between the RGB color and the filter's reference color is smaller than the filter's lower limit, the output alpha is set to 0;
        - if that square is bigger than the filter's upper limit, the output alpha is set to 255;
        - otherwise the output alpha is linarly extrapoled between 0 and 255 in the interval of the limits."""

        self.color = (0, 0, 255)  # type: tuple[int, int, int]
        """Reference color."""

        self.limits = (64, 64)  # type: tuple[int, int]
        """Reference color limits."""

        self.previous = None  # type: FilterBGR24 | FilterBlueScreen | FilterColor | FilterGray | FilterLevel | FilterNormal | FilterRGB24 | FilterRGBA32
        """Previous pixel filter."""


class FilterColor:

    def __init__(self):
        # type: () -> None
        """Filter for color calculations. The output color is obtained by multiplying the reduced 4x4 matrix with the input color and adding the remaining column to the result."""

        self.matrix = (
            (256, 0, 0, 0, 0),
            (0, 256, 0, 0, 0),
            (0, 0, 256, 0, 0),
            (0, 0, 0, 256, 0),
        )  # type: tuple[tuple[int, int, int, int, int]]
        """Matrix [4][5] for color calculation."""

        self.previous = None  # type: FilterBGR24 | FilterBlueScreen | FilterColor | FilterGray | FilterLevel | FilterNormal | FilterRGB24 | FilterRGBA32
        """Previous pixel filter."""


class FilterGray:

    def __init__(self):
        # type: () -> None
        """Filter for gray scale effect. Proportions of R, G and B contributions in the output gray scale are 28:151:77."""

        self.previous = None  # type: FilterBGR24 | FilterBlueScreen | FilterColor | FilterGray | FilterLevel | FilterNormal | FilterRGB24 | FilterRGBA32
        """Previous pixel filter."""


class FilterLevel:

    def __init__(self):
        # type: () -> None
        """Filter for levels calculations. Each output color component is obtained as follows:

        - if it is smaller than its corresponding min value, it is set to 0;
        - if it is bigger than its corresponding max value, it is set to 255;
        - Otherwise it is linearly extrapoled between 0 and 255 in the (min, max) interval."""

        self.levels = ((0, 255), (0, 255), (0, 255), (0, 255))  # type: tuple[tuple[int, int]]
        """Levels matrix [4] (min, max)."""

        self.previous = None  # type: FilterBGR24 | FilterBlueScreen | FilterColor | FilterGray | FilterLevel | FilterNormal | FilterRGB24 | FilterRGBA32
        """Previous pixel filter."""


class FilterNormal:

    def __init__(self):
        # type: () -> None
        """Normal map filter."""

        self.colorIdx = 0  # type: int
        """Index of color used to calculate normal (0 - red, 1 - green, 2 - blue, 3 - alpha)."""

        self.depth = 4.0  # type: float
        """Depth of relief."""

        self.previous = None  # type: FilterBGR24 | FilterBlueScreen | FilterColor | FilterGray | FilterLevel | FilterNormal | FilterRGB24 | FilterRGBA32
        """Previous pixel filter."""


class FilterRGB24:
    """Returns a new input filter object to be used with ImageBuff object when the image passed to the ImageBuff.load() function has the 3-bytes pixel format BGR."""

    pass


class FilterRGBA32:
    """Source filter RGBA32."""

    pass


# Functions
def getLastError():
    # type: () -> str
    """Last error that occurred in a bge.texture function.

    Returns:
        str: The description of the last error occurred in a bge.texture function."""

    pass


def imageToArray(image, mode):
    # type: (VideoFFmpeg | ImageFFmpeg | ImageBuff | ImageMirror | ImageMix | ImageRender | ImageViewport, str) -> _bgl.Buffer
    """Returns a Buffer corresponding to the current image stored in a texture source object.

    Args:
        image: Image source object.
        mode (str): Optional argument representing the pixel format. You can use the characters R, G, B for the 3 color channels, A for the alpha channel, 0 to force a fixed 0 color channel and 1 to force a fixed 255 color channel.

    Examples for mode:
        - "BGR" will return 3 bytes per pixel with the Blue, Green and Red channels in that order.
        - "RGB1" will return 4 bytes per pixel with the Red, Green, Blue channels in that order and the alpha channel forced to 255.
        - A special mode "F" allows to return the image as an array of float. This mode should only be used to retrieve the depth buffer of the class:ImageViewport and ImageRender objects. The default mode is "RGBA".

    Returns:
        Buffer: An object representing the image as one dimensional array of bytes of size (pixel_size*width*height), line by line starting from the bottom of the image. The pixel size and format is determined by the mode parameter. For mode 'F', the array is a one dimensional array of float of size (width*height)."""

    pass


def materialID(object, name):
    # type: (_types.KX_GameObject, str) -> int
    """Returns a numeric value that can be used in Texture to create a dynamic texture.

    The value corresponds to an internal material number that uses the texture identified by name. name is a string representing a texture name with IM prefix if you want to identify the texture directly. This method works for basic tex face and for material, provided the material has a texture channel using that particular texture in first position of the texture stack. name can also have MA prefix if you want to identify the texture by material. In that case the material must have a texture channel in first position.

    If the object has no material that matches name, it generates a runtime error. Use try/except to catch the exception.

    Ex: bge.texture.materialID(obj, 'IMvideo.png')

    Args:
        object (KX_GameObject): The game object that uses the texture you want to make dynamic.
        name (str): Name of the texture/material you want to make dynamic.

    Returns:
        int: The internal material number."""

    pass


def setLogFile(filename):
    # type: (str) -> None
    """Sets the name of a text file in which runtime error messages will be written, in addition to the printing of the messages on the Python console. Only the runtime errors specific to the VideoTexture module are written in that file, ordinary runtime time errors are not written.

    Args:
        filename (str): Name of the error log file.

    Returns:
        int: -1 if the parameter name is invalid (not of type string), else 0."""

    pass
