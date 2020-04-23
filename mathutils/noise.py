"""Noise Utilities (mathutils.noise)

The Blender noise module"""

class distance_metrics:
	CHEBYCHEV = 3
	DISTANCE = 0
	DISTANCE_SQUARED = 1
	MANHATTAN = 2
	MINKOVSKY = 6
	MINKOVSKY_FOUR = 5
	MINKOVSKY_HALF = 4

class types:
	BLENDER = 0
	CELLNOISE = 14
	NEWPERLIN = 2
	STDPERLIN = 1
	VORONOI_CRACKLE = 8
	VORONOI_F1 = 3
	VORONOI_F2 = 4
	VORONOI_F2F1 = 7
	VORONOI_F3 = 5
	VORONOI_F4 = 6

def cell(position):
	"""Returns cell noise value at the specified position.

	Parameters:
	position (mathutils.Vector) – The position to evaluate the selected noise function at.
	
	Returns: The cell noise value.
	
	Return type: float"""
	
	return 1.0

def cell_vector(position):
	"""Returns cell noise vector at the specified position.

	Parameters:	position (mathutils.Vector) – The position to evaluate the selected noise function at.
	
	Returns: The cell noise vector.
	
	Return type: mathutils.Vector"""
	
	from . import Vector
	return Vector

def fractal(position, H, lacunarity, octaves, noise_basis=types.STDPERLIN):
	"""Returns the fractal Brownian motion (fBm) noise value from the noise basis at the specified position.

	Parameters:	
	position (mathutils.Vector) – The position to evaluate the selected noise function at.
	H (float) – The fractal increment factor.
	lacunarity (float) – The gap between successive frequencies.
	octaves (int) – The number of different noise frequencies used.
	noise_basis (Value in noise.types or int) – The type of noise to be evaluated.
	
	Returns: The fractal Brownian motion noise value.

	Return type: float"""
	
	return 1.0

def hetero_terrain(position, H, lacunarity, octaves, offset, noise_basis=types.STDPERLIN):
	"""Returns the heterogeneous terrain value from the noise basis at the specified position.

	Parameters:	
	position (mathutils.Vector) – The position to evaluate the selected noise function at.
	H (float) – The fractal dimension of the roughest areas.
	lacunarity (float) – The gap between successive frequencies.
	octaves (int) – The number of different noise frequencies used.
	offset (float) – The height of the terrain above ‘sea level’.
	noise_basis (Value in noise.types or int) – The type of noise to be evaluated.
	
	Returns: The heterogeneous terrain value.

	Return type: float"""
	
	return 1.0

def hybrid_multi_fractal(position, H, lacunarity, octaves, offset, gain, noise_basis=types.STDPERLIN):
	"""Returns hybrid multifractal value from the noise basis at the specified position.

	Parameters:	
	position (mathutils.Vector) – The position to evaluate the selected noise function at.
	H (float) – The fractal dimension of the roughest areas.
	lacunarity (float) – The gap between successive frequencies.
	octaves (int) – The number of different noise frequencies used.
	offset (float) – The height of the terrain above ‘sea level’.
	gain (float) – Scaling applied to the values.
	noise_basis (Value in noise.types or int) – The type of noise to be evaluated.
	
	Returns: The hybrid multifractal value.

	Return type: float"""
	
	return 1.0

def multi_fractal(position, H, lacunarity, octaves, noise_basis=types.STDPERLIN):
	"""Returns multifractal noise value from the noise basis at the specified position.

	Parameters:	
	position (mathutils.Vector) – The position to evaluate the selected noise function at.
	H (float) – The fractal increment factor.
	lacunarity (float) – The gap between successive frequencies.
	octaves (int) – The number of different noise frequencies used.
	noise_basis (Value in noise.types or int) – The type of noise to be evaluated.
	
	Returns: The multifractal noise value.

	Return type: float"""
	
	return 1.0

def noise(position, noise_basis=types.STDPERLIN):
	"""Returns the noise vector from the noise basis at the specified position.

	Parameters:	
	position (mathutils.Vector) – The position to evaluate the selected noise function at.
	noise_basis (Value in noise.types or int) – The type of noise to be evaluated.
	
	Returns: The noise vector.

	Return type: mathutils.Vector"""
	
	from . import Vector
	return Vector
	
