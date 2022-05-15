"""KDTree Utilities (mathutils.kdtree)

Generic 3-dimentional kd-tree to perform spatial searches."""

from . import Vector as _Vector
from typing import Callable as _Callable


class KDTree:
    """KdTree(size) -> new kd-tree initialized to hold size items.

    Note:
        KDTree.balance must have been called before using any of the find methods."""

    def balance(self):
        # type: () -> None
        """Balance the tree.

        Note:
            This builds the entire tree, avoid calling after each insertion."""

        pass

    def find(self, co, filter=None):
        # type: (list, _Callable) -> tuple[_Vector, int, float]
        """Find nearest point to co.

        Args:
            co (float triplet) - 3d coordinates.
            filter (callable) - function which takes an index and returns True for indices to include in the search.

        Returns:
            tuple: (Vector, index, distance)."""

        pass

    def find_n(self, co, n):
        # type: (list, int) -> tuple[_Vector, int, float]
        """Find nearest n points to co.

        Args:
            co (float triplet) - 3d coordinates.
            n (int) - Number of points to find.

        Returns:
            list: Returns a list of tuples (Vector, index, distance)."""

        pass

    def find_range(self, co, radius):
        # type: (list, float) -> list[tuple[_Vector, int, float]]
        """Find all points within radius of co.

        Args:
            co (float triplet): 3d coordinates.
            radius (float): Distance to search for points.

        Returns:
            list: Returns a list of tuples (Vector, index, distance)."""

        pass

    def insert(self, co, index):
        # type: (list, int) -> None
        """Insert a point into the KDTree.

        Args:
            co (float triplet): Point 3d position.
            index (int): The index of the point."""

        pass
