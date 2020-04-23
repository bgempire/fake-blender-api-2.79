"""This module contains the classes that appear as instances in the Game Engine. A script must interact with these classes if it is to affect the behaviour of objects in a game."""

class PyObjectPlus:
	
	"""class bge.PyObjectPlus

	PyObjectPlus base class of most other types in the Game Engine."""

	def __init__(self):
		self.invalid = True

class CValue(PyObjectPlus):
	
	"""base class - PyObjectPlus

	class bge.CValue(PyObjectPlus)

	This class is a basis for other classes."""

	def __init__(self):
		self.name = "str"

class CPropValue(CValue):
	
	"""base class - CValue

	class bge.CPropValue(CValue)
	This class has no python functions"""
	
	pass

class CListValue(CPropValue):
	
	"""base class - CPropValue

	class bge.CListValue(CPropValue)

	This is a list like object used in the game engine internally that behaves similar to a python list in most ways.

	As well as the normal index lookup (val= clist[i]), CListValue supports string lookups (val= scene.objects["Cube"])

	Other operations such as len(clist), list(clist), clist[0:10] are also supported."""
	
	def append():
		"""Add an item to the list (like pythons append)

		Warning: Appending values to the list can cause crashes when the list is used internally by the game engine."""
		pass
		
	def count():
		"""Count the number of instances of a value in the list.

		Returns:	
		number of instances

		Return type:
		integer"""
		return 0
		
	def index():
		"""Return the index of a value in the list.

		Returns:
		The index of the value in the list.

		Return type:
		integer"""
		return 0
		
	def reverse():
		"""Reverse the order of the list."""
		pass
		
	def get():
		"""Return the value matching key, or the default value if its not found.

		Returns:	
		The key value or a default."""
		pass
		
	def from_id():
		"""This is a funtion especially for the game engine to return a value with a spesific id.

		Since object names are not always unique, the id of an object can be used to get an object from the CValueList."""
		pass
		
	pass

class SCA_IObject(CValue):
	
	"""base class - CValue

	class bge.SCA_IObject(CValue)

	This class has no python functions"""

	pass

