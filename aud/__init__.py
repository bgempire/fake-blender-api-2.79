"""Audio System (aud)

This module provides access to the audaspace audio library."""


# Constants
AUD_DEVICE_JACK = 3 # type: int
AUD_DEVICE_NULL = 0 # type: int
AUD_DEVICE_OPENAL = 1 # type: int
AUD_DEVICE_SDL = 2 # type: int
AUD_DISTANCE_MODEL_EXPONENT = 5 # type: int
AUD_DISTANCE_MODEL_EXPONENT_CLAMPED = 6 # type: int
AUD_DISTANCE_MODEL_INVALID = 0 # type: int
AUD_DISTANCE_MODEL_INVERSE = 1 # type: int
AUD_DISTANCE_MODEL_INVERSE_CLAMPED = 2 # type: int
AUD_DISTANCE_MODEL_LINEAR = 3 # type: int
AUD_DISTANCE_MODEL_LINEAR_CLAMPED = 4 # type: int
AUD_FORMAT_FLOAT32 = 36 # type: int
AUD_FORMAT_FLOAT64 = 40 # type: int
AUD_FORMAT_INVALID = 0 # type: int
AUD_FORMAT_S16 = 18 # type: int
AUD_FORMAT_S24 = 19 # type: int
AUD_FORMAT_S32 = 20 # type: int
AUD_FORMAT_U8 = 1 # type: int
AUD_STATUS_INVALID = 0 # type: int
AUD_STATUS_PAUSED = 2 # type: int
AUD_STATUS_PLAYING = 1 # type: int
AUD_STATUS_STOPPED = 3 # type: int


# Classes
class Device:
	"""Device objects represent an audio output backend like OpenAL or SDL, 
	but might also represent a file output or RAM buffer output."""
	
	
	def __init__(self):
		self.channels = 2 # type: int
		self.distance_model = AUD_DISTANCE_MODEL_LINEAR # type: int
		self.doppler_factor = 1.0 # type: float
		self.format = 16 # type: int
		self.listener_location = (1.0, 1.0, 1.0) # type: tuple[float]
		self.listener_orientation = (1.0, 1.0, 1.0, 1.0) # type: tuple[float]
		self.listener_velocity = (1.0, 1.0, 1.0) # type: tuple[float]
		self.rate = 44100 # type: int
		self.speed_of_sound = 343.3 # type: float
		self.volume = 1.0 # type: float
	
	
	def lock(self):
		# type: () -> None
		"""Locks the device so that it's guaranteed, that no samples are read 
		from the streams until `unlock()` is called. This is useful if you want 
		to do start/stop/pause/resume some sounds at the same time.

		#### Note:
		The device has to be unlocked as often as locked to be able to 
		continue playback.
		
		#### Warning:
		Make sure the time between locking and unlocking is as short 
		as possible to avoid clicks."""
		
		pass
	
	
	def play(self, factory, keep=False):
		# type: (Factory, bool) -> Handle
		"""Plays a factory.
		
		#### Parameters:
		- factory (Factory) - The factory to play.
		- keep (bool) - See Handle.keep.
		
		#### Returns:
		The playback handle with which playback can be controlled with.
		
		#### Return type
		Handle"""
		
		return Handle()
	
	
	def stopAll(self):
		# type: () -> None
		"""Stops all playing and paused sounds."""
		
		pass
	
	
	def unlock(self):
		# type: () -> None
		"""Unlocks the device after a lock call, see lock() for details."""
		
		pass


