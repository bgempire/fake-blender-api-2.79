"""Audio System (aud)

This module provides access to the audaspace audio library."""

class Device: pass
class Factory: pass
class Handle: pass

# Constants
AUD_DEVICE_JACK = 3
AUD_DEVICE_NULL = 0
AUD_DEVICE_OPENAL = 1
AUD_DEVICE_SDL = 2
AUD_DISTANCE_MODEL_EXPONENT = 5
AUD_DISTANCE_MODEL_EXPONENT_CLAMPED = 6
AUD_DISTANCE_MODEL_INVALID = 0
AUD_DISTANCE_MODEL_INVERSE = 1
AUD_DISTANCE_MODEL_INVERSE_CLAMPED = 2
AUD_DISTANCE_MODEL_LINEAR = 3
AUD_DISTANCE_MODEL_LINEAR_CLAMPED = 4
AUD_FORMAT_FLOAT32 = 36
AUD_FORMAT_FLOAT64 = 40
AUD_FORMAT_INVALID = 0
AUD_FORMAT_S16 = 18
AUD_FORMAT_S24 = 19
AUD_FORMAT_S32 = 20
AUD_FORMAT_U8 = 1
AUD_STATUS_INVALID = 0
AUD_STATUS_PAUSED = 2
AUD_STATUS_PLAYING = 1
AUD_STATUS_STOPPED = 3

# Classes
class Device:
	"""Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output."""
	
	def __init__(self):
		self.channels = 2
		self.distance_model = AUD_DISTANCE_MODEL_LINEAR
		self.doppler_factor = 1.0
		self.format = 16
		self.listener_location = (1.0, 1.0, 1.0)
		self.listener_orientation = (1.0, 1.0, 1.0, 1.0)
		self.listener_velocity = (1.0, 1.0, 1.0)
		self.rate = 44100
		self.speed_of_sound = 343.3
		self.volume = 1.0
	
	def lock(self):
		"""Locks the device so that it’s guaranteed, that no samples are read from the streams until unlock() is called. This is useful if you want to do start/stop/pause/resume some sounds at the same time.

		Note: The device has to be unlocked as often as locked to be able to continue playback.
		
		Warning: Make sure the time between locking and unlocking is as short as possible to avoid clicks."""
		
		pass
	
	def play(self, factory, keep=False):
		"""Plays a factory.

		Parameters:
		factory (Factory) – The factory to play.
		keep (bool) – See Handle.keep.
		
		Returns: The playback handle with which playback can be controlled with.

		Return type: Handle"""
		
		return Handle()
	
	def stopAll(self):
		"""Stops all playing and paused sounds."""
		
		pass
	
	def unlock(self):
		"""Unlocks the device after a lock call, see lock() for details."""
		
		pass