class KX_GameObject(SCA_IObject):
	
	"""base class - SCA_IObject

	class bge.KX_GameObject(SCA_IObject)

	All game objects are derived from this class.

	Properties assigned to game objects are accessible as attributes of this class.

	Note: Calling ANY method or attribute on an object that has been removed from a scene will raise a SystemError, if an object may have been removed since last accessing it use the invalid attribute to check.

	KX_GameObject can be subclassed to extend functionality."""
	
	def __init__(self):
		self.parent = KX_GameObject
		self.groupMembers = CListValue
		self.groupObject = KX_GameObject
		self.scene = KX_Scene
		self.children = CListValue
		self.childrenRecursive = CListValue
		self.name = "str"
		self.mass = 0.0
		self.isSuspendedDynamics = True
		self.linearDamping = 0.0
		self.angularDamping = 0.0
		self.linVelocityMin = 0.0
		self.linVelocityMax = 0.0
		self.angularVelocityMin = 0.0
		self.angularVelocityMax = 0.0
		self.localInertia = ((0.0,0.0,0.0))
		self.collisionGroup = 0
		self.collisionMask = 0
		self.collisionCallbacks = []
		self.visible = True
		self.record_animation = True
		self.color = [0,0,0,255]
		self.occlusion = True
		self.position = [0.0,0.0,0.0]
		self.orientation = [0.0,0.0,0.0]
		self.scaling = [0.0,0.0,0.0]
		self.localOrientation = ([0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0])
		self.worldOrientation = ([0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0])
		self.localScale = [0.0,0.0,0.0]
		self.worldScale = [0.0,0.0,0.0]
		self.localPosition = [0.0,0.0,0.0]
		self.worldPosition = [0.0,0.0,0.0]
		self.localTransform = ([0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0])
		self.worldTransform = ([0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0])
		self.localLinearVelocity = [0.0,0.0,0.0]
		self.worldLinearVelocity = [0.0,0.0,0.0]
		self.localAngularVelocity = [0.0,0.0,0.0]
		self.worldAngularVelocity = [0.0,0.0,0.0]
		self.timeOffset = 0.0
		self.state = 0
		self.meshes = []
		self.sensors = []
		self.controllers = []
		self.actuators = []
		self.attrDict = {}
		self.life = 0.0
		self.debug = True
		self.debugRecursive = True
		self.currentLodLevel = 0
		self.maxJumps = 0
		
	def endObject():
		"""Delete this object, can be used in place of the EndObject Actuator.

		The actual removal of the object from the scene is delayed."""
		pass
		
	def replaceMesh(mesh, useDisplayMesh=True, usePhysicsMesh=False):
		"""Replace the mesh of this object with a new mesh. This works the same was as the actuator.

		Parameters:
		mesh (MeshProxy or string) - mesh to replace or the meshes name.
		useDisplayMesh (boolean) - when enabled the display mesh will be replaced (optional argument).
		usePhysicsMesh (boolean) - when enabled the physics mesh will be replaced (optional argument)."""
		pass
		
	def setVisible(visible, recursive=False):
		"""Sets the game object's visible flag.

		Parameters:
		visible (boolean) - the visible state to set.
		recursive (boolean) - optional argument to set all childrens visibility flag too."""
		pass
		
	def setOcclusion(occlusion, recursive=False):
		"""Sets the game object's occlusion capability.

		Parameters:
		occlusion (boolean) - the state to set the occlusion to.
		recursive (boolean) - optional argument to set all childrens occlusion flag too."""
		pass
		
	def alignAxisToVect(vect, axis=2, factor=1.0):
		"""Aligns any of the game object's axis along the given vector.

		Parameters:
		vect (3D vector) - a vector to align the axis.
		axis (integer) -
		The axis you want to align
		0: X axis
		1: Y axis
		2: Z axis
		factor (float) - Only rotate a feaction of the distance to the target vector (0.0 - 1.0)"""
		pass
		
	def getAxisVect(vect):
		"""Returns the axis vector rotates by the objects worldspace orientation. This is the equivalent of multiplying the vector by the orientation matrix.

		Parameters:
		vect (3D Vector) - a vector to align the axis.

		Returns:	
		The vector in relation to the objects rotation.

		Return type:
		3d vector."""
		return [0.0,0.0,0.0]
		
	def applyMovement(movement, local=False):
		"""Sets the game object's movement.

		Parameters:
		movement (3D Vector) - movement vector.
		local -
		False: you get the "global" movement ie: relative to world orientation.
		True: you get the "local" movement ie: relative to object orientation.
		local - boolean"""
		pass
		
	def applyRotation(rotation, local=False):
		"""Sets the game object's rotation.

		Parameters:
		rotation (3D Vector) - rotation vector.
		local -
		False: you get the "global" rotation ie: relative to world orientation.
		True: you get the "local" rotation ie: relative to object orientation.
		local - boolean"""
		pass
		
	def applyForce(force, local=False):
		"""Sets the game object's force.

		This requires a dynamic object.

		Parameters:
		force (3D Vector) - force vector.
		local (boolean) -
		False: you get the "global" force ie: relative to world orientation.
		True: you get the "local" force ie: relative to object orientation."""
		pass
		
	def applyTorque(torque, local=False):
		"""Sets the game object's torque.

		This requires a dynamic object.

		Parameters:
		torque (3D Vector) - torque vector.
		local (boolean) -
		False: you get the "global" torque ie: relative to world orientation.
		True: you get the "local" torque ie: relative to object orientation."""
		pass
		
	def getLinearVelocity(local=False):
		"""Gets the game object's linear velocity.

		This method returns the game object's velocity through it's centre of mass, ie no angular velocity component.

		Parameters:
		local (boolean) -
		False: you get the "global" velocity ie: relative to world orientation.
		True: you get the "local" velocity ie: relative to object orientation.
		Returns:	the object's linear velocity.
		Return type:	Vector((vx, vy, vz))"""
		return ((0.0,0.0,0.0))
		
	def setLinearVelocity(velocity, local=False):
		"""Sets the game object's linear velocity.

		This method sets game object's velocity through it's centre of mass, ie no angular velocity component.

		This requires a dynamic object.

		Parameters:
		velocity (3D Vector) - linear velocity vector.
		local (boolean) -
		False: you get the "global" velocity ie: relative to world orientation.
		True: you get the "local" velocity ie: relative to object orientation."""
		pass
		
	def getAngularVelocity(local=False):
		"""Gets the game object's angular velocity.

		Parameters:
		local (boolean) -
		False: you get the "global" velocity ie: relative to world orientation.
		True: you get the "local" velocity ie: relative to object orientation.

		Returns:	
		the object's angular velocity.

		Return type:
		Vector((vx, vy, vz))"""
		return ((0.0,0.0,0.0))
		
	def setAngularVelocity(velocity, local=False):
		"""Sets the game object's angular velocity.

		This requires a dynamic object.

		Parameters:
		velocity (boolean) - angular velocity vector.
		local -
		False: you get the "global" velocity ie: relative to world orientation.
		True: you get the "local" velocity ie: relative to object orientation."""
		pass
		
	def getVelocity(point=(0,0,0)):
		"""Gets the game object's velocity at the specified point.

		Gets the game object's velocity at the specified point, including angular components.

		Parameters:
		point (3D Vector) - optional point to return the velocity for, in local coordinates.

		Returns:
		the velocity at the specified point.

		Return type:
		Vector((vx, vy, vz))"""
		return ((0.0,0.0,0.0))
		
	def getReactionForce():
		"""Gets the game object's reaction force.

		The reaction force is the force applied to this object over the last simulation timestep. This also includes impulses, eg from collisions.

		Returns:	
		the reaction force of this object.

		Return type:
		Vector((fx, fy, fz))

		Note: This is not implimented at the moment."""
		return ((0.0,0.0,0.0))
		
	def applyImpulse(point, impulse, local=False):
		"""Applies an impulse to the game object.

		This will apply the specified impulse to the game object at the specified point. If point != position, applyImpulse will also change the object's angular momentum. Otherwise, only linear momentum will change.

		Parameters:
		point (point [ix, iy, iz] the point to apply the impulse to (in world or local coordinates)) - the point to apply the impulse to (in world or local coordinates)
		impulse (3D Vector) - impulse vector.
		local (boolean) -
		False: you get the "global" impulse ie: relative to world coordinates with world orientation.
		True: you get the "local" impulse ie: relative to local coordinates with object orientation."""
		pass
		
	def setDamping(linear_damping, angular_damping):
		"""Sets both the linearDamping and angularDamping simultaneously. This is more efficient than setting both properties individually.

		Parameters:
		linear_damping (float ? [0, 1]) - Linear ("translational") damping factor.
		angular_damping (float ? [0, 1]) - Angular ("rotational") damping factor."""
		pass
	
	def suspendPhysics(freeConstraints=False):
		"""Suspends physics for this object.

		Parameters:
		freeConstraints (bool) – When set to True physics constraints used by the object are deleted. Else when False (the default) constraints are restored when restoring physics."""
		pass
	
	def restorePhysics():
		"""Resumes physics for this object. Also reinstates collisions."""
		pass
	
	def suspendDynamics(ghost=False):
		"""Suspends physics for this object.

		Parameters:
		ghost (bool) - When set to True, collisions with the object will be ignored, similar to the "ghost" checkbox in Blender. When False (the default), the object becomes static but still collide with other objects.

		See also isSuspendDynamics allows you to inspect whether the object is in a suspended state."""
		pass
		
	def restoreDynamics():
		"""Resumes physics for this object. Also reinstates collisions; the object will no longer be a ghost.

		Note: The objects linear velocity will be applied from when the dynamics were suspended."""
		pass
		
	def enableRigidBody():
		"""Enables rigid body physics for this object.

		Rigid body physics allows the object to roll on collisions."""
		pass
		
	def disableRigidBody():
		"""Disables rigid body physics for this object."""
		pass
		
	def setParent(parent, compound=True, ghost=True):
		"""Sets this object's parent. Control the shape status with the optional compound and ghost parameters:

		In that case you can control if it should be ghost or not:

		Parameters:
		parent (KX_GameObject) - new parent object.
		compound (boolean) -
		whether the shape should be added to the parent compound shape.
		True: the object shape should be added to the parent compound shape.
		False: the object should keep its individual shape.
		ghost (boolean) -
		whether the object should be ghost while parented.
		True: if the object should be made ghost while parented.
		False: if the object should be solid while parented.

		Note: If the object type is sensor, it stays ghost regardless of ghost parameter"""
		pass
		
	def removeParent():
		"""Removes this objects parent."""
		pass
		
	def getPhysicsId():
		"""Returns the user data object associated with this game object's physics controller."""
		pass
		
	def getPropertyNames():
		"""Gets a list of all property names.

		Returns:	
		All property names for this object.

		Return type:
		list"""
		return []
		
	def getDistanceTo():
		"""Parameters:	other (KX_GameObject or list [x, y, z]) - a point or another KX_GameObject to measure the distance to.

		Returns:	
		distance to another object or point.

		Return type:
		float"""
		return 0.0
		
	def getVectTo(other):
		"""Returns the vector and the distance to another object or point. The vector is normalized unless the distance is 0, in which a zero length vector is returned.

		Parameters:
		other (KX_GameObject or list [x, y, z]) - a point or another KX_GameObject to get the vector and distance to.

		Returns:	
		(distance, globalVector(3), localVector(3))

		Return type:
		3-tuple (float, 3-tuple (x, y, z), 3-tuple (x, y, z))"""
		return (0.0,(0.0,0.0,0.0),(0.0,0.0,0.0))
		
	def rayCastTo(other, dist=0, prop=""):
		"""Look towards another point/object and find first object hit within dist that matches prop.

		The ray is always casted from the center of the object, ignoring the object itself. The ray is casted towards the center of another object or an explicit [x, y, z] point. Use rayCast() if you need to retrieve the hit point

		Parameters:
		other (KX_GameObject or 3-tuple) - [x, y, z] or object towards which the ray is casted
		dist (float) - max distance to look (can be negative => look behind); 0 or omitted => detect up to other
		prop (string) - property name that object must have; can be omitted => detect any object

		Returns:
		the first object hit or None if no object or object does not match prop

		Return type:
		KX_GameObject"""
		value = KX_GameObject
		return value
		
	def rayCast(objto, objfrom=None, dist=0, prop="", face=False, xray=False, poly=0, mask=0xFFFF):
		"""Look from a point/object to another point/object and find first object hit within dist that matches prop. if poly is 0, returns a 3-tuple with object reference, hit point and hit normal or (None, None, None) if no hit. if poly is 1, returns a 4-tuple with in addition a KX_PolyProxy as 4th element. if poly is 2, returns a 5-tuple with in addition a 2D vector with the UV mapping of the hit point as 5th element.
		
		Return type:
		3-tuple (KX_GameObject, 3-tuple (x, y, z), 3-tuple (nx, ny, nz))
		or 4-tuple (KX_GameObject, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), KX_PolyProxy)
		or 5-tuple (KX_GameObject, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), KX_PolyProxy, 2-tuple (u, v))

		Note: The ray ignores the object on which the method is called. It is casted from/to object center or explicit [x, y, z] points."""
		object = KX_GameObject
		polyproxy = KX_PolyProxy
		return (obj,(0.0,0.0,0.0),(0.0,0.0,0.0,),polyproxy,(0,0))
	
	def collide(obj):
		"""Test if this object collides object obj.
		
		Parameters:
		obj (string or KX_GameObject) – the object to test collision with
		
		Returns:
		(collide, points)
		collide, True if this object collides object obj
		points, contact point data of the collision or None
		
		Return type:
		2-tuple (boolean, list of KX_CollisionContactPoint or None)"""
		
		return (False, None)
	
	def setCollisionMargin(margin):
		"""Set the objects collision margin.

		Parameters:
		margin (float) - the collision margin distance in blender units.

		Note: If this object has no physics controller (a physics ID of zero), this function will raise RuntimeError."""
		pass
		
	def sendMessage(subject, body="", to=""):
		"""Sends a message.

		Parameters:
		subject (string) - The subject of the message
		body (string) - The body of the message (optional)
		to (string) - The name of the object to send the message to (optional)"""
		pass
		
	def reinstancePhysicsMesh(gameObject, meshObject, dupli):
		"""Updates the physics system with the changed mesh.

		If no arguments are given the physics mesh will be re-created from the first mesh assigned to the game object.

		Parameters:	
		gameObject (string, KX_GameObject or None) - optional argument, set the physics shape from this gameObjets mesh.
		meshObject (string, MeshProxy or None) - optional argument, set the physics shape from this mesh.

		Returns:
		True if reinstance succeeded, False if it failed.

		Return type:
		boolean

		Note: If this object has instances the other instances will be updated too.

		Note: The gameObject argument has an advantage that it can convert from a mesh with modifiers applied (such as subsurf).

		Warning: Only triangle mesh type objects are supported currently (not convex hull)

		Warning: If the object is a part of a combound object it will fail (parent or child)

		Warning: Rebuilding the physics mesh can be slow, running many times per second will give a performance hit."""
		return True
	
	def replacePhysicsShape(gameObject):
		"""Replace the current physics shape.
		
		Parameters:
		gameObject (string, KX_GameObject) – set the physics shape from this gameObjets."""
	
	def get(key, default=""):
		"""Return the value matching key, or the default value if its not found.

		return: The key value or a default."""
		pass
		
	def playAction(name, start_frame, end_frame, layer=0, priority=0, blendin=0, play_mode=1, layer_weight=0.0, ipo_flags=0, speed=1.0, blend_mode=1):
		"""Plays an action.

		Parameters:
		name (string) - the name of the action
		start (float) - the start frame of the action
		end (float) - the end frame of the action
		layer (integer) - the layer the action will play in (actions in different layers are added/blended together)
		priority (integer) - only play this action if there isn't an action currently playing in this layer with a higher (lower number) priority
		blendin (float) - the amount of blending between this animation and the previous one on this layer
		play_mode (one of these constants) - the play mode
		layer_weight (float) - how much of the previous layer to use for blending
		ipo_flags (int bitfield) - flags for the old IPO behaviors (force, etc)
		speed (float) - the playback speed of the action as a factor (1.0 = normal speed, 2.0 = 2x speed, etc)
		blend_mode (one of these constants) - how to blend this layer with previous layers"""
		pass
		
	def stopAction(layer=0):
		"""Stop playing the action on the given layer.

		Parameters:
		layer (integer) - The layer to stop playing."""
		pass
		
	def getActionFrame(layer=0):
		"""Gets the current frame of the action playing in the supplied layer.

		Parameters:
		layer (integer) - The layer that you want to get the frame from.

		Returns:
		The current frame of the action

		Return type:
		float"""
		return 0.0
		
	def getActionName(layer=0):
		"""Gets the name of the current action playing in the supplied layer.

		Parameters:
		layer (integer) - The layer that you want to get the action name from.

		Returns:	
		The name of the current action

		Return type:
		string"""
		return "str"
		
	def setActionFrame(frame, layer=0):
		"""Set the current frame of the action playing in the supplied layer.

		Parameters:
		layer (integer) - The layer where you want to set the frame
		frame (float) - The frame to set the action to"""
		pass
		
	def isPlayingAction(layer=0):
		"""Checks to see if there is an action playing in the given layer.

		Parameters:
		layer (integer) - The layer to check for a playing action.

		Returns:
		Whether or not the action is playing

		Return type:
		boolean"""
		return True
		
	def addDebugProperty(name, debug=True):
		"""Adds a single debug property to the debug list.

		Parameters:
		name (string) - name of the property that added to the debug list.
		debug (boolean) - the debug state."""
		pass

	pass

