"""Math Types & Utilities (mathutils)

This module provides access to math operations.

Note:
    - Classes, methods and attributes that accept vectors also accept other numeric sequences, such as tuples, lists.

Submodules:

- Geometry Utilities (mathutils.geometry)
- BVHTree Utilities (mathutils.bvhtree)
- KDTree Utilities (mathutils.kdtree)
- Interpolation Utilities (mathutils.interpolate)
- Noise Utilities (mathutils.noise)

The mathutils module provides the following classes:

- Color
- Euler
- Matrix
- Quaternion
- Vector"""

from . import bvhtree, geometry, interpolate, kdtree, noise
from typing import Sequence as __Sequence, Union as __Union, Any as __Any


class Color:
    """This object gives access to Colors in Blender."""

    def __init__(self, rgb=None):
        # type: (__Sequence[__Union[float, int]]) -> None
        """This object gives access to Colors in Blender.

        Args:
            rgb (__Sequence[float, float, float]): (r, g, b) color values"""

        self.r = 1.0  # type: float
        """Red color channel."""

        self.g = 1.0  # type: float
        """Green color channel."""

        self.b = 1.0  # type: float
        """Blue color channel."""

        self.h = 1.0  # type: float
        """HSV Hue component in [0, 1]."""

        self.s = 1.0  # type: float
        """HSV Saturation component in [0, 1]."""

        self.v = 1.0  # type: float
        """HSV Value component in [0, 1]."""

        self.hsv = [1.0, 1.0, 1.0]  # type: list[float, float, float]
        """HSV Values in [0, 1]."""

        self.is_frozen = False  # type: bool
        """True when this object has been frozen (read-only)."""

        self.is_wrapped = False  # type: bool
        """True when this object wraps external data (read-only)."""

        self.owner = self  # type: Color
        """The item this is wrapping or None (read-only)."""

    def __getitem__(self, item):
        # type: (int) -> float
        pass

    def __setitem__(self, key, value):
        # type: (int, float) -> None
        pass

    def __sub__(self, other):
        # type: (Color) -> Color
        pass

    def __add__(self, other):
        # type: (Color) -> Color
        pass

    def __mul__(self, other):
        # type: (__Union[Color, int, float]) -> Color
        pass

    def __truediv__(self, other):
        # type: (__Union[int, float]) -> Color
        pass

    def copy(self):
        # type: () -> Color
        """Returns a copy of this color.

        Returns:
            Color: A copy of the color."""

        pass

    def freeze(self):
        # type: () -> Color
        """Make this object immutable. After this the object can be hashed, used in dictionaries & sets.

        Returns:
            Color: An instance of this object."""

        pass


class Euler:
    """This object gives access to Eulers in Blender."""

    def __init__(self, angles=None, order="XYZ"):
        # type: (__Sequence[float], str) -> None
        """This object gives access to Eulers in Blender.

        Args:
            angles (__Sequence[float]): Three angles, in radians.
            order (str): Optional order of the angles, a permutation of XYZ."""

        self.is_frozen = False  # type: bool
        """True when this object has been frozen (read-only)."""

        self.is_wrapped = False  # type: bool
        """True when this object wraps external data (read-only)."""

        self.order = "XYZ"  # type: str
        """Euler rotation order."""

        self.owner = self  # type: Euler
        """The item this is wrapping or None (read-only)."""

        self.x = 1.0  # type: float
        """Euler axis angle in radians."""

        self.y = 1.0  # type: float
        """Euler axis angle in radians."""

        self.z = 1.0  # type: float
        """Euler axis angle in radians."""

    def __getitem__(self, item):
        # type: (int) -> float
        pass

    def __setitem__(self, key, value):
        # type: (int, float) -> None
        pass

    def copy(self):
        # type: () -> Euler
        """Returns a copy of this euler.

        Returns:
            Euler: A copy of the euler.

        Note:
            - Use this to get a copy of a wrapped euler with no reference to the original data."""

        pass

    def freeze(self):
        # type: () -> Euler
        """Make this object immutable. After this the object can be hashed, used in dictionaries and sets.

        Returns:
            An instance of this object."""

        pass

    def make_compatible(self, other):
        # type: (Euler) -> None
        """Make this euler compatible with another, so interpolating between them works as intended.

        Args:
            other (Euler): Other Euler to make this compatible with

        Note:
            - The rotation order is not taken into account for this function."""

        pass

    def rotate(self, other):
        # type: (__Union[Euler, Quaternion, Matrix]) -> None
        """Rotates the euler by another mathutils value.

        Args:
            other (__Union[Euler, Quaternion, Matrix]): rotation component of mathutils value"""

        pass

    def rotate_axis(self, axis, angle):
        # type: (str, float) -> None
        """Rotates the euler a certain amount and returning a unique euler rotation (no 720 degree pitches).

        Args:
            axis (str): single character in ['X, 'Y', 'Z'].
            angle (float): angle in radians."""

        pass

    def to_matrix(self):
        # type: () -> Matrix
        """Return a matrix representation of the euler.

        Returns:
            Matrix: A 3x3 roation matrix representation of the euler."""

        pass

    def to_quaternion(self):
        # type: () -> Quaternion
        """Return a quaternion representation of the euler.

        Returns:
            Quaternion: Quaternion representation of the euler."""

        pass

    def zero(self):
        # type: () -> None
        """Set all values to zero."""

        pass