class Factory:
	"""Factory objects are immutable and represent a sound that can be played simultaneously multiple times. They are called factories because they create reader objects internally that are used for playback."""
	
	def file(self, filename):
		"""Creates a factory object of a sound file.

		Parameters:
		filename (string) – Path of the file.
		
		Returns: The created Factory object.
		
		Return type: Factory
		
		Warning: If the file doesn’t exist or can’t be read you will not get an exception immediately, but when you try to start playback of that factory."""
		
		return self
	
	def sine(self, frequency, rate=48000):
		"""Creates a sine factory which plays a sine wave.

		Parameters:
		frequency (float) – The frequency of the sine wave in Hz.
		rate (int) – The sampling rate in Hz. It’s recommended to set this value to the playback device’s samling rate to avoid resamping.
		
		Returns: The created Factory object.

		Return type: Factory"""
		
		return self
	
	def buffer(self):
		"""Buffers a factory into RAM. This saves CPU usage needed for decoding and file access if the underlying factory reads from a file on the harddisk, but it consumes a lot of memory.

		Returns: The created Factory object.
		
		Return type: Factory
		
		Note: Only known-length factories can be buffered.
		
		Warning: Raw PCM data needs a lot of space, only buffer short factories."""
		
		return self
	
	def delay(self, time):
		"""Delays by playing adding silence in front of the other factory’s data.

		Parameters:
		time (float) – How many seconds of silence should be added before the factory.
		
		Returns: The created Factory object.
		
		Return type: Factory"""
		
		return self
	
	def fadein(self, start, length):
		"""Fades a factory in by raising the volume linearly in the given time interval.

		Parameters:	
		start (float) – Time in seconds when the fading should start.
		length (float) – Time in seconds how long the fading should last.
		
		Returns: The created Factory object.

		Return type: Factory

		Note: Before the fade starts it plays silence."""
		
		return self
	
	def fadeout(self, start, length):
		"""Fades a factory in by lowering the volume linearly in the given time interval.

		Parameters:
		start (float) – Time in seconds when the fading should start.
		length (float) – Time in seconds how long the fading should last.
		
		Returns: The created Factory object.

		Return type: Factory

		Note: After the fade this factory plays silence, so that the length of the factory is not altered."""
		
		return self
	
	def filter(self, b, a=1.0):
		"""Filters a factory with the supplied IIR filter coefficients. Without the second parameter you’ll get a FIR filter. If the first value of the a sequence is 0 it will be set to 1 automatically. If the first value of the a sequence is neither 0 nor 1, all filter coefficients will be scaled by this value so that it is 1 in the end, you don’t have to scale yourself.

		Parameters:
		b (sequence of float) – The nominator filter coefficients.
		a (sequence of float) – The denominator filter coefficients.
		
		Returns: The created Factory object.

		Return type: Factory"""
		
		return self
	
	def highpass(self, frequency, Q=0.5):
		"""Creates a second order highpass filter based on the transfer function H(s) = s^2 / (s^2 + s/Q + 1)

		Parameters:	
		frequency (float) – The cut off trequency of the highpass.
		Q (float) – Q factor of the lowpass.
		
		Returns: The created Factory object.

		Return type: Factory"""
		
		return self
	
	def join(self, factory):
		"""Plays two factories in sequence.

		Parameters:
		factory (Factory) – The factory to play second.
		
		Returns: The created Factory object.
		
		Return type: Factory
		
		Note: The two factories have to have the same specifications (channels and samplerate)."""
		
		return self
	
	def limit(self, start, end):
		"""Limits a factory within a specific start and end time.

		Parameters:	
		start (float) – Start time in seconds.
		end (float) – End time in seconds.
		
		Returns: The created Factory object.

		Return type: Factory"""
		
		return self
	
	def loop(self, count):
		"""Loops a factory.

		Parameters:
		count (integer) – How often the factory should be looped. Negative values mean endlessly.
		
		Returns: The created Factory object.
		
		Return type: Factory
		
		Note: This is a filter function, you might consider using Handle.loop_count instead."""
		
		return self
	
	def lowpass(self, frequency, Q=0.5):
		"""Creates a second order lowpass filter based on the transfer function H(s) = 1 / (s^2 + s/Q + 1)

		Parameters:
		frequency (float) – The cut off trequency of the lowpass.
		Q (float) – Q factor of the lowpass.
		
		Returns: The created Factory object.

		Return type: Factory"""
		
		return self
	
	def mix(self, factory):
		"""Mixes two factories.

		Parameters:
		factory (Factory) – The factory to mix over the other.
		
		Returns: The created Factory object.
		
		Return type: Factory
		
		Note: The two factories have to have the same specifications (channels and samplerate)."""
		
		return self
	
	def pingpong(self):
		"""Plays a factory forward and then backward. This is like joining a factory with its reverse.

		Returns: The created Factory object.
		
		Return type: Factory"""
		
		return self
	
	def pitch(self, factor):
		"""Changes the pitch of a factory with a specific factor.

		Parameters:
		factor (float) – The factor to change the pitch with.
		
		Returns: The created Factory object.
		
		Return type: Factory
		
		Note: This is done by changing the sample rate of the underlying factory, which has to be an integer, so the factor value rounded and the factor may not be 100 % accurate.
		
		Note: This is a filter function, you might consider using Handle.pitch instead."""
		
		return self
	
	def reverse(self):
		"""Plays a factory reversed.

		Returns: The created Factory object.
		
		Return type: Factory
		
		Note: The factory has to have a finite length and has to be seekable. It’s recommended to use this only with factories with fast and accurate seeking, which is not true for encoded audio files, such ones should be buffered using buffer() before being played reversed.
		
		Warning: If seeking is not accurate in the underlying factory you’ll likely hear skips/jumps/cracks."""
		
		return self
	
	def square(self, threshold=0):
		"""Makes a square wave out of an audio wave by setting all samples with a amplitude >= threshold to 1, all <= -threshold to -1 and all between to 0.

		Parameters:
		threshold (float) – Threshold value over which an amplitude counts non-zero.
		
		Returns: The created Factory object.
		
		Return type: Factory"""
		
		return self
	
	def volume(self, volume):
		"""Changes the volume of a factory.

		Parameters:
		volume (float) – The new volume.
		
		Returns: The created Factory object.
		
		Return type: Factory
		
		Note: Should be in the range [0, 1] to avoid clipping.
		
		Note: This is a filter function, you might consider using Handle.volume instead."""
		
		return self

class Handle:
	"""Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles."""
	
	def __init__(self):
		self.attenuation = 1.0
		self.cone_angle_inner = 1.0
		self.cone_angle_outer = 1.0
		self.cone_volume_outer = 1.0
		self.distance_maximum = 1.0
		self.distance_reference = 1.0
		self.keep = False
		self.location = (1.0, 1.0, 1.0)
		self.loop_count = 1
		self.orientation = (1.0, 1.0, 1.0, 1.0)
		self.pitch = 1.0
		self.position = 1.0
		self.relative = False
		self.status = AUD_STATUS_PLAYING
		self.velocity = (1.0, 1.0, 1.0)
		self.volume = 1.0
		self.volume_maximum = 1.0
		self.volume_minimum = 1.0
		
	def pause(self):
		"""Pauses playback.

		Returns: Whether the action succeeded.
		
		Return type: bool"""
		
		return True
		
	def resume(self):
		"""Resumes playback.

		Returns: Whether the action succeeded.
		
		Return type: bool"""
		
		return True
		
	def stop(self):
		"""Stops playback.

		Returns: Whether the action succeeded.
		
		Return type: bool
		
		Note: This makes the handle invalid."""
		
		return True
	
# Functions
def device():
	"""Returns the application’s Device.

	Return: The application’s Device.
	
	Return type: Device"""
	
	return Device()

class error:
	pass