class Factory:
	"""Factory objects are immutable and represent a sound that can be played 
	simultaneously multiple times. They are called factories because they 
	create reader objects internally that are used for playback."""
	
	
	def file(self, filename):
		# type: (str) -> Factory
		"""Creates a factory object of a sound file.

		#### Parameters:
		- filename (string) - Path of the file.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory
		
		#### Warning:
		If the file doesn't exist or can't be read you will not get 
		an exception immediately, but when you try to start playback of that 
		factory."""
		
		return self
	
	
	def sine(self, frequency, rate=48000):
		# type: (float, int) -> Factory
		"""Creates a sine factory which plays a sine wave.

		#### Parameters:
		- frequency (float) - The frequency of the sine wave in Hz.
		- rate (int) - The sampling rate in Hz. It's recommended to set this 
		value to the playback device's sampling rate to avoid resampling.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory"""
		
		return self
	
	
	def buffer(self):
		# type: () -> Factory
		"""Buffers a factory into RAM. This saves CPU usage needed for 
		decoding and file access if the underlying factory reads from a file 
		on the harddisk, but it consumes a lot of memory.

		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory
		
		#### Note:
		Only known-length factories can be buffered.
		
		#### Warning:
		Raw PCM data needs a lot of space, only buffer short factories."""
		
		return self
	
	
	def delay(self, time):
		# type: (float) -> Factory
		"""Delays by playing adding silence in front of the other factory's data.

		#### Parameters:
		- time (float) - How many seconds of silence should be added before the factory.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory"""
		
		return self
	
	
	def fadein(self, start, length):
		# type: (float, float) -> Factory
		"""Fades a factory in by raising the volume linearly in the given 
		time interval.

		#### Parameters:
		- start (float) - Time in seconds when the fading should start.
		- length (float) - Time in seconds how long the fading should last.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory

		#### Note:
		Before the fade starts it plays silence."""
		
		return self
	
	
	def fadeout(self, start, length):
		# type: (float, float) -> Factory
		"""Fades a factory in by lowering the volume linearly in the given 
		time interval.

		#### Parameters:
		- start (float) - Time in seconds when the fading should start.
		- length (float) - Time in seconds how long the fading should last.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory

		#### Note:
		After the fade this factory plays silence, so that the length 
		of the factory is not altered."""
		
		return self
	
	
	def filter(self, b, a=1.0):
		# type: (tuple[float], tuple[float]) -> Factory
		"""Filters a factory with the supplied IIR filter coefficients. 
		Without the second parameter you'll get a FIR filter. If the first 
		value of the a sequence is 0 it will be set to 1 automatically. If 
		the first value of the a sequence is neither 0 nor 1, all filter 
		coefficients will be scaled by this value so that it is 1 in the 
		end, you don't have to scale yourself.

		#### Parameters:
		- b (sequence of float) - The nominator filter coefficients.
		- a (sequence of float) - The denominator filter coefficients.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory"""
		
		return self
	
	
	def highpass(self, frequency, Q=0.5):
		# type: (float, float) -> Factory
		"""Creates a second order highpass filter based on the transfer 
		function H(s) = s^2 / (s^2 + s/Q + 1)

		#### Parameters:	
		- frequency (float) - The cut off trequency of the highpass.
		- Q (float) - Q factor of the lowpass.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory"""
		
		return self
	
	
	def join(self, factory):
		# type: (Factory) -> Factory
		"""Plays two factories in sequence.

		#### Parameters:
		- factory (Factory) - The factory to play second.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory
		
		#### Note:
		The two factories have to have the same specifications 
		(channels and samplerate)."""
		
		return self
	
	
	def limit(self, start, end):
		# type: (float, float) -> Factory
		"""Limits a factory within a specific start and end time.

		#### Parameters:	
		- start (float) - Start time in seconds.
		- end (float) - End time in seconds.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory"""
		
		return self
	
	
	def loop(self, count):
		# type: (int) -> Factory
		"""Loops a factory.

		#### Parameters:
		- count (integer) - How often the factory should be looped. Negative 
		- values mean endlessly.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory
		
		#### Note:
		This is a filter function, you might consider using 
		Handle.loop_count instead."""
		
		return self
	
	
	def lowpass(self, frequency, Q=0.5):
		# type: (float, float) -> Factory
		"""Creates a second order lowpass filter based on the transfer 
		function H(s) = 1 / (s^2 + s/Q + 1)

		#### Parameters:
		- frequency (float) - The cut off trequency of the lowpass.
		- Q (float) - Q factor of the lowpass.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory"""
		
		return self
	
	
	def mix(self, factory):
		# type: (Factory) -> Factory
		"""Mixes two factories.
		
		#### Parameters:
		- factory (Factory) - The factory to mix over the other.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory
		
		#### Note:
		The two factories have to have the same specifications 
		(channels and samplerate)."""
		
		return self
	
	
	def pingpong(self):
		# type: () -> Factory
		"""Plays a factory forward and then backward. This is like joining 
		a factory with its reverse.

		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory"""
		
		return self
	
	
	def pitch(self, factor):
		# type: (float) -> Factory
		"""Changes the pitch of a factory with a specific factor.

		#### Parameters:
		- factor (float) - The factor to change the pitch with.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory
		
		#### Notes:
		- This is done by changing the sample rate of the underlying 
		factory, which has to be an integer, so the factor value rounded and 
		the factor may not be 100% accurate.
		- This is a filter function, you might consider using 
		Handle.pitch instead."""
		
		return self
	
	
	def reverse(self):
		# type: () -> Factory
		"""Plays a factory reversed.

		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory
		
		#### Note:
		The factory has to have a finite length and has to be seekable. 
		It's recommended to use this only with factories with fast and 
		accurate seeking, which is not true for encoded audio files, such 
		ones should be buffered using buffer() before being played reversed.
		
		#### Warning:
		If seeking is not accurate in the underlying factory you'll 
		likely hear skips/jumps/cracks."""
		
		return self
	
	
	def square(self, threshold=0.0):
		# type: (float) -> Factory
		"""Makes a square wave out of an audio wave by setting all samples 
		with a amplitude >= threshold to 1, all <= -threshold to -1 and 
		all between to 0.

		#### Parameters:
		- threshold (float) - Threshold value over which an amplitude counts non-zero.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory"""
		
		return self
	
	
	def volume(self, volume):
		# type: (float) -> Factory
		"""Changes the volume of a factory.

		#### Parameters:
		- volume (float) - The new volume.
		
		#### Returns:
		The created Factory object.
		
		#### Return type:
		Factory
		
		#### Notes:
		- Should be in the range [0, 1] to avoid clipping.
		- This is a filter function, you might consider using 
		Handle.volume instead."""
		
		return self


