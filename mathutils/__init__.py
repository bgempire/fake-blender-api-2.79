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
        self.g = 1.0  # type: float
        self.b = 1.0  # type: float
        self.h = 1.0  # type: float
        self.s = 1.0  # type: float
        self.v = 1.0  # type: float
        self.hsv = [1.0, 1.0, 1.0]  # type: list[float, float, float]
        self.is_frozen = False  # type: bool
        self.is_wrapped = False  # type: bool
        self.owner = self  # type: Color

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
        self.is_wrapped = False  # type: bool
        self.order = "XYZ"  # type: str
        self.owner = self  # type: Euler
        self.x = 1.0  # type: float
        self.y = 1.0  # type: float
        self.z = 1.0  # type: float

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
        self.is_frozen = False  # type: bool
        self.is_negative = False  # type: bool
        self.is_orthogonal = False  # type: bool
        self.is_orthogonal_axis_vectors = False  # type: bool
        self.is_wrapped = False  # type: bool
        self.median_scale = 1.0  # type: float
        self.owner = self  # type: Matrix
        self.row = []  # type: __Sequence[Vector]
        self.translation = Vector()  # type: Vector

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

        self.angle = 1.0
        self.axis = Vector(False)
        self.is_frozen = False
        self.is_wrapped = False
        self.magnitude = 1.0
        self.owner = self
        self.w = 1.0
        self.x = 1.0
        self.y = 1.0
        self.z = 1.0

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

    def to_euler(self, order, euler_compat):
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
	"""This object gives access to Vectors in Blender.

	Parameters:
	seq (sequence of numbers) - Components of the vector, must be a sequence of at least two"""
	
	def __init__(self, seq):
		self.is_frozen = False
		self.is_wrapped = False
		self.length = 1.0
		self.length_squared = 1.0
		self.magnitude = 1.0
		self.owner = self
		self.w = 1.0
		self.x = 1.0
		self.y = 1.0
		self.z = 1.0
		self.ww = self
		self.www = self
		self.wwww = self
		self.wwwx = self
		self.wwwy = self
		self.wwwz = self
		self.wwx = self
		self.wwxw = self
		self.wwxx = self
		self.wwxy = self
		self.wwxz = self
		self.wwy = self
		self.wwyw = self
		self.wwyx = self
		self.wwyy = self
		self.wwyz = self
		self.wwz = self
		self.wwzw = self
		self.wwzx = self
		self.wwzy = self
		self.wwzz = self
		self.wx = self
		self.wxw = self
		self.wxww = self
		self.wxwx = self
		self.wxwy = self
		self.wxwz = self
		self.wxx = self
		self.wxxw = self
		self.wxxx = self
		self.wxxy = self
		self.wxxz = self
		self.wxy = self
		self.wxyw = self
		self.wxyx = self
		self.wxyy = self
		self.wxyz = self
		self.wxz = self
		self.wxzw = self
		self.wxzx = self
		self.wxzy = self
		self.wxzz = self
		self.wy = self
		self.wyw = self
		self.wyww = self
		self.wywx = self
		self.wywy = self
		self.wywz = self
		self.wyx = self
		self.wyxw = self
		self.wyxx = self
		self.wyxy = self
		self.wyxz = self
		self.wyy = self
		self.wyyw = self
		self.wyyx = self
		self.wyyy = self
		self.wyyz = self
		self.wyz = self
		self.wyzw = self
		self.wyzx = self
		self.wyzy = self
		self.wyzz = self
		self.wz = self
		self.wzw = self
		self.wzww = self
		self.wzwx = self
		self.wzwy = self
		self.wzwz = self
		self.wzx = self
		self.wzxw = self
		self.wzxx = self
		self.wzxy = self
		self.wzxz = self
		self.wzy = self
		self.wzyw = self
		self.wzyx = self
		self.wzyy = self
		self.wzyz = self
		self.wzz = self
		self.wzzw = self
		self.wzzx = self
		self.wzzy = self
		self.wzzz = self
		self.xw = self
		self.xww = self
		self.xwww = self
		self.xwwx = self
		self.xwwy = self
		self.xwwz = self
		self.xwx = self
		self.xwxw = self
		self.xwxx = self
		self.xwxy = self
		self.xwxz = self
		self.xwy = self
		self.xwyw = self
		self.xwyx = self
		self.xwyy = self
		self.xwyz = self
		self.xwz = self
		self.xwzw = self
		self.xwzx = self
		self.xwzy = self
		self.xwzz = self
		self.xx = self
		self.xxw = self
		self.xxww = self
		self.xxwx = self
		self.xxwy = self
		self.xxwz = self
		self.xxx = self
		self.xxxw = self
		self.xxxx = self
		self.xxxy = self
		self.xxxz = self
		self.xxy = self
		self.xxyw = self
		self.xxyx = self
		self.xxyy = self
		self.xxyz = self
		self.xxz = self
		self.xxzw = self
		self.xxzx = self
		self.xxzy = self
		self.xxzz = self
		self.xy = self
		self.xyw = self
		self.xyww = self
		self.xywx = self
		self.xywy = self
		self.xywz = self
		self.xyx = self
		self.xyxw = self
		self.xyxx = self
		self.xyxy = self
		self.xyxz = self
		self.xyy = self
		self.xyyw = self
		self.xyyx = self
		self.xyyy = self
		self.xyyz = self
		self.xyz = self
		self.xyzw = self
		self.xyzx = self
		self.xyzy = self
		self.xyzz = self
		self.xz = self
		self.xzw = self
		self.xzww = self
		self.xzwx = self
		self.xzwy = self
		self.xzwz = self
		self.xzx = self
		self.xzxw = self
		self.xzxx = self
		self.xzxy = self
		self.xzxz = self
		self.xzy = self
		self.xzyw = self
		self.xzyx = self
		self.xzyy = self
		self.xzyz = self
		self.xzz = self
		self.xzzw = self
		self.xzzx = self
		self.xzzy = self
		self.xzzz = self
		self.yw = self
		self.yww = self
		self.ywww = self
		self.ywwx = self
		self.ywwy = self
		self.ywwz = self
		self.ywx = self
		self.ywxw = self
		self.ywxx = self
		self.ywxy = self
		self.ywxz = self
		self.ywy = self
		self.ywyw = self
		self.ywyx = self
		self.ywyy = self
		self.ywyz = self
		self.ywz = self
		self.ywzw = self
		self.ywzx = self
		self.ywzy = self
		self.ywzz = self
		self.yx = self
		self.yxw = self
		self.yxww = self
		self.yxwx = self
		self.yxwy = self
		self.yxwz = self
		self.yxx = self
		self.yxxw = self
		self.yxxx = self
		self.yxxy = self
		self.yxxz = self
		self.yxy = self
		self.yxyw = self
		self.yxyx = self
		self.yxyy = self
		self.yxyz = self
		self.yxz = self
		self.yxzw = self
		self.yxzx = self
		self.yxzy = self
		self.yxzz = self
		self.yy = self
		self.yyw = self
		self.yyww = self
		self.yywx = self
		self.yywy = self
		self.yywz = self
		self.yyx = self
		self.yyxw = self
		self.yyxx = self
		self.yyxy = self
		self.yyxz = self
		self.yyy = self
		self.yyyw = self
		self.yyyx = self
		self.yyyy = self
		self.yyyz = self
		self.yyz = self
		self.yyzw = self
		self.yyzx = self
		self.yyzy = self
		self.yyzz = self
		self.yz = self
		self.yzw = self
		self.yzww = self
		self.yzwx = self
		self.yzwy = self
		self.yzwz = self
		self.yzx = self
		self.yzxw = self
		self.yzxx = self
		self.yzxy = self
		self.yzxz = self
		self.yzy = self
		self.yzyw = self
		self.yzyx = self
		self.yzyy = self
		self.yzyz = self
		self.yzz = self
		self.yzzw = self
		self.yzzx = self
		self.yzzy = self
		self.yzzz = self
		self.zw = self
		self.zww = self
		self.zwww = self
		self.zwwx = self
		self.zwwy = self
		self.zwwz = self
		self.zwx = self
		self.zwxw = self
		self.zwxx = self
		self.zwxy = self
		self.zwxz = self
		self.zwy = self
		self.zwyw = self
		self.zwyx = self
		self.zwyy = self
		self.zwyz = self
		self.zwz = self
		self.zwzw = self
		self.zwzx = self
		self.zwzy = self
		self.zwzz = self
		self.zx = self
		self.zxw = self
		self.zxww = self
		self.zxwx = self
		self.zxwy = self
		self.zxwz = self
		self.zxx = self
		self.zxxw = self
		self.zxxx = self
		self.zxxy = self
		self.zxxz = self
		self.zxy = self
		self.zxyw = self
		self.zxyx = self
		self.zxyy = self
		self.zxyz = self
		self.zxz = self
		self.zxzw = self
		self.zxzx = self
		self.zxzy = self
		self.zxzz = self
		self.zy = self
		self.zyw = self
		self.zyww = self
		self.zywx = self
		self.zywy = self
		self.zywz = self
		self.zyx = self
		self.zyxw = self
		self.zyxx = self
		self.zyxy = self
		self.zyxz = self
		self.zyy = self
		self.zyyw = self
		self.zyyx = self
		self.zyyy = self
		self.zyyz = self
		self.zyz = self
		self.zyzw = self
		self.zyzx = self
		self.zyzy = self
		self.zyzz = self
		self.zz = self
		self.zzw = self
		self.zzww = self
		self.zzwx = self
		self.zzwy = self
		self.zzwz = self
		self.zzx = self
		self.zzxw = self
		self.zzxx = self
		self.zzxy = self
		self.zzxz = self
		self.zzy = self
		self.zzyw = self
		self.zzyx = self
		self.zzyy = self
		self.zzyz = self
		self.zzz = self
		self.zzzw = self
		self.zzzx = self
		self.zzzy = self
		self.zzzz = self
		
    def __getitem__(self, item):
        # type: (int) -> float
        pass

    def __setitem__(self, key, value):
        # type: (int, float) -> None
        pass

	@classmethod
	def Fill(self, size, fill=0.0):
		"""Create a vector of length size with all values set to fill.

		Parameters:
		size (int) - The length of the vector to be created.
		fill (float) - The value used to fill the vector."""
		
		return self
		
	@classmethod
	def Linspace(self, start, stop, size):
		"""Create a vector of the specified size which is filled with linearly spaced values between start and stop values.

		Parameters:
		start (int) - The start of the range used to fill the vector.
		stop (int) - The end of the range used to fill the vector.
		size (int) - The size of the vector to be created."""
		
		return self
		
	@classmethod
	def Range(self, start, stop, step=1):
		"""Create a filled with a range of values.

		Parameters:	
		start (int) - The start of the range used to fill the vector.
		stop (int) - The end of the range used to fill the vector.
		step (int) - The step between successive values in the vector."""
		
		return self
		
	@classmethod
	def Repeat(self, vector, size):
		"""Create a vector by repeating the values in vector until the required size is reached.

		Parameters:
		tuple (mathutils.Vector) - The vector to draw values from.
		size (int) - The size of the vector to be created."""
		
		return self
		
	def angle(self, other, fallback=None):
		"""Return the angle between two vectors.

		Parameters:
		other (Vector) - another vector to compare the angle with
		fallback (any) - return this when the angle can't be calculated (zero length vector), (instead of raising a ValueError).
		
		Returns: angle in radians or fallback when given

		Return type: float"""
		
		return 1.0
		
	def angle_signed(self, other, fallback):
		"""Return the signed angle between two 2D vectors (clockwise is positive).

		Parameters:
		other (Vector) - another vector to compare the angle with
		fallback (any) - return this when the angle can't be calculated (zero length vector), (instead of raising a ValueError).
		
		Returns: angle in radians or fallback when given

		Return type: float"""
		
		return 1.0
		
	def copy(self):
		"""Returns a copy of this vector.

		Returns: A copy of the vector.
		
		Return type: Vector
		
		Note: use this to get a copy of a wrapped vector with no reference to the original data."""
		
		return self
		
	def cross(self, other):
		"""Return the cross product of this vector and another.

		Parameters:
		other (Vector) - The other vector to perform the cross product with.
		
		Returns: The cross product.
		
		Return type: Vector or float when 2D vectors are used
		
		Note: both vectors must be 2D or 3D"""
		
		return self
		
	def dot(self, other):
		"""Return the dot product of this vector and another.

		Parameters:
		other (Vector) - The other vector to perform the dot product with.
		
		Returns: The dot product.
		
		Return type: Vector"""
		
		return self
		
	def freeze(self):
		"""Make this object immutable.

		After this the object can be hashed, used in dictionaries & sets.

		Returns: An instance of this object."""
		
		return self
		
	def lerp(self, other, factor):
		"""Returns the interpolation of two vectors.

		Parameters:	
		other (Vector) - value to interpolate with.
		factor (float) - The interpolation value in [0.0, 1.0].
		
		Returns: The interpolated vector.

		Return type: Vector"""
		
		return self
		
	def negate(self):
		"""Set all values to their negative."""
		
		pass
		
	def normalize(self):
		"""Normalize the vector, making the length of the vector always 1.0.

		Warning: Normalizing a vector where all values are zero has no effect.
		
		Note: Normalize works for vectors of all sizes, however 4D Vectors w axis is left untouched."""
		
		pass
		
	def normalized(self):
		"""Return a new, normalized vector.

		Returns: a normalized copy of the vector
		
		Return type: Vector"""
		
		return self
		
	def orthogonal(self):
		"""Return a perpendicular vector.

		Returns: a new vector 90 degrees from this vector.
		
		Return type: Vector
		
		Note: the axis is undefined, only use when any orthogonal vector is acceptable."""
		
		return self
		
	def project(self, other):
		"""Return the projection of this vector onto the other.

		Parameters:
		other (Vector) - second vector.
		
		Returns: the parallel projection vector
		Return type: Vector"""
		
		return self
		
	def reflect(self, mirror):
		"""Return the reflection vector from the mirror argument.

		Parameters:
		mirror (Vector) - This vector could be a normal from the reflecting surface.
		
		Returns: The reflected vector matching the size of this vector.
		
		Return type: Vector"""
		
		return self
		
	def resize(self, size=3):
		"""Resize the vector to have size number of elements."""
		
		pass
		
	def resize_2d(self):
		"""Resize the vector to 2D (x, y)."""
		
		pass
		
	def resize_3d(self):
		"""Resize the vector to 3D (x, y, z)."""
		
		pass
		
	def resize_4d(self):
		"""Resize the vector to 4D (x, y, z, w)."""
		
		pass
		
	def resized(self, size=3):
		"""Return a resized copy of the vector with size number of elements.

		Returns: a new vector
		
		Return type: Vector"""
		
		return self
		
	def rotate(self, other):
		"""Rotate the vector by a rotation value.

		Parameters:
		other (Euler, Quaternion or Matrix) - rotation component of mathutils value"""
		
		pass
		
	def rotation_difference(self, other):
		"""Returns a quaternion representing the rotational difference between this vector and another.

		Parameters:
		other (Vector) - second vector.
		
		Returns: the rotational difference between the two vectors.
		
		Return type: Quaternion
		
		Note: 2D vectors raise an AttributeError."""
		
		return Quaternion
		
	def slerp(self, other, factor, fallback=None):
		"""Returns the interpolation of two non-zero vectors (spherical coordinates).

		Parameters:
		other (Vector) - value to interpolate with.
		factor (float) - The interpolation value typically in [0.0, 1.0].
		fallback (any) - return this when the vector can't be calculated (zero length vector or direct opposites), (instead of raising a ValueError).
		
		Returns: The interpolated vector.

		Return type: Vector"""
		
		return Vector(False)
		
	def to_2d(self):
		"""Return a 2d copy of the vector.

		Returns: a new vector
		
		Return type: Vector"""
		
		return Vector(False)
		
	def to_3d(self):
		"""Return a 3d copy of the vector.

		Returns: a new vector
		Return type: Vector"""
		
		return Vector(False)
		
	def to_4d(self):
		"""Return a 4d copy of the vector.

		Returns: a new vector
		Return type: Vector"""
		
		return Vector(False)
		
	def to_track_quat(self, track, up):
		"""Return a quaternion rotation from the vector and the track and up axis.

		Parameters:
		track (string) - Track axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z'].
		up (string) - Up axis in ['X', 'Y', 'Z'].
		
		Returns: rotation from the vector and the track and up axis.

		Return type: Quaternion"""
		
		return Quaternion(False, False)
		
	def to_tuple(self, precision=-1):
		"""Return this vector as a tuple with.

		Parameters:
		precision (int) - The number to round the value to in [-1, 21].
		
		Returns: the values of the vector rounded by precision
		
		Return type: tuple"""
		
		return (0.0, 0.0, 0.0, 0.0)
		
	def zero(self):
		"""Set all values to zero."""
		
		pass