class SCA_ILogicBrick(CValue):
	
	"""base class - CValue

	class bge.SCA_ILogicBrick(CValue)

	Base class for all logic bricks."""
	
	def __init__(self):
		self.owner = KX_GameObject()
		self.executePriority = 0
		self.name = "str"

class SCA_ISensor(SCA_ILogicBrick):
	
	"""base class - SCA_ILogicBrick

	class bge.SCA_ISensor(SCA_ILogicBrick)

	Base class for all sensor logic bricks."""

	def __init__(self):
		self.usePosPulseMode = 0
		self.useNegPulseMode = 0
		self.frequency = 0
		self.skippedTicks = 0
		self.level = 0
		self.tap = 0
		self.invert = 0
		self.triggered = 0
		self.positive = 0
		self.pos_ticks = 0
		self.neg_ticks = 0
		self.status = 0
		
	def reset():
		"""Reset sensor internal state, effect depends on the type of sensor and settings.

		The sensor is put in its initial state as if it was just activated."""
		pass

	pass

class SCA_IActuator(SCA_ILogicBrick):
	
	"""base class - SCA_ILogicBrick

	class bge.SCA_IActuator(SCA_ILogicBrick)

	Base class for all actuator logic bricks."""

	pass

class SCA_IController(SCA_ILogicBrick):
	
	"""base class - SCA_ILogicBrick

	class bge.SCA_IController(SCA_ILogicBrick)

	Base class for all controller logic bricks."""

	def __init__(self):
		self.state = 0
		self.sensors = {"key" : SCA_ISensor()}
		self.actuators = {"key" : SCA_IActuator()}
		self.useHighPriority = 0

class SCA_2DFilterActuator(SCA_IActuator):
	
	"""base class - SCA_IActuator

	class bge.SCA_2DFilterActuator(SCA_IActuator)
	Create, enable and disable 2D filters.

	The following properties don't have an immediate effect. You must active the actuator to get the result. The actuator is not persistent: it automatically stops itself after setting up the filter but the filter remains active. To stop a filter you must activate the actuator with 'type' set to RAS_2DFILTER_DISABLED or RAS_2DFILTER_NOFILTER."""

	def __init__(self):
		self.shaderText = 0
		self.disableMotionBlur = 0
		self.mode = 0
		self.passNumber = 0
		self.value = 0

class SCA_ANDController(SCA_IController):
	
	"""base class - SCA_IController

	class bge.SCA_ANDController(SCA_IController)

	An AND controller activates only when all linked sensors are activated.

	There are no special python methods for this controller."""

	pass

class SCA_ActuatorSensor(SCA_ISensor):
	
	"""base class - SCA_ISensor

	class bge.SCA_ActuatorSensor(SCA_ISensor)

	Actuator sensor detect change in actuator state of the parent object. It generates a positive pulse if the corresponding actuator is activated and a negative pulse if the actuator is deactivated."""

	def __init__(self):
		self.actuator = 0

class SCA_AlwaysSensor(SCA_ISensor):
	
	"""base class - SCA_ISensor

	class bge.SCA_AlwaysSensor(SCA_ISensor)

	This sensor is always activated."""

	pass

class SCA_DelaySensor(SCA_ISensor):
	
	"""base class - SCA_ISensor

	class bge.SCA_DelaySensor(SCA_ISensor)

	The Delay sensor generates positive and negative triggers at precise time, expressed in number of frames. The delay parameter defines the length of the initial OFF period. A positive trigger is generated at the end of this period.

	The duration parameter defines the length of the ON period following the OFF period. There is a negative trigger at the end of the ON period. If duration is 0, the sensor stays ON and there is no negative trigger.

	The sensor runs the OFF-ON cycle once unless the repeat option is set: the OFF-ON cycle repeats indefinately (or the OFF cycle if duration is 0).

	Use SCA_ISensor.reset at any time to restart sensor."""

	def __init__(self):
		self.delay = 0
		self.duration = 0
		self.repeat = 0

class SCA_JoystickSensor(SCA_ISensor):
	
	"""base class - SCA_ISensor

	class bge.SCA_JoystickSensor(SCA_ISensor)

	This sensor detects player joystick events."""

	def __init__(self):
		self.axisValues = 0
		self.axisSingle = 0
		self.hatValues = 0
		self.hatSingle = 0
		self.numAxis = 0
		self.numButtons = 0
		self.numHats = 0
		self.connected = 0
		self.index = 0
		self.threshold = 0
		self.button = 0
		self.axis = 0
		self.hat = 0
		
	def getButtonActiveList():
		"""Returns:	
		A list containing the indicies of the currently pressed buttons.

		Return type:
		list"""
		pass
		
	def getButtonStatus():
		"""Parameters:
		buttonIndex (integer) - the button index, 0=first button

		Returns:	
		The current pressed state of the specified button.

		Return type:
		boolean"""
		pass

	pass

class SCA_KeyboardSensor(SCA_ISensor):
	
	"""base class - SCA_ISensor

	class bge.SCA_KeyboardSensor(SCA_ISensor)

	A keyboard sensor detects player key presses.

	See module bge.events for keycode values."""

	def __init__(self):
		self.key = 0
		self.hold1 = 0
		self.hold2 = 0
		self.toggleProperty = 0
		self.targetProperty = 0
		self.useAllKeys = 0
		self.events = 0
		
	def getKeyStatus():
		"""Get the status of a key.

		Parameters:
		keycode (integer) - The code that represents the key you want to get the state of, use one of these constants

		Returns:
		The state of the given key, can be one of these constants

		Return type:
		int"""
		pass
		
	pass

class SCA_MouseSensor(SCA_ISensor):
	
	"""base class - SCA_ISensor

	class bge.SCA_MouseSensor(SCA_ISensor)

	Mouse Sensor logic brick."""

	def __init__(self):
		self.position = 0
		self.mode = 0
		
	def getButtonStatus():
		"""Get the mouse button status.

		Parameters:
		button (int) - The code that represents the key you want to get the state of, use one of these constants

		Returns:
		The state of the given key, can be one of these constants

		Return type:
		int"""
		pass

	pass

class SCA_NANDController(SCA_IController):
	
	"""base class - SCA_IController

	class bge.SCA_NANDController(SCA_IController)

	An NAND controller activates when all linked sensors are not active.

	There are no special python methods for this controller."""

	pass

class SCA_NORController(SCA_IController):
	
	"""base class - SCA_IController

	class bge.SCA_NORController(SCA_IController)

	An NOR controller activates only when all linked sensors are de-activated.

	There are no special python methods for this controller."""

	pass

class SCA_ORController(SCA_IController):
	
	"""base class - SCA_IController

	class bge.SCA_ORController(SCA_IController)

	An OR controller activates when any connected sensor activates.

	There are no special python methods for this controller."""

	pass

class SCA_PropertyActuator(SCA_IActuator):
	
	"""base class - SCA_IActuator

	class bge.SCA_PropertyActuator(SCA_IActuator)

	Property Actuator"""

	def __init__(self):
		self.propName = 0
		self.value = 0
		self.mode = 0

class SCA_PropertySensor(SCA_ISensor):
	
	"""base class - SCA_ISensor

	class bge.SCA_PropertySensor(SCA_ISensor)

	Activates when the game object property matches."""

	def __init__(self):
		self.mode = 0
		self.propName = 0
		self.value = 0
		self.min = 0
		self.max = 0

class SCA_PythonController(SCA_IController):
	
	"""base class - SCA_IController

	class bge.SCA_PythonController(SCA_IController)

	A Python controller uses a Python script to activate it's actuators, based on it's sensors."""

	def __init__(self):
		self.owner = KX_GameObject()
		self.script = ""
		self.mode = 0
		
	def activate():
		"""Activates an actuator attached to this controller.

		Parameters:
		actuator (actuator or the actuator name as a string) - The actuator to operate on."""
		pass
		
	def deactivate():
		"""Deactivates an actuator attached to this controller.

		Parameters:
		actuator (actuator or the actuator name as a string) - The actuator to operate on."""
		pass

	pass

class SCA_PythonJoystick(PyObjectPlus):
	
	"""base class - PyObjectPlus

	class bge.SCA_PythonJoystick(PyObjectPlus)

	A Python interface to a joystick."""

	def __init__(self):
		self.name = 0
		self.activeButtons = 0
		self.axisValues = 0
		self.hatValues = 0
		self.numAxis = 0
		self.numButtons = 0
		self.numHats = 0

class SCA_PythonKeyboard(PyObjectPlus):
	
	"""base class - PyObjectPlus

	class bge.SCA_PythonKeyboard(PyObjectPlus)

	The current keyboard."""

	def __init__(self):
		self.events = 0
		self.active_events = 0
	
	def getClipboard():
		"""Gets the clipboard text.

		Return type:
		string"""
		pass
		
	def setClipboard():
		"""Sets the clipboard text.

		Parameters:
		text (string) - New clipboard text"""
		pass

	pass

class SCA_PythonMouse(PyObjectPlus):
	
	"""base class - PyObjectPlus

	class bge.SCA_PythonMouse(PyObjectPlus)

	The current mouse."""

	def __init__(self):
		self.events = 0
		self.active_events = 0
		self.position = 0
		self.visible = 0