class Handle:
	"""Handle objects are playback handles that can be used to control 
	playback of a sound. If a sound is played back multiple times then 
	there are as many handles."""
	
	
	def __init__(self):
		self.attenuation = 1.0 # type: float
		self.cone_angle_inner = 1.0 # type: float
		self.cone_angle_outer = 1.0 # type: float
		self.cone_volume_outer = 1.0 # type: float
		self.distance_maximum = 1.0 # type: float
		self.distance_reference = 1.0 # type: float
		self.keep = False # type: bool
		self.location = (1.0, 1.0, 1.0) # type: tuple[float]
		self.loop_count = 1 # type: int
		self.orientation = (1.0, 1.0, 1.0, 1.0) # type: tuple[float]
		self.pitch = 1.0 # type: float
		self.position = 1.0 # type: float
		self.relative = False # type: bool
		self.status = AUD_STATUS_PLAYING # type: int
		self.velocity = (1.0, 1.0, 1.0) # type: tuple[float]
		self.volume = 1.0 # type: float
		self.volume_maximum = 1.0 # type: float
		self.volume_minimum = 1.0 # type: float
	
	
	def pause(self):
		# type: () -> bool
		"""Pauses playback.

		#### Returns:
		Whether the action succeeded.
		
		#### Return type:
		bool"""
		
		return True
	
	
	def resume(self):
		# type: () -> bool
		"""Resumes playback.

		#### Returns:
		Whether the action succeeded.
		
		#### Return type:
		bool"""
		
		return True
	
	
	def stop(self):
		# type: () -> bool
		"""Stops playback.

		#### Returns:
		Whether the action succeeded.
		
		#### Return type:
		bool
		
		#### Note:
		This makes the handle invalid."""
		
		return True


# Functions
def device():
	# type: () -> Device
	"""Returns the application's Device.

	#### Return:
	The application's Device.
	
	#### Return type:
	Device"""
	
	return Device()


class error:
	pass
