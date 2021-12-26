
class IDPropertyArray:
	
	def __init__(self):
		self.typecode = 'f'
	
	def to_list(self):
		"""Return the array as a list."""
		
		return []
		
class IDPropertyGroup:
	
	def __init__(self):
		self.name = ""
	
	def clear(self):
		"""Clear all members from this group."""
		
		pass
	
	def get(self, key, default=None):
		"""Return the value for key, if it exists, else default."""
		
		pass
	
	def items(self):
		"""Return the items associated with this group."""
		
		pass
	
	def iteritems(self):
		"""Iterate through the items in the dict; behaves like dictionary method iteritems."""
		
		pass
	
	def keys(self):
		"""Return the keys associated with this group as a list of strings."""
		
		pass
	
	def pop(self, key):
		"""Remove an item from the group, returning a Python representation.

		Raises: KeyError - When the item doesn't exist.
		
		Parameters:
		key (string) - Name of item to remove."""
		
		pass
	
	def to_dict(self):
		"""Return a purely python version of the group."""
		
		return {}
	
	def update(self, other):
		"""Update key, values.

		Parameters:
		other (IDPropertyGroup or dict) - Updates the values in the group with this."""
		
		pass
	
	def values(self):
		"""Return the values associated with this group."""
		
		pass
		
class IDPropertyGroupIter:
	pass