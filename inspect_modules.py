import inspect
import importlib

MODULES = [
	# "aud",
	# "bge.app",
	# "bge.constraints",
	# "bge.events",
	"bge.logic",
	# "bge.render",
	# "bge.texture",
	"bge.types",
	# "mathutils",
	# "mathutils.noise",
]

def inspectModule(moduleName):
	
	_module = None
	
	try:
		_module = importlib.import_module(moduleName)
		print("\n> Imported module:", moduleName)
		
	except:
		print("\nX Could not import", moduleName)
		return

	finalString = "### MODULE: " + moduleName + " ###\n\n"
	functionsString = ""
	attributesString = ""
	classesString = "\n# Classes\n"
	functions = []
	attributes = []

	# Iterate over module attribute names
	for _attr1Name in dir(_module):

		if _attr1Name[0] != '_':

			# Get string in format 'module.attribute'
			attributePath = _module.__name__ + "." + _attr1Name
			_attr1 = eval("_module." + _attr1Name)

			# Append functions to list
			if inspect.isfunction(_attr1):
				functions.append([_attr1Name, _attr1])

			# Build string for classes
			elif inspect.isclass(_attr1):
				
				# Main class variables
				members = []
				methods = []
				
				# Add class name
				classesString += attributePath + "\n"
				_instance = None
				
				# Get the class constructor arguments and instance it
				if "__init__" in dir(_attr1):
					_init_args = inspect.getfullargspec(_attr1.__init__).args
					_init_args = ['"' + arg + '"' for arg in _init_args if arg != "self"]
					_init_args = ", ".join(_init_args)
					_instance = eval("_attr1(" + _init_args + ")")
					
				# Iterate over instance members
				for _attr2Name in dir(_instance):
					if _attr2Name[0] != '_':
						
						# Get the literal member of the instance
						_attr2 = eval("_instance." + _attr2Name)
						
						# Append attribute member to attributes
						if _attr2Name[0] != '_' and not inspect.isfunction(_attr2) and not inspect.ismethod(_attr2):
							members.append([_attr2Name, _attr2])
							
						# Append method member to methods
						else:
							methods.append([_attr2Name, _attr2])
							
				# Build attributes string based on the list attributes
				members.sort()
				classesString += "\n\t# Attributes:\n" if members else ""
				for attr in members:
					classesString += "\t" + attr[0] + " = " + str(type(attr[1])) + "\n"

				# Build methods string based on the list methods
				methods.sort()
				classesString += "\n\t# Methods:\n" if methods else ""
				
				# Get method arg names and set default values for the incoming call
				for meth in methods:
					returnValue = None
					argNames = ""
					argValues = ""
					args = inspect.getfullargspec(meth[1]).args
					
					for _arg in args:
						if _arg != "self":
							argNames += _arg
							argValues += "None"
							
							if args.index(_arg) < len(args) - 1:
								argNames += ", "
								argValues += ", "
						
					# Call method to retrieve the return value		
					returnValue = eval("meth[1](" + argValues + ")")
					
					# Adds to the class string the built method representation
					classesString += "\t" + meth[0] + "(" + argNames + ") -> " + str(type(returnValue)) + "\n"

				classesString += "\n"
				
			# Append module attribute to attributes list
			elif not inspect.ismodule(_attr1):
				attributes.append([_attr1Name, _attr1])
			
	# Build the functions string	
	functions.sort()
	functionsString += "# Functions:\n" if functions else ""
	
	# Get function arg names and set default values for the incoming call
	for func in functions:
		returnValue = None
		argNames = ""
		argValues = ""
		args = inspect.getfullargspec(func[1]).args
		
		for _arg in args:
			if _arg != "self":
				argNames += _arg
				argValues += "None"
				
				if args.index(_arg) < len(args) - 1:
					argNames += ", "
					argValues += ", "
					
		# Call function to retrieve the return value
		returnValue = eval("func[1](" + argValues + ")")

		# Adds to the function string the built function representation
		functionsString += func[0] + "(" + argNames + ") -> " + str(type(returnValue)) + "\n"		
	
	# Build the module attributes string
	attributes.sort()
	attributesString += "\n# Attributes:\n" if attributes else ""
	for attr in attributes:
		attributesString += attr[0] + " = " + str(attr[1]) + "\n"
	
	# Build the final string based on the build strings
	finalString += functionsString + attributesString + classesString
	
	with open("result_" + moduleName + ".txt", "w") as openedFile:
		openedFile.write(finalString)
		print("Introspection results saved to:", openedFile.name)
		
for _mod in MODULES: inspectModule(_mod)