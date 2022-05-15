"""Audio System (aud)

This module provides access to the Audaspace audio library."""

# Constants
AUD_DEVICE_JACK = 3  # type: int
AUD_DEVICE_NULL = 0  # type: int
AUD_DEVICE_OPENAL = 1  # type: int
AUD_DEVICE_SDL = 2  # type: int
AUD_DISTANCE_MODEL_EXPONENT = 5  # type: int
AUD_DISTANCE_MODEL_EXPONENT_CLAMPED = 6  # type: int
AUD_DISTANCE_MODEL_INVALID = 0  # type: int
AUD_DISTANCE_MODEL_INVERSE = 1  # type: int
AUD_DISTANCE_MODEL_INVERSE_CLAMPED = 2  # type: int
AUD_DISTANCE_MODEL_LINEAR = 3  # type: int
AUD_DISTANCE_MODEL_LINEAR_CLAMPED = 4  # type: int
AUD_FORMAT_FLOAT32 = 36  # type: int
AUD_FORMAT_FLOAT64 = 40  # type: int
AUD_FORMAT_INVALID = 0  # type: int
AUD_FORMAT_S16 = 18  # type: int
AUD_FORMAT_S24 = 19  # type: int
AUD_FORMAT_S32 = 20  # type: int
AUD_FORMAT_U8 = 1  # type: int
AUD_STATUS_INVALID = 0  # type: int
AUD_STATUS_PAUSED = 2  # type: int
AUD_STATUS_PLAYING = 1  # type: int
AUD_STATUS_STOPPED = 3  # type: int


# Classes
class Device:

    def __init__(self):
        # type: () -> None
        """Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output."""

        self.channels = 2  # type: int
        """The channel count of the device."""

        self.distance_model = AUD_DISTANCE_MODEL_LINEAR  # type: int
        """The distance model of the device.

        See also the OpenAL documentation: https://www.openal.org/documentation """

        self.doppler_factor = 1.0  # type: float
        """The doppler factor of the device. This factor is a scaling factor for the velocity vectors in doppler calculation. So a value bigger than 1 will exaggerate the effect as it raises the velocity."""

        self.format = 16  # type: int
        """The native sample format of the device."""

        self.listener_location = (1.0, 1.0, 1.0)  # type: tuple[float, float, float]
        """The listeners's location in 3D space, a 3D tuple of floats."""

        self.listener_orientation = (1.0, 1.0, 1.0, 1.0)  # type: tuple[float, float, float, float]
        """The listener's orientation in 3D space as quaternion, a 4 float tuple."""

        self.listener_velocity = (1.0, 1.0, 1.0)  # type: tuple[float, float, float]
        """The listener's velocity in 3D space, a 3D tuple of floats."""

        self.rate = 44100  # type: int
        """The sampling rate of the device in Hz."""

        self.speed_of_sound = 343.3  # type: float
        """The speed of sound of the device. The speed of sound in air is typically 343.3 m/s."""

        self.volume = 1.0  # type: float
        """The overall volume of the device."""

    def lock(self):
        # type: () -> None
        """Locks the device so that it's guaranteed, that no samples are read from the streams until unlock() is called. This is useful if you want to do start/stop/pause/resume some sounds at the same time.

        Notes:
            - The device has to be unlocked as often as locked to be able to continue playback.
            - Make sure the time between locking and unlocking is as short as possible to avoid clicks."""

        pass

    def play(self, factory, keep=False):
        # type: (Factory, bool) -> Handle
        """Plays a factory.

        Args:
            factory (Factory): The factory to play.
            keep (bool): See Handle.keep.

        Returns:
            Handle: The playback handle with which playback can be controlled with."""

        pass

    def stopAll(self):
        # type: () -> None
        """Stops all playing and paused sounds."""

        pass

    def unlock(self):
        # type: () -> None
        """Unlocks the device after a lock call, see lock() for details."""

        pass