class Matrix:
    """This object gives access to Matrices in Blender, supporting square and rectangular matrices from 2x2 up to 4x4."""

    def __init__(self, rows=None):
        # type: (__Sequence[__Sequence[float]]) -> None
        """This object gives access to Matrices in Blender, supporting square and rectangular matrices from 2x2 up to 4x4.

        Args:
            rows (__Sequence[__Sequence[float]]): Sequence of rows. When ommitted, a 4x4 identity matrix is constructed."""

        self.col = self  # type: Matrix
        """Access the matix by colums, 3x3 and 4x4 only, (read-only)."""

        self.is_frozen = False  # type: bool
        """True when this object has been frozen (read-only)."""

        self.is_negative = False  # type: bool
        """True if this matrix results in a negative scale, 3x3 and 4x4 only, (read-only)."""

        self.is_orthogonal = False  # type: bool
        """True if this matrix is orthogonal, 3x3 and 4x4 only, (read-only)."""

        self.is_orthogonal_axis_vectors = False  # type: bool
        """True if this matrix has got orthogonal axis vectors, 3x3 and 4x4 only, (read-only)."""

        self.is_wrapped = False  # type: bool
        """True when this object wraps external data (read-only)."""

        self.median_scale = 1.0  # type: float
        """The average scale applied to each axis (read-only)."""

        self.owner = self  # type: Matrix
        """The item this is wrapping or None (read-only)."""

        self.row = []  # type: __Sequence[Vector]
        """Access the matix by rows (default), (read-only)."""

        self.translation = Vector()  # type: Vector
        """The translation component of the matrix."""

    def __getitem__(self, item):
        # type: (int) -> Vector
        return self.row[item]

    def __setitem__(self, key, value):
        # type: (int, float) -> None
        pass

    @classmethod
    def Identity(cls, size):
        # type: (int) -> Matrix
        """Create an identity matrix.

        Args:
            size (int): The size of the identity matrix to construct [2, 4].

        Returns:
            Matrix: A new identity matrix."""

        pass

    @classmethod
    def OrthoProjection(cls, axis, size):
        # type: (__Union[str, Vector], int) -> Matrix
        """Create a matrix to represent an orthographic projection.

        Args:
            axis (__Union[str, Vector]): Can be any of the following: ['X', 'Y', 'XY', 'XZ', 'YZ'], where a single axis is for a 2D matrix. Or a vector for an arbitrary axis
            size (int): The size of the projection matrix to construct [2, 4].

        Returns:
            Matrix: A new projection matrix."""

        pass

    @classmethod
    def Rotation(cls, angle, size, axis=None):
        # type: (float, int, __Union[str, Vector]) -> Matrix
        """Create a matrix representing a rotation.

        Args:
            angle (float): The angle of rotation desired, in radians.
            size (int): The size of the rotation matrix to construct [2, 4].
            axis (__Union[str, Vector]): a string in ['X', 'Y', 'Z'] or a 3D Vector Object (optional when size is 2).

        Returns:
            Matrix: A new rotation matrix."""

        pass

    @classmethod
    def Scale(cls, factor, size, axis=None):
        # type: (float, int, Vector) -> Matrix
        """Create a matrix representing a scaling.

        Args:
            factor (float): The factor of scaling to apply.
            size (int): The size of the scale matrix to construct [2, 4].
            axis (Vector): Direction to influence scale. (optional).

        Returns:
            Matrix: A new scale matrix."""

        pass

    @classmethod
    def Shear(cls, plane, size, factor):
        # type: (str, int, __Union[float, __Sequence[float, float]]) -> Matrix
        """Create a matrix to represent an shear transformation.

        Args:
            plane (str): Can be any of the following: ['X', 'Y', 'XY', 'XZ', 'YZ'], where a single axis is for a 2D matrix only.
            size (int): The size of the shear matrix to construct [2, 4].
            factor (__Union[float, __Sequence[float, float]]): The factor of shear to apply. For a 3 or 4 size matrix pass a pair of floats corresponding with the plane axis.

        Returns:
            Matrix: A new shear matrix."""

        pass

    @classmethod
    def Translation(cls, vector):
        # type: (Vector) -> Matrix
        """Create a matrix representing a translation.

        Args:
            vector (Vector): The translation vector.

        Returns:
            Matrix: An identity matrix with a translation."""

        pass

    def adjugate(self):
        # type: () -> None
        """Set the matrix to its adjugate.

        Note:
            - When the matrix cannot be adjugated a ValueError exception is raised."""

        pass

    def adjugated(self):
        # type: () -> Matrix
        """Return an adjugated copy of the matrix.

        Returns:
            Matrix: The adjugated matrix.

        Note:
            - When the matrix cant be adjugated a ValueError exception is raised."""

        pass

    def copy(self):
        # type: () -> Matrix
        """Returns a copy of this matrix.

        Returns:
            Matrix: An instance of itself"""

        pass

    def decompose(self):
        # type: () -> tuple[Vector, Quaternion, Vector]
        """Return the translation, rotation and scale components of this matrix.

        Returns:
            tuple[Vector, Quaternion, Vector]: trans, rot, scale triple."""

        pass

    def determinant(self):
        # type: () -> float
        """Return the determinant of a matrix.

        Returns:
            float: Return the determinant of a matrix."""

        pass

    def freeze(self):
        # type: () -> Matrix
        """Make this object immutable.

        After this the object can be hashed, used in dictionaries & sets.

        Returns:
            Matrix: An instance of this object."""

        pass

    def identity(self):
        # type: () -> None
        """Set the matrix to the identity matrix.

        Note:
            - An object with a location and rotation of zero, and a scale of one will have an identity matrix."""

        pass

    def invert(self, fallback=None):
        # type: (Matrix) -> None
        """Set the matrix to its inverse.

        Args:
            fallback (Matrix): Set the matrix to this value when the inverse cannot be calculated (instead of raising a ValueError exception)."""

        pass

    def invert_safe(self):
        # type: () -> None
        """Set the matrix to its inverse, will never error. If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one. If tweaked matrix is still degenerated, set to the identity matrix instead."""

        pass

    def inverted(self, fallback=None):
        # type: (Matrix) -> Matrix
        """Return an inverted copy of the matrix.

        Args:
            fallback (Matrix): return this when the inverse can't be calculated (instead of raising a ValueError).

        Returns:
            Matrix: The inverted matrix or fallback when given."""

        pass

    def inverted_safe(self):
        # type: () -> Matrix
        """Return an inverted copy of the matrix, will never error. If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one. If tweaked matrix is still degenerated, return the identity matrix instead.

        Returns:
            Matrix: The inverted matrix."""

        pass

    def lerp(self, other, factor):
        # type: (Matrix, float) -> Matrix
        """Returns the interpolation of two matrices.

        Args:
            other (Matrix): value to interpolate with.
            factor (float): The interpolation value in [0.0, 1.0].

        Returns:
            Matrix: The interpolated matrix."""

        pass

    def normalize(self):
        # type: () -> None
        """Normalize each of the matrix columns."""

        pass

    def normalized(self):
        # type: () -> Matrix
        """Return a column normalized matrix

        Returns:
            Matrix: a column normalized matrix"""

        pass

    def resize_4x4(self):
        # type: () -> None
        """Resize the matrix to 4x4."""

        pass

    def rotate(self, other):
        # type: (__Union[Euler, Quaternion, Matrix]) -> None
        """Rotates the matrix by another mathutils value.

        Args:
            other (__Union[Euler, Quaternion, Matrix]): rotation component of mathutils value

        Note:
            - If any of the columns are not unit length this may not have desired results."""

        pass

    def to_3x3(self):
        # type: () -> Matrix
        """Return a 3x3 copy of this matrix.

        Returns:
            Matrix: A new matrix."""

        pass

    def to_4x4(self):
        # type: () -> Matrix
        """Return a 4x4 copy of this matrix.

        Returns:
            Matrix: A new matrix."""

        pass

    def to_euler(self, order="", euler_compat=None):
        # type: (str, Euler) -> Euler
        """Return an Euler representation of the rotation matrix (3x3 or 4x4 matrix only).

        Args:
            order (str): Optional rotation order argument in ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
            euler_compat (Euler): Optional euler argument the new euler will be made compatible with (no axis flipping between them). Useful for converting a series of matrices to animation curves.

        Returns:
            Euler: Euler representation of the matrix."""

        pass

    def to_quaternion(self):
        # type: () -> Quaternion
        """Return a quaternion representation of the rotation matrix.

        Returns:
            Quaternion: Quaternion representation of the rotation matrix."""

        pass

    def to_scale(self):
        # type: () -> Vector
        """Return the scale part of a 3x3 or 4x4 matrix.

        Returns:
            Vector: Return the scale of a matrix.

        Note:
            - This method does not return a negative scale on any axis because it is not possible to obtain this data from the matrix alone."""

        pass

    def to_translation(self):
        # type: () -> Vector
        """Return the translation part of a 4 row matrix.

        Returns:
            Vector: The translation of a matrix."""

        pass

    def transpose(self):
        # type: () -> None
        """Set the matrix to its transpose."""

        pass

    def transposed(self):
        # type: () -> Matrix
        """Return a new, transposed matrix.

        Returns:
            Matrix: A transposed matrix"""

        pass

    def zero(self):
        # type: () -> None
        """Set all the matrix values to zero."""

        pass

    pass