class SCA_RandomActuator(SCA_IActuator):
	
	"""base class - SCA_IActuator

	class bge.SCA_RandomActuator(SCA_IActuator)

	Random Actuator"""

	def __init__(self):
		self.seed = 0
		self.para1 = 0
		self.para2 = 0
		self.distribution = 0
		self.propName = 0
		
	def setBoolConst():
		"""Sets this generator to produce a constant boolean value.

		Parameters:
		value (boolean) - The value to return."""
		pass
		
	def setBoolUniform():
		"""Sets this generator to produce a uniform boolean distribution.

		The generator will generate True or False with 50% chance."""
		pass
		
	def setBoolBernouilli():
		"""Sets this generator to produce a Bernouilli distribution.

		Parameters:
		value (float) -
		Specifies the proportion of False values to produce.
		0.0: Always generate True
		1.0: Always generate False"""
		pass
		
	def setIntConst():
		"""Sets this generator to always produce the given value.

		Parameters:
		value (integer) - the value this generator produces."""
		pass
		
	def setIntUniform():
		"""Sets this generator to produce a random value between the given lower and upper bounds (inclusive)."""
		pass
		
	def setIntPoisson():
		"""Generate a Poisson-distributed number.

		This performs a series of Bernouilli tests with parameter value. It returns the number of tries needed to achieve succes."""
		pass
		
	def setFloatConst():
		"""Always generate the given value."""
		pass
		
	def setFloatUniform():
		"""Generates a random float between lower_bound and upper_bound with a uniform distribution."""
		pass
		
	def setFloatNormal():
		"""Generates a random float from the given normal distribution.

		Parameters:
		mean (float) - The mean (average) value of the generated numbers
		standard_deviation (float) - The standard deviation of the generated numbers."""
		pass
		
	def setFloatNegativeExponential():
		"""Generate negative-exponentially distributed numbers.

		The half-life 'time' is characterized by half_life."""
		pass

	pass

class SCA_RandomSensor(SCA_ISensor):
	
	"""base class - SCA_ISensor

	class bge.SCA_RandomSensor(SCA_ISensor)

	This sensor activates randomly."""

	def __init__(self):
		self.lastDraw = 0
		self.seed = 0

class SCA_XNORController(SCA_IController):
	"""base class - SCA_IController

	class bge.SCA_XNORController(SCA_IController)

	An XNOR controller activates when all linked sensors are the same (activated or inative).

	There are no special python methods for this controller."""
	pass

class SCA_XORController(SCA_IController):
	"""base class - SCA_IController

	class bge.SCA_XORController(SCA_IController)

	An XOR controller activates when there is the input is mixed, but not when all are on or off.

	There are no special python methods for this controller."""
	pass

class BL_ActionActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.BL_ActionActuator(SCA_IActuator)

	Action Actuators apply an action to an actor."""

	def __init__(self):
		self.action = 0
		self.frameStart = 0
		self.frameEnd = 0
		self.blendIn = 0
		self.priority = 0
		self.frame = 0
		self.propName = 0
		self.blendTime = 0
		self.mode = 0
		self.useContinue = 0
		self.framePropName = 0

class BL_ArmatureActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.BL_ArmatureActuator(SCA_IActuator)

	Armature Actuators change constraint condition on armatures."""

	def __init__(self):
		self.type = 0
		self.constraint = 0
		self.target = 0
		self.subtarget = 0
		self.weight = 0
		self.influence = 0

class BL_ArmatureBone(PyObjectPlus):
	"""base class - PyObjectPlus

	class bge.BL_ArmatureBone(PyObjectPlus)

	Proxy to Blender bone structure. All fields are read-only and comply to RNA names. All space attribute correspond to the rest pose."""

	def __init__(self):
		self.name = 0
		self.connected = 0
		self.hinge = 0
		self.inherit_scale = 0
		self.bbone_segments = 0
		self.roll = 0
		self.head = 0
		self.tail = 0
		self.length = 0
		self.arm_head = 0
		self.arm_tail = 0
		self.arm_mat = 0
		self.bone_mat = 0
		self.parent = 0
		self.children = 0

class BL_ArmatureChannel(PyObjectPlus):
	"""base class - PyObjectPlus

	class bge.BL_ArmatureChannel(PyObjectPlus)

	Proxy to armature pose channel. Allows to read and set armature pose. The attributes are identical to RNA attributes, but mostly in read-only mode."""

	def __init__(self):
		self.name = 0
		self.bone = 0
		self.parent = 0
		self.has_ik = 0
		self.ik_dof_x = 0
		self.ik_dof_y = 0
		self.ik_dof_z = 0
		self.ik_limit_x = 0
		self.ik_limit_y = 0
		self.ik_limit_z = 0
		self.ik_rot_control = 0
		self.ik_lin_control = 0
		self.location = 0
		self.scale = 0
		self.rotation_quaternion = 0
		self.rotation_euler = 0
		self.rotation_mode = 0
		self.channel_matrix = 0
		self.pose_matrix = 0
		self.pose_head = 0
		self.pose_tail = 0
		self.ik_min_x = 0
		self.ik_max_x = 0
		self.ik_min_y = 0
		self.ik_max_y = 0
		self.ik_min_z = 0
		self.ik_max_z = 0
		self.ik_stiffness_x = 0
		self.ik_stiffness_y = 0
		self.ik_stiffness_z = 0
		self.ik_stretch = 0
		self.ik_rot_weight = 0
		self.ik_lin_weight = 0
		self.joint_rotation = 0

class BL_ArmatureConstraint(PyObjectPlus):
	"""base class - PyObjectPlus

	class bge.BL_ArmatureConstraint(PyObjectPlus)

	Proxy to Armature Constraint. Allows to change constraint on the fly. Obtained through BL_ArmatureObject.constraints.

	Note: Not all armature constraints are supported in the GE."""

	def __init__(self):
		self.type = 0
		self.name = 0
		self.enforce = 0
		self.headtail = 0
		self.lin_error = 0
		self.rot_error = 0
		self.target = 0
		self.subtarget = 0
		self.active = 0
		self.ik_weight = 0
		self.ik_type = 0
		self.ik_flag = 0
		self.ik_dist = 0
		self.ik_mode = 0

class BL_ArmatureObject(KX_GameObject):
	"""base class - KX_GameObject

	class bge.BL_ArmatureObject(KX_GameObject)

	An armature object."""

	def __init__(self):
		self.constraints = 0
		self.channels = 0
		
	def update():
		"""Ensures that the armature will be updated on next graphic frame.

		This action is unecessary if a KX_ArmatureActuator with mode run is active or if an action is playing. Use this function in other cases. It must be called on each frame to ensure that the armature is updated continously."""
		pass

	pass

class BL_Shader(PyObjectPlus):
	"""base class - PyObjectPlus

	class bge.BL_Shader(PyObjectPlus)

	BL_Shader GLSL shaders.

	TODO - Description"""
	
	def setUniformfv():
		"""Set a uniform with a list of float values

		Parameters:
		name (string) - the uniform name
		fList (list[float]) - a list (2, 3 or 4 elements) of float values"""
		pass
		
	def delSource():
		"""Clear the shader. Use this method before the source is changed with setSource."""
		pass
		
	def getFragmentProg():
		"""Returns the fragment program.

		Returns:	The fragment program.

		Return type:
		string"""
		return "str"
		
	def getVertexProg():
		"""Get the vertex program.

		Returns: The vertex program.

		Return type:
		string"""
		return "str"
		
	def isValid():
		"""Check if the shader is valid.

		Returns: True if the shader is valid

		Return type:
		boolean"""
		return True
		
	def setAttrib():
		"""Set attribute location. (The parameter is ignored a.t.m. and the value of "tangent" is always used.)

		Parameters:
		enum (integer) - attribute location value"""
		pass
		
	def setNumberOfPasses():
		"""Set the maximum number of passes. Not used a.t.m.

		Parameters:
		max_pass (integer) - the maximum number of passes"""
		pass
		
	def setSampler():
		"""Set uniform texture sample index.

		Parameters:
		name (string) - Uniform name
		index (integer) - Texture sample index."""
		pass
		
	def setSource():
		"""Set the vertex and fragment programs

		Parameters:
		vertexProgram (string) - Vertex program
		fragmentProgram (string) - Fragment program"""
		pass
		
	def setUniform1f():
		"""Set a uniform with 1 float value.

		Parameters:
		name (string) - the uniform name
		fx (float) - Uniform value"""
		pass
		
	def setUniform1i():
		"""Set a uniform with an integer value.

		Parameters:
		name (string) - the uniform name
		ix (integer) - the uniform value"""
		pass
		
	def setUniform2f():
		"""Set a uniform with 2 float values

		Parameters:
		name (string) - the uniform name
		fx (float) - first float value
		fy (float) - second float value"""
		pass
		
	def setUniform2i():
		"""Set a uniform with 2 integer values

		Parameters:
		name (string) - the uniform name
		ix (integer) - first integer value
		iy (integer) - second integer value"""
		pass
		
	def setUniform3f():
		"""Set a uniform with 3 float values.

		Parameters:
		name (string) - the uniform name
		fx (float) - first float value
		fy (float) - second float value
		fz (float) - third float value"""
		pass
		
	def setUniform3i():
		"""Set a uniform with 3 integer values

		Parameters:
		name (string) - the uniform name
		ix (integer) - first integer value
		iy (integer) - second integer value
		iz (integer) - third integer value"""
		pass
		
	def setUniform4f():
		"""Set a uniform with 4 float values.

		Parameters:
		name (string) - the uniform name
		fx (float) - first float value
		fy (float) - second float value
		fz (float) - third float value
		fw (float) - fourth float value"""
		pass
		
	def setUniform4i():
		"""Set a uniform with 4 integer values

		Parameters:
		name (string) - the uniform name
		ix (integer) - first integer value
		iy (integer) - second integer value
		iz (integer) - third integer value
		iw (integer) - fourth integer value"""
		pass
		
	def setUniformDef():
		"""Define a new uniform

		Parameters:
		name (string) - the uniform name
		type (UNI_NONE, UNI_INT, UNI_FLOAT, UNI_INT2, UNI_FLOAT2, UNI_INT3, UNI_FLOAT3, UNI_INT4, UNI_FLOAT4, UNI_MAT3, UNI_MAT4, UNI_MAX) - uniform type"""
		pass
		
	def setUniformMatrix3():
		"""Set a uniform with a 3x3 matrix value

		Parameters:
		name (string) - the uniform name
		mat (3x3 matrix) - A 3x3 matrix [[f, f, f], [f, f, f], [f, f, f]]
		transpose (boolean) - set to True to transpose the matrix"""
		pass
		
	def setUniformMatrix4():
		"""Set a uniform with a 4x4 matrix value

		Parameters:
		name (string) - the uniform name
		mat (4x4 matrix) - A 4x4 matrix [[f, f, f, f], [f, f, f, f], [f, f, f, f], [f, f, f, f]]
		transpose (boolean) - set to True to transpose the matrix"""
		pass
		
	def setUniformv():
		"""Set a uniform with a list of integer values

		Parameters:
		name (string) - the uniform name
		iList (list[integer]) - a list (2, 3 or 4 elements) of integer values"""
		pass
		
	def validate():
		"""Validate the shader object."""
		pass

	pass

