"""BVHTree Utilities (mathutils.bvhtree)

BVH tree structures for proximity searches and ray casts on geometry."""


class BVHTree:
	
	@classmethod
	def FromBMesh(self, bmesh, epsilon=0.0):
		"""BVH tree based on BMesh data.

		Parameters:	
		bmesh (BMesh) – BMesh data.
		epsilon (float) – Increase the threshold for detecting overlap and raycast hits."""
		
		return self
	
	@classmethod
	def FromObject(self, object, scene, deform=True, render=False, cage=False, epsilon=0.0):
		"""BVH tree based on Object data.

		Parameters:	
		object (Object) – Object data.
		scene (Scene) – Scene data to use for evaluating the mesh.
		deform (bool) – Use mesh with deformations.
		render (bool) – Use render settings.
		cage (bool) – Use render settings.
		epsilon (float) – Increase the threshold for detecting overlap and raycast hits."""
		
		return self
	
	@classmethod
	def FromPolygons(self, vertices, polygons, all_triangles=False, epsilon=0.0):
		"""BVH tree constructed geometry passed in as arguments.

		Parameters:	
		vertices (float triplet sequence) – float triplets each representing (x, y, z)
		polygons (Sequence of sequences containing ints) – Sequence of polyugons, each containing indices to the vertices argument.
		all_triangles (bool) – Use when all polygons are triangles for more efficient conversion.
		epsilon (float) – Increase the threshold for detecting overlap and raycast hits."""
		
		return self
		
	def find_nearest(origin, distance=1.84467e+19):
		"""Find the nearest elements to a point in the distance range.

		Parameters:	
		co (Vector) – Find nearest elements to this point.
		distance (float) – Maximum distance threshold.
		
		Returns: Returns a list of tuples (Vector location, Vector normal, int index, float distance),

		Return type: list"""
		
		from . import Vector
		return [(Vector, Vector, 1, 1.0), (Vector, Vector, 1, 1.0), (Vector, Vector, 1, 1.0), (Vector, Vector, 1, 1.0)]
		
	def find_nearest_range(origin, distance=1.84467e+19):
		"""Find the nearest elements to a point in the distance range.

		Parameters:
		origin (Vector) – Find nearest elements to this point.
		distance (float) – Maximum distance threshold.
		
		Returns: Returns a list of tuples (Vector location, Vector normal, int index, float distance),

		Return type: list"""
		
		from . import Vector
		return [(Vector, Vector, 1, 1.0), (Vector, Vector, 1, 1.0), (Vector, Vector, 1, 1.0), (Vector, Vector, 1, 1.0)]
		
	def overlap(other_tree):
		"""Find overlapping indices between 2 trees.

		Parameters:	other_tree (BVHTree) – Other tree to preform overlap test on.
		
		Returns: Returns a list of unique index pairs, the first index referencing this tree, the second referencing the other_tree.
		
		Return type: list"""
		
		return [1, 1]
		
	def ray_cast(origin, direction, distance):
		"""Cast a ray onto the mesh.

		Parameters:	
		co (Vector) – Start location of the ray in object space.
		direction (Vector) – Direction of the ray in object space.
		distance (float) – Maximum distance threshold.
		
		Returns: Returns a tuple (Vector location, Vector normal, int index, float distance), Values will all be None if no hit is found.

		Return type: tuple"""
		
		from . import Vector
		return (Vector, Vector, 1, 1.0)