class Factory:
    """Factory objects are immutable and represent a sound that can be played simultaneously multiple times. They are called factories because they create reader objects internally that are used for playback."""

    @staticmethod
    def file(filename):
        # type: (str) -> Factory
        """Creates a factory object of a sound file.

        Args:
            filename (string): Path of the file.

        Returns:
            Factory: The created Factory object.

        Note:
            - If the file doesn't exist or can't be read you will not get an exception immediately, but when you try to start playback of that factory."""

        pass

    @staticmethod
    def sine(frequency, rate=48000):
        # type: (float, int) -> Factory
        """Creates a sine factory which plays a sine wave.

        Args:
            frequency (float): The frequency of the sine wave in Hz.
            rate (int): The sampling rate in Hz. It's recommended to set this value to the playback device's sampling rate to avoid resampling.

        Returns:
            Factory: The created Factory object."""

        pass

    def buffer(self):
        # type: () -> Factory
        """Buffers a factory into RAM. This saves CPU usage needed for decoding and file access if the underlying factory reads from a file on the hard-disk, but it consumes a lot of memory.

        Returns:
            Factory: The created Factory object.

        Notes:
            - Only known-length factories can be buffered.
            - Raw PCM data needs a lot of space, only buffer short factories."""

        pass

    def delay(self, time):
        # type: (float) -> Factory
        """Delays by playing adding silence in front of the other factory's data.

        Args:
            time (float): How many seconds of silence should be added before the factory.

        Returns:
            Factory: The created Factory object."""

        pass

    def fadein(self, start, length):
        # type: (float, float) -> Factory
        """Fades a factory in by raising the volume linearly in the given time interval.

        Args:
            start (float): Time in seconds when the fading should start.
            length (float): Time in seconds how long the fading should last.

        Returns:
            Factory: The created Factory object.

        Note:
            - Before the fade starts it plays silence."""

        pass

    def fadeout(self, start, length):
        # type: (float, float) -> Factory
        """Fades a factory in by lowering the volume linearly in the given time interval.

        Args:
            start (float): Time in seconds when the fading should start.
            length (float): Time in seconds how long the fading should last.

        Returns:
            Factory: The created Factory object.

        Note:
            - After the fade this factory plays silence, so that the length of the factory is not altered."""

        pass

    def filter(self, b, a=1.0):
        # type: (tuple[float], tuple[float]) -> Factory
        """Filters a factory with the supplied IIR filter coefficients. Without the second parameter you'll get a FIR filter. If the first value of the sequence is 0 it will be set to 1 automatically. If the first value of the sequence is neither 0 nor 1, all filter coefficients will be scaled by this value so that it is 1 in the end, you don't have to scale yourself.

        Args:
            b (tuple[float]): The nominator filter coefficients.
            a (tuple[float]): The denominator filter coefficients.

        Returns:
            Factory: The created Factory object."""

        pass

    def highpass(self, frequency, Q=0.5):
        # type: (float, float) -> Factory
        """Creates a second order highpass filter based on the transfer function H(s) = s^2 / (s^2 + s/Q + 1).

        Args:
            frequency (float): The cut-off frequency of the highpass.
            Q (float): Q factor of the lowpass.

        Returns:
            Factory: The created Factory object."""

        pass

    def join(self, factory):
        # type: (Factory) -> Factory
        """Plays two factories in sequence.

        Args:
            factory (Factory): The factory to play second.

        Returns:
            Factory: The created Factory object.

        Note:
            - The two factories have to have the same specifications (channels and samplerate)."""

        pass

    def limit(self, start, end):
        # type: (float, float) -> Factory
        """Limits a factory within a specific start and end time.

        Args:
            start (float): Start time in seconds.
            end (float): End time in seconds.

        Returns:
            Factory: The created Factory object."""

        pass

    def loop(self, count):
        # type: (int) -> Factory
        """Loops a factory.

        Args:
            count (integer): How often the factory should be looped. Negative values mean endlessly.

        Returns:
            Factory: The created Factory object.

        Note:
            - This is a filter function, you might consider using Handle.loop_count instead."""

        pass

    def lowpass(self, frequency, Q=0.5):
        # type: (float, float) -> Factory
        """Creates a second order lowpass filter based on the transfer function H(s) = 1 / (s^2 + s/Q + 1)

        Args:
            frequency (float): The cut-off frequency of the lowpass.
            Q (float): Q factor of the lowpass.

        Returns:
            Factory: The created Factory object."""

        pass

    def mix(self, factory):
        # type: (Factory) -> Factory
        """Mixes two factories.

        Args:
            factory (Factory): The factory to mix over the other.

        Returns:
            Factory: The created Factory object.

        Note:
            - The two factories have to have the same specifications (channels and samplerate)."""

        pass

    def pingpong(self):
        # type: () -> Factory
        """Plays a factory forward and then backward. This is like joining a factory with its reverse.

        Returns:
            Factory: The created Factory object."""

        pass

    def pitch(self, factor):
        # type: (float) -> Factory
        """Changes the pitch of a factory with a specific factor.

        Args:
            factor (float): The factor to change the pitch with.

        Returns:
            Factory: The created Factory object.

        Notes:
            - This is done by changing the sample rate of the underlying factory, which has to be an integer, so the factor value rounded and the factor may not be 100% accurate.
            - This is a filter function, you might consider using Handle.pitch instead."""

        pass

    def reverse(self):
        # type: () -> Factory
        """Plays a factory reversed.

        Returns:
            Factory: The created Factory object.

        Notes:
            - The factory has to have a finite length and has to be seekable. It's recommended to use this only with factories with fast and accurate seeking, which is not true for encoded audio files, such ones should be buffered using buffer() before being played reversed.
            - If seeking is not accurate in the underlying factory you'll likely hear skips/jumps/cracks."""

        pass

    def square(self, threshold=0.0):
        # type: (float) -> Factory
        """Makes a square wave out of an audio wave by setting all samples with a amplitude >= threshold to 1, all <= -threshold to -1 and all between to 0.

        Args:
            threshold (float): Threshold value over which an amplitude counts non-zero.

        Returns:
            Factory: The created Factory object."""

        pass

    def volume(self, volume):
        # type: (float) -> Factory
        """Changes the volume of a factory.

        Args:
            volume (float): The new volume.

        Returns:
            Factory: The created Factory object.

        Notes:
            - Should be in the range [0, 1] to avoid clipping.
            - This is a filter function, you might consider using Handle.volume instead."""

        pass


