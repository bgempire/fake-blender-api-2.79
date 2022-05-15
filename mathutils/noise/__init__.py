from . import types
from .. import Vector as _Vector


def cell(position):
    # type: (_Vector) -> float
    """Returns cell noise value at the specified position.

    Args:
        position (Vector): The position to evaluate the selected noise function at.

    Returns:
        float: The cell noise value."""

    pass


def cell_vector(position):
    # type: (_Vector) -> _Vector
    """Returns cell noise vector at the specified position.

    Args:
        position (Vector): The position to evaluate the selected noise function at.

    Returns:
        Vector: The cell noise vector."""

    pass


def fractal(position, H, lacunarity, octaves, noise_basis = types.STDPERLIN):
    # type: (_Vector, float, float, int, int) -> float
    """Returns the fractal Brownian motion (fBm) noise value from the noise basis at the specified position.

    Args:
        position (Vector): The position to evaluate the selected noise function at.
        H (float): The fractal increment factor.
        lacunarity (float): The gap between successive frequencies.
        octaves (int): The number of different noise frequencies used.
        noise_basis (int): The type of noise to be evaluated.

    Returns:
        float: The fractal Brownian motion noise value."""

    pass


def hetero_terrain(position, H, lacunarity, octaves, offset, noise_basis = types.STDPERLIN):
    # type: (_Vector, float, float, int, float, int) -> float
    """Returns the heterogeneous terrain value from the noise basis at the specified position.

    Args:
        position (Vector): The position to evaluate the selected noise function at.
        H (float): The fractal dimension of the roughest areas.
        lacunarity (float): The gap between successive frequencies.
        octaves (int): The number of different noise frequencies used.
        offset (float): The height of the terrain above 'sea level'.
        noise_basis (int): The type of noise to be evaluated.

    Returns:
        float: The heterogeneous terrain value."""

    pass


def hybrid_multi_fractal(position, H, lacunarity, octaves, offset, gain, noise_basis = types.STDPERLIN):
    # type: (_Vector, float, float, int, float, float, int) -> float
    """Returns hybrid multifractal value from the noise basis at the specified position.

    Args:
        position (Vector): The position to evaluate the selected noise function at.
        H (float): The fractal dimension of the roughest areas.
        lacunarity (float): The gap between successive frequencies.
        octaves (int): The number of different noise frequencies used.
        offset (float): The height of the terrain above 'sea level'.
        gain (float): Scaling applied to the values.
        noise_basis (int): The type of noise to be evaluated.

    Returns:
        float: The hybrid multifractal value."""

    pass


def multi_fractal(position, H, lacunarity, octaves, noise_basis = types.STDPERLIN):
    # type: (_Vector, float, float, int, int) -> float
    """Returns multifractal noise value from the noise basis at the specified position.

    Args:
        position (Vector): The position to evaluate the selected noise function at.
        H (float): The fractal increment factor.
        lacunarity (float): The gap between successive frequencies.
        octaves (int): The number of different noise frequencies used.
        noise_basis (int): The type of noise to be evaluated.

    Returns:
        float: The multifractal noise value."""

    pass


def noise(position, noise_basis = types.STDPERLIN):
    # type: (_Vector, int) -> float
    """Returns noise value from the noise basis at the position specified.

    Args:
        position (Vector): The position to evaluate the selected noise function at.
        noise_basis (int): The type of noise to be evaluated.

    Returns:
        float: The noise value."""

    pass


def noise_vector(position, noise_basis = types.STDPERLIN):
    # type: (_Vector, int) -> _Vector
    """Returns the noise vector from the noise basis at the specified position.

    Args:
        position (Vector): The position to evaluate the selected noise function at.
        noise_basis (int): The type of noise to be evaluated.

    Returns:
        Vector: The noise vector."""

    pass


def random() -> float:
    # type: () -> float
    """Returns a random number in the range [0, 1].

    Returns:
        float: The random number."""

    pass


def random_unit_vector(size = 3):
    # type: (int) -> _Vector
    """Returns a unit vector with random entries.

    Args:
        size (int): The size of the vector to be produced.

    Returns:
        Vector: The random unit vector."""

    pass


def ridged_multi_fractal(position, H, lacunarity, octaves, offset, gain, noise_basis = types.STDPERLIN):
    # type: (_Vector, float, float, int, float, float, int) -> float
    """Returns ridged multifractal value from the noise basis at the specified position.

    Args:
        position (Vector): The position to evaluate the selected noise function at.
        H (float): The fractal dimension of the roughest areas.
        lacunarity (float): The gap between successive frequencies.
        octaves (int): The number of different noise frequencies used.
        offset (float): The height of the terrain above 'sea level'.
        gain (float): Scaling applied to the values.
        noise_basis (int): The type of noise to be evaluated.

    Returns:
        float: The ridged multifractal value."""

    pass


def seed_set(seed):
    # type: (int) -> None
    """Sets the random seed used for random_unit_vector, random_vector and random.

    Args:
        seed (int): Seed used for the random generator. When seed is zero, the current time will be used instead."""

    pass


def turbulence(position, octaves, hard, noise_basis = types.STDPERLIN, amplitude_scale = 0.5, frequency_scale = 2.0):
    # type: (_Vector, int, bool, int, float, float) -> float
    """Returns the turbulence value from the noise basis at the specified position.

    Args:
        position (Vector): The position to evaluate the selected noise function at.
        octaves (int): The number of different noise frequencies used.
        hard (bool): Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
        noise_basis (int): The type of noise to be evaluated.
        amplitude_scale (float): The amplitude scaling factor.
        frequency_scale (float): The frequency scaling factor

    Returns:
        float: The turbulence value."""

    pass


def turbulence_vector(position, octaves, hard, noise_basis = types.STDPERLIN, amplitude_scale = 0.5, frequency_scale = 2.0):
    # type: (_Vector, int, bool, int, float, float) -> _Vector
    """Returns the turbulence vector from the noise basis at the specified position.

    Args:
        position (Vector): The position to evaluate the selected noise function at.
        octaves (int): The number of different noise frequencies used.
        hard (bool): Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
        noise_basis (int): The type of noise to be evaluated.
        amplitude_scale (float): The amplitude scaling factor.
        frequency_scale (float): The frequency scaling factor

    Returns:
        Vector: The turbulence vector."""

    pass


def variable_lacunarity(position, distortion, noise_type1 = types.STDPERLIN, noise_type2 = types.STDPERLIN):
    # type: (_Vector, float, int, int) -> float
    """Returns variable lacunarity noise value, a distorted variety of noise, from noise type 1 distorted by noise type 2 at the specified position.

    Args:
        position (Vector): The position to evaluate the selected noise function at.
        distortion (float): The amount of distortion.
        noise_type1 (int): The type of noise to be distorted.
        noise_type2 (int): The type of noise used to distort noise_type1.

    Returns:
        float: The variable lacunarity noise value."""

    pass


def voronoi(position, distance_metric, exponent = 2.5):
    # type: (_Vector, int, float) -> list[_Vector]
    """Returns a list of distances to the four closest features and their locations.

    Args:
        position (Vector): The position to evaluate the selected noise function at.
        distance_metric (int): Method of measuring distance.
        exponent (float): The exponent for Minkowski distance metric.

    Returns:
        list: A list of distances to the four closest features and their locations."""

    pass