class BL_ShapeActionActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.BL_ShapeActionActuator(SCA_IActuator)

	ShapeAction Actuators apply an shape action to an mesh object."""

	def __init__(self):
		self.action = 0
		self.frameStart = 0
		self.frameEnd = 0
		self.blendIn = 0
		self.priority = 0
		self.frame = 0
		self.propName = 0
		self.blendTime = 0
		self.mode = 0
		self.framePropName = 0

class KX_TouchSensor(SCA_ISensor):
	"""base class - SCA_ISensor

	class bge.KX_TouchSensor(SCA_ISensor)

	Touch sensor detects collisions between objects."""

	def __init__(self):
		self.propName = 0
		self.useMaterial = 0
		self.usePulseCollision = 0
		self.hitObject = 0
		self.hitObjectList = 0
		self.hitMaterial = 0

class KX_ArmatureSensor(SCA_ISensor):
	"""base class - SCA_ISensor

	class bge.KX_ArmatureSensor(SCA_ISensor)

	Armature sensor detect conditions on armatures."""

	def __init__(self):
		self.type = 0
		self.constraint = 0
		self.value = 0

class KX_BlenderMaterial(PyObjectPlus):
	"""base class - PyObjectPlus

	class bge.KX_BlenderMaterial(PyObjectPlus)
	This is the interface to materials in the game engine.

	Materials define the render state to be applied to mesh objects."""

	def __init__(self):
		self.shader = 0
		self.blending = 0
		self.material_index = 0
		self.alpha = 0
		self.hardness = 0
		self.emit = 0
		self.specularIntensity = 0
		self.diffuseIntensity = 0
		self.specularColor = 0
		self.diffuseColor = 0
		
	def getShader():
		"""Returns the material's shader.

		Returns:	
		the material's shader

		Return type:
		BL_Shader"""
		value = BL_Shader
		return value
		
	def setBlending():
		"""Set the pixel color arithmetic functions.

		Parameters:	
		src (int) -
		Specifies how the red, green, blue, and alpha source blending factors are computed, one of...
		GL_ZERO
		GL_ONE
		GL_SRC_COLOR
		GL_ONE_MINUS_SRC_COLOR
		GL_DST_COLOR
		GL_ONE_MINUS_DST_COLOR
		GL_SRC_ALPHA
		GL_ONE_MINUS_SRC_ALPHA
		GL_DST_ALPHA
		GL_ONE_MINUS_DST_ALPHA
		GL_SRC_ALPHA_SATURATE

		dest (int) - 
		Specifies how the red, green, blue, and alpha destination blending factors are computed, one of...
		GL_ZERO
		GL_ONE
		GL_SRC_COLOR
		GL_ONE_MINUS_SRC_COLOR
		GL_DST_COLOR
		GL_ONE_MINUS_DST_COLOR
		GL_SRC_ALPHA
		GL_ONE_MINUS_SRC_ALPHA
		GL_DST_ALPHA
		GL_ONE_MINUS_DST_ALPHA
		GL_SRC_ALPHA_SATURATE"""
		pass
		
	def getMaterialIndex():
		"""Returns the material's index.

		Returns:	
		the material's index

		Return type:
		integer"""
		return 0

	pass

class KX_Camera(KX_GameObject):
	"""base class - KX_GameObject

	class bge.KX_Camera(KX_GameObject)

	A Camera object."""

	# Constants
	INSIDE = 1
	INTERSECT = 2
	OUTSIDE = 3

	def __init__(self):
		self.lens = 0.0
		self.lodDistanceFactor = 0.0
		self.fov = 0.0
		self.ortho_scale = 0.0
		self.near = 0.0
		self.far = 0.0
		self.shift_x = 0.0
		self.shift_y = 0.0
		self.perspective = False
		self.frustum_culling = False
		self.activityCulling = False
		self.projection_matrix = ((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
		self.modelview_matrix = ((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
		self.camera_to_world = ((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
		self.world_to_camera = ((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
		self.useViewPort = False
	
	def sphereInsideFrustum(centre, radius):
		"""Tests the given sphere against the view frustum.

		Parameters:
		centre (list [x, y, z]) - The centre of the sphere (in world coordinates.)
		radius (float) - the radius of the sphere

		Returns:	
		INSIDE, OUTSIDE or INTERSECT

		Return type:
		integer

		Note: When the camera is first initialized the result will be invalid because the projection matrix has not been set."""
		return 0
		
	def boxInsideFrustum(box):
		"""Tests the given box against the view frustum.

		Parameters:
		box (list of lists) - Eight (8) corner points of the box (in world coordinates.)

		Returns:	
		INSIDE, OUTSIDE or INTERSECT

		Note: When the camera is first initialized the result will be invalid because the projection matrix has not been set."""
		return 0
		
	def pointInsideFrustum(point):
		"""Tests the given point against the view frustum.

		Parameters:
		point (3D Vector) - The point to test (in world coordinates.)

		Returns:	
		True if the given point is inside this camera's viewing frustum.

		Return type:
		boolean

		Note: When the camera is first initialized the result will be invalid because the projection matrix has not been set."""
		return True
		
	def getCameraToWorld():
		"""Returns the camera-to-world transform.

		Returns: the camera-to-world transform matrix.

		Return type:
		matrix (4x4 list)"""
		return [(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0)]
		
	def getWorldToCamera():
		"""Returns the world-to-camera transform.

		This returns the inverse matrix of getCameraToWorld().

		Returns: the world-to-camera transform matrix.

		Return type:
		matrix (4x4 list)"""
		return [(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0)]
		
	def setOnTop():
		"""Set this cameras viewport ontop of all other viewport."""
		pass
		
	def setViewport(left, bottom, right, top):
		"""Sets the region of this viewport on the screen in pixels.

		Use bge.render.getWindowHeight and bge.render.getWindowWidth to calculate values relative to the entire display.

		Parameters:
		left (integer) - left pixel coordinate of this viewport
		bottom (integer) - bottom pixel coordinate of this viewport
		right (integer) - right pixel coordinate of this viewport
		top (integer) - top pixel coordinate of this viewport"""
		pass
		
	def getScreenPosition(object):
		"""Gets the position of an object projected on screen space.

		# For an object in the middle of the screen, coord = [0.5, 0.5]
		coord = camera.getScreenPosition(object)

		Parameters:
		object (KX_GameObject or 3D Vector) - object name or list [x, y, z]

		Returns:	
		the object's position in screen coordinates.

		Return type:
		list [x, y]"""
		return [0,0]
		
	def getScreenVect(x, y):
		"""Gets the vector from the camera position in the screen coordinate direction.

		Parameters:
		x (float) - X Axis
		y (float) - Y Axis

		Return type:
		3D Vector

		Returns:
		The vector from screen coordinate.

		# Gets the vector of the camera front direction:
		m_vect = camera.getScreenVect(0.5, 0.5)"""
		return (0.0,0.0,0.0)
		
	def getScreenRay(x, y, dist=999.0, property=None):
		"""Look towards a screen coordinate (x, y) and find first object hit within dist that matches prop. The ray is similar to KX_GameObject->rayCastTo.

		Parameters:
		x (float) - X Axis
		y (float) - Y Axis
		dist (float) - max distance to look (can be negative => look behind); 0 or omitted => detect up to other
		property (string) - property name that object must have; can be omitted => detect any object

		Return type:
		KX_GameObject

		Returns:	
		the first object hit or None if no object or object does not match prop

		# Gets an object with a property "wall" in front of the camera within a distance of 100:
		target = camera.getScreenRay(0.5, 0.5, 100, "wall")"""
		value = KX_GameObject
		return value
		
	pass

class KX_CameraActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_CameraActuator(SCA_IActuator)

	Applies changes to a camera."""

	def __init__(self):
		self.damping = 0
		self.axis = 0
		self.min = 0
		self.max = 0
		self.height = 0
		self.object = 0