def random():
	"""Returns a random number in the range [0, 1].

	Returns: The random number.
	
	Return type: float"""
	
	return 1.0

def random_unit_vector(size=3):
	"""Returns a unit vector with random entries.

	Parameters:
	size (Int) – The size of the vector to be produced.
	
	Returns: The random unit vector.
	
	Return type: mathutils.Vector"""
	
	from . import Vector
	return Vector
	
def random():
	"""Returns a random number in the range [0, 1].

	Returns: The random number.
	
	Return type: float"""
	
	return 1.0
	
def ridged_multi_fractal(position, H, lacunarity, octaves, offset, gain, noise_basis=types.STDPERLIN):
	"""Returns ridged multifractal value from the noise basis at the specified position.

	Parameters:
	position (mathutils.Vector) – The position to evaluate the selected noise function at.
	H (float) – The fractal dimension of the roughest areas.
	lacunarity (float) – The gap between successive frequencies.
	octaves (int) – The number of different noise frequencies used.
	offset (float) – The height of the terrain above ‘sea level’.
	gain (float) – Scaling applied to the values.
	noise_basis (Value in noise.types or int) – The type of noise to be evaluated.
	
	Returns: The ridged multifractal value.

	Return type: float"""
	
	return 1.0
	
def seed_set(seed):
	"""Sets the random seed used for random_unit_vector, random_vector and random.

	Parameters:
	seed (Int) – Seed used for the random generator. When seed is zero, the current time will be used instead."""
	
	pass
	
def turbulence(position, octaves, hard, noise_basis=types.STDPERLIN, amplitude_scale=0.5, frequency_scale=2.0):
	"""Returns the turbulence value from the noise basis at the specified position.

	Parameters:
	position (mathutils.Vector) – The position to evaluate the selected noise function at.
	octaves (int) – The number of different noise frequencies used.
	hard (:boolean) – Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
	noise_basis (Value in mathutils.noise.types or int) – The type of noise to be evaluated.
	amplitude_scale (float) – The amplitude scaling factor.
	frequency_scale (Value in noise.types or int) – The frequency scaling factor
	
	Returns: The turbulence value.

	Return type: float"""
	
	return 1.0
	
def turbulence_vector(position, octaves, hard, noise_basis=types.STDPERLIN, amplitude_scale=0.5, frequency_scale=2.0):
	"""Returns the turbulence vector from the noise basis at the specified position.

	Parameters:
	position (mathutils.Vector) – The position to evaluate the selected noise function at.
	octaves (int) – The number of different noise frequencies used.
	hard (:boolean) – Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
	noise_basis (Value in mathutils.noise.types or int) – The type of noise to be evaluated.
	amplitude_scale (float) – The amplitude scaling factor.
	frequency_scale (Value in noise.types or int) – The frequency scaling factor
	
	Returns: The turbulence vector.

	Return type: mathutils.Vector"""
	
	from . import Vector
	return Vector
	
def variable_lacunarity(position, distortion, noise_type1=types.STDPERLIN, noise_type2=types.STDPERLIN):
	"""Returns variable lacunarity noise value, a distorted variety of noise, from noise type 1 distorted by noise type 2 at the specified position.

	Parameters:	
	position (mathutils.Vector) – The position to evaluate the selected noise function at.
	distortion (float) – The amount of distortion.
	noise_type1 (Value in noise.types or int) – The type of noise to be distorted.
	noise_type2 (Value in noise.types or int) – The type of noise used to distort noise_type1.
	
	Returns: The variable lacunarity noise value.

	Return type: float"""
	
	return 1.0
	
def voronoi(position, distance_metric=distance_metrics.DISTANCE, exponent=2.5):
	"""Returns a list of distances to the four closest features and their locations.

	Parameters:	
	position (mathutils.Vector) – The position to evaluate the selected noise function at.
	distance_metric (Value in noise.distance_metrics or int) – Method of measuring distance.
	exponent (float) – The exponent for Minkowski distance metric.
	
	Returns: A list of distances to the four closest features and their locations.

	Return type: list of four floats, list of four mathutils.Vector types"""
	
	from . import Vector
	return [[1.0, 1.0, 1.0, 1.0], [Vector, Vector, Vector, Vector]]