class Quaternion:
    """This object gives access to Quaternions in Blender."""

    def __init__(self, seq=None, angle=None):
        # type: (Vector, float) -> None
        """This object gives access to Quaternions in Blender. The constructor takes arguments in various forms:

        - (), no args - Create an identity quaternion
        - (wxyz) - Create a quaternion from a (w, x, y, z) vector.
        - (exponential_map) - Create a quaternion from a 3d exponential map vector.
        - (axis, angle) - Create a quaternion representing a rotation of angle radians over axis.

        Args:
            seq (Vector): size 3 or 4
            angle (float): rotation angle, in radians"""

        self.angle = 1.0  # type: float
        """Angle of the quaternion."""

        self.axis = Vector()  # type: Vector
        """Quaternion axis as a vector."""

        self.is_frozen = False  # type: bool
        """True when this object has been frozen (read-only)."""

        self.is_wrapped = False  # type: bool
        """True when this object wraps external data (read-only)."""

        self.magnitude = 1.0  # type: float
        """Size of the quaternion (read-only)."""

        self.owner = self  # type: Quaternion
        """The item this is wrapping or None (read-only)."""

        self.w = 1.0  # type: float
        """Quaternion axis value."""

        self.x = 1.0  # type: float
        """Quaternion axis value."""

        self.y = 1.0  # type: float
        """Quaternion axis value."""

        self.z = 1.0  # type: float
        """Quaternion axis value."""

    def __getitem__(self, item):
        # type: (int) -> float
        pass

    def __setitem__(self, key, value):
        # type: (int, float) -> None
        pass

    def conjugate(self):
        # type: () -> None
        """Set the quaternion to its conjugate (negate x, y, z)."""
        pass

    def conjugated(self):
        # type: () -> Quaternion
        """Return a new conjugated quaternion.

        Returns:
            Quaternion: A new quaternion."""

        pass

    def copy(self):
        # type: () -> Quaternion
        """Returns a copy of this quaternion.

        Returns:
            Quaternion: A copy of the quaternion.

        Note:
            Use this to get a copy of a wrapped quaternion with no reference to the original data."""

        pass

    def cross(self, other):
        # type: (Quaternion) -> Quaternion
        """Return the cross product of this quaternion and another.

        Args:
            other (Quaternion): The other quaternion to perform the cross product with.

        Returns:
            Quaternion: The cross product."""

        pass

    def dot(self, other):
        # type: (Quaternion) -> Quaternion
        """Return the dot product of this quaternion and another.

        Args:
            other (Quaternion): The other quaternion to perform the dot product with.

        Returns:
            Quaternion: The dot product."""

        pass

    def freeze(self):
        # type: () -> Quaternion
        """Make this object immutable.

        After this the object can be hashed, used in dictionaries & sets.

        Returns:
            Quaternion: An instance of this object."""

        pass

    def identity(self):
        # type: () -> Quaternion
        """Set the quaternion to an identity quaternion.

        Returns:
            Quaternion: Quaternion as an identity quaternion."""

        pass

    def invert(self):
        # type: () -> Quaternion
        """Return a new, inverted quaternion.

        Returns:
            Quaternion: the inverted value."""

        pass

    def inverted(self):
        # type: () -> Quaternion
        """Return a new, inverted quaternion.

        Returns:
            Quaternion: The inverted value."""

        pass

    def negate(self):
        # type: () -> Quaternion
        """Set the quaternion to its negative.

        Returns:
            Quaternion: Negative quaternion."""

        pass

    def normalize(self):
        # type: () -> None
        """Normalize the quaternion."""

        pass

    def normalized(self):
        # type: () -> Quaternion
        """Return a new normalized quaternion.

        Returns:
            Quaternion: A normalized copy."""

        pass

    def rotate(self, other):
        # type: (__Union[Euler, Quaternion, Matrix]) -> None
        """Rotates the quaternion by another mathutils value.

        Args:
            other (__Union[Euler, Quaternion, Matrix]): rotation component of mathutils value"""

        pass

    def rotation_difference(self, other):
        # type: (Quaternion) -> Quaternion
        """Returns a quaternion representing the rotational difference.

        Args:
            other (Quaternion): second quaternion.

        Returns:
            Quaternion: The rotational difference between the two quat rotations."""

        pass

    def slerp(self, other, factor):
        # type: (Quaternion, float) -> Quaternion
        """Returns the interpolation of two quaternions.

        Args:
            other (Quaternion): value to interpolate with.
            factor (float): The interpolation value in [0.0, 1.0].

        Returns:
            Quaternion: The interpolated rotation."""

        pass

    def to_axis_angle(self):
        # type: () -> tuple[Vector, float]
        """Return the axis, angle representation of the quaternion.

        Returns:
            tuple[Vector, float]: axis, angle."""

        pass

    def to_euler(self, order="", euler_compat=None):
        # type: (str, Euler) -> Euler
        """Return Euler representation of the quaternion.

        Args:
            order (str): Optional rotation order argument in ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
            euler_compat (Euler): Optional euler argument the new euler will be made compatible with (no axis flipping between them). Useful for converting a series of matrices to animation curves.

        Returns:
            Euler: Euler representation of the quaternion."""

        pass

    def to_exponential_map(self):
        # type: () -> Vector
        """Return the exponential map representation of the quaternion. This representation consist of the rotation
        axis multiplied by the rotation angle. Such a representation is useful for interpolation between multiple orientations.

        Returns:
            Vector: Exponential map.

        Note:
            To convert back to a quaternion, pass it to the Quaternion constructor."""

        pass

    def to_matrix(self):
        # type: () -> Matrix
        """Return a matrix representation of the quaternion.

        Returns:
            Matrix: A 3x3 rotation matrix representation of the quaternion."""

        pass