class KX_CharacterWrapper(PyObjectPlus):
	"""base class - PyObjectPlus

	class bge.KX_CharacterWrapper(PyObjectPlus)

	A wrapper to expose character physics options."""

	def __init__(self):
		self.onGround = 0
		self.gravity = 0
		self.maxJumps = 0
		self.jumpCount = 0
		self.walkDirection = 0

	
	def jump():
		"""The character jumps based on it's jump speed."""
		pass

	pass

class KX_ConstraintActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_ConstraintActuator(SCA_IActuator)

	A constraint actuator limits the position, rotation, distance or orientation of an object."""

	def __init__(self):
		self.damp = 0
		self.rotDamp = 0
		self.direction = 0
		self.option = 0
		self.time = 0
		self.propName = 0
		self.min = 0
		self.distance = 0
		self.max = 0
		self.rayLength = 0
		self.limit = 0

class KX_ConstraintWrapper(PyObjectPlus):
	"""base class - PyObjectPlus

	class bge.KX_ConstraintWrapper(PyObjectPlus)

	KX_ConstraintWrapper"""

	def __init__(self):
		self.constraint_id = 0
		self.constraint_type = 0
		
	def getConstraintId():
		"""Returns the contraint ID

		Returns:	
		the constraint ID

		Return type:
		integer"""
		return 0
	def setParam():
		"""Set the contraint limits

		Parameters:
		axis (integer)
		value0 - Set the minimum limit of the axis
		value1 - Set the maximum limit of the axis"""
		pass
	def getParam():
		"""Get the contraint position or euler angle of a generic 6DOF constraint

		Parameters:
		axis (integer)

		axis = 0..2 are linear constraint values
		0: X axis position
		1: Y axis position
		2: Z axis position

		Returns:	
		position

		Return type:
		float

		axis = 3..5 are relative constraint (Euler) angles in radians
		3: X axis angle
		4: Y axis angle
		5: Z axis angle

		Returns:	
		angle

		Return type:
		float"""
		return 0.0

	pass

class KX_FontObject(KX_GameObject):
	"""base class - KX_GameObject

	class bge.KX_FontObject(KX_GameObject)

	A Font object.

	# Display a message about the exit key using a Font object.
	import bge

	co = bge.logic.getCurrentController()
	font = co.owner

	exit_key = bge.events.EventToString(bge.logic.getExitKey())

	if exit_key.endswith("KEY"):
		exit_key = exit_key[:-3]

	font.text = "Press key '%s' to quit the game." % exit_key"""

	def __init__(self):
		self.text = 0

class KX_GameActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_GameActuator(SCA_IActuator)

	The game actuator loads a new .blend file, restarts the current .blend file or quits the game."""

	def __init__(self):
		self.fileName = 0
		self.mode = 0

class KX_IpoActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_IpoActuator(SCA_IActuator)
	IPO actuator activates an animation."""

	def __init__(self):
		self.frameStart = 0
		self.frameEnd = 0
		self.propName = 0
		self.framePropName = 0
		self.mode = 0
		self.useIpoAsForce = 0
		self.useIpoAdd = 0
		self.useIpoLocal = 0
		self.useChildren = 0

class KX_LibLoadStatus(PyObjectPlus):
	"""base class - PyObjectPlus

	class bge.KX_LibLoadStatus(PyObjectPlus)

	An object providing information about a LibLoad() operation.

	# Print a message when an async LibLoad is done
	import bge

	def finished_cb(status):
		print("Library (%s) loaded in %.2fms." % (status.libraryName, status.timeTaken))

	bge.logic.LibLoad('myblend.blend', 'Scene', async=True).onFinish = finished_cb"""

	def __init__(self):
		self.onFinish = 0
		self.progress = 0
		self.libraryName = 0
		self.timeTaken = 0

class KX_LightObject(KX_GameObject):
	"""base class - KX_GameObject

	class bge.KX_LightObject(KX_GameObject)

	A Light object.

	# Turn on a red alert light.
	import bge

	co = bge.logic.getCurrentController()
	light = co.owner

	light.energy = 1.0
	light.color = [1.0, 0.0, 0.0]"""

	# Constants
	SPOT = 1
	SUN = 2
	NORMAL = 0
	HEMI = 3

	def __init__(self):
		self.type = 0
		self.layer = 0
		self.energy = 0
		self.distance = 0
		self.color = 0
		self.lin_attenuation = 0
		self.quad_attenuation = 0
		self.spotsize = 0
		self.spotblend = 0

class KX_MeshProxy(SCA_IObject):
	"""base class - SCA_IObject

	class bge.KX_MeshProxy(SCA_IObject)

	A mesh object.

	You can only change the vertex properties of a mesh object, not the mesh topology.

	To use mesh objects effectively, you should know a bit about how the game engine handles them.

	Mesh Objects are converted from Blender at scene load.

	The Converter groups polygons by Material. This means they can be sent to the renderer efficiently. A material holds: The texture, the Blender material, the Tile properties, the face properties - (From the "Texture Face" panel), transparency & z sorting, light layer, polygon shape (triangle/quad), game Object

	Vertices will be split by face if necessary. Vertices can only be shared between faces if: They are at the same position, UV coordinates are the same, their normals are the same (both polygons are "Set Smooth"), they are the same color, for example: a cube has 24 vertices: 6 faces with 4 vertices per face"""

	def __init__(self):
		self.materials = 0
		self.numPolygons = 0
		self.numMaterials = 0
		
	def getMaterialName():
		"""Gets the name of the specified material.

		Parameters:
		matid (integer) - the specified material.

		Returns:	
		the attached material name.

		Return type:
		string"""
		return "str"
		
	def getTextureName():
		"""Gets the name of the specified material's texture.

		Parameters:
		matid (integer) - the specified material

		Returns:	
		the attached material's texture name.

		Return type:
		string"""
		return "str"
		
	def getVertexArray():
		"""Gets the length of the vertex array associated with the specified material.

		There is one vertex array for each material.

		Parameters:
		matid (integer) - the specified material

		Returns:	
		the number of verticies in the vertex array.

		Return type:
		integer"""
		return 0
		
	def getVertex():
		"""Gets the specified vertex from the mesh object.

		Parameters:
		matid (integer) - the specified material
		index (integer) - the index into the vertex array.

		Returns:
		a vertex object.

		Return type:
		KX_VertexProxy"""
		value = KX_PolyProxy
		return value
		
	def getPolygon():
		"""Gets the specified polygon from the mesh.

		Parameters:
		index (integer) - polygon number

		Returns:	
		a polygon object.

		Return type:
		KX_PolyProxy"""
		value = KX_PolyProxy
		return value
		
	def transform():
		"""Transforms the vertices of a mesh.

		Parameters:
		matid (integer) - material index, -1 transforms all.
		matrix (4x4 matrix [[float]]) - transformation matrix."""
		pass
		
	def transformUV():
		"""Transforms the vertices UV's of a mesh.

		Parameters:
		matid (integer) - material index, -1 transforms all.
		matrix (4x4 matrix [[float]]) - transformation matrix.
		uv_index (integer) - optional uv index, -1 for all, otherwise 0 or 1.
		uv_index_from (integer) - optional uv index to copy from, -1 to transform the current uv."""
		pass

	pass

class KX_MouseActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_MouseActuator(SCA_IActuator)

	The mouse actuator gives control over the visibility of the mouse cursor and rotates the parent object according to mouse movement."""

	def __init__(self):
		self.visible = 0
		self.use_axis_x = 0
		self.use_axis_y = 0
		self.threshold = 0
		self.reset_x = 0
		self.reset_y = 0
		self.object_axis = 0
		self.local_x = 0
		self.local_y = 0
		self.sensitivity = 0
		self.limit_x = 0
		self.limit_y = 0
		self.angle = 0
	
	def reset():
		"""Undoes the rotation caused by the mouse actuator."""
		pass

	pass

class KX_MouseFocusSensor(SCA_MouseSensor):
	"""base class - SCA_MouseSensor

	class bge.KX_MouseFocusSensor(SCA_MouseSensor)

	The mouse focus sensor detects when the mouse is over the current game object.

	The mouse focus sensor works by transforming the mouse coordinates from 2d device space to 3d space then raycasting away from the camera."""

	def __init__(self):
		self.raySource = 0
		self.rayTarget = 0
		self.rayDirection = 0
		self.hitObject = 0
		self.hitPosition = 0
		self.hitNormal = 0
		self.hitUV = 0
		self.usePulseFocus = 0
		self.useXRay = 0
		self.propName = 0
		self.useMaterial = 0

class KX_NavMeshObject(KX_GameObject):
	
	"""base class - KX_GameObject

	class bge.KX_NavMeshObject(KX_GameObject)

	Python interface for using and controlling navigation meshes."""
	
	def findPath():
		"""Finds the path from start to goal points.

		Parameters:
		start - the start point
		start - 3D Vector
		goal - the goal point
		start - 3D Vector

		Returns:	
		a path as a list of points

		Return type:
		list of points"""
		return []
		
	def raycast():
		"""Raycast from start to goal points.

		Parameters:
		start - the start point
		start - 3D Vector
		goal - the goal point
		start - 3D Vector

		Returns:	
		the hit factor

		Return type:
		float"""
		return 0.0
		
	def draw():
		"""Draws a debug mesh for the navigation mesh.

		Parameters:
		mode - the drawing mode (one of these constants)
		mode - integer

		Returns:	
		None"""
		return None
		
	def rebuild():
		"""Rebuild the navigation mesh.

		Returns: None"""
		return None
		
	pass

class KX_NearSensor(KX_TouchSensor):
	
	"""base class - KX_TouchSensor

	class bge.KX_NearSensor(KX_TouchSensor)

	A near sensor is a specialised form of touch sensor."""

	def __init__(self):
		self.distance = 0
		self.resetDistance = 0

