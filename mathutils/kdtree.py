"""KDTree Utilities (mathutils.kdtree)

Generic 3-dimentional kd-tree to perform spatial searches."""

class KDTree:
	"""KdTree(size) -> new kd-tree initialized to hold size items.

	Note: KDTree.balance must have been called before using any of the find methods."""
	
	def balance(self):
		"""Balance the tree.

		Note: This builds the entire tree, avoid calling after each insertion."""
		
		pass
		
	def find(self, co, filter=None):
		"""Find nearest point to co.

		Parameters:	
		co (float triplet) - 3d coordinates.
		filter (callable) - function which takes an index and returns True for indices to include in the search.
		
		Returns: Returns (Vector, index, distance).

		Return type: tuple"""
		
		from . import Vector
		return (Vector, 1, 1.0)
		
	def find_n(self, co, n):
		"""Find nearest n points to co.

		Parameters:	
		co (float triplet) - 3d coordinates.
		n (int) - Number of points to find.
		
		Returns: Returns a list of tuples (Vector, index, distance).

		Return type: list"""
		
		from . import Vector
		return [Vector, 1, 1.0]
		
	def find_range(self, co, radius):
		"""Find nearest n points to co.

		Parameters:	
		co (float triplet) - 3d coordinates.
		n (int) - Number of points to find.
		
		Returns: Returns a list of tuples (Vector, index, distance).

		Return type: list"""
		
		from . import Vector
		return [Vector, 1, 1.0]