class Vector:
    """This object gives access to Vectors in Blender."""

    def __init__(self, seq=None):
        # type: (__Sequence[float]) -> None
        """This object gives access to Vectors in Blender.

        Args:
            seq (__Sequence[float]): Components of the vector, must be a sequence of at least two"""

        self.is_frozen = False  # type: bool
        """True when this object has been frozen (read-only)."""

        self.is_wrapped = False  # type: bool
        """True when this object wraps external data (read-only)."""

        self.length = 1.0  # type: float
        """Vector Length."""

        self.length_squared = 1.0  # type: float
        """Vector length squared (v.dot(v))."""

        self.magnitude = 1.0  # type: float
        """Vector Length."""

        self.owner = self  # type: Vector
        """The item this is wrapping or None (read-only)."""

        self.w = 1.0  # type: float
        """Vector W axis (4D Vectors only)."""

        self.x = 1.0  # type: float
        """Vector X axis."""

        self.y = 1.0  # type: float
        """Vector Y axis."""

        self.z = 1.0  # type: float
        """Vector Z axis (3D Vectors only)."""

        self.ww = self  # type: Vector
        self.www = self  # type: Vector
        self.wwww = self  # type: Vector
        self.wwwx = self  # type: Vector
        self.wwwy = self  # type: Vector
        self.wwwz = self  # type: Vector
        self.wwx = self  # type: Vector
        self.wwxw = self  # type: Vector
        self.wwxx = self  # type: Vector
        self.wwxy = self  # type: Vector
        self.wwxz = self  # type: Vector
        self.wwy = self  # type: Vector
        self.wwyw = self  # type: Vector
        self.wwyx = self  # type: Vector
        self.wwyy = self  # type: Vector
        self.wwyz = self  # type: Vector
        self.wwz = self  # type: Vector
        self.wwzw = self  # type: Vector
        self.wwzx = self  # type: Vector
        self.wwzy = self  # type: Vector
        self.wwzz = self  # type: Vector
        self.wx = self  # type: Vector
        self.wxw = self  # type: Vector
        self.wxww = self  # type: Vector
        self.wxwx = self  # type: Vector
        self.wxwy = self  # type: Vector
        self.wxwz = self  # type: Vector
        self.wxx = self  # type: Vector
        self.wxxw = self  # type: Vector
        self.wxxx = self  # type: Vector
        self.wxxy = self  # type: Vector
        self.wxxz = self  # type: Vector
        self.wxy = self  # type: Vector
        self.wxyw = self  # type: Vector
        self.wxyx = self  # type: Vector
        self.wxyy = self  # type: Vector
        self.wxyz = self  # type: Vector
        self.wxz = self  # type: Vector
        self.wxzw = self  # type: Vector
        self.wxzx = self  # type: Vector
        self.wxzy = self  # type: Vector
        self.wxzz = self  # type: Vector
        self.wy = self  # type: Vector
        self.wyw = self  # type: Vector
        self.wyww = self  # type: Vector
        self.wywx = self  # type: Vector
        self.wywy = self  # type: Vector
        self.wywz = self  # type: Vector
        self.wyx = self  # type: Vector
        self.wyxw = self  # type: Vector
        self.wyxx = self  # type: Vector
        self.wyxy = self  # type: Vector
        self.wyxz = self  # type: Vector
        self.wyy = self  # type: Vector
        self.wyyw = self  # type: Vector
        self.wyyx = self  # type: Vector
        self.wyyy = self  # type: Vector
        self.wyyz = self  # type: Vector
        self.wyz = self  # type: Vector
        self.wyzw = self  # type: Vector
        self.wyzx = self  # type: Vector
        self.wyzy = self  # type: Vector
        self.wyzz = self  # type: Vector
        self.wz = self  # type: Vector
        self.wzw = self  # type: Vector
        self.wzww = self  # type: Vector
        self.wzwx = self  # type: Vector
        self.wzwy = self  # type: Vector
        self.wzwz = self  # type: Vector
        self.wzx = self  # type: Vector
        self.wzxw = self  # type: Vector
        self.wzxx = self  # type: Vector
        self.wzxy = self  # type: Vector
        self.wzxz = self  # type: Vector
        self.wzy = self  # type: Vector
        self.wzyw = self  # type: Vector
        self.wzyx = self  # type: Vector
        self.wzyy = self  # type: Vector
        self.wzyz = self  # type: Vector
        self.wzz = self  # type: Vector
        self.wzzw = self  # type: Vector
        self.wzzx = self  # type: Vector
        self.wzzy = self  # type: Vector
        self.wzzz = self  # type: Vector
        self.xw = self  # type: Vector
        self.xww = self  # type: Vector
        self.xwww = self  # type: Vector
        self.xwwx = self  # type: Vector
        self.xwwy = self  # type: Vector
        self.xwwz = self  # type: Vector
        self.xwx = self  # type: Vector
        self.xwxw = self  # type: Vector
        self.xwxx = self  # type: Vector
        self.xwxy = self  # type: Vector
        self.xwxz = self  # type: Vector
        self.xwy = self  # type: Vector
        self.xwyw = self  # type: Vector
        self.xwyx = self  # type: Vector
        self.xwyy = self  # type: Vector
        self.xwyz = self  # type: Vector
        self.xwz = self  # type: Vector
        self.xwzw = self  # type: Vector
        self.xwzx = self  # type: Vector
        self.xwzy = self  # type: Vector
        self.xwzz = self  # type: Vector
        self.xx = self  # type: Vector
        self.xxw = self  # type: Vector
        self.xxww = self  # type: Vector
        self.xxwx = self  # type: Vector
        self.xxwy = self  # type: Vector
        self.xxwz = self  # type: Vector
        self.xxx = self  # type: Vector
        self.xxxw = self  # type: Vector
        self.xxxx = self  # type: Vector
        self.xxxy = self  # type: Vector
        self.xxxz = self  # type: Vector
        self.xxy = self  # type: Vector
        self.xxyw = self  # type: Vector
        self.xxyx = self  # type: Vector
        self.xxyy = self  # type: Vector
        self.xxyz = self  # type: Vector
        self.xxz = self  # type: Vector
        self.xxzw = self  # type: Vector
        self.xxzx = self  # type: Vector
        self.xxzy = self  # type: Vector
        self.xxzz = self  # type: Vector
        self.xy = self  # type: Vector
        self.xyw = self  # type: Vector
        self.xyww = self  # type: Vector
        self.xywx = self  # type: Vector
        self.xywy = self  # type: Vector
        self.xywz = self  # type: Vector
        self.xyx = self  # type: Vector
        self.xyxw = self  # type: Vector
        self.xyxx = self  # type: Vector
        self.xyxy = self  # type: Vector
        self.xyxz = self  # type: Vector
        self.xyy = self  # type: Vector
        self.xyyw = self  # type: Vector
        self.xyyx = self  # type: Vector
        self.xyyy = self  # type: Vector
        self.xyyz = self  # type: Vector
        self.xyz = self  # type: Vector
        self.xyzw = self  # type: Vector
        self.xyzx = self  # type: Vector
        self.xyzy = self  # type: Vector
        self.xyzz = self  # type: Vector
        self.xz = self  # type: Vector
        self.xzw = self  # type: Vector
        self.xzww = self  # type: Vector
        self.xzwx = self  # type: Vector
        self.xzwy = self  # type: Vector
        self.xzwz = self  # type: Vector
        self.xzx = self  # type: Vector
        self.xzxw = self  # type: Vector
        self.xzxx = self  # type: Vector
        self.xzxy = self  # type: Vector
        self.xzxz = self  # type: Vector
        self.xzy = self  # type: Vector
        self.xzyw = self  # type: Vector
        self.xzyx = self  # type: Vector
        self.xzyy = self  # type: Vector
        self.xzyz = self  # type: Vector
        self.xzz = self  # type: Vector
        self.xzzw = self  # type: Vector
        self.xzzx = self  # type: Vector
        self.xzzy = self  # type: Vector
        self.xzzz = self  # type: Vector
        self.yw = self  # type: Vector
        self.yww = self  # type: Vector
        self.ywww = self  # type: Vector
        self.ywwx = self  # type: Vector
        self.ywwy = self  # type: Vector
        self.ywwz = self  # type: Vector
        self.ywx = self  # type: Vector
        self.ywxw = self  # type: Vector
        self.ywxx = self  # type: Vector
        self.ywxy = self  # type: Vector
        self.ywxz = self  # type: Vector
        self.ywy = self  # type: Vector
        self.ywyw = self  # type: Vector
        self.ywyx = self  # type: Vector
        self.ywyy = self  # type: Vector
        self.ywyz = self  # type: Vector
        self.ywz = self  # type: Vector
        self.ywzw = self  # type: Vector
        self.ywzx = self  # type: Vector
        self.ywzy = self  # type: Vector
        self.ywzz = self  # type: Vector
        self.yx = self  # type: Vector
        self.yxw = self  # type: Vector
        self.yxww = self  # type: Vector
        self.yxwx = self  # type: Vector
        self.yxwy = self  # type: Vector
        self.yxwz = self  # type: Vector
        self.yxx = self  # type: Vector
        self.yxxw = self  # type: Vector
        self.yxxx = self  # type: Vector
        self.yxxy = self  # type: Vector
        self.yxxz = self  # type: Vector
        self.yxy = self  # type: Vector
        self.yxyw = self  # type: Vector
        self.yxyx = self  # type: Vector
        self.yxyy = self  # type: Vector
        self.yxyz = self  # type: Vector
        self.yxz = self  # type: Vector
        self.yxzw = self  # type: Vector
        self.yxzx = self  # type: Vector
        self.yxzy = self  # type: Vector
        self.yxzz = self  # type: Vector
        self.yy = self  # type: Vector
        self.yyw = self  # type: Vector
        self.yyww = self  # type: Vector
        self.yywx = self  # type: Vector
        self.yywy = self  # type: Vector
        self.yywz = self  # type: Vector
        self.yyx = self  # type: Vector
        self.yyxw = self  # type: Vector
        self.yyxx = self  # type: Vector
        self.yyxy = self  # type: Vector
        self.yyxz = self  # type: Vector
        self.yyy = self  # type: Vector
        self.yyyw = self  # type: Vector
        self.yyyx = self  # type: Vector
        self.yyyy = self  # type: Vector
        self.yyyz = self  # type: Vector
        self.yyz = self  # type: Vector
        self.yyzw = self  # type: Vector
        self.yyzx = self  # type: Vector
        self.yyzy = self  # type: Vector
        self.yyzz = self  # type: Vector
        self.yz = self  # type: Vector
        self.yzw = self  # type: Vector
        self.yzww = self  # type: Vector
        self.yzwx = self  # type: Vector
        self.yzwy = self  # type: Vector
        self.yzwz = self  # type: Vector
        self.yzx = self  # type: Vector
        self.yzxw = self  # type: Vector
        self.yzxx = self  # type: Vector
        self.yzxy = self  # type: Vector
        self.yzxz = self  # type: Vector
        self.yzy = self  # type: Vector
        self.yzyw = self  # type: Vector
        self.yzyx = self  # type: Vector
        self.yzyy = self  # type: Vector
        self.yzyz = self  # type: Vector
        self.yzz = self  # type: Vector
        self.yzzw = self  # type: Vector
        self.yzzx = self  # type: Vector
        self.yzzy = self  # type: Vector
        self.yzzz = self  # type: Vector
        self.zw = self  # type: Vector
        self.zww = self  # type: Vector
        self.zwww = self  # type: Vector
        self.zwwx = self  # type: Vector
        self.zwwy = self  # type: Vector
        self.zwwz = self  # type: Vector
        self.zwx = self  # type: Vector
        self.zwxw = self  # type: Vector
        self.zwxx = self  # type: Vector
        self.zwxy = self  # type: Vector
        self.zwxz = self  # type: Vector
        self.zwy = self  # type: Vector
        self.zwyw = self  # type: Vector
        self.zwyx = self  # type: Vector
        self.zwyy = self  # type: Vector
        self.zwyz = self  # type: Vector
        self.zwz = self  # type: Vector
        self.zwzw = self  # type: Vector
        self.zwzx = self  # type: Vector
        self.zwzy = self  # type: Vector
        self.zwzz = self  # type: Vector
        self.zx = self  # type: Vector
        self.zxw = self  # type: Vector
        self.zxww = self  # type: Vector
        self.zxwx = self  # type: Vector
        self.zxwy = self  # type: Vector
        self.zxwz = self  # type: Vector
        self.zxx = self  # type: Vector
        self.zxxw = self  # type: Vector
        self.zxxx = self  # type: Vector
        self.zxxy = self  # type: Vector
        self.zxxz = self  # type: Vector
        self.zxy = self  # type: Vector
        self.zxyw = self  # type: Vector
        self.zxyx = self  # type: Vector
        self.zxyy = self  # type: Vector
        self.zxyz = self  # type: Vector
        self.zxz = self  # type: Vector
        self.zxzw = self  # type: Vector
        self.zxzx = self  # type: Vector
        self.zxzy = self  # type: Vector
        self.zxzz = self  # type: Vector
        self.zy = self  # type: Vector
        self.zyw = self  # type: Vector
        self.zyww = self  # type: Vector
        self.zywx = self  # type: Vector
        self.zywy = self  # type: Vector
        self.zywz = self  # type: Vector
        self.zyx = self  # type: Vector
        self.zyxw = self  # type: Vector
        self.zyxx = self  # type: Vector
        self.zyxy = self  # type: Vector
        self.zyxz = self  # type: Vector
        self.zyy = self  # type: Vector
        self.zyyw = self  # type: Vector
        self.zyyx = self  # type: Vector
        self.zyyy = self  # type: Vector
        self.zyyz = self  # type: Vector
        self.zyz = self  # type: Vector
        self.zyzw = self  # type: Vector
        self.zyzx = self  # type: Vector
        self.zyzy = self  # type: Vector
        self.zyzz = self  # type: Vector
        self.zz = self  # type: Vector
        self.zzw = self  # type: Vector
        self.zzww = self  # type: Vector
        self.zzwx = self  # type: Vector
        self.zzwy = self  # type: Vector
        self.zzwz = self  # type: Vector
        self.zzx = self  # type: Vector
        self.zzxw = self  # type: Vector
        self.zzxx = self  # type: Vector
        self.zzxy = self  # type: Vector
        self.zzxz = self  # type: Vector
        self.zzy = self  # type: Vector
        self.zzyw = self  # type: Vector
        self.zzyx = self  # type: Vector
        self.zzyy = self  # type: Vector
        self.zzyz = self  # type: Vector
        self.zzz = self  # type: Vector
        self.zzzw = self  # type: Vector
        self.zzzx = self  # type: Vector
        self.zzzy = self  # type: Vector
        self.zzzz = self  # type: Vector

    def __getitem__(self, item):
        # type: (int) -> float
        pass

    def __setitem__(self, key, value):
        # type: (int, float) -> None
        pass

    @classmethod
    def Fill(cls, size, fill=0.0):
        # type: (int, float) -> Vector
        """Create a vector of length size with all values set to fill.

        Args:
            size (int): The length of the vector to be created.
            fill (float): The value used to fill the vector."""

        pass

    @classmethod
    def Linspace(cls, start, stop, size):
        # type: (int, int, int) -> Vector
        """Create a vector of the specified size which is filled with linearly spaced values between start and stop values.

        Args:
            start (int): The start of the range used to fill the vector.
            stop (int): The end of the range used to fill the vector.
            size (int): The size of the vector to be created."""

        pass

    @classmethod
    def Range(cls, start, stop, step=1):
        # type: (int, int, int) -> Vector
        """Create a filled with a range of values.

        Args:
            start (int): The start of the range used to fill the vector.
            stop (int): The end of the range used to fill the vector.
            step (int): The step between successive values in the vector."""

        pass

    @classmethod
    def Repeat(cls, vector, size):
        # type: (Vector, int) -> Vector
        """Create a vector by repeating the values in vector until the required size is reached.

        Args:
            vector (Vector): The vector to draw values from.
            size (int): The size of the vector to be created.

        Returns:
            Vector: Created vector"""

        pass

    def angle(self, other, fallback=None):
        # type: (Vector, __Any) -> float
        """Return the angle between two vectors.

        Args:
            other (Vector): another vector to compare the angle with
            fallback (__Any): return this when the angle can't be calculated (zero length vector), (instead of raising a ValueError).

        Returns:
            float: Angle in radians or fallback when given"""

        pass

    def angle_signed(self, other, fallback=None):
        # type: (Vector, __Any) -> float
        """Return the signed angle between two 2D vectors (clockwise is positive).

        Args:
            other (Vector): another vector to compare the angle with
            fallback (__Any): return this when the angle can't be calculated (zero length vector), (instead of raising a ValueError).

        Returns:
            float: Angle in radians or fallback when given"""

        pass

    def copy(self):
        # type: () -> Vector
        """Returns a copy of this vector.

        Returns:
            Vector: A copy of the vector.

        Note:
            Use this to get a copy of a wrapped vector with no reference to the original data."""

        pass

    def cross(self, other):
        # type: (Vector) -> Vector
        """Return the cross product of this vector and another.

        Args:
            other (Vector): The other vector to perform the cross product with.

        Returns:
            Vector: The cross product. Returns Vector, or float when 2D vectors are used.

        Note:
            Both vectors must be 2D or 3D"""

        pass

    def dot(self, other):
        # type: (Vector) -> Vector
        """Return the dot product of this vector and another.

        Args:
            other (Vector): The other vector to perform the dot product with.

        Returns:
            Vector: The dot product."""

        pass

    def freeze(self):
        # type: () -> Vector
        """Make this object immutable.

        After this the object can be hashed, used in dictionaries & sets.

        Returns:
            Vector: An instance of this object."""

        pass

    def lerp(self, other, factor):
        # type: (Vector, float) -> Vector
        """Returns the interpolation of two vectors.

        Args:
            other (Vector): value to interpolate with.
            factor (float): The interpolation value in [0.0, 1.0].

        Returns:
            Vector: The interpolated vector."""

        pass

    def negate(self):
        # type: () -> None
        """Set all values to their negative."""

        pass

    def normalize(self):
        # type: () -> None
        """Normalize the vector, making the length of the vector always 1.0.

        Note:
            - Normalize works for vectors of all sizes, however 4D Vectors w axis is left untouched.
            - Normalizing a vector where all values are zero has no effect."""

        pass

    def normalized(self):
        # type: () -> Vector
        """Return a new, normalized vector.

        Returns:
            Vector: A normalized copy of the vector"""

        pass

    def orthogonal(self):
        # type: () -> Vector
        """Return a perpendicular vector.

        Returns:
            Vector: A new vector 90 degrees from this vector.

        Note:
            - The axis is undefined, only use when any orthogonal vector is acceptable."""

        pass

    def project(self, other):
        # type: (Vector) -> Vector
        """Return the projection of this vector onto the other.

        Args:
            other (Vector): second vector.

        Returns:
            Vector: The parallel projection vector"""

        pass

    def reflect(self, mirror):
        # type: (Vector) -> Vector
        """Return the reflection vector from the mirror argument.

        Args:
            mirror (Vector): This vector could be a normal from the reflecting surface.

        Returns:
            Vector: The reflected vector matching the size of this vector."""

        pass

    def resize(self, size=3):
        # type: (int) -> None
        """Resize the vector to have size number of elements.

        Args:
            size (int): New vector size (optional)"""

        pass

    def resize_2d(self):
        # type: () -> None
        """Resize the vector to 2D (x, y)."""

        pass

    def resize_3d(self):
        # type: () -> None
        """Resize the vector to 3D (x, y, z)."""

        pass

    def resize_4d(self):
        # type: () -> None
        """Resize the vector to 4D (x, y, z, w)."""

        pass

    def resized(self, size=3):
        # type: (int) -> Vector
        """Return a resized copy of the vector with size number of elements.

        Args:
            size (int): New vector size (optional)

        Returns:
            Vector: A new vector"""

        pass

    def rotate(self, other):
        # type: (__Union[Euler, Quaternion, Matrix]) -> None
        """Rotate the vector by a rotation value.

        Args:
            other (__Union[Euler, Quaternion, Matrix]): rotation component of mathutils value"""

        pass

    def rotation_difference(self, other):
        # type: (Vector) -> Quaternion
        """Returns a quaternion representing the rotational difference between this vector and another.

        Args:
            other (Vector): second vector.

        Returns:
            Quaternion: The rotational difference between the two vectors.

        Note:
            - 2D vectors raise an AttributeError."""

        pass

    def slerp(self, other, factor, fallback=None):
        # type: (Vector, float, __Any) -> Vector
        """Returns the interpolation of two non-zero vectors (spherical coordinates).

        Args:
            other (Vector): value to interpolate with.
            factor (float): The interpolation value typically in [0.0, 1.0].
            fallback (__Any): return this when the vector can't be calculated (zero length vector or direct opposites), (instead of raising a ValueError).

        Returns:
            Vector: The interpolated vector."""

        pass

    def to_2d(self):
        # type: () -> Vector
        """Return a 2d copy of the vector.

        Returns:
            Vector: A new vector"""

        pass

    def to_3d(self):
        # type: () -> Vector
        """Return a 3d copy of the vector.

        Returns:
            Vector: A new vector"""

        pass

    def to_4d(self):
        # type: () -> Vector
        """Return a 4d copy of the vector.

        Returns:
            Vector: A new vector"""

        pass

    def to_track_quat(self, track, up):
        # type: (str, str) -> Quaternion
        """Return a quaternion rotation from the vector and the track and up axis.

        Args:
            track (str): Track axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z'].
            up (str): Up axis in ['X', 'Y', 'Z'].

        Returns:
            Quaternion: Rotation from the vector and the track and up axis."""

        pass

    def to_tuple(self, precision=-1):
        # type: (int) -> tuple[float]
        """Return this vector as a tuple with.

        Args:
            precision (int): The number to round the value to in [-1, 21].

        Returns:
            tuple[float]: the values of the vector rounded by precision"""

        pass

    def zero(self):
        # type: () -> None
        """Set all values to zero."""

        pass