class KX_NetworkMessageActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_NetworkMessageActuator(SCA_IActuator)

	Message Actuator"""

	def __init__(self):
		self.propName = 0
		self.subject = 0
		self.body = 0
		self.usePropBody = 0

class KX_NetworkMessageSensor(SCA_ISensor):
	"""base class - SCA_ISensor

	class bge.KX_NetworkMessageSensor(SCA_ISensor)

	The Message Sensor logic brick.

	Currently only loopback (local) networks are supported."""

	def __init__(self):
		self.subject = 0
		self.frameMessageCount = 0
		self.subjects = 0
		self.bodies = 0

class KX_ObjectActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_ObjectActuator(SCA_IActuator)

	The object actuator ("Motion Actuator") applies force, torque, displacement, angular displacement, velocity, or angular velocity to an object. Servo control allows to regulate force to achieve a certain speed target."""

	def __init__(self):
		self.force = 0
		self.useLocalForce = 0
		self.torque = 0
		self.useLocalTorque = 0
		self.dLoc = 0
		self.useLocalDLoc = 0
		self.dRot = 0
		self.useLocalDRot = 0
		self.linV = 0
		self.useLocalLinV = 0
		self.angV = 0
		self.useLocalAngV = 0
		self.damping = 0
		self.forceLimitX = 0
		self.forceLimitY = 0
		self.forceLimitZ = 0
		self.pid = 0
		self.reference = 0

class KX_ParentActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_ParentActuator(SCA_IActuator)

	The parent actuator can set or remove an objects parent object."""

	def __init__(self):
		self.object = 0
		self.mode = 0
		self.compound = 0
		self.ghost = 0

class KX_PolyProxy(SCA_IObject):
	"""base class - SCA_IObject

	class bge.KX_PolyProxy(SCA_IObject)

	A polygon holds the index of the vertex forming the poylgon.

	Note: The polygon attributes are read-only, you need to retrieve the vertex proxy if you want to change the vertex settings."""

	def __init__(self):
		self.material_name = 0
		self.material = 0
		self.texture_name = 0
		self.material_id = 0
		self.v1 = 0
		self.v2 = 0
		self.v3 = 0
		self.v4 = 0
		self.visible = 0
		self.collide = 0
	
	def getMaterialName():
		"""Returns the polygon material name with MA prefix

		Returns:	
		material name

		Return type:
		string"""
		return "str"
	def getMaterial():
		"""Returns:	
		The polygon material

		Return type:
		KX_BlenderMaterial"""
		value = KX_BlenderMaterial
		return value
	def getTextureName():
		"""Returns:	
		The texture name

		Return type:
		string"""
		return "str"
	def getMaterialIndex():
		"""Returns the material bucket index of the polygon. This index and the ones returned by getVertexIndex() are needed to retrieve the vertex proxy from MeshProxy.

		Returns:	
		the material index in the mesh

		Return type:
		integer"""
		return 0
	def getNumVertex():
		"""Returns the number of vertex of the polygon.

		Returns:	
		number of vertex, 3 or 4.

		Return type:
		integer"""
		return 0
	def isVisible():
		"""Returns whether the polygon is visible or not

		Returns:	
		0=invisible, 1=visible

		Return type:
		boolean"""
		return 0
	def isCollider():
		"""Returns whether the polygon is receives collision or not

		Returns: 0=collision free, 1=receives collision

		Return type:
		integer"""
		return 0
	def getVertexIndex():
		"""Returns the mesh vertex index of a polygon vertex This index and the one returned by getMaterialIndex() are needed to retrieve the vertex proxy from MeshProxy.

		Parameters:
		vertex - index of the vertex in the polygon: 0->3
		vertex - integer

		Returns:	
		mesh vertex index

		Return type:
		integer"""
		return 0
	def getMesh():
		"""Returns a mesh proxy

		Returns:	
		mesh proxy

		Return type:
		MeshProxy"""
		value = KX_MeshProxy
		return value

	pass

class KX_RadarSensor(KX_NearSensor):
	"""base class - KX_NearSensor

	class bge.KX_RadarSensor(KX_NearSensor)

	Radar sensor is a near sensor with a conical sensor object."""

	def __init__(self):
		self.coneOrigin = 0
		self.coneTarget = 0
		self.distance = 0
		self.angle = 0
		self.axis = 0

class KX_RaySensor(SCA_ISensor):
	"""base class - SCA_ISensor

	class bge.KX_RaySensor(SCA_ISensor)

	A ray sensor detects the first object in a given direction."""

	def __init__(self):
		self.propName = 0
		self.range = 0
		self.useMaterial = 0
		self.useXRay = 0
		self.hitObject = 0
		self.hitPosition = 0
		self.hitNormal = 0
		self.hitMaterial = 0
		self.rayDirection = 0
		self.axis = 0

class KX_SCA_AddObjectActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_SCA_AddObjectActuator(SCA_IActuator)

	Edit Object Actuator (in Add Object Mode)

	Warning: An Add Object actuator will be ignored if at game start, the linked object doesn't exist (or is empty) or the linked object is in an active layer.

	Error: GameObject 'Name' has a AddObjectActuator 'ActuatorName' without object (in 'nonactive' layer)"""

	def __init__(self):
		self.object = 0
		self.objectLastCreated = 0
		self.time = 0
		self.linearVelocity = 0
		self.angularVelocity = 0
	
	def instantAddObject():
		"""Adds the object without needing to calling SCA_PythonController.activate()

		Note: Use objectLastCreated to get the newly created object."""
		pass

	pass

class KX_SCA_DynamicActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_SCA_DynamicActuator(SCA_IActuator)

	Dynamic Actuator."""

	def __init__(self):
		self.mode = 0
		self.mass = 0

class KX_SCA_EndObjectActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_SCA_EndObjectActuator(SCA_IActuator)

	Edit Object Actuator (in End Object mode)

	This actuator has no python methods."""
	pass

class KX_SCA_ReplaceMeshActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_SCA_ReplaceMeshActuator(SCA_IActuator)

	Edit Object actuator, in Replace Mesh mode.

	Warning: Replace mesh actuators will be ignored if at game start, the named mesh doesn't exist.
	This will generate a warning in the console

	Error: GameObject 'Name' ReplaceMeshActuator 'ActuatorName' without object"""

	def __init__(self):
		self.mesh = 0
		self.useDisplayMesh = 0
		self.usePhysicsMesh = 0
	
	def instantReplaceMesh():
		pass

	pass

class KX_Scene(PyObjectPlus):
	"""base class - PyObjectPlus

	class bge.KX_Scene(PyObjectPlus)

	An active scene that gives access to objects, cameras, lights and scene attributes.

	The activity culling stuff is supposed to disable logic bricks when their owner gets too far from the active camera. It was taken from some code lurking at the back of KX_Scene - who knows what it does!"""

	def __init__(self):
		self.name = 0
		self.objects = 0
		self.objectsInactive = 0
		self.lights = 0
		self.cameras = 0
		self.active_camera = 0
		self.world = 0
		self.suspended = 0
		self.activity_culling = 0
		self.activity_culling_radius = 0
		self.dbvt_culling = 0
		self.pre_draw = 0
		self.post_draw = 0
		self.pre_draw_setup = 0
		self.gravity = 0
	
	def addObject():
		"""Adds an object to the scene like the Add Object Actuator would.

		Parameters:
		object (KX_GameObject or string) - The (name of the) object to add.
		reference (KX_GameObject or string) - The (name of the) object which position, orientation, and scale to copy (optional), if the object to add is a light and there is not reference the light's layer will be the same that the active layer in the blender scene.
		time (integer) - The lifetime of the added object, in frames. A time of 0 means the object will last forever (optional).

		Returns:	
		The newly added object.

		Return type:
		KX_GameObject"""
		value = KX_GameObject
		return value
		
	def end():
		"""Removes the scene from the game."""
		pass
		
	def restart():
		"""Restarts the scene."""
		pass
		
	def replace():
		"""Replaces this scene with another one.

		Parameters:
		scene (string) - The name of the scene to replace this scene with.

		Returns:	
		True if the scene exists and was scheduled for addition, False otherwise.

		Return type:
		boolean"""
		return True
		
	def suspend():
		"""Suspends this scene."""
		pass
		
	def resume():
		"""Resume this scene."""
		pass
		
	def get():
		"""Return the value matching key, or the default value if its not found.
		
		Return: The key value or a default."""
		pass
		
	def drawObstacleSimulation():
		"""Draw debug visualization of obstacle simulation."""
		pass

	pass

class KX_SceneActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_SceneActuator(SCA_IActuator)

	Scene Actuator logic brick.

	Warning: Scene actuators that use a scene name will be ignored if at game start, the named scene doesn't exist or is empty
	This will generate a warning in the console:

	Error: GameObject 'Name' has a SceneActuator 'ActuatorName' (SetScene) without scene"""

	def __init__(self):
		self.scene = 0
		self.camera = 0
		self.useRestart = 0
		self.mode = 0

class KX_SoundActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_SoundActuator(SCA_IActuator)

	Sound Actuator.

	The startSound, pauseSound and stopSound do not require the actuator to be activated - they act instantly provided that the actuator has been activated once at least."""

	def __init__(self):
		self.volume = 0
		self.time = 0
		self.pitch = 0
		self.mode = 0
		self.sound = 0
		self.is3D = 0
		self.volume_maximum = 0
		self.volume_minimum = 0
		self.distance_reference = 0
		self.distance_maximum = 0
		self.attenuation = 0
		self.cone_angle_inner = 0
		self.cone_angle_outer = 0
	
	def startSound():
		"""Starts the sound.

		Returns:
		None"""
		return None
		
	def pauseSound():
		"""Pauses the sound.

		Returns:
		None"""
		return None
		
	def stopSound():
		"""Stops the sound.

		Returns:
		None"""
		return None
		
	pass

class KX_StateActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_StateActuator(SCA_IActuator)

	State actuator changes the state mask of parent object."""

	def __init__(self):
		self.operation = 0
		self.mask = 0

