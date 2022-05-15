"""BVHTree Utilities (mathutils.bvhtree)

BVH tree structures for proximity searches and ray casts on geometry."""


from ..bmesh.types import BMesh as _BMesh
from ..bpy.types import Object as _Object, Scene as _Scene
from ..mathutils import Vector as _Vector


class BVHTree:

    @classmethod
    def FromBMesh(cls, bmesh, epsilon=0.0):
        # type: (_BMesh, float) -> BVHTree
        """BVH tree based on BMesh data.

        Args:
            bmesh (BMesh): BMesh data.
            epsilon (float): Increase the threshold for detecting overlap and raycast hits."""

        pass

    @classmethod
    def FromObject(cls, object, scene, deform=True, render=False, cage=False, epsilon=0.0):
        # type: (_Object, _Scene, bool, bool, bool, float) -> BVHTree
        """BVH tree based on Object data.

        Args:
            object (Object): Object data.
            scene (Scene): Scene data to use for evaluating the mesh.
            deform (bool): Use mesh with deformations.
            render (bool): Use render settings.
            cage (bool): Use render settings.
            epsilon (float): Increase the threshold for detecting overlap and raycast hits."""

        pass

    @classmethod
    def FromPolygons(cls, vertices, polygons, all_triangles=False, epsilon=0.0):
        # type: (list, list, bool, float) -> BVHTree
        """BVH tree constructed geometry passed in as arguments.

        Args:
            vertices (float triplet sequence): float triplets each representing (x, y, z)
            polygons (Sequence of sequences containing ints): Sequence of polyugons, each containing indices to the vertices argument.
            all_triangles (bool): Use when all polygons are triangles for more efficient conversion.
            epsilon (float): Increase the threshold for detecting overlap and raycast hits."""

        pass

    def find_nearest(origin, distance=1.84467):
        # type: (_Vector, float) -> list[tuple[_Vector, _Vector, int, float]]
        """Find the nearest elements to a point in the distance range.

        Args:
            co (Vector): Find nearest elements to this point.
            distance (float): Maximum distance threshold.

        Returns:
            list: Returns a list of tuples (Vector location, Vector normal, int index, float distance)"""

        pass

    def find_nearest_range(origin, distance=1.84467):
        # type: (_Vector, float) -> list[tuple[_Vector, _Vector, int, float]]
        """Find the nearest elements to a point in the distance range.

        Args:
            origin (Vector): Find nearest elements to this point.
            distance (float): Maximum distance threshold.

        Returns:
            list: Returns a list of tuples (Vector location, Vector normal, int index, float distance)"""

        pass

    def overlap(other_tree):
        # type: (BVHTree) -> list[int, int]
        """Find overlapping indices between 2 trees.

        Args:
            other_tree (BVHTree): Other tree to preform overlap test on.

        Returns:
            list: Returns a list of unique index pairs, the first index referencing this tree, the second referencing the other_tree."""

        pass

    def ray_cast(origin, direction, distance):
        # type: (_Vector, _Vector, float) -> tuple[_Vector, _Vector, int, float]
        """Cast a ray onto the mesh.

        Args:
            co (Vector): Start location of the ray in object space.
            direction (Vector): Direction of the ray in object space.
            distance (float): Maximum distance threshold.

        Returns:
            tuple: Returns a tuple (Vector location, Vector normal, int index, float distance), Values will all be None if no hit is found."""

        pass