class Handle:

    def __init__(self):
        # type: () -> None
        """Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles."""

        self.attenuation = 1.0  # type: float
        """This factor is used for distance based attenuation of the source."""

        self.cone_angle_inner = 1.0  # type: float
        """The opening angle of the inner cone of the source. If the cone values of a source are set there are two (audible) cones with the apex at the location of the source and with infinite height, heading in the direction of the source’s orientation. In the inner cone the volume is normal. Outside the outer cone the volume will be cone_volume_outer and in the area between the volume will be interpolated linearly."""

        self.cone_angle_outer = 1.0  # type: float
        """The opening angle of the outer cone of the source."""

        self.cone_volume_outer = 1.0  # type: float
        """The volume outside the outer cone of the source."""

        self.distance_maximum = 1.0  # type: float
        """The maximum distance of the source. If the listener is further away the source volume will be 0."""

        self.distance_reference = 1.0  # type: float
        """The reference distance of the source. At this distance the volume will be exactly volume."""

        self.keep = False  # type: bool
        """Whether the sound should be kept paused in the device when its end is reached. This can be used to seek the sound to some position and start playback again.

        Warning:
            If this is set to true and you forget stopping this equals a memory leak as the handle exists until the device is destroyed."""

        self.location = (1.0, 1.0, 1.0)  # type: tuple[float, float, float]
        """The source’s location in 3D space, a 3D tuple of floats."""

        self.loop_count = 1  # type: int
        """The (remaining) loop count of the sound. A negative value indicates infinity."""

        self.orientation = (1.0, 1.0, 1.0, 1.0)  # type: tuple[float, float, float, float]
        """The source’s orientation in 3D space as quaternion, a 4 float tuple."""

        self.pitch = 1.0  # type: float
        """The pitch of the sound."""

        self.position = 1.0  # type: float
        """The playback position of the sound in seconds."""

        self.relative = False  # type: bool
        """Whether the source’s location, velocity and orientation is relative or absolute to the listener."""

        self.status = AUD_STATUS_PLAYING  # type: int
        """Whether the sound is playing, paused or stopped (=invalid)."""

        self.velocity = (1.0, 1.0, 1.0)  # type: tuple[float, float, float]
        """The source’s velocity in 3D space, a 3D tuple of floats."""

        self.volume = 1.0  # type: float
        """The volume of the sound."""

        self.volume_maximum = 1.0  # type: float
        """The maximum volume of the source."""

        self.volume_minimum = 1.0  # type: float
        """The minimum volume of the source."""

    def pause(self):
        # type: () -> bool
        """Pauses playback.

        Returns:
            bool: Whether the action succeeded."""

        pass

    def resume(self):
        # type: () -> bool
        """Resumes playback.

        Returns:
            bool: Whether the action succeeded."""

        pass

    def stop(self):
        # type: () -> bool
        """Stops playback.

        Returns:
            bool: Whether the action succeeded.

        Note:
            - This makes the handle invalid."""

        pass


# Functions
def device():
    # type: () -> Device
    """Returns the application's Device.

    Returns:
        Device: The application's Device."""

    pass


class error:
    pass