class KX_SteeringActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_SteeringActuator(SCA_IActuator)

	Steering Actuator for navigation."""

	def __init__(self):
		self.behavior = 0
		self.velocity = 0
		self.acceleration = 0
		self.turnspeed = 0
		self.distance = 0
		self.target = 0
		self.navmesh = 0
		self.selfterminated = 0
		self.enableVisualization = 0
		self.pathUpdatePeriod = 0

class KX_TrackToActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_TrackToActuator(SCA_IActuator)

	Edit Object actuator in Track To mode.

	Warning: Track To Actuators will be ignored if at game start, the object to track to is invalid.
	This will generate a warning in the console:

	GameObject 'Name' no object in EditObjectActuator 'ActuatorName'"""

	def __init__(self):
		self.object = 0
		self.time = 0
		self.use3D = 0
		self.upAxis = 0
		self.trackAxis = 0

class KX_VehicleWrapper(PyObjectPlus):
	"""base class - PyObjectPlus

	class bge.KX_VehicleWrapper(PyObjectPlus)

	KX_VehicleWrapper

	TODO - description"""
	
	def addWheel():
		"""Add a wheel to the vehicle

		Parameters:	
		wheel (KX_GameObject or a KX_GameObject name) - The object to use as a wheel.
		attachPos (vector of 3 floats) - The position to attach the wheel, relative to the chassis object center.
		downDir (vector of 3 floats) - The direction vector pointing down to where the vehicle should collide with the floor.
		axleDir (vector of 3 floats) - The axis the wheel rotates around, relative to the chassis.
		suspensionRestLength (float) - The length of the suspension when no forces are being applied.
		wheelRadius (float) - The radius of the wheel (half the diameter).
		hasSteering (boolean) - True if the wheel should turn with steering, typically used in front wheels."""
		pass
		
	def applyBraking():
		"""Apply a braking force to the specified wheel

		Parameters:	
		force (float) - the brake force
		wheelIndex (integer) - index of the wheel where the force needs to be applied"""
		pass
		
	def applyEngineForce():
		"""Apply an engine force to the specified wheel

		Parameters:	
		force (float) - the engine force
		wheelIndex (integer) - index of the wheel where the force needs to be applied"""
		pass
		
	def getConstraintId():
		"""Get the constraint ID

		Returns:	
		the constraint id

		Return type:
		integer"""
		return 0
		
	def getConstraintType():
		"""Returns the constraint type.

		Returns:	
		constraint type

		Return type:
		integer"""
		return 0
		
	def getNumWheels():
		"""Returns the number of wheels.

		Returns:	
		the number of wheels for this vehicle

		Return type:
		integer"""
		return 0
		
	def getWheelOrientationQuaternion():
		"""Returns the wheel orientation as a quaternion.

		Parameters:
		wheelIndex (integer) - the wheel index

		Returns:	
		TODO Description

		Return type:
		TODO - type should be quat as per method name but from the code it looks like a matrix"""
		return [(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0)]
		
	def getWheelPosition():
		"""Returns the position of the specified wheel

		Parameters:
		wheelIndex (integer) - the wheel index

		Returns:	
		position vector

		Return type:
		list[x, y, z]"""
		return [0.0,0.0,0.0]
		
	def getWheelRotation():
		"""Returns the rotation of the specified wheel

		Parameters:
		wheelIndex (integer) - the wheel index

		Returns:	
		the wheel rotation

		Return type:
		float"""
		return 0.0
		
	def setRollInfluence():
		"""Set the specified wheel's roll influence. The higher the roll influence the more the vehicle will tend to roll over in corners.

		Parameters:
		rollInfluece (float) - the wheel roll influence
		wheelIndex (integer) - the wheel index"""
		pass
		
	def setSteeringValue():
		"""Set the specified wheel's steering

		Parameters:
		steering (float) - the wheel steering
		wheelIndex (integer) - the wheel index"""
		pass
	def setSuspensionCompression():
		"""Set the specified wheel's compression

		Parameters:
		compression (float) - the wheel compression
		wheelIndex (integer) - the wheel index"""
		pass
		
	def setSuspensionDamping():
		"""Set the specified wheel's damping

		Parameters:
		damping (float) - the wheel damping
		wheelIndex (integer) - the wheel index"""
		pass
		
	def setSuspensionStiffness():
		"""Set the specified wheel's stiffness

		Parameters:
		stiffness (float) - the wheel stiffness
		wheelIndex (integer) - the wheel index"""
		pass
		
	def setTyreFriction():
		"""Set the specified wheel's tyre friction

		Parameters:
		friction (float) - the tyre friction
		wheelIndex (integer) - the wheel index"""
		pass
		
	pass

class KX_VertexProxy(SCA_IObject):
	"""base class - SCA_IObject

	class bge.KX_VertexProxy(SCA_IObject)

	A vertex holds position, UV, color and normal information.

	Note: The physics simulation is NOT currently updated - physics will not respond to changes in the vertex position."""

	def __init__(self):
		self.XYZ = 0
		self.UV = 0
		self.normal = 0
		self.color = 0
		self.x = 0
		self.y = 0
		self.z = 0
		self.u = 0
		self.v = 0
		self.u2 = 0
		self.v2 = 0
		self.r = 0
		self.g = 0
		self.b = 0
		self.a = 0
	
	def getXYZ():
		"""Gets the position of this vertex.

		Returns:	
		this vertexes position in local coordinates.

		Return type:
		Vector((x, y, z))"""
		return ((0.0,0.0,0.0))
		
	def setXYZ():
		"""Sets the position of this vertex.

		Type:
		Vector((x, y, z))

		Parameters:
		pos - the new position for this vertex in local coordinates."""
		pass
		
	def getUV():
		"""Gets the UV (texture) coordinates of this vertex.

		Returns:	
		this vertexes UV (texture) coordinates.

		Return type:
		Vector((u, v))"""
		return ((0.0,0.0))
		
	def setUV():
		"""Sets the UV (texture) coordinates of this vertex.

		Type:
		Vector((u, v))"""
		pass
		
	def getUV2():
		"""Gets the 2nd UV (texture) coordinates of this vertex.

		Returns:	
		this vertexes UV (texture) coordinates.

		Return type:
		Vector((u, v))"""
		return ((0.0,0.0))
		
	def setUV2():
		"""Sets the 2nd UV (texture) coordinates of this vertex.

		Type:
		Vector((u, v))

		Parameters:
		unit - optional argument, FLAT==1, SECOND_UV==2, defaults to SECOND_UV
		unit - integer"""
		pass
		
	def getRGBA():
		"""Gets the color of this vertex.

		The color is represented as four bytes packed into an integer value. The color is packed as RGBA.

		Since Python offers no way to get each byte without shifting, you must use the struct module to access color in an machine independent way.

		Because of this, it is suggested you use the r, g, b and a attributes or the color attribute instead.

		import struct;
		col = struct.unpack('4B', struct.pack('I', v.getRGBA()))
		# col = (r, g, b, a)
		# black = (  0, 0, 0, 255)
		# white = (255, 255, 255, 255)

		Returns:
		packed color. 4 byte integer with one byte per color channel in RGBA format.

		Return type:
		integer"""
		return 0
		
	def setRGBA():
		"""Sets the color of this vertex.

		See getRGBA() for the format of col, and its relevant problems. Use the r, g, b and a attributes or the color attribute instead.

		setRGBA() also accepts a four component list as argument col. The list represents the color as [r, g, b, a] with black = [0.0, 0.0, 0.0, 1.0] and white = [1.0, 1.0, 1.0, 1.0]

		v.setRGBA(0xff0000ff) # Red
		v.setRGBA(0xff00ff00) # Green on little endian, transparent purple on big endian
		v.setRGBA([1.0, 0.0, 0.0, 1.0]) # Red
		v.setRGBA([0.0, 1.0, 0.0, 1.0]) # Green on all platforms.

		Parameters:
		col (integer or list [r, g, b, a]) - the new color of this vertex in packed RGBA format."""
		pass
		
	def getNormal():
		"""Gets the normal vector of this vertex.

		Returns:
		normalized normal vector.

		Return type:
		Vector((nx, ny, nz))"""
		return ((0.0,0.0,0.0))
		
	def setNormal():
		"""Sets the normal vector of this vertex.

		Type:
		sequence of floats [r, g, b]

		Parameters:
		normal - the new normal of this vertex."""
		pass
		
	pass

class KX_VisibilityActuator(SCA_IActuator):
	"""base class - SCA_IActuator

	class bge.KX_VisibilityActuator(SCA_IActuator)

	Visibility Actuator."""

	def __init__(self):
		self.visibility = 0
		self.useOcclusion = 0
		self.useRecursion = 0

class KX_WorldInfo(PyObjectPlus):
	"""base class - PyObjectPlus

	class bge.KX_WorldInfo(PyObjectPlus)

	A world object.

	# Set the mist color to red.
	import bge

	sce = bge.logic.getCurrentScene()

	sce.world.mistColor = [1.0, 0.0, 0.0]"""

	# Constants
	KX_MIST_QUADRATIC = 0
	KX_MIST_LINEAR = 0
	KX_MIST_INV_QUADRATIC = 0

	def __init__(self):
		self.mistEnable = 0
		self.mistStart = 0
		self.mistDistance = 0
		self.mistIntensity = 0
		self.mistType = 0
		self.mistColor = 0
		self.backgroundColor = 0
		self.ambientColor = 0
