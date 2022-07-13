"""This module contains the classes that appear as instances in the Game Engine. A script must interact with these classes if it is to affect the behaviour of objects in a game."""

from ...mathutils import Vector as _Vector, Matrix as _Matrix, Color as _Color
from typing import Callable as _Callable


class PyObjectPlus:
    """Base class of most other types in the Game Engine."""

    def __init__(self):
        # type: () -> None

        self.invalid = False  # type: bool
        """Test if the object has been freed by the game engine and is no longer valid.

        Normally this is not a problem but when storing game engine data in the GameLogic module, KX_Scenes or other KX_GameObjects its possible to hold a reference to invalid data. Calling an attribute or method on an invalid object will raise a SystemError.

        The invalid attribute allows testing for this case without exception handling."""


class CValue(PyObjectPlus):
    """This class is a basis for other classes."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.name = ""  # type: str
        """The name of this CValue derived object (read-only)."""


class CPropValue(CValue):
    """This class has no python functions."""

    pass


class CListValue(CPropValue):
    """This is a list like object used in the game engine internally that behaves similar to a Python list in most ways.

    As well as the normal index lookup (val= clist[i]), CListValue supports string lookups (val= scene.objects["Cube"])

    Other operations such as len(clist), list(clist), clist[0:10] are also supported."""

    def __init__(self):
        # type: () -> None
        super().__init__()

    def __setitem__(self, key, value):
        # type: (str | int, object | CValue) -> None

        pass

    def __getitem__(self, item):
        # type: (str | int) -> object

        pass

    def __len__(self):
        # type: () -> int

        pass

    def append(self, val):
        # type: (object | CValue) -> None
        """Add an item to the list (like pythons append)

        Args:
            val (object): The value to add to the list.

        Warning:
            Appending values to the list can cause crashes when the list is used internally by the game engine."""

        pass

    def count(self, val):
        # type: (object | CValue) -> int
        """Count the number of instances of a value in the list.

        Args:
            val (object): The value to count instances of.

        Returns:
            int: number of instances"""

        pass

    def index(self, val):
        # type: (object | CValue) -> int
        """Return the index of a value in the list.

        Args:
            val (object): The value to search for.

        Returns:
            int: The index of the value in the list."""

        pass

    def reverse(self):
        """Reverse the order of the list."""

        pass

    def get(self, key, default=None):
        # type: (str, object) -> object | CValue
        """Return the value matching key, or the default value if its not found.

        Args:
            key (str): The key to search for.
            default (object): The default value to return if the key is not found.

        Returns:
            The key value or a default."""

        pass

    def from_id(self, id):
        # type: (int) -> object | CValue
        """This is a funtion especially for the game engine to return a value with a specific id.

        Since object names are not always unique, the id of an object can be used to get an object from the CValueList.

        Returns:
            object: The object with the specified id.

        Warning:
            - The id is derived from a memory location and will be different each time the game engine starts.
            - The id can't be stored as an integer in game object properties, as those only have a limited range that the id may not be contained in. Instead an id can be stored as a string game property and converted back to an integer for use in from_id lookups."""

        pass


class SCA_IObject(CValue):
    """This class has no Python methods."""

    pass


class KX_GameObject(SCA_IObject):
    """All game objects are derived from this class.

    Properties assigned to game objects are accessible as attributes of this class.

    Note:
        - Calling ANY method or attribute on an object that has been removed from a scene will raise a SystemError, if an object may have been removed since last accessing it use the invalid attribute to check.
        - KX_GameObject can be subclassed to extend functionality."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.parent = None # type: KX_GameObject
        """The object's parent object. (read-only)."""

        self.groupMembers = {} # type: dict[str, KX_GameObject]
        """Returns the list of group members if the object is a group object (dupli group instance), otherwise None is returned."""

        self.groupObject = None # type: KX_GameObject
        """Returns the group object (dupli group instance) that the object belongs to or None if the object is not part of a group."""

        self.children = None # type: dict[str, KX_GameObject]
        """Direct children of this object, (read-only)."""

        self.childrenRecursive = None # type: dict[str, KX_GameObject]
        """All children of this object including children's children, (read-only)."""

        self.scene = None  # type: KX_Scene
        """The object's scene. (read-only)."""

        self.name = ""  # type: str
        """The object's name. (read-only)."""

        self.mass = 0.0  # type: float
        """The object's mass"""

        self.isSuspendedDynamics = True  # type: bool
        """The object's dynamic state (read-only)."""

        self.linearDamping = 0.0  # type: float
        """The object's linear damping, also known as translational damping. Can be set simultaneously with angular damping using the setDamping() method."""

        self.angularDamping = 0.0  # type: float
        """The object's angular damping, also known as rotationation damping. Can be set simultaneously with linear damping using the setDamping() method."""

        self.linVelocityMin = 0.0  # type: float
        """Enforces the object keeps moving at a minimum velocity."""

        self.linVelocityMax = 0.0  # type: float
        """Clamp the maximum linear velocity to prevent objects moving beyond a set speed.

        Notes:
            - Applies to dynamic and rigid body objects only.
            - A value of 0.0 disables this option (rather than setting it stationary)."""

        self.angularVelocityMin = 0.0  # type: float
        """Enforces the object keeps rotating at a minimum velocity. A value of 0.0 disables this.

        Note:
            Applies to dynamic and rigid body objects only. While objects are stationary the minimum velocity will not be applied."""

        self.angularVelocityMax = 0.0  # type: float
        """Clamp the maximum angular velocity to prevent objects rotating beyond a set speed. A value of 0.0 disables clamping; it does not stop rotation.

        Note:
            Applies to dynamic and rigid body objects only."""

        self.localInertia = None  # type: _Vector
        """The object's inertia vector in local coordinates. Read only."""

        self.collisionGroup = 0  # type: int
        """The object's collision group."""

        self.collisionMask = 0  # type: int
        """The object's collision mask."""

        self.collisionCallbacks = []  # type: list[_Callable]
        """A list of functions to be called when a collision occurs.

        Callbacks should either accept one argument (object), or three arguments (object, point, normal). For simplicity, per colliding object only the first collision point is reported.

        Note:
            For backward compatibility, a callback with variable number of arguments (using *args) will be passed only the object argument. Only when there is more than one fixed argument (not counting self for methods) will the three-argument form be used."""

        self.visible = True  # type: bool
        """Visibility flag.

        Note:
            Game logic will still run for invisible objects."""

        self.record_animation = True  # type: bool
        """Record animation for this object."""

        self.color = []  # type: list[float, float, float, float]
        """The object color of the object. [r, g, b, a]"""

        self.occlusion = True  # type: bool
        """Ccclusion capability flag."""

        self.position = None  # type: _Vector
        """The object's position. [x, y, z] On write: local position, on read: world position."""

        self.orientation = None  # type: _Matrix
        """The object's orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector. On write: local orientation, on read: world orientation

        Warning:
            Deprecated. Use: localOrientation and worldOrientation."""

        self.scaling = None  # type: _Vector
        """The object's scaling factor. [sx, sy, sz] On write: local scaling, on read: world scaling.

        Warning:
            Deprecated. Use: localScale and worldScale."""

        self.localOrientation = None  # type: _Matrix
        """The object's local orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector."""

        self.worldOrientation = None  # type: _Matrix
        """The object's world orientation. 3x3 Matrix."""

        self.localScale = None  # type: _Vector
        """The object's local scaling factor. [sx, sy, sz]"""

        self.worldScale = None  # type: _Vector
        """The object's world scaling factor. [sx, sy, sz]"""

        self.localPosition = None  # type: _Vector
        """The object's local position. [x, y, z]"""

        self.worldPosition = None  # type: _Vector
        """The object's world position. [x, y, z]"""

        self.localTransform = None  # type: _Matrix
        """The object's local space transform matrix. 4x4 Matrix."""

        self.worldTransform = None  # type: _Matrix
        """The object's world space transform matrix. 4x4 Matrix."""

        self.localLinearVelocity = None  # type: _Vector
        """The object's local linear velocity. [x, y, z]"""

        self.worldLinearVelocity = None  # type: _Vector
        """"The object's world linear velocity. [x, y, z]"""

        self.localAngularVelocity = None  # type: _Vector
        """The object's local angular velocity. [x, y, z]"""

        self.worldAngularVelocity = None  # type: _Vector
        """The object's world angular velocity. [x, y, z]"""

        self.timeOffset = 0.0  # type: float
        """Adjust the slowparent delay at runtime."""

        self.state = 0  # type: int
        """The game object's state bitmask, using the first 30 bits, one bit must always be set."""

        self.meshes = []  # type: list[KX_MeshProxy]
        """A list meshes for this object."""

        self.sensors = {}  # type: dict[str, SCA_ISensor]
        """A sequence of SCA_ISensor objects with string/index lookups and iterator support."""

        self.controllers = {}  # type: dict[str, SCA_IController]
        """A sequence of SCA_IController objects with string/index lookups and iterator support."""

        self.actuators = {}  # type: dict[str, SCA_IActuator]
        """A list of SCA_IActuator with string/index lookups and iterator support."""

        self.attrDict = {}  # type: dict[str, object]
        """Get the objects internal python attribute dictionary for direct (faster) access."""

        self.life = 0.0  # type: float
        """The number of seconds until the object ends, assumes 50fps. (when added with an add object actuator), (read-only)."""

        self.debug = True  # type: bool
        """If true, the object's debug properties will be displayed on screen."""

        self.debugRecursive = True  # type: bool
        """If true, the object's and children's debug properties will be displayed on screen."""

        self.currentLodLevel = 0  # type: int
        """The index of the level of detail (LOD) currently used by this object (read-only)."""

    def endObject(self):
        # type: () -> None
        """Delete this object, can be used in place of the End Object Actuator.

        The actual removal of the object from the scene is delayed."""

        pass

    def replaceMesh(self, mesh, useDisplayMesh=True, usePhysicsMesh=False):
        # type: (KX_MeshProxy | str, bool, bool) -> None
        """Replace the mesh of this object with a new mesh. This works the same was as the actuator.

        Args:
            mesh (MeshProxy or string): mesh to replace or the meshes name.
            useDisplayMesh (boolean): when enabled the display mesh will be replaced (optional argument).
            usePhysicsMesh (boolean): when enabled the physics mesh will be replaced (optional argument)."""

        pass

    def setVisible(self, visible, recursive=False):
        # type: (bool, bool) -> None
        """Sets the game object's visible flag.

        Args:
            visible (boolean): the visible state to set.
            recursive (boolean): optional argument to set all childrens visibility flag too."""

        pass

    def setOcclusion(self, occlusion, recursive=False):
        # type: (bool, bool) -> None
        """Sets the game object's occlusion capability.

        Args:
            occlusion (boolean): the state to set the occlusion to.
            recursive (boolean): optional argument to set all childrens occlusion flag too."""

        pass

    def alignAxisToVect(self, vect, axis=2, factor=1.0):
        # type: (_Vector, int, float) -> None
        """Aligns any of the game object's axis along the given vector.

        Args:
            vect (3D vector): a vector to align the axis.
            axis (integer): The axis you want to align (0 = X axis, 1 = Y axis, 2 = Z axis)
            factor (float): Only rotate a feaction of the distance to the target vector (0.0 - 1.0)"""

        pass

    def getAxisVect(self, vect):
        # type: (_Vector) -> _Vector
        """Returns the axis vector rotates by the objects worldspace orientation. This is the equivalent of multiplying the vector by the orientation matrix.

        Args:
            vect (3D Vector): a vector to align the axis.

        Returns:
            Vector: The vector in relation to the objects rotation."""

        pass

    def applyMovement(self, movement, local=False):
        """Sets the game object's movement.

        Args:
            movement (3D Vector): movement vector.
            local (bool): if False you get the "global" movement (relative to world orientation), if True you get the "local" movement (relative to object orientation)."""

        pass

    def applyRotation(self, rotation, local=False):
        # type: (_Vector, bool) -> None
        """Sets the game object's rotation.

        Args:
            rotation (3D Vector): rotation vector.
            local (bool): ifFalse you get the "global" rotation (relative to world orientation), if True you get the "local" rotation (relative to object orientation)."""

        pass

    def applyForce(self, force, local=False):
        # type: (_Vector, bool) -> None
        """Sets the game object's force.

        This requires a dynamic object.

        Args:
            force (3D Vector): force vector.
            local (boolean): if False you get the "global" force (relative to world orientation), if True you get the "local" force (relative to object orientation)."""

        pass

    def applyTorque(self, torque, local=False):
        # type: (_Vector, bool) -> None
        """Sets the game object's torque.

        This requires a dynamic object.

        Args:
            torque (3D Vector): torque vector.
            local (boolean): if False you get the "global" torque (relative to world orientation), if True you get the "local" torque (relative to object orientation)."""

        pass

    def getLinearVelocity(self, local=False):
        # type: (bool) -> _Vector
        """Gets the game object's linear velocity.

        This method returns the game object's velocity through it's centre of mass, ie no angular velocity component.

        Args:
            local (boolean): if False you get the "global" velocity (relative to world orientation), if True you get the "local" velocity (relative to object orientation).

        Returns:
            Vector: The object's linear velocity."""

        pass

    def setLinearVelocity(self, velocity, local=False):
        # type: (_Vector, bool) -> None
        """Sets the game object's linear velocity.

        This method sets game object's velocity through it's centre of mass, ie no angular velocity component.

        This requires a dynamic object.

        Args:
            velocity (3D Vector): linear velocity vector.
            local (boolean): if False you get the "global" velocity (relative to world orientation), if True you get the "local" velocity (relative to object orientation)."""

        pass

    def getAngularVelocity(self, local=False):
        # type: (bool) -> _Vector
        """Gets the game object's angular velocity.

        Args:
            local (boolean): if False you get the "global" velocity (relative to world orientation), if True you get the "local" velocity (relative to object orientation).

        Returns:
            Vector: The object's angular velocity."""

        pass

    def setAngularVelocity(self, velocity, local=False):
        # type: (_Vector, bool) -> None
        """Sets the game object's angular velocity.

        This requires a dynamic object.

        Args:
            velocity (boolean): angular velocity vector.
            local (boolean): if False you get the "global" velocity (relative to world orientation), if True you get the "local" velocity (relative to object orientation)."""

        pass

    def getVelocity(self, point=(0,0,0)):
        # type: (_Vector) -> _Vector
        """Gets the game object's velocity at the specified point.

        Gets the game object's velocity at the specified point, including angular components.

        Args:
            point (3D Vector): optional point to return the velocity for, in local coordinates.

        Returns:
            Vector: The velocity at the specified point."""

        pass

    def getReactionForce(self):
        # type: () -> _Vector
        """Gets the game object's reaction force.

        The reaction force is the force applied to this object over the last simulation timestep. This also includes impulses, eg from collisions.

        Returns:
            Vector: The reaction force of this object.

        Note:
            This is not implimented at the moment."""

        pass

    def applyImpulse(self, point, impulse, local=False):
        # type: (_Vector, _Vector, bool) -> None
        """Applies an impulse to the game object.

        This will apply the specified impulse to the game object at the specified point. If point != position, applyImpulse will also change the object's angular momentum. Otherwise, only linear momentum will change.

        Args:
            point (point [ix, iy, iz] the point to apply the impulse to (in world or local coordinates)): the point to apply the impulse to (in world or local coordinates)
            impulse (3D Vector): impulse vector.
            local (boolean): if False you get the "global" impulse (relative to world coordinates with world orientation), if True you get the "local" impulse (relative to local coordinates with object orientation)."""

        pass

    def setDamping(self, linear_damping, angular_damping):
        # type: (float, float) -> None
        """Sets both the linearDamping and angularDamping simultaneously. This is more efficient than setting both properties individually.

        Args:
            linear_damping (float ? [0, 1]): Linear ("translational") damping factor.
            angular_damping (float ? [0, 1]): Angular ("rotational") damping factor."""

        pass

    def suspendPhysics(self, freeConstraints=False):
        # type: (bool) -> None
        """Suspends physics for this object.

        Args:
            freeConstraints (bool): When set to True physics constraints used by the object are deleted. Else when False (the default) constraints are restored when restoring physics."""

        pass

    def restorePhysics(self):
        # type: () -> None
        """Resumes physics for this object. Also reinstates collisions."""

        pass

    def suspendDynamics(self, ghost=False):
        # type: (bool) -> None
        """Suspends physics for this object.

        Args:
            ghost (bool): When set to True, collisions with the object will be ignored, similar to the "ghost" checkbox in Blender. When False (the default), the object becomes static but still collide with other objects.

        Note:
            See also isSuspendDynamics allows you to inspect whether the object is in a suspended state."""
        pass

    def restoreDynamics(self):
        # type: () -> None
        """Resumes physics for this object. Also reinstates collisions; the object will no longer be a ghost.

        Note:
            The objects linear velocity will be applied from when the dynamics were suspended."""

        pass

    def enableRigidBody(self):
        # type: () -> None
        """Enables rigid body physics for this object.

        Rigid body physics allows the object to roll on collisions."""

        pass

    def disableRigidBody(self):
        # type: () -> None
        """Disables rigid body physics for this object."""

        pass

    def setParent(self, parent, compound=True, ghost=True):
        # type: (KX_GameObject, bool, bool) -> None
        """Sets this object's parent. Control the shape status with the optional compound and ghost Args:

        In that case you can control if it should be ghost or not:

        Args:
            parent (KX_GameObject): new parent object.
            compound (boolean): whether the shape should be added to the parent compound shape. If True the object shape should be added to the parent compound shape, if False the object should keep its individual shape.
            ghost (boolean): whether the object should be ghost while parented. If True the object should be made ghost while parented, if False the object should be solid while parented.

        Note:
            If the object type is sensor, it stays ghost regardless of ghost parameter"""

        pass

    def removeParent(self):
        # type: () -> None
        """Removes this objects parent."""

        pass

    def getPhysicsId(self):
        # type: () -> int
        """Returns the user data object associated with this game object's physics controller."""

        pass

    def getPropertyNames(self):
        # type: () -> list[str]
        """Gets a list of all property names.

        Returns:
            list: All property names for this object."""

        pass

    def getDistanceTo(self, other):
        # type: (KX_GameObject | _Vector) -> float
        """Get distance to another object or point.

        Args:
            other (KX_GameObject or list [x, y, z]): a point or another KX_GameObject to measure the distance to.

        Returns:
            float: distance to another object or point."""

        pass

    def getVectTo(self, other):
        # type: (KX_GameObject | _Vector) -> tuple[float, _Vector, _Vector]
        """Returns the vector and the distance to another object or point. The vector is normalized unless the distance is 0, in which a zero length vector is returned.

        Args:
            other (KX_GameObject or list [x, y, z]): a point or another KX_GameObject to get the vector and distance to.

        Returns:
            tuple: (distance, globalVector(3), localVector(3)) as 3-tuple (float, 3-tuple (x, y, z), 3-tuple (x, y, z))"""

        pass

    def rayCastTo(self, other, dist=0.0, prop=""):
        # type: (KX_GameObject | _Vector, float, str) -> KX_GameObject
        """Look towards another point/object and find first object hit within dist that matches prop.

        The ray is always casted from the center of the object, ignoring the object itself. The ray is casted towards the center of another object or an explicit [x, y, z] point. Use rayCast() if you need to retrieve the hit point

        Args:
            other (KX_GameObject or 3-tuple): [x, y, z] or object towards which the ray is casted
            dist (float): max distance to look (can be negative => look behind); 0 or omitted => detect up to other
            prop (string): property name that object must have; can be omitted => detect any object

        Returns:
            KX_GameObject: the first object hit or None if no object or object does not match prop"""

        pass

    def rayCast(self, objto, objfrom=None, dist=0, prop="", face=False, xray=False, poly=0, mask=0xFFFF):
        # type: (KX_GameObject | _Vector, _Vector, float, str, bool, bool, int, int) -> tuple[KX_GameObject, _Vector, _Vector, KX_PolyProxy, _Vector]
        """Look from a point/object to another point/object and find first object hit within dist that matches prop. if poly is 0, returns a 3-tuple with object reference, hit point and hit normal or (None, None, None) if no hit. if poly is 1, returns a 4-tuple with in addition a KX_PolyProxy as 4th element. if poly is 2, returns a 5-tuple with in addition a 2D vector with the UV mapping of the hit point as 5th element.

        Args:
            objto (KX_GameObject or 3-tuple): [x, y, z] or object to which the ray is casted
            objfrom (KX_GameObject or 3-tuple or None): [x, y, z] or object from which the ray is casted; None or omitted => use self object center
            dist (float): max distance to look (can be negative => look behind); 0 or omitted => detect up to to
            prop (string): property name that object must have; can be omitted or "" => detect any object
            face (integer): normal option. 1=>return face normal; 0 or omitted => normal is oriented towards origin
            xray (integer): X-ray option. 1=>skip objects that don't match prop; 0 or omitted => stop on first object
            poly (integer): polygon option. 0, 1 or 2 to return a 3-, 4- or 5-tuple with information on the face hit. 0 or omitted return value is a 3-tuple (object, hitpoint, hitnormal) or (None, None, None) if no hit. 1 return value is a 4-tuple and the 4th element is a KX_PolyProxy or None if no hit or the object doesn't use a mesh collision shape. 2 return value is a 5-tuple and the 5th element is a 2-tuple (u, v) with the UV mapping of the hit point or None if no hit, or the object doesn't use a mesh collision shape, or doesn't have a UV mapping.
            mask (bitfield): collision mask. The collision mask (16 layers mapped to a 16-bit integer) is combined with each object's collision group, to hit only a subset of the objects in the scene. Only those objects for which collisionGroup & mask is true can be hit.

        Returns:
            3-tuple (KX_GameObject, 3-tuple (x, y, z), 3-tuple (nx, ny, nz))
            or 4-tuple (KX_GameObject, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), KX_PolyProxy)
            or 5-tuple (KX_GameObject, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), KX_PolyProxy, 2-tuple (u, v))

        Note:
            The ray ignores the object on which the method is called. It is casted from/to object center or explicit [x, y, z] points."""

        pass

    def setCollisionMargin(self, margin):
        # type: (float) -> None
        """Set the objects collision margin.

        Args:
            margin (float): the collision margin distance in blender units.

        Note:
            If this object has no physics controller (a physics ID of zero), this function will raise RuntimeError."""

        pass

    def sendMessage(self, subject, body="", to=""):
        # type: (str, str, str) -> None
        """Sends a message.

        Args:
            subject (string): The subject of the message
            body (string): The body of the message (optional)
            to (string): The name of the object to send the message to (optional)"""

        pass

    def reinstancePhysicsMesh(self, gameObject, meshObject=None, dupli=False):
        # type: (KX_GameObject | str, KX_MeshProxy | str, bool) -> bool
        """Updates the physics system with the changed mesh.

        If no arguments are given the physics mesh will be re-created from the first mesh assigned to the game object.

        Args:
            gameObject (string, KX_GameObject or None): optional argument, set the physics shape from this gameObjets mesh.
            meshObject (string, MeshProxy or None): optional argument, set the physics shape from this mesh.

        Returns:
            bool: True if reinstance succeeded, False if it failed.

        Notes:
            - If this object has instances the other instances will be updated too.
            - The gameObject argument has an advantage that it can convert from a mesh with modifiers applied (such as subsurf).

        Warnings:
            - Only triangle mesh type objects are supported currently (not convex hull)
            - If the object is a part of a combound object it will fail (parent or child)
            - Rebuilding the physics mesh can be slow, running many times per second will give a performance hit."""

        pass

    def replacePhysicsShape(self, gameObject):
        # type: (KX_GameObject | str) -> bool
        """Replace the current physics shape.

        Args:
            gameObject (string, KX_GameObject): set the physics shape from this gameObjects."""

        pass

    def get(self, key, default=""):
        # type: (str, object) -> object
        """Return the value matching key, or the default value if its not found.

        Returns:
            The key value or a default."""

        pass

    def playAction(self, name, start_frame, end_frame, layer=0, priority=0, blendin=0, play_mode=1, layer_weight=0.0, ipo_flags=0, speed=1.0, blend_mode=1):
        # type: (str, float, float, int, int, float, int, float, int, float, int) -> None
        """Plays an action.

        Args:
            name (string): the name of the action
            start (float): the start frame of the action
            end (float): the end frame of the action
            layer (integer): the layer the action will play in (actions in different layers are added/blended together)
            priority (integer): only play this action if there isn't an action currently playing in this layer with a higher (lower number) priority
            blendin (float): the amount of blending between this animation and the previous one on this layer
            play_mode (one of these constants): the play mode
            layer_weight (float): how much of the previous layer to use for blending
            ipo_flags (int bitfield): flags for the old IPO behaviors (force, etc)
            speed (float): the playback speed of the action as a factor (1.0 = normal speed, 2.0 = 2x speed, etc)
            blend_mode (one of these constants): how to blend this layer with previous layers"""

        pass

    def stopAction(self, layer=0):
        # type: (int) -> None
        """Stop playing the action on the given layer.

        Args:
            layer (integer): The layer to stop playing."""

        pass

    def getActionFrame(self, layer=0):
        # type: (int) -> float
        """Gets the current frame of the action playing in the supplied layer.

        Args:
            layer (integer): The layer that you want to get the frame from.

        Returns:
            float: The current frame of the action"""

        pass

    def getActionName(self, layer=0):
        # type: (int) -> str
        """Gets the name of the current action playing in the supplied layer.

        Args:
            layer (integer): The layer that you want to get the action name from.

        Returns:
            str: The name of the current action"""

        pass

    def setActionFrame(self, frame, layer=0):
        # type: (float, int) -> None
        """Set the current frame of the action playing in the supplied layer.

        Args:
            layer (integer): The layer where you want to set the frame
            frame (float): The frame to set the action to"""

        pass

    def isPlayingAction(self, layer=0):
        # type: (int) -> bool
        """Checks to see if there is an action playing in the given layer.

        Args:
            layer (integer): The layer to check for a playing action.

        Returns:
            bool: Whether or not the action is playing"""

        pass

    def addDebugProperty(self, name, debug=True):
        # type: (str, bool) -> None
        """Adds a single debug property to the debug list.

        Args:
            name (string): name of the property that added to the debug list.
            debug (boolean): the debug state."""

        pass


class SCA_ILogicBrick(CValue):
    """Base class for all logic bricks."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.executePriority = 0  # type: int
        """This determines the order controllers are evaluated, and actuators are activated (lower priority is executed first)."""

        self.owner = None  # type: KX_GameObject
        """The game object this logic brick is attached to (read-only)."""

        self.name = ""  # type: str
        """The name of this logic brick (read-only)."""


class SCA_ISensor(SCA_ILogicBrick):
    """Base class for all sensor logic bricks."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.usePosPulseMode = True  # type: bool
        """Flag to turn positive pulse mode on and off."""

        self.useNegPulseMode = True  # type: bool
        """Flag to turn negative pulse mode on and off."""

        self.frequency = 0  # type: int
        """The frequency for pulse mode sensors.

        Warning:
            Deprecated. Use SCA_ISensor.skippedTicks"""

        self.skippedTicks = 0  # type: int
        """Number of logic ticks skipped between 2 active pulses."""

        self.level = True  # type: bool
        """Whether to detect level or edge transition when entering a state. It makes a difference only in case of logic state transition (state actuator). A level detector will immediately generate a pulse, negative or positive depending on the sensor condition, as soon as the state is activated. A edge detector will wait for a state change before generating a pulse.

        Note:
            Mutually exclusive with tap, enabling will disable tap."""

        self.tap = True  # type: bool
        """When enabled only sensors that are just activated will send a positive event, after this they will be detected as negative by the controllers. This will make a key thats held act as if its only tapped for an instant.

        Note:
            Mutually exclusive with level, enabling will disable level."""

        self.invert = True  # type: bool
        """Flag to set if this sensor activates on positive or negative events."""

        self.triggered = True  # type: bool
        """True if this sensor brick is in a positive state. (read-only)."""

        self.positive = True  # type: bool
        """True if this sensor brick is in a positive state. (read-only)."""

        self.pos_ticks = 0  # type: int
        """The number of ticks since the last positive pulse (read-only)."""

        self.neg_ticks = 0  # type: int
        """The number of ticks since the last negative pulse (read-only)."""

        self.status = 0  # type: int
        """The status of the sensor (read-only)."""

    def reset(self):
        # type: () -> None
        """Reset sensor internal state, effect depends on the type of sensor and settings.

        The sensor is put in its initial state as if it was just activated."""

        pass


class SCA_IActuator(SCA_ILogicBrick):
    """Base class for all actuator logic bricks."""

    pass


class SCA_IController(SCA_ILogicBrick):
    """Base class for all controller logic bricks."""


    def __init__(self):
        # type: () -> None
        super().__init__()

        self.state = 0  # type: int
        """The controllers state bitmask. This can be used with the GameObject's state to test if the controller is active."""

        self.sensors = {}  # type: dict[str, SCA_ISensor]
        """A list of sensors linked to this controller.

        Notes:
            - The sensors are not necessarily owned by the same object.
            - When objects are instanced in dupligroups links may be lost from objects outside the dupligroup."""

        self.actuators = {}  # type: dict[str, SCA_IActuator]
        """A list of actuators linked to this controller.

        Notes:
            - The sensors are not necessarily owned by the same object.
            - When objects are instanced in dupligroups links may be lost from objects outside the dupligroup."""

        self.useHighPriority = True  # type: bool
        """When set the controller executes always before all other controllers that dont have this set.

        Note:
            Order of execution between high priority controllers is not guaranteed."""


class SCA_2DFilterActuator(SCA_IActuator):
    """Create, enable and disable 2D filters.

    The following properties don't have an immediate effect. You must activate the actuator to get the result. The actuator is not persistent: it automatically stops itself after setting up the filter but the filter remains active. To stop a filter you must activate the actuator with 'type' set to RAS_2DFILTER_DISABLED or RAS_2DFILTER_NOFILTER."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.shaderText = ""  # type: str
        """Shader source code for custom shader."""

        self.disableMotionBlur = 0  # type: int
        """Action on motion blur: 0=enable, 1=disable."""

        self.mode = 0  # type: int
        """Type of 2D filter, use one of these constants."""

        self.passNumber = 0  # type: int
        """Order number of filter in the stack of 2D filters. Filters are executed in increasing order of passNb.

        Only be one filter can be defined per passNb."""

        self.value = 0.0  # type: float
        """Argument for motion blur filter."""


class SCA_ANDController(SCA_IController):
    """An AND controller activates only when all linked sensors are activated.

    There are no special Python methods for this controller."""

    pass


class SCA_ActuatorSensor(SCA_ISensor):
    """Actuator sensor detect change in actuator state of the parent object. It generates a positive pulse if the corresponding actuator is activated and a negative pulse if the actuator is deactivated."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.actuator = ""  # type: str
        """The name of the actuator that the sensor is monitoring."""


class SCA_AlwaysSensor(SCA_ISensor):
    """This sensor is always activated."""

    pass


class SCA_DelaySensor(SCA_ISensor):
    """The Delay sensor generates positive and negative triggers at precise time, expressed in number of frames. The delay parameter defines the length of the initial OFF period. A positive trigger is generated at the end of this period.

    The duration parameter defines the length of the ON period following the OFF period. There is a negative trigger at the end of the ON period. If duration is 0, the sensor stays ON and there is no negative trigger.

    The sensor runs the OFF-ON cycle once unless the repeat option is set: the OFF-ON cycle repeats indefinately (or the OFF cycle if duration is 0).

    Use SCA_ISensor.reset at any time to restart sensor."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.delay = 0  # type: int
        """Length of the initial OFF period as number of frame, 0 for immediate trigger."""

        self.duration = 0  # type: int
        """Length of the ON period in number of frame after the initial OFF period.

        If duration is greater than 0, a negative trigger is sent at the end of the ON pulse."""

        self.repeat = 0  # type: int
        """1 if the OFF-ON cycle should be repeated indefinately, 0 if it should run once."""


class SCA_InputEvent(PyObjectPlus):
    """Events for a keyboard or mouse input."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.status = []  # type: list[int]
        """A list of existing status of the input from the last frame.
        Can contain bge.logic.KX_INPUT_NONE and bge.logic.KX_INPUT_ACTIVE.
        The list always contains one value.
        The first value of the list is the last value of the list in the last frame. (read-only)"""

        self.queue = []  # type: list[int]
        """A list of existing events of the input from the last frame.
        Can contain bge.logic.KX_INPUT_JUST_ACTIVATED and bge.logic.KX_INPUT_JUST_RELEASED.
        The list can be empty. (read-only)"""

        self.values = []  # type: list[int]
        """A list of existing value of the input from the last frame.
        For keyboard it contains 1 or 0 and for mouse the coordinate of the mouse or the movement of the wheel mouse.
        The list contains always one value, the size of the list is the same than queue + 1 only for keyboard inputs.
        The first value of the list is the last value of the list in the last frame. (read-only)"""

        self.inactive = False  # type: bool
        """True if the input was inactive from the last frame."""

        self.active = False  # type: bool
        """True if the input was active from the last frame."""

        self.activated = False  # type: bool
        """True if the input was activated from the last frame."""

        self.released = False  # type: bool
        """True if the input was released from the last frame."""

        self.type = 0  # type: int
        """The type of the input. One of these constants: bge.logic.KX_INPUT_NONE, bge.logic.KX_INPUT_JUST_ACTIVATED, bge.logic.KX_INPUT_ACTIVE, bge.logic.KX_INPUT_JUST_RELEASED."""


class SCA_JoystickSensor(SCA_ISensor):
    """This sensor detects player joystick events."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.axisValues = []  # type: list[int]
        """The state of the joysticks axis as a list of values numAxis long. (read-only).

        Each specifying the value of an axis between -32767 and 32767 depending on how far the axis is pushed, 0 for nothing.
        The first 2 values are used by most joysticks and game-pads for directional control.
        3rd and 4th values are only on some joysticks and can be used for arbitrary controls."""

        self.axisSingle = 0  # type: int
        """Like axisValues but returns a single axis value that is set by the sensor. (read-only).

        Note:
            Only use this for "Single Axis" type sensors otherwise it will raise an error."""

        self.hatValues = []
        """The state of the joysticks hats as a list of values numHats long. (read-only).

        Each specifying the direction of the hat from 1 to 12, 0 when inactive.

        Hat directions are as follows:
        - 0: None
        - 1: Up
        - 2: Right
        - 4: Down
        - 8: Left
        - 3: Up - Right
        - 6: Down - Right
        - 12: Down - Left
        - 9: Up - Left

        Note:
            Deprecated. Use button instead."""

        self.hatSingle = 0  # type: int
        """Like hatValues but returns a single hat direction value that is set by the sensor. (read-only).

        Note:
            Deprecated. Use button instead."""

        self.numAxis = 0  # type: int
        """The number of axes for the joystick at this index. (read-only)."""

        self.numButtons = 0  # type: int
        """The number of buttons for the joystick at this index. (read-only)."""

        self.numHats = 0  # type: int
        """The number of hats for the joystick at this index. (read-only).

        Note:
            Deprecated. Use numButtons instead."""

        self.connected = True  # type: bool
        """True if a joystick is connected at this joysticks index. (read-only)."""

        self.index = 0  # type: int
        """The joystick index to use (from 0 to 7). The first joystick is always 0."""

        self.threshold = 0  # type: int
        """Axis threshold. Joystick axis motion below this threshold wont trigger an event. Use values between (0 and 32767), lower values are more sensitive."""

        self.button = 0  # type: int
        """The button index the sensor reacts to (first button = 0). When the “All Events” toggle is set, this option has no effect."""

        self.axis = [0, 0]  # type: list[int]
        """The axis this sensor reacts to, as a list of two values [axisIndex, axisDirection]

        - axisIndex: the axis index to use when detecting axis movement, 1=primary directional control, 2=secondary directional control.
        - axisDirection: 0 = right, 1 = up, 2 = left, 3 = down."""

        self.hat = [0, 0]  # type: list[int]
        """The hat the sensor reacts to, as a list of two values: [hatIndex, hatDirection]

        - hatIndex: the hat index to use when detecting hat movement, 1 = primary hat, 2 = secondary hat (4 max).
        - hatDirection: 1-12.

        Note:
            Deprecated. Use button instead"""

    def getButtonActiveList(self):
        # type: () -> list[int]
        """Get a list containing the indices of the currently pressed buttons.

        Returns:
            list: A list containing the indices of the currently pressed buttons."""

        pass

    def getButtonStatus(self, buttonIndex):
        # type: (int) -> bool
        """Get the current pressed state of the specified button.

        Args:
            buttonIndex (integer): the button index, 0=first button

        Returns:
            bool: The current pressed state of the specified button."""

        pass


class SCA_KeyboardSensor(SCA_ISensor):
    """A keyboard sensor detects player key presses.

    See module bge.events for keycode values."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.key = 0  # type: int
        """The key code this sensor is looking for."""

        self.hold1 = 0  # type: int
        """The key code for the first modifier this sensor is looking for."""

        self.hold2 = 0  # type: int
        """The key code for the second modifier this sensor is looking for."""

        self.toggleProperty = ""  # type: str
        """The name of the property that indicates whether or not to log keystrokes as a string."""

        self.targetProperty = ""  # type: str
        """The name of the property that receives keystrokes in case in case a string is logged."""

        self.useAllKeys = True  # type: bool
        """Flag to determine whether or not to accept all keys."""

        self.inputs = {}  # type: dict[int, SCA_InputEvent]
        """A list of pressed keys that have either been pressed, just released or active this frame. (read-only)."""

        self.events = {}  # type: dict[int, int]
        """A list of pressed keys that have either been pressed, or just released, or are active this frame. (read-only).

        Note:
            Deprecated since version use: inputs"""

    def getKeyStatus(self, keycode):
        # type: (int) -> int
        """Get the status of a key.

        Args:
            keycode (int): The code that represents the key you want to get the state of, use one of bge.events constants

        Returns:
            int: The state of the given key, can be one of these constants: bge.logic.KX_INPUT_NONE, bge.logic.KX_INPUT_JUST_ACTIVATED, bge.logic.KX_INPUT_ACTIVE, bge.logic.KX_INPUT_JUST_RELEASED."""

        pass


class SCA_MouseSensor(SCA_ISensor):
    """Mouse Sensor logic brick."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.position = (0, 0)  # type: tuple[int, int]
        """Current [x, y] coordinates of the mouse, in frame coordinates (pixels)."""

        self.mode = 0  # type: int
        """Sensor mode. One of the following constants:

        - KX_MOUSESENSORMODE_LEFTBUTTON = 1
        - KX_MOUSESENSORMODE_MIDDLEBUTTON = 2
        - KX_MOUSESENSORMODE_RIGHTBUTTON = 3
        - KX_MOUSESENSORMODE_WHEELUP = 4
        - KX_MOUSESENSORMODE_WHEELDOWN = 5
        - KX_MOUSESENSORMODE_MOVEMENT = 6"""

    def getButtonStatus(self, button):
        # type: (int) -> int
        """Get the mouse button status.

        Args:
            button (int): The code that represents the key you want to get the state of, use one of bge.events constants.

        Returns:
            int: The state of the given key, can be one of these constants: bge.logic.KX_INPUT_NONE, bge.logic.KX_INPUT_JUST_ACTIVATED, bge.logic.KX_INPUT_ACTIVE, bge.logic.KX_INPUT_JUST_RELEASED."""

        pass


class SCA_NANDController(SCA_IController):
    """An NAND controller activates when all linked sensors are not active.

    There are no special Python methods for this controller."""

    pass


class SCA_NORController(SCA_IController):
    """An NOR controller activates only when all linked sensors are de-activated.

    There are no special Python methods for this controller."""

    pass


class SCA_ORController(SCA_IController):
    """An OR controller activates when any connected sensor activates.

    There are no special Python methods for this controller."""

    pass


class SCA_PropertyActuator(SCA_IActuator):
    """Property Actuator"""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.propName = ""  # type: str
        """the property on which to operate."""

        self.value = ""  # type: str
        """the value with which the actuator operates."""

        self.mode = 0  # type: int


class SCA_PropertySensor(SCA_ISensor):
    """Activates when the game object property matches."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.mode = 0  # type: int
        """Type of check on the property."""

        self.propName = ""  # type: str
        """The property the sensor operates."""

        self.value = ""  # type: str
        """The value with which the sensor compares to the value of the property."""

        self.min = ""  # type: str
        """The minimum value of the range used to evaluate the property when in interval mode."""

        self.max = ""  # type: str
        """The maximum value of the range used to evaluate the property when in interval mode."""


class SCA_PythonController(SCA_IController):
    """A Python controller uses a Python script to activate it's actuators, based on it's sensors."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.owner = None  # type: KX_GameObject
        """The object the controller is attached to."""

        self.script = ""  # type: str
        """The value of this variable depends on the execution method.

        - When 'Script' execution mode is set this value contains the entire Python script as a single string (not the script name as you might expect) which can be modified to run different scripts.
        - When 'Module' execution mode is set this value will contain a single line string - module name and function "module.func" or "package.module.func" where the module names are python textblocks or external scripts.

        Note:
            Once this is set the script name given for warnings will remain unchanged."""

        self.mode = 0  # type: int
        """The execution mode for this controller (read-only).

        - Script: 0, Execute the script as a python code.
        - Module: 1, Execute the script as a module and function."""

    def activate(self, actuator):
        # type: (SCA_IActuator | str) -> None
        """Activates an actuator attached to this controller.

        Args:
            actuator (actuator or the actuator name as a string): The actuator to operate on."""
        pass

    def deactivate(self, actuator):
        # type: (SCA_IActuator | str) -> None
        """Deactivates an actuator attached to this controller.

        Args:
            actuator (actuator or the actuator name as a string): The actuator to operate on."""

        pass


class SCA_PythonJoystick(PyObjectPlus):
    """A Python interface to a joystick."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.name = ""  # type: str
        """The name assigned to the joystick by the operating system. (read-only)"""

        self.activeButtons = []  # type: list[int]
        """A list of active button values. (read-only)"""

        self.axisValues = []  # type: list[int]
        """The state of the joysticks axis as a list of values numAxis long. (read-only).

        Each specifying the value of an axis between -1.0 and 1.0 depending on how far the axis is pushed, 0 for nothing.
        The first 2 values are used by most joysticks and gamepads for directional control.
        3rd and 4th values are only on some joysticks and can be used for arbitary controls."""

        self.hatValues = []  # type: list[int]
        """The state of the joysticks hats as a list of values numHats long. (read-only).

        Each specifying the direction of the hat from 1 to 12, 0 when inactive.

        Hat directions are as follows:

        - 0: None
        - 1: Up
        - 2: Right
        - 4: Down
        - 8: Left
        - 3: Up - Right
        - 6: Down - Right
        - 12: Down - Left
        - 9: Up - Left

        Note:
            Deprecated. Use activeButtons instead."""

        self.numAxis = 0  # type: int
        """The number of axes for the joystick at this index. (read-only)."""

        self.numButtons = 0  # type: int
        """The number of buttons for the joystick at this index. (read-only)."""

        self.numHats = 0  # type: int
        """The number of hats for the joystick at this index. (read-only).

        Note:
            Deprecated. Use numButtons instead."""


class SCA_PythonKeyboard(PyObjectPlus):
    """The current keyboard."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.events = {}  # type: dict[int, int]
        """A dictionary containing the status of each keyboard event or key. (read-only)."""

        self.active_events = {}  # type: dict[int, int]
        """A dictionary containing the status of only the active keyboard events or keys. (read-only)."""

    def getClipboard(self):
        # type: () -> str
        """Gets the clipboard text.

        Returns:
            string"""

        pass

    def setClipboard(self, text):
        # type: (str) -> None
        """Sets the clipboard text.

        Args:
            text (string): New clipboard text"""

        pass


class SCA_PythonMouse(PyObjectPlus):
    """The current mouse."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.events = {}  # type: dict[int, int]
        """A dictionary containing the status of each mouse event. (read-only)."""

        self.active_events = {}  # type: dict[int, int]
        """A dictionary containing the status of only the active mouse events. (read-only)."""

        self.position = tuple()  # type: tuple[int, int]
        """The normalized x and y position of the mouse cursor."""

        self.visible = True  # type: bool
        """The visibility of the mouse cursor."""


class SCA_RandomActuator(SCA_IActuator):
    """Random Actuator"""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.seed = 0  # type: int
        """Seed of the random number generator."""

        self.para1 = 0.0  # type: float
        """The first parameter of the active distribution.

        Refer to the documentation of the generator types for the meaning of this value."""

        self.para2 = 0.0  # type: float
        """The second parameter of the active distribution.

        Refer to the documentation of the generator types for the meaning of this value."""

        self.distribution = 0  # type: int
        """Distribution type. (read-only).

        Can be one of these constants:

        - bge.logic.KX_RANDOMACT_BOOL_CONST = 1
        - bge.logic.KX_RANDOMACT_BOOL_UNIFORM = 2
        - bge.logic.KX_RANDOMACT_BOOL_BERNOUILLI = 3
        - bge.logic.KX_RANDOMACT_INT_CONST = 4
        - bge.logic.KX_RANDOMACT_INT_UNIFORM = 5
        - bge.logic.KX_RANDOMACT_INT_POISSON = 6
        - bge.logic.KX_RANDOMACT_FLOAT_CONST = 7
        - bge.logic.KX_RANDOMACT_FLOAT_UNIFORM = 8
        - bge.logic.KX_RANDOMACT_FLOAT_NORMAL = 9
        - bge.logic.KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL = 10"""

        self.propName = ""  # type: str
        """The name of the property to set with the random value.

        If the generator and property types do not match, the assignment is ignored."""

    def setBoolConst(self, value):
        # type: (bool) -> None
        """Sets this generator to produce a constant boolean value.

        Args:
            value (boolean): The value to return."""
        pass

    def setBoolUniform(self):
        # type: () -> None
        """Sets this generator to produce a uniform boolean distribution.

        The generator will generate True or False with 50% chance."""
        pass

    def setBoolBernouilli(self, value):
        # type: (float) -> None
        """Sets this generator to produce a Bernouilli distribution.

        Args:
            value (float): Specifies the proportion of False values to produce. 0.0: Always generate True, 1.0: Always generate False"""
        pass

    def setIntConst(self, value):
        # type: (int) -> None
        """Sets this generator to always produce the given value.

        Args:
            value (int): the value this generator produces."""
        pass

    def setIntUniform(self, lower_bound, upper_bound):
        # type: (int, int) -> None
        """Sets this generator to produce a random value between the given lower and upper bounds (inclusive)."""
        pass

    def setIntPoisson(self, value):
        # type: (int) -> None
        """Generate a Poisson-distributed number.

        This performs a series of Bernouilli tests with parameter value. It returns the number of tries needed to achieve success."""
        pass

    def setFloatConst(self, value):
        # type: (float) -> None
        """Always generate the given value."""
        pass

    def setFloatUniform(self, lower_bound, upper_bound):
        # type: (float, float) -> None
        """Generates a random float between lower_bound and upper_bound with a uniform distribution."""
        pass

    def setFloatNormal(self, mean, standard_deviation):
        # type: (float, float) -> None
        """Generates a random float from the given normal distribution.

        Args:
            mean (float): The mean (average) value of the generated numbers
            standard_deviation (float): The standard deviation of the generated numbers."""
        pass

    def setFloatNegativeExponential(self, half_life):
        # type: (float) -> None
        """Generate negative-exponentially distributed numbers.

        The half-life 'time' is characterized by half_life."""
        pass


class SCA_RandomSensor(SCA_ISensor):
    """This sensor activates randomly."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.lastDraw = 0  # type: int
        """The seed of the random number generator."""

        self.seed = 0  # type: int
        """The seed of the random number generator."""


class SCA_XNORController(SCA_IController):
    """An XNOR controller activates when all linked sensors are the same (activated or inative).

    There are no special Python methods for this controller."""

    pass


class SCA_XORController(SCA_IController):
    """An XOR controller activates when there is the input is mixed, but not when all are on or off.

    There are no special Python methods for this controller."""

    pass


class BL_ActionActuator(SCA_IActuator):
    """Action Actuators apply an action to an actor."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.action = ""  # type: str
        """The name of the action to set as the current action."""

        self.frameStart = 0.0  # type: float
        """Specifies the starting frame of the animation."""

        self.frameEnd = 0.0  # type: float
        """Specifies the ending frame of the animation."""

        self.blendIn = 0.0  # type: float
        """Specifies the number of frames of animation to generate when making transitions between actions."""

        self.priority = 0  # type: int
        """Sets the priority of this actuator. Actuators will lower priority numbers will override actuators with higher numbers."""

        self.frame = 0.0  # type: float
        """Sets the current frame for the animation."""

        self.propName = ""  # type: str
        """Sets the property to be used in FromProp playback mode."""

        self.mode = 0  # type: int
        """The operation mode of the actuator. Can be one of these constants."""

        self.blendTime = 0.0  # type: float
        """Sets the internal frame timer. This property must be in the range from 0.0 to blendIn."""

        self.useContinue = True  # type: bool
        """The actions continue option, True or False. When True, the action will always play from where last left off, otherwise negative events to this actuator will reset it to its start frame."""

        self.framePropName = ""  # type: str
        """The name of the property that is set to the current frame number."""


class BL_ArmatureActuator(SCA_IActuator):
    """Armature Actuators change constraint condition on armatures."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.type = 0  # type: int
        """The type of action that the actuator executes when it is active."""

        self.constraint = None  # type: BL_ArmatureConstraint
        """The constraint object this actuator is controlling."""

        self.target = None  # type: KX_GameObject
        """The object that this actuator will set as primary target to the constraint it controls."""

        self.subtarget = None  # type: KX_GameObject
        """The object that this actuator will set as secondary target to the constraint it controls.

        Note:
            Currently, the only secondary target is the pole target for IK constraint."""

        self.weight = 0.0  # type: float
        """The weight this actuator will set on the constraint it controls.

        Notes:
            - Currently only the IK constraint has a weight. It must be a value between 0 and 1.
            - A weight of 0 disables a constraint while still updating constraint runtime values (see BL_ArmatureConstraint)"""

        self.influence = 0.0  # type: float
        """The influence this actuator will set on the constraint it controls."""


class BL_ArmatureBone(PyObjectPlus):
    """Proxy to Blender bone structure. All fields are read-only and comply to RNA names. All space attribute correspond to the rest pose."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.parent = None  # type: BL_ArmatureBone
        """Parent bone, or None for root bone."""

        self.children = []  # type: list[BL_ArmatureBone]
        """List of bone's children."""

        self.name = ""  # type: str
        """Bone name."""

        self.connected = True  # type: bool
        """True when the bone head is struck to the parent's tail."""

        self.hinge = True  # type: bool
        """True when bone doesn't inherit rotation or scale from parent bone."""

        self.inherit_scale = True  # type: bool
        """True when bone inherits scaling from parent bone."""

        self.bbone_segments = 0  # type: int
        """Number of B-bone segments."""

        self.roll = 0.0  # type: float
        """Bone rotation around head-tail axis."""

        self.head = None  # type: _Vector
        """Location of head end of the bone in parent bone space."""

        self.tail = None  # type: _Vector
        """Location of head end of the bone in parent bone space."""

        self.length = 0.0  # type: float
        """Bone length."""

        self.arm_head = None  # type: _Vector
        """Location of head end of the bone in armature space."""

        self.arm_tail = None  # type: _Vector
        """Location of tail end of the bone in armature space."""

        self.arm_mat = None  # type: _Matrix
        """Matrix of the bone head in armature space.

        Note:
            This matrix has no scale part."""

        self.bone_mat = None  # type: _Matrix
        """Rotation matrix of the bone in parent bone space."""


class BL_ArmatureChannel(PyObjectPlus):
    """Proxy to armature pose channel. Allows to read and set armature pose. The attributes are identical to RNA attributes, but mostly in read-only mode."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.name = ""  # type: str
        """Channel name (=bone name), read-only."""

        self.bone = None  # type: BL_ArmatureBone
        """Return the bone object corresponding to this pose channel, read-only."""

        self.parent = None  # type: BL_ArmatureChannel
        """Return the parent channel object, None if root channel, read-only."""

        self.has_ik = False  # type: bool
        """True if the bone is part of an active IK chain, read-only. This flag is not set when an IK constraint is defined but not enabled (miss target information for example)."""

        self.ik_dof_x = False  # type: bool
        """True if the bone is free to rotation in the X axis, read-only."""

        self.ik_dof_y = False  # type: bool
        """True if the bone is free to rotation in the Y axis, read-only."""

        self.ik_dof_z = False  # type: bool
        """True if the bone is free to rotation in the Z axis, read-only."""

        self.ik_limit_x = False  # type: bool
        """True if a limit is imposed on X rotation, read-only."""

        self.ik_limit_y = False  # type: bool
        """True if a limit is imposed on Y rotation, read-only."""

        self.ik_limit_z = False  # type: bool
        """True if a limit is imposed on Z rotation, read-only."""

        self.ik_rot_control = False  # type: bool
        """True if channel rotation should applied as IK constraint, read-only."""

        self.ik_lin_control = False  # type: bool
        """True if channel size should applied as IK constraint, read-only."""

        self.location = None  # type: _Vector
        """Displacement of the bone head in armature local space, read-write.

        Notes:
            - You can only move a bone if it is unconnected to its parent. An action playing on the armature may change the value. An IK chain does not update this value, see joint_rotation.
            - Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see BL_ArmatureObject.update)."""

        self.scale = None  # type: _Vector
        """Scale of the bone relative to its parent, read-write.

        Notes:
            - An action playing on the armature may change the value. An IK chain does not update this value, see joint_rotation.
            - Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see BL_ArmatureObject.update)"""

        self.rotation_quaternion = None  # type: _Vector
        """Rotation of the bone relative to its parent expressed as a quaternion, read-write.

        Notes:
            - This field is only used if rotation_mode is 0. An action playing on the armature may change the value. An IK chain does not update this value, see joint_rotation.
            - Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see BL_ArmatureObject.update)"""

        self.rotation_euler = None  # type: _Vector
        """Rotation of the bone relative to its parent expressed as a set of euler angles, read-write.

        Notes:
            - This field is only used if rotation_mode is > 0. You must always pass the angles in [X, Y, Z] order; the order of applying the angles to the bone depends on rotation_mode. An action playing on the armature may change this field. An IK chain does not update this value, see joint_rotation.
            - Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see BL_ArmatureObject.update)"""

        self.rotation_mode = 0  # type: int
        """Method of updating the bone rotation, read-write."""

        self.channel_matrix = None  # type: _Matrix
        """Pose matrix in bone space (deformation of the bone due to action, constraint, etc), Read-only. This field is updated after the graphic render, it represents the current pose."""

        self.pose_matrix = None  # type: _Matrix
        """Pose matrix in armature space, read-only, This field is updated after the graphic render, it represents the current pose."""

        self.pose_head = None  # type: _Vector
        """Position of bone head in armature space, read-only."""

        self.pose_tail = None  # type: _Vector
        """Position of bone tail in armature space, read-only."""

        self.ik_min_x = 0.0  # type: float
        """Minimum value of X rotation in degree (<= 0) when X rotation is limited (see ik_limit_x), read-only."""

        self.ik_max_x = 0.0  # type: float
        """Maximum value of X rotation in degree (>= 0) when X rotation is limited (see ik_limit_x), read-only."""

        self.ik_min_y = 0.0  # type: float
        """Minimum value of Y rotation in degree (<= 0) when Y rotation is limited (see ik_limit_y), read-only."""

        self.ik_max_y = 0.0  # type: float
        """Maximum value of Y rotation in degree (>= 0) when Y rotation is limited (see ik_limit_y), read-only."""

        self.ik_min_z = 0.0  # type: float
        """Minimum value of Z rotation in degree (<= 0) when Z rotation is limited (see ik_limit_z), read-only."""

        self.ik_max_z = 0.0  # type: float
        """Maximum value of Z rotation in degree (>= 0) when Z rotation is limited (see ik_limit_z), read-only."""

        self.ik_stiffness_x = 0.0  # type: float
        """Bone rotation stiffness in X axis, read-only."""

        self.ik_stiffness_y = 0.0  # type: float
        """Bone rotation stiffness in Y axis, read-only."""

        self.ik_stiffness_z = 0.0  # type: float
        """Bone rotation stiffness in Z axis, read-only."""

        self.ik_stretch = 0.0  # type: float
        """Ratio of scale change that is allowed, 0=bone can't change size, read-only."""

        self.ik_rot_weight = 0.0  # type: float
        """Weight of rotation constraint when ik_rot_control is set, read-write."""

        self.ik_lin_weight = 0.0  # type: float
        """Weight of size constraint when ik_lin_control is set, read-write."""

        self.joint_rotation = None  # type: _Vector
        """Control bone rotation in term of joint angle (for robotic applications), read-write.

        When writing to this attribute, you pass a [x, y, z] vector and an appropriate set of euler angles or quaternion is calculated according to the rotation_mode.

        When you read this attribute, the current pose matrix is converted into a [x, y, z] vector representing the joint angles.

        The value and the meaning of the x, y, z depends on the ik_dof_x/ik_dof_y/ik_dof_z attributes:

        - 1DoF joint X, Y or Z: the corresponding x, y, or z value is used an a joint angle in radiant

        - 2DoF joint X+Y or Z+Y: treated as 2 successive 1DoF joints: first X or Z, then Y. The x or z value is used as a joint angle in radiant along the X or Z axis, followed by a rotation along the new Y axis of y radiants.

        - 2DoF joint X+Z: treated as a 2DoF joint with rotation axis on the X/Z plane. The x and z values are used as the coordinates of the rotation vector in the X/Z plane.

        - 3DoF joint X+Y+Z: treated as a revolute joint. The [x, y, z] vector represents the equivalent rotation vector to bring the joint from the rest pose to the new pose.

        Notes:
        - The bone must be part of an IK chain if you want to set the ik_dof_x/ik_dof_y/ik_dof_z attributes via the UI, but this will interfere with this attribute since the IK solver will overwrite the pose. You can stay in control of the armature if you create an IK constraint but do not finalize it (e.g. don't set a target) the IK solver will not run but the IK panel will show up on the UI for each bone in the chain.
        - [0, 0, 0] always corresponds to the rest pose.
        - You must request the armature pose to update and wait for the next graphic frame to see the effect of setting this attribute (see BL_ArmatureObject.update).
        - You can read the result of the calculation in rotation or euler_rotation attributes after setting this attribute."""


class BL_ArmatureConstraint(PyObjectPlus):
    """Proxy to Armature Constraint. Allows to change constraint on the fly. Obtained through BL_ArmatureObject.constraints.

    Note:
        Not all armature constraints are supported in the GE."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.type = 0  # type: int
        """Type of constraint, (read-only)."""

        self.name = ""  # type: str
        """Name of constraint constructed as <bone_name>:<constraint_name>. constraints list.

        This name is also the key subscript on BL_ArmatureObject."""

        self.enforce = 0.0  # type: float
        """fraction of constraint effect that is enforced. Between 0 and 1."""

        self.headtail = 0.0  # type: float
        """Position of target between head and tail of the target bone: 0=head, 1=tail.

        Note:
            Only used if the target is a bone (i.e target object is an armature."""

        self.lin_error = 0.0  # type: float
        """runtime linear error (in Blender units) on constraint at the current frame.

        This is a runtime value updated on each frame by the IK solver. Only available on IK constraint and iTaSC solver."""

        self.rot_error = 0.0  # type: float
        """Runtime rotation error (in radiant) on constraint at the current frame.

        This is a runtime value updated on each frame by the IK solver. Only available on IK constraint and iTaSC solver.

        It is only set if the constraint has a rotation part, for example, a CopyPose+Rotation IK constraint."""

        self.target = None  # type: KX_GameObject
        """Primary target object for the constraint. The position of this object in the GE will be used as target for the constraint."""

        self.subtarget = None  # type: KX_GameObject
        """Secondary target object for the constraint. The position of this object in the GE will be used as secondary target for the constraint.

        Currently this is only used for pole target on IK constraint."""

        self.active = True  # type: bool
        """True if the constraint is active.

        Note:
            An inactive constraint does not update lin_error and rot_error."""

        self.ik_weight = 0.0  # type: float
        """Weight of the IK constraint between 0 and 1.

        Only defined for IK constraint."""

        self.ik_type = 0  # type: int
        """Type of IK constraint, (read-only).

        Use one of these constants."""

        self.ik_flag = 0  # type: int
        """Combination of IK constraint option flags, read-only.

        Use one of these constants."""

        self.ik_dist = 0.0  # type: float
        """Distance the constraint is trying to maintain with target, only used when ik_type=CONSTRAINT_IK_DISTANCE."""

        self.ik_mode = 0  # type: int
        """Use one of these constants.

        Additional mode for IK constraint. Currently only used for Distance constraint."""


class BL_ArmatureObject(KX_GameObject):
    """An armature object."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.constraints = 0
        """The list of armature constraint defined on this armature. Elements of the list can be accessed by index or string. The key format for string access is '<bone_name>:<constraint_name>'."""

        self.channels = []  # type: list[BL_ArmatureChannel]
        """The list of armature channels. Elements of the list can be accessed by index or name the bone."""

    def update(self):
        # type: () -> None
        """Ensures that the armature will be updated on next graphic frame.

        This action is unecessary if a KX_ArmatureActuator with mode run is active or if an action is playing. Use this function in other cases. It must be called on each frame to ensure that the armature is updated continously."""

        pass

    def draw(self):
        # type: () -> None
        """Draw lines that represent armature to view it in real time."""

        pass

class BL_Shader(PyObjectPlus):
    """base class - PyObjectPlus

    class bge.BL_Shader(PyObjectPlus)

    BL_Shader GLSL shaders.

    TODO - Description"""

    def setUniformfv(self):
        """Set a uniform with a list of float values

        Args:
        name (string): the uniform name
        fList (list[float]): a list (2, 3 or 4 elements) of float values"""
        pass

    def delSource(self):
        """Clear the shader. Use this method before the source is changed with setSource."""
        pass

    def getFragmentProg(self):
        """Returns the fragment program.

        Returns:	The fragment program.

        Return type:
        string"""
        return "str"

    def getVertexProg(self):
        """Get the vertex program.

        Returns: The vertex program.

        Return type:
        string"""
        return "str"

    def isValid(self):
        """Check if the shader is valid.

        Returns: True if the shader is valid

        Return type:
        boolean"""
        return True

    def setAttrib(self):
        """Set attribute location. (The parameter is ignored a.t.m. and the value of "tangent" is always used.)

        Args:
        enum (integer): attribute location value"""
        pass

    def setNumberOfPasses(self):
        """Set the maximum number of passes. Not used a.t.m.

        Args:
        max_pass (integer): the maximum number of passes"""
        pass

    def setSampler(self):
        """Set uniform texture sample index.

        Args:
        name (string): Uniform name
        index (integer): Texture sample index."""
        pass

    def setSource(self):
        """Set the vertex and fragment programs

        Args:
        vertexProgram (string): Vertex program
        fragmentProgram (string): Fragment program"""
        pass

    def setUniform1f(self):
        """Set a uniform with 1 float value.

        Args:
        name (string): the uniform name
        fx (float): Uniform value"""
        pass

    def setUniform1i(self):
        """Set a uniform with an integer value.

        Args:
        name (string): the uniform name
        ix (integer): the uniform value"""
        pass

    def setUniform2f(self):
        """Set a uniform with 2 float values

        Args:
        name (string): the uniform name
        fx (float): first float value
        fy (float): second float value"""
        pass

    def setUniform2i(self):
        """Set a uniform with 2 integer values

        Args:
        name (string): the uniform name
        ix (integer): first integer value
        iy (integer): second integer value"""
        pass

    def setUniform3f(self):
        """Set a uniform with 3 float values.

        Args:
        name (string): the uniform name
        fx (float): first float value
        fy (float): second float value
        fz (float): third float value"""
        pass

    def setUniform3i(self):
        """Set a uniform with 3 integer values

        Args:
        name (string): the uniform name
        ix (integer): first integer value
        iy (integer): second integer value
        iz (integer): third integer value"""
        pass

    def setUniform4f(self):
        """Set a uniform with 4 float values.

        Args:
        name (string): the uniform name
        fx (float): first float value
        fy (float): second float value
        fz (float): third float value
        fw (float): fourth float value"""
        pass

    def setUniform4i(self):
        """Set a uniform with 4 integer values

        Args:
        name (string): the uniform name
        ix (integer): first integer value
        iy (integer): second integer value
        iz (integer): third integer value
        iw (integer): fourth integer value"""
        pass

    def setUniformDef(self):
        """Define a new uniform

        Args:
        name (string): the uniform name
        type (UNI_NONE, UNI_INT, UNI_FLOAT, UNI_INT2, UNI_FLOAT2, UNI_INT3, UNI_FLOAT3, UNI_INT4, UNI_FLOAT4, UNI_MAT3, UNI_MAT4, UNI_MAX): uniform type"""
        pass

    def setUniformMatrix3(self):
        """Set a uniform with a 3x3 matrix value

        Args:
        name (string): the uniform name
        mat (3x3 matrix): A 3x3 matrix [[f, f, f], [f, f, f], [f, f, f]]
        transpose (boolean): set to True to transpose the matrix"""
        pass

    def setUniformMatrix4(self):
        """Set a uniform with a 4x4 matrix value

        Args:
        name (string): the uniform name
        mat (4x4 matrix): A 4x4 matrix [[f, f, f, f], [f, f, f, f], [f, f, f, f], [f, f, f, f]]
        transpose (boolean): set to True to transpose the matrix"""
        pass

    def setUniformv(self):
        """Set a uniform with a list of integer values

        Args:
        name (string): the uniform name
        iList (list[integer]): a list (2, 3 or 4 elements) of integer values"""
        pass

    def validate(self):
        """Validate the shader object."""
        pass

    pass


class BL_ShapeActionActuator(SCA_IActuator):
    """ShapeAction Actuators apply an shape action to an mesh object."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.action = ""  # type: str
        """The name of the action to set as the current shape action."""

        self.frameStart = 0.0  # type: float
        """Specifies the starting frame of the shape animation."""

        self.frameEnd = 0.0  # type: float
        """Specifies the ending frame of the shape animation."""

        self.blendIn = 0.0  # type: float
        """Specifies the number of frames of animation to generate when making transitions between actions."""

        self.priority = 0  # type: int
        """Sets the priority of this actuator. Actuators will lower priority numbers will override actuators with higher numbers."""

        self.frame = 0.0  # type: float
        """Sets the current frame for the animation."""

        self.propName = ""  # type: str
        """Sets the property to be used in FromProp playback mode."""

        self.blendTime = 0.0  # type: float
        """Sets the internal frame timer. This property must be in the range from 0.0 to blendin."""

        self.mode = 0  # type: int
        """The operation mode of the actuator. Can be one of these constants."""

        self.framePropName = ""  # type: str
        """The name of the property that is set to the current frame number."""


class KX_TouchSensor(SCA_ISensor):
    """Touch sensor detects collisions between objects."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.propName = ""  # type: str
        """The property or material to collide with."""

        self.useMaterial = False  # type: bool
        """Determines if the sensor is looking for a property or material. KX_True = Find material; KX_False = Find property."""

        self.usePulseCollision = False  # type: bool
        """When enabled, changes to the set of colliding objects generate a pulse."""

        self.hitObject = None  # type: KX_GameObject
        """The last collided object. (read-only)."""

        self.hitObjectList = []  # type: list[KX_GameObject]
        """A list of colliding objects. (read-only)."""

        self.hitMaterial = ""  # type: str
        """The material of the object in the face hit by the ray. (read-only)."""


class KX_ArmatureSensor(SCA_ISensor):
    """Armature sensor detect conditions on armatures."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.type = 0  # type: int
        """The type of measurement that the sensor make when it is active. Can be one of these constants:

        - bge.logic.KX_ARMSENSOR_STATE_CHANGED
        - bge.logic.KX_ARMSENSOR_LIN_ERROR_BELOW
        - bge.logic.KX_ARMSENSOR_LIN_ERROR_ABOVE
        - bge.logic.KX_ARMSENSOR_ROT_ERROR_BELOW
        - bge.logic.KX_ARMSENSOR_ROT_ERROR_ABOVE"""

        self.constraint = None  # type: BL_ArmatureConstraint
        """The constraint object this sensor is watching."""

        self.value = 0.0  # type: float
        """The threshold used in the comparison with the constraint error.

        - The linear error is only updated on CopyPose/Distance IK constraint with iTaSC solver.
        - The rotation error is only updated on CopyPose+rotation IK constraint with iTaSC solver.
        - The linear error on CopyPose is always >= 0: it is the norm of the distance between the target and the bone.
        - The rotation error on CopyPose is always >= 0: it is the norm of the equivalent rotation vector between the bone and the target orientations.
        - The linear error on Distance can be positive if the distance between the bone and the target is greater than the desired distance, and negative if the distance is smaller."""


class KX_BlenderMaterial(PyObjectPlus):
    """This is the interface to materials in the game engine.

    Materials define the render state to be applied to mesh objects."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.shader = None  # type: BL_Shader
        """The material's shader."""

        self.blending = (0, 0)  # type: tuple[int, int]
        """Ints used for pixel blending, (src, dst), matching the setBlending method."""

        self.material_index = 0  # type: int
        """The material's index."""

        self.alpha = 0.0  # type: float
        """The material's alpha transparency."""

        self.hardness = 0  # type: int
        """How hard (sharp) the material's specular reflection is."""

        self.emit = 0.0  # type: float
        """Amount of light to emit."""

        self.ambient = 0.0  # type: float
        """Amount of ambient light on the material."""

        self.specularAlpha = 0.0  # type: float
        """Alpha transparency for specular areas."""

        self.specularIntensity = 0.0  # type: float
        """How intense (bright) the material's specular reflection is."""

        self.diffuseIntensity = 0.0  # type: float
        """The material's amount of diffuse reflection."""

        self.specularColor = None  # type: _Color
        """The material's specular color."""

        self.diffuseColor = None  # type: _Color
        """The material's diffuse color."""

        self.textures = []  # type: list[BL_Texture]
        """List of all material's textures."""

    def getTextureBindcode(textureslot):
        # type: (int) -> int
        """Returns the material's texture OpenGL bind code/id/number/name.

        Note:
            Deprecated since version use: bge.types.BL_Texture.bindCode()"""
        pass

    def getShader(self):
        # type: () -> BL_Shader
        """Returns the material's shader.

        Returns:
            BL_Shader: the material's shader"""
        pass

    def setBlending(self, src, dest):
        # type: (int, int) -> None
        """Set the pixel color arithmetic functions.

        Args:
            src (int): Specifies how the red, green, blue, and alpha source blending factors are computed
            dest (int): Specifies how the red, green, blue, and alpha destination blending factors are computed

        Arguments can be one of:

        - GL_ZERO
        - GL_ONE
        - GL_SRC_COLOR
        - GL_ONE_MINUS_SRC_COLOR
        - GL_DST_COLOR
        - GL_ONE_MINUS_DST_COLOR
        - GL_SRC_ALPHA
        - GL_ONE_MINUS_SRC_ALPHA
        - GL_DST_ALPHA
        - GL_ONE_MINUS_DST_ALPHA
        - GL_SRC_ALPHA_SATURATE"""
        pass

    def getMaterialIndex(self):
        # type: () -> int
        """Returns the material's index.

        Returns:
            int: the material's index"""
        pass


class BL_Texture(CValue):
    """A texture object that contains attributes of a material texture."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.diffuseIntensity = 0.0  # type: float
        """Amount texture affects diffuse reflectivity."""

        self.diffuseFactor = 0.0  # type: float
        """Amount texture affects diffuse color."""

        self.alpha = 0.0  # type: float
        """Amount texture affects alpha."""

        self.specularIntensity = 0.0  # type: float
        """Amount texture affects specular reflectivity."""

        self.specularFactor = 0.0  # type: float
        """Amount texture affects specular color."""

        self.hardness = 0.0  # type: float
        """Amount texture affects hardness."""

        self.emit = 0.0  # type: float
        """Amount texture affects emission."""

        self.mirror = 0.0  # type: float
        """Amount texture affects mirror color."""

        self.normal = 0.0  # type: float
        """Amount texture affects normal values."""

        self.parallaxBump = 0.0  # type: float
        """Height of parallax occlusion mapping."""

        self.parallaxStep = 0.0  # type: float
        """Number of steps to achieve parallax effect."""

        self.lodBias = 0.0  # type: float
        """Amount bias on mipmapping."""

        self.bindCode = 0  # type: int
        """Texture bind code/Id/number."""

        self.renderer = None  # type: KX_CubeMap | KX_PlanarMap
        """Texture renderer of this texture."""

        self.ior = 0.0  # type: float
        """Index Of Refraction used to compute refraction."""

        self.refractionRatio = 0.0  # type: float
        """Amount refraction mixed with reflection."""

        self.uvOffset = None  # type: _Vector
        """Offset applied to texture UV coordinates (mainly translation on U and V axis)."""

        self.uvSize = None  # type: _Vector
        """Scale applied to texture UV coordinates."""

        self.uvRotation = 0.0  # type: float
        """Rotation applied to texture UV coordinates."""


class KX_TextureRenderer(CValue):
    """Python API for object doing a render stored in a texture."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.autoUpdate = False  # type: bool
        """Choose to update automatically each frame the texture renderer or not."""

        self.viewpointObject = None  # type: KX_GameObject
        """The object where the texture renderer will render the scene."""

        self.enabled = False  # type: bool
        """Enable the texture renderer to render the scene."""

        self.ignoreLayers = 0  # type: int
        """The layers to ignore when rendering."""

        self.clipStart = 0.0  # type: float
        """The projection view matrix near plane, used for culling."""

        self.clipEnd = 0.0  # type: float
        """The projection view matrix far plane, used for culling."""

        self.lodDistanceFactor = 0.0  # type: float
        """The factor to multiply distance to camera to adjust levels of detail.
        A float < 1.0f will make the distance to camera used to compute levels of detail decrease."""

    def update(self):
        # type: () -> None
        """Request to update this texture renderer during the rendering stage.
        This function is effective only when autoUpdate is disabled."""
        pass


class KX_CubeMap(KX_TextureRenderer):
    """Python API for realtime cube map textures."""

    pass


class KX_PlanarMap(KX_TextureRenderer):
    """Python API for realtime planar map textures."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.normal = None  # type: _Vector
        """Plane normal used to compute the reflection or refraction orientation of the render camera."""

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

    def sphereInsideFrustum(self, centre, radius):
        """Tests the given sphere against the view frustum.

        Args:
        centre (list [x, y, z]): The centre of the sphere (in world coordinates.)
        radius (float): the radius of the sphere

        Returns:
        INSIDE, OUTSIDE or INTERSECT

        Return type:
        integer

        Note: When the camera is first initialized the result will be invalid because the projection matrix has not been set."""
        return 0

    def boxInsideFrustum(self, box):
        """Tests the given box against the view frustum.

        Args:
        box (list of lists): Eight (8) corner points of the box (in world coordinates.)

        Returns:
        INSIDE, OUTSIDE or INTERSECT

        Note: When the camera is first initialized the result will be invalid because the projection matrix has not been set."""
        return 0

    def pointInsideFrustum(self, point):
        """Tests the given point against the view frustum.

        Args:
        point (3D Vector): The point to test (in world coordinates.)

        Returns:
        True if the given point is inside this camera's viewing frustum.

        Return type:
        boolean

        Note: When the camera is first initialized the result will be invalid because the projection matrix has not been set."""
        return True

    def getCameraToWorld(self):
        """Returns the camera-to-world transform.

        Returns: the camera-to-world transform matrix.

        Return type:
        matrix (4x4 list)"""
        return [(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0)]

    def getWorldToCamera(self):
        """Returns the world-to-camera transform.

        This returns the inverse matrix of getCameraToWorld().

        Returns: the world-to-camera transform matrix.

        Return type:
        matrix (4x4 list)"""
        return [(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0)]

    def setOnTop(self):
        """Set this cameras viewport ontop of all other viewport."""
        pass

    def setViewport(self, left, bottom, right, top):
        """Sets the region of this viewport on the screen in pixels.

        Use bge.render.getWindowHeight and bge.render.getWindowWidth to calculate values relative to the entire display.

        Args:
        left (integer): left pixel coordinate of this viewport
        bottom (integer): bottom pixel coordinate of this viewport
        right (integer): right pixel coordinate of this viewport
        top (integer): top pixel coordinate of this viewport"""
        pass

    def getScreenPosition(self, object):
        """Gets the position of an object projected on screen space.

        # For an object in the middle of the screen, coord = [0.5, 0.5]
        coord = camera.getScreenPosition(object)

        Args:
        object (KX_GameObject or 3D Vector): object name or list [x, y, z]

        Returns:
        the object's position in screen coordinates.

        Return type:
        list [x, y]"""
        return [0,0]

    def getScreenVect(self, x, y):
        """Gets the vector from the camera position in the screen coordinate direction.

        Args:
        x (float): X Axis
        y (float): Y Axis

        Return type:
        3D Vector

        Returns:
        The vector from screen coordinate.

        # Gets the vector of the camera front direction:
        m_vect = camera.getScreenVect(0.5, 0.5)"""
        from mathutils import Vector
        return Vector(None)

    def getScreenRay(self, x, y, dist=999.0, property=None):
        """Look towards a screen coordinate (x, y) and find first object hit within dist that matches prop. The ray is similar to KX_GameObject->rayCastTo.

        Args:
        x (float): X Axis
        y (float): Y Axis
        dist (float): max distance to look (can be negative => look behind); 0 or omitted => detect up to other
        property (string): property name that object must have; can be omitted => detect any object

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

    def jump(self):
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
    """KX_ConstraintWrapper"""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.constraint_id = 0  # type: int
        """Returns the contraint ID (read only)"""

        self.constraint_type = 0  # type: int
        """Returns the contraint type (read only).

        Can be one of the following constants:

        - bge.constraints.POINTTOPOINT_CONSTRAINT = 1
        - bge.constraints.LINEHINGE_CONSTRAINT = 2
        - bge.constraints.ANGULAR_CONSTRAINT = 3
        - bge.constraints.CONETWIST_CONSTRAINT = 4
        - bge.constraints.VEHICLE_CONSTRAINT = 11
        - bge.constraints.GENERIC_6DOF_CONSTRAINT = 12"""

        self.breakingThreshold = 0.0  # type: float
        """The impulse threshold breaking the constraint, if the constraint is broken enabled is set to False."""

        self.enabled = False  # type: bool
        """The status of the constraint. Set to True to restore a constraint after breaking."""

    def getConstraintId(self):
        # type: () -> int
        """Returns the contraint ID.

        Returns:
            int: the constraint ID"""
        pass

    def setParam(self, axis, value0, value1):
        # type: (int, float, float) -> None
        """Set the contraint limits

        Args:
            axis (integer)
            value0: Set the minimum limit of the axis
            value1: Set the maximum limit of the axis"""
        pass

    def getParam(self, axis):
        # type: (int) -> float
        """Get the contraint position or euler angle of a generic 6DOF constraint.

        Args:
            axis (integer)

        Returns:
            float: position or angle"""
        pass


class KX_FontObject(KX_GameObject):
    """A Font object."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.text = ""  # type: str
        """The text displayed by this Font object."""

        self.resolution = 0.0  # type: float
        """The resolution of the font police.

        Warning:
            High resolution can use a lot of memory and may crash."""

        self.size = 0.0  # type: float
        """The size (scale factor) of the font object, scaled from font object origin (affects text resolution).

        Warning:
            High size can use a lot of memory and may crash."""

        self.dimensions = None  # type: _Vector
        """The size (width and height) of the current text in Blender Units."""


class KX_GameActuator(SCA_IActuator):
    """The game actuator loads a new .blend file, restarts the current .blend file or quits the game."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.fileName = ""  # type: str
        """The new .blend file to load."""

        self.mode = 0  # type: int
        """The mode of this actuator.

        Can be on of these constants:

        - bge.logic.KX_GAME_LOAD = 1
        - bge.logic.KX_GAME_START = 2
        - bge.logic.KX_GAME_RESTART = 3
        - bge.logic.KX_GAME_QUIT = 4
        - bge.logic.KX_GAME_SAVECFG = 5
        - bge.logic.KX_GAME_LOADCFG = 6"""


class KX_IpoActuator(SCA_IActuator):
    """IPO actuator activates an animation."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.frameStart = 0.0  # type: float
        """Start frame."""

        self.frameEnd = 0.0  # type: float
        """End frame."""

        self.propName = ""  # type: str
        """Use this property to define the Ipo position."""

        self.framePropName = ""  # type: str
        """Assign this property this action current frame number."""

        self.mode = 0  # type: int
        """Play mode for the ipo. Can be on of these constants."""

        self.useIpoAsForce = False  # type: bool
        """Apply Ipo as a global or local force depending on the local option (dynamic objects only)."""

        self.useIpoAdd = False  # type: bool
        """Ipo is added to the current loc/rot/scale in global or local coordinate according to Local flag."""

        self.useIpoLocal = False  # type: bool
        """Let the ipo acts in local coordinates, used in Force and Add mode."""

        self.useChildren = False  # type: bool
        """Update IPO on all children Objects as well."""


class KX_LibLoadStatus(PyObjectPlus):
    """An object providing information about a LibLoad() operation."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.onFinish = None  # type: _Callable
        """A callback that gets called when the lib load is done."""

        self.finished = False  # type: bool
        """The current status of the lib load."""

        self.progress = 0.0  # type: float
        """The current progress of the lib load as a normalized value from 0.0 to 1.0."""

        self.libraryName = ""  # type: str
        """The name of the library being loaded (the first argument to LibLoad)."""

        self.timeTaken = 0.0  # type: float
        """The amount of time, in seconds, the lib load took (0 until the operation is complete)."""


class KX_LightObject(KX_GameObject):
    """A Light object."""

    # Constants
    SPOT = 0  # type: int
    """A spot light source. See attribute type"""

    SUN = 0  # type: int
    """A point light source with no attenuation. See attribute type"""

    NORMAL = 0  # type: int
    """A point light source. See attribute type"""

    HEMI = 0  # type: int
    """A hemi light source. See attribute type"""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.type = 0  # type: int
        """The type of light - must be SPOT, SUN or NORMAL."""

        self.layer = 0  # type: int
        """The layer mask that this light affects object on."""

        self.energy = 0.0  # type: float
        """The brightness of this light."""

        self.shadowClipStart = 0.0  # type: float
        """The shadowmap clip start, below which objects will not generate shadows."""

        self.shadowClipEnd = 0.0  # type: float
        """The shadowmap clip end, beyond which objects will not generate shadows."""

        self.shadowFrustumSize = 0.0  # type: float
        """Size of the frustum used for creating the shadowmap."""

        self.shadowBindId = 0  # type: int
        """The OpenGL shadow texture bind number/id."""

        self.shadowMapType = 0  # type: int
        """The shadow shadow map type (0 -> Simple; 1 -> Variance)"""

        self.shadowBias = 0.0  # type: float
        """The shadow buffer sampling bias."""

        self.shadowBleedBias = 0.0  # type: float
        """The bias for reducing light-bleed on variance shadow maps."""

        self.useShadow = False  # type: bool
        """Returns True if the light has Shadow option activated, else returns False."""

        self.shadowColor = None  # type: _Color
        """The color of this light shadows. Black = (0.0, 0.0, 0.0), White = (1.0, 1.0, 1.0)."""

        self.shadowMatrix = None  # type: _Matrix

        self.distance = 0.0  # type: float
        """The maximum distance this light can illuminate. (SPOT and NORMAL lights only)."""

        self.color = [1.0, 1.0, 1.0]  # type: list[float]
        """The color of this light. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0]."""

        self.lin_attenuation = 0.0  # type: float
        """The linear component of this light's attenuation. (SPOT and NORMAL lights only)."""

        self.quad_attenuation = 0.0  # type: float
        """The quadratic component of this light's attenuation (SPOT and NORMAL lights only)."""

        self.spotsize = 0.0  # type: float
        """The cone angle of the spot light, in degrees (SPOT lights only)."""

        self.spotblend = 0.0  # type: float
        """Specifies the intensity distribution of the spot light (SPOT lights only)."""

        self.staticShadow = False  # type: bool
        """Enables static shadows.
        By default (staticShadow=False) the shadow cast by the lamp is recalculated every frame.
        When this is not needed, set staticShadow=True.
        In that case, call updateShadow() to request a shadow update."""

    def updateShadow(self):
        # type: () -> None
        """Set the shadow to be updated next frame if the lamp uses a static shadow, see staticShadow."""
        pass

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

    def getMaterialName(self):
        """Gets the name of the specified material.

        Args:
        matid (integer): the specified material.

        Returns:
        the attached material name.

        Return type:
        string"""
        return "str"

    def getTextureName(self):
        """Gets the name of the specified material's texture.

        Args:
        matid (integer): the specified material

        Returns:
        the attached material's texture name.

        Return type:
        string"""
        return "str"

    def getVertexArray(self):
        """Gets the length of the vertex array associated with the specified material.

        There is one vertex array for each material.

        Args:
        matid (integer): the specified material

        Returns:
        the number of verticies in the vertex array.

        Return type:
        integer"""
        return 0

    def getVertex(self):
        """Gets the specified vertex from the mesh object.

        Args:
        matid (integer): the specified material
        index (integer): the index into the vertex array.

        Returns:
        a vertex object.

        Return type:
        KX_VertexProxy"""
        value = KX_PolyProxy
        return value

    def getPolygon(self):
        """Gets the specified polygon from the mesh.

        Args:
        index (integer): polygon number

        Returns:
        a polygon object.

        Return type:
        KX_PolyProxy"""
        value = KX_PolyProxy
        return value

    def transform(self):
        """Transforms the vertices of a mesh.

        Args:
        matid (integer): material index, -1 transforms all.
        matrix (4x4 matrix [[float]]): transformation matrix."""
        pass

    def transformUV(self):
        """Transforms the vertices UV's of a mesh.

        Args:
        matid (integer): material index, -1 transforms all.
        matrix (4x4 matrix [[float]]): transformation matrix.
        uv_index (integer): optional uv index, -1 for all, otherwise 0 or 1.
        uv_index_from (integer): optional uv index to copy from, -1 to transform the current uv."""
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

    def reset(self):
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
    """Python interface for using and controlling navigation meshes."""

    def findPath(self, start, goal):
        # type: (_Vector, _Vector) -> list[_Vector]
        """Finds the path from start to goal points.

        Args:
            start (3D Vector): the start point
            goal (3D Vector): the goal point

        Returns:
            list: a path as a list of points"""

        pass

    def raycast(self, start, goal):
        # type: (_Vector, _Vector) -> float
        """Raycast from start to goal points.

        Args:
            start (3D Vector): the start point
            goal (3D Vector): the goal point

        Returns:
            float: the hit factor"""

        pass

    def draw(self, mode):
        # type: (int) -> None
        """Draws a debug mesh for the navigation mesh.

        Args:
            mode (integer): the drawing mode (one of these constants)"""

        pass

    def rebuild(self):
        # type: () -> None
        """Rebuild the navigation mesh."""

        pass


class KX_NearSensor(KX_TouchSensor):
    """A near sensor is a specialised form of touch sensor."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.distance = 0.0  # type: float
        """The near sensor activates when an object is within this distance."""

        self.resetDistance = 0.0  # type: float
        """The near sensor deactivates when the object exceeds this distance."""


class KX_NetworkMessageActuator(SCA_IActuator):
    """Message Actuator"""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.propName = ""  # type: str
        """Messages will only be sent to objects with the given property name."""

        self.subject = ""  # type: str
        """The subject field of the message."""

        self.body = ""  # type: str
        """The body of the message."""

        self.usePropBody = False  # type: bool
        """Send a property instead of a regular body message."""


class KX_NetworkMessageSensor(SCA_ISensor):
    """The Message Sensor logic brick.

    Currently only loopback (local) networks are supported."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.subject = ""  # type: str
        """The subject the sensor is looking for."""

        self.frameMessageCount = 0  # type: int
        """The number of messages received since the last frame. (read-only)."""

        self.subjects = []  # type: list[str]
        """The list of message subjects received. (read-only)."""

        self.bodies = []  # type: list[str]
        """The list of message bodies received. (read-only)."""

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
    """The parent actuator can set or remove an objects parent object."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.object = None  # type: KX_GameObject
        """the object this actuator sets the parent too."""

        self.mode = 0  # type: int
        """The mode of this actuator."""

        self.compound = False  # type: bool
        """Whether the object shape should be added to the parent compound shape when parenting.

        Effective only if the parent is already a compound shape."""

        self.ghost = False  # type: bool
        """Whether the object should be made ghost when parenting.

        Effective only if the shape is not added to the parent compound shape."""


class KX_PolyProxy(SCA_IObject):
    """A polygon holds the index of the vertex forming the poylgon.

    Note:
        The polygon attributes are read-only, you need to retrieve the vertex proxy if you want to change the vertex settings."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.material_name = ""  # type: str
        """The name of polygon material, empty if no material."""

        self.material = None  # type: KX_BlenderMaterial
        """The material of the polygon."""

        self.texture_name = ""  # type: str
        """The texture name of the polygon."""

        self.material_id = 0  # type: int
        """The material index of the polygon, use this to retrieve vertex proxy from mesh proxy."""

        self.v1 = 0  # type: int
        """vertex index of the first vertex of the polygon, use this to retrieve vertex proxy from mesh proxy."""

        self.v2 = 0  # type: int
        """vertex index of the second vertex of the polygon, use this to retrieve vertex proxy from mesh proxy."""

        self.v3 = 0  # type: int
        """vertex index of the third vertex of the polygon, use this to retrieve vertex proxy from mesh proxy."""

        self.v4 = 0  # type: int
        """Deprecated since version polygons: are triangles."""

        self.visible = 0  # type: int
        """visible state of the polygon: 1=visible, 0=invisible."""

        self.collide = 0  # type: int
        """collide state of the polygon: 1=receives collision, 0=collision free."""

        self.vertices = []  # type: list[KX_VertexProxy]
        """Returns the list of vertices of this polygon."""

    def getMaterialName(self):
        # type: () -> str
        """Returns the polygon material name with MA prefix.

        Returns:
            str: material name"""
        pass

    def getMaterial(self):
        # type: () -> KX_BlenderMaterial
        """Returns:
            KX_BlenderMaterial: The polygon material"""
        pass

    def getTextureName(self):
        # type: () -> str
        """Returns:
            str: The texture name"""
        pass

    def getMaterialIndex(self):
        # type: () -> int
        """Returns the material bucket index of the polygon.
        This index and the ones returned by getVertexIndex() are needed to retrieve the vertex proxy from MeshProxy.

        Returns:
            int: the material index in the mesh"""
        pass

    def getNumVertex(self):
        # type: () -> int
        """Returns the number of vertex of the polygon.

        Returns:
            int: number of vertex, 3 or 4."""
        pass

    def isVisible(self):
        # type: () -> bool
        """Returns whether the polygon is visible or not

        Returns:
            bool: 0=invisible, 1=visible"""
        pass

    def isCollider(self):
        # type: () -> int
        """Returns whether the polygon is receives collision or not

        Returns:
            int: 0=collision free, 1=receives collision"""
        pass

    def getVertexIndex(self, vertex):
        # type: (int) -> list[int]
        """Returns the mesh vertex index of a polygon vertex This index and the one returned by getMaterialIndex() are needed to retrieve the vertex proxy from MeshProxy.

        Args:
            vertex: index of the vertex in the polygon (0-3)

        Returns:
            int: mesh vertex index"""
        pass

    def getMesh(self):
        # type: () -> KX_MeshProxy
        """Returns a mesh proxy

        Returns:
            KX_MeshProxy: mesh proxy"""
        pass


class KX_RadarSensor(KX_NearSensor):
    """Radar sensor is a near sensor with a conical sensor object."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.coneOrigin = []  # type: list[float, float, float]
        """The origin of the cone with which to test. The origin is in the middle of the cone. (read-only)."""

        self.coneTarget = []  # type: list[float, float, float]
        """The center of the bottom face of the cone with which to test. (read-only)."""

        self.distance = 0.0  # type: float
        """The height of the cone with which to test."""

        self.angle = 0.0  # type: float
        """The angle of the cone (in degrees) with which to test."""

        self.axis = 0  # type: int
        """The axis on which the radar cone is cast. Can be one of these constants."""


class KX_RaySensor(SCA_ISensor):
    """A ray sensor detects the first object in a given direction."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.propName = ""  # type: str
        """The property the ray is looking for."""

        self.range = 0.0  # type: float
        """The distance of the ray."""

        self.useMaterial = False  # type: bool
        """Whether or not to look for a material (false = property)."""

        self.useXRay = False  # type: bool
        """Whether or not to use XRay."""

        self.mask = 0  # type: int
        """The collision mask (16 layers mapped to a 16-bit integer) combined with each
        object's collision group, to hit only a subset of the objects in the scene.
        Only those objects for which collisionGroup & mask is true can be hit."""

        self.hitObject = None  # type: KX_GameObject
        """The game object that was hit by the ray. (read-only)."""

        self.hitPosition = None  # type: _Vector
        """The position (in worldcoordinates) where the object was hit by the ray. (read-only)."""

        self.hitNormal = None  # type: _Vector
        """The normal (in worldcoordinates) of the object at the location where the object was hit by the ray. (read-only)."""

        self.hitMaterial = ""  # type: str
        """The material of the object in the face hit by the ray. (read-only)."""

        self.rayDirection = None  # type: _Vector
        """The direction from the ray (in worldcoordinates). (read-only)."""

        self.axis = 0  # type: int
        """The axis the ray is pointing on. Can be one of these constants."""


class KX_SCA_AddObjectActuator(SCA_IActuator):
    """Edit Object Actuator (in Add Object Mode)

    Note:
        An Add Object actuator will be ignored if at game start, the linked object doesn't exist (or is empty) or the linked object is in an active layer."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.object = None  # type: KX_GameObject
        """The object this actuator adds."""

        self.objectLastCreated = None  # type: KX_GameObject
        """The last added object from this actuator (read-only)."""

        self.time = 0.0  # type: float
        """The lifetime of added objects, in frames. Set to 0 to disable automatic deletion."""

        self.linearVelocity = []  # type: list[float, float, float]
        """The initial linear velocity of added objects."""

        self.angularVelocity = []  # type: list[float, float, float]
        """The initial angular velocity of added objects."""

    def instantAddObject(self):
        """Adds the object without needing to calling SCA_PythonController.activate()

        Note:
            Use objectLastCreated to get the newly created object."""
        pass


class KX_SCA_DynamicActuator(SCA_IActuator):
    """Dynamic Actuator."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.mode = 0  # type: int
        """The type of operation of the actuator, 0-4.

        - KX_DYN_RESTORE_DYNAMICS = 0
        - KX_DYN_DISABLE_DYNAMICS = 1
        - KX_DYN_ENABLE_RIGID_BODY = 2
        - KX_DYN_DISABLE_RIGID_BODY = 3
        - KX_DYN_SET_MASS = 4"""

        self.mass = 0.0  # type: float
        """The mass value for the KX_DYN_SET_MASS operation."""


class KX_SCA_EndObjectActuator(SCA_IActuator):
    """Edit Object Actuator (in End Object mode).

    This actuator has no Python methods."""

    pass


class KX_SCA_ReplaceMeshActuator(SCA_IActuator):
    """Edit Object actuator, in Replace Mesh mode.

    Note:
        Replace mesh actuators will be ignored if at game start, the named mesh doesn't exist. This will generate a warning in the console."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.mesh = None  # type: KX_MeshProxy
        """MeshProxy or the name of the mesh that will replace the current one. Set to None to disable actuator."""

        self.useDisplayMesh = False  # type: bool
        """When true the displayed mesh is replaced."""

        self.usePhysicsMesh = False  # type: bool
        """When true the physics mesh is replaced."""

    def instantReplaceMesh(self):
        # type: () -> None
        """Immediately replace mesh without delay."""
        pass


class KX_Scene(PyObjectPlus):
    """An active scene that gives access to objects, cameras, lights and scene attributes.

    The activity culling stuff is supposed to disable logic bricks when their owner gets too far from the active camera. It was taken from some code lurking at the back of KX_Scene - who knows what it does!"""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.name = ""  # type: str
        """The scene's name (read-only)."""

        self.objects = None # type: dict[str, KX_GameObject]
        """A list of objects in the scene, (read-only)."""

        self.objectsInactive = None # type: dict[str, KX_GameObject]
        """A list of objects on background layers (used for the addObject actuator), (read-only)."""

        self.lights = None # type: dict[str, KX_LightObject]
        """A list of lights in the scene, (read-only)."""

        self.cameras = None # type: dict[str, KX_Camera]
        """A list of cameras in the scene, (read-only)."""

        self.active_camera = None  # type: KX_Camera
        """The current active camera.

        Note:
            This can be set directly from Python to avoid using the KX_SceneActuator."""

        self.world = None  # type: KX_WorldInfo
        """The current active world, (read-only)."""

        self.suspended = True  # type: bool
        """True if the scene is suspended (read-only)."""

        self.activity_culling = True  # type: bool
        """True if the scene is activity culling."""

        self.activity_culling_radius = 0.0  # type: float
        """The distance outside which to do activity culling. Measured in manhattan distance."""

        self.dbvt_culling = True  # type: bool
        """True when Dynamic Bounding box Volume Tree is set (read-only)."""

        self.pre_draw = []  # type: list[_Callable]
        """A list of callables to be run before the render step."""

        self.post_draw = []  # type: list[_Callable]
        """A list of callables to be run after the render step."""

        self.pre_draw_setup = []  # type: list[_Callable]
        """A list of callables to be run before the drawing setup (i.e., before the model view and projection matrices are computed)."""

        self.gravity = None  # type: _Vector
        """The scene gravity using the world x, y and z axis."""

    def addObject(self, object, reference=None, time=0):
        # type: (str | KX_GameObject, str | KX_GameObject, int) -> KX_GameObject
        """Adds an object to the scene like the Add Object Actuator would.

        Args:
            object (KX_GameObject or string): The (name of the) object to add.
            reference (KX_GameObject or string): The (name of the) object which position, orientation, and scale to copy (optional), if the object to add is a light and there is not reference the light's layer will be the same that the active layer in the blender scene.
            time (integer): The lifetime of the added object, in frames. A time of 0 means the object will last forever (optional).

        Returns:
            KX_GameObject: The newly added object."""

        return

    def end(self):
        # type: () -> None
        """Removes the scene from the game."""

        pass

    def restart(self):
        # type: () -> None
        """Restarts the scene."""

        pass

    def replace(self, scene):
        # type: (str) -> bool
        """Replaces this scene with another one.

        Args:
            scene (string): The name of the scene to replace this scene with.

        Returns:
            bool: True if the scene exists and was scheduled for addition, False otherwise."""

        pass

    def suspend(self):
        # type: () -> None
        """Suspends this scene."""

        pass

    def resume(self):
        # type: () -> None
        """Resume this scene."""

        pass

    def get(self, key, default=None):
        # type: (str, object) -> object
        """Return the value matching key, or the default value if its not found.

        Returns:
            The key value or a default."""

        pass

    def drawObstacleSimulation(self):
        # type: () -> None
        """Draw debug visualization of obstacle simulation."""

        pass


class KX_SceneActuator(SCA_IActuator):
    """Scene Actuator logic brick.

    Warning:
        Scene actuators that use a scene name will be ignored if at game start, the named scene doesn't exist or is empty. This will generate a warning in the console: Error: GameObject 'Name' has a SceneActuator 'ActuatorName' (SetScene) without scene"""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.scene = ""  # type: str
        """The name of the scene to change to/overlay/underlay/remove/suspend/resume."""

        self.camera = None  # type: KX_Camera
        """The camera to change to. KX_Camera on read, string or KX_Camera on write.

        Note:
            When setting the attribute, you can use either a KX_Camera or the name of the camera."""

        self.useRestart = False  # type: bool
        """Set flag to True to restart the scene."""

        self.mode = 0  # type: int
        """The mode of the actuator."""

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

    def startSound(self):
        """Starts the sound.

        Returns:
        None"""
        return None

    def pauseSound(self):
        """Pauses the sound.

        Returns:
        None"""
        return None

    def stopSound(self):
        """Stops the sound.

        Returns:
        None"""
        return None

    pass


class KX_StateActuator(SCA_IActuator):
    """State actuator changes the state mask of parent object."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.operation = 0  # type: int
        """Type of bit operation to be applied on object state mask."""

        self.mask = 0  # type: int
        """Value that defines the bits that will be modified by the operation.

        - The bits that are 1 in the mask will be updated in the object state.
        - The bits that are 0 are will be left unmodified expect for the Copy operation which copies the mask to the object state."""


class KX_SteeringActuator(SCA_IActuator):
    """Steering Actuator for navigation."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.behavior = 0  # type: int
        """The steering behavior to use."""

        self.velocity = 0.0  # type: float
        """Velocity magnitude."""

        self.acceleration = 0.0  # type: float
        """Max acceleration."""

        self.turnspeed = 0.0  # type: float
        """Max turn speed."""

        self.distance = 0.0  # type: float
        """Relax distance."""

        self.target = None  # type: KX_GameObject
        """Target object."""

        self.navmesh = None  # type: KX_NavMeshObject | KX_GameObject
        """Navigation mesh"""

        self.selfterminated = False  # type: bool
        """Terminate when target is reached."""

        self.enableVisualization = False  # type: bool
        """Enable debug visualization."""

        self.pathUpdatePeriod = 0  # type: int
        """Path update period."""

        self.path = []  # type: list[_Vector]
        """Path point list."""


class KX_TrackToActuator(SCA_IActuator):
    """Edit Object actuator in Track To mode.

    Warning:
        Track To Actuators will be ignored if at game start, the object to track to is invalid. This will generate a warning in the console: GameObject 'Name' no object in EditObjectActuator 'ActuatorName'"""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.object = None  # type: KX_GameObject
        """The object this actuator tracks."""

        self.time = 0  # type: int
        """The time in frames with which to delay the tracking motion."""

        self.use3D = False  # type: bool
        """If tracking motion will use 3D."""

        self.upAxis = 0  # type: int
        """The axis that points upward."""

        self.trackAxis = 0  # type: int
        """The axis that points to the target object."""

class KX_VehicleWrapper(PyObjectPlus):
    """base class - PyObjectPlus

    class bge.KX_VehicleWrapper(PyObjectPlus)

    KX_VehicleWrapper

    TODO - description"""

    def addWheel(self):
        """Add a wheel to the vehicle

        Args:
        wheel (KX_GameObject or a KX_GameObject name): The object to use as a wheel.
        attachPos (vector of 3 floats): The position to attach the wheel, relative to the chassis object center.
        downDir (vector of 3 floats): The direction vector pointing down to where the vehicle should collide with the floor.
        axleDir (vector of 3 floats): The axis the wheel rotates around, relative to the chassis.
        suspensionRestLength (float): The length of the suspension when no forces are being applied.
        wheelRadius (float): The radius of the wheel (half the diameter).
        hasSteering (boolean): True if the wheel should turn with steering, typically used in front wheels."""
        pass

    def applyBraking(self):
        """Apply a braking force to the specified wheel

        Args:
        force (float): the brake force
        wheelIndex (integer): index of the wheel where the force needs to be applied"""
        pass

    def applyEngineForce(self):
        """Apply an engine force to the specified wheel

        Args:
        force (float): the engine force
        wheelIndex (integer): index of the wheel where the force needs to be applied"""
        pass

    def getConstraintId(self):
        """Get the constraint ID

        Returns:
        the constraint id

        Return type:
        integer"""
        return 0

    def getConstraintType(self):
        """Returns the constraint type.

        Returns:
        constraint type

        Return type:
        integer"""
        return 0

    def getNumWheels(self):
        """Returns the number of wheels.

        Returns:
        the number of wheels for this vehicle

        Return type:
        integer"""
        return 0

    def getWheelOrientationQuaternion(self):
        """Returns the wheel orientation as a quaternion.

        Args:
        wheelIndex (integer): the wheel index

        Returns:
        TODO Description

        Return type:
        TODO - type should be quat as per method name but from the code it looks like a matrix"""
        return [(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0)]

    def getWheelPosition(self):
        """Returns the position of the specified wheel

        Args:
        wheelIndex (integer): the wheel index

        Returns:
        position vector

        Return type:
        list[x, y, z]"""
        return [0.0,0.0,0.0]

    def getWheelRotation(self):
        """Returns the rotation of the specified wheel

        Args:
        wheelIndex (integer): the wheel index

        Returns:
        the wheel rotation

        Return type:
        float"""
        return 0.0

    def setRollInfluence(self):
        """Set the specified wheel's roll influence. The higher the roll influence the more the vehicle will tend to roll over in corners.

        Args:
        rollInfluece (float): the wheel roll influence
        wheelIndex (integer): the wheel index"""
        pass

    def setSteeringValue(self):
        """Set the specified wheel's steering

        Args:
        steering (float): the wheel steering
        wheelIndex (integer): the wheel index"""
        pass

    def setSuspensionCompression(self):
        """Set the specified wheel's compression

        Args:
        compression (float): the wheel compression
        wheelIndex (integer): the wheel index"""
        pass

    def setSuspensionDamping(self):
        """Set the specified wheel's damping

        Args:
        damping (float): the wheel damping
        wheelIndex (integer): the wheel index"""
        pass

    def setSuspensionStiffness(self):
        """Set the specified wheel's stiffness

        Args:
        stiffness (float): the wheel stiffness
        wheelIndex (integer): the wheel index"""
        pass

    def setTyreFriction(self):
        """Set the specified wheel's tyre friction

        Args:
        friction (float): the tyre friction
        wheelIndex (integer): the wheel index"""
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

    def getXYZ(self):
        """Gets the position of this vertex.

        Returns:
        this vertexes position in local coordinates.

        Return type:
        Vector((x, y, z))"""
        from mathutils import Vector
        return Vector(None)

    def setXYZ(self):
        """Sets the position of this vertex.

        Type:
        Vector((x, y, z))

        Args:
        pos - the new position for this vertex in local coordinates."""
        pass

    def getUV(self):
        """Gets the UV (texture) coordinates of this vertex.

        Returns:
        this vertexes UV (texture) coordinates.

        Return type:
        Vector((u, v))"""
        from mathutils import Vector
        return Vector(None)

    def setUV(self):
        """Sets the UV (texture) coordinates of this vertex.

        Type:
        Vector((u, v))"""
        pass

    def getUV2(self):
        """Gets the 2nd UV (texture) coordinates of this vertex.

        Returns:
        this vertexes UV (texture) coordinates.

        Return type:
        Vector((u, v))"""
        from mathutils import Vector
        return Vector(None)

    def setUV2(self):
        """Sets the 2nd UV (texture) coordinates of this vertex.

        Type:
        Vector((u, v))

        Args:
        unit - optional argument, FLAT==1, SECOND_UV==2, defaults to SECOND_UV
        unit - integer"""
        pass

    def getRGBA(self):
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

    def setRGBA(self):
        """Sets the color of this vertex.

        See getRGBA() for the format of col, and its relevant problems. Use the r, g, b and a attributes or the color attribute instead.

        setRGBA() also accepts a four component list as argument col. The list represents the color as [r, g, b, a] with black = [0.0, 0.0, 0.0, 1.0] and white = [1.0, 1.0, 1.0, 1.0]

        v.setRGBA(0xff0000ff) # Red
        v.setRGBA(0xff00ff00) # Green on little endian, transparent purple on big endian
        v.setRGBA([1.0, 0.0, 0.0, 1.0]) # Red
        v.setRGBA([0.0, 1.0, 0.0, 1.0]) # Green on all platforms.

        Args:
        col (integer or list [r, g, b, a]): the new color of this vertex in packed RGBA format."""
        pass

    def getNormal(self):
        """Gets the normal vector of this vertex.

        Returns:
        normalized normal vector.

        Return type:
        Vector((nx, ny, nz))"""
        from mathutils import Vector
        return Vector(None)

    def setNormal(self):
        """Sets the normal vector of this vertex.

        Type:
        sequence of floats [r, g, b]

        Args:
        normal - the new normal of this vertex."""
        pass

    pass


class KX_VisibilityActuator(SCA_IActuator):
    """Visibility Actuator."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.visibility = False  # type: bool
        """Whether the actuator makes its parent object visible or invisible."""

        self.useOcclusion = False  # type: bool
        """whether the actuator makes its parent object an occluder or not."""

        self.useRecursion = False  # type: bool
        """whether the visibility/occlusion should be propagated to all children of the object."""


class KX_WorldInfo(PyObjectPlus):
    """A world object."""

    # Constants
    KX_MIST_QUADRATIC = 0  # type: int
    """Type of quadratic attenuation used to fade mist. See bge.types.KX_WorldInfo.mistType."""

    KX_MIST_LINEAR = 1  # type: int
    """Type of linear attenuation used to fade mist. See bge.types.KX_WorldInfo.mistType."""

    KX_MIST_INV_QUADRATIC = 2  # type: int
    """Type of inverse quadratic attenuation used to fade mist. See bge.types.KX_WorldInfo.mistType."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.mistEnable = True  # type: bool
        """Return the state of the mist."""

        self.mistStart = 0.0  # type: float
        """The mist start point."""

        self.mistDistance = 0.0  # type: float
        """The mist distance fom the start point to reach 100% mist."""

        self.mistIntensity = 0.0  # type: float
        """The mist intensity."""

        self.mistType = 0  # type: int
        """The type of mist - must be KX_MIST_QUADRATIC, KX_MIST_LINEAR or KX_MIST_INV_QUADRATIC"""

        self.mistColor =  None  # type: _Color
        """The color of the mist. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].
        Mist and background color sould always set to the same color."""

        self.horizonColor = None  # type: _Vector
        """The horizon color. Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0].
        Mist and horizon color should always be set to the same color."""

        self.zenithColor = None  # type: _Vector
        """The zenith color. Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0]."""

        self.ambientColor = None  # type: _Color
        """The color of the ambient light. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0]."""

        self.exposure = 0.0  # type: float
        """Amount of exponential color correction for light."""

        self.range = 0.0  # type: float
        """The color range that will be mapped to 0 - 1."""

        self.envLightEnergy = 0.0  # type: float
        """The environment light energy."""

        self.envLightEnabled = False  # type: bool
        """Returns True if Environment Lighting is enabled. Else returns False"""

        self.envLightColor = None  # type: _Vector
        """White: returns 0 SkyColor: returns 1 SkyTexture: returns 2"""

        self.backgroundColor = None  # type: _Color
        """The color of the background. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].
        Mist and background color sould always set to the same color."""


class KX_PythonComponent(CValue):
    """Python component can be compared to python logic bricks with parameters. The python component is a script loaded in the UI, this script defined a component class by inheriting from KX_PythonComponent. This class must contain a dictionary of properties: args and two default functions: start() and update().

    The script must have .py extension.

    The component properties are loaded from the args attribute from the UI at loading time. When the game start the function start() is called with as arguments a dictionary of the properties' name and value. The update() function is called every frames during the logic stage before running logics bricks, the goal of this function is to handle and process everything.

    Since the components are loaded for the first time outside the bge, then bge is a fake module that contains only the class KX_PythonComponent to avoid importing all the bge modules. This behavior is safer but creates some issues at loading when the user want to use functions or attributes from the bge modules other than the KX_PythonComponent class. The way is to not call these functions at loading outside the bge. To detect it, the bge module contains the attribute __component__ when it's imported outside the bge.

    The property types supported are float, integer, boolean, string, set (for enumeration) and Vector 2D, 3D and 4D."""

    def __init__(self):
        # type: () -> None
        super().__init__()

        self.object = None  # type: KX_GameObject
        """The object owner of the component."""

        self.args = {}  # type: dict[str, object]
        """Dictionary of the component properties, the keys are string and the value can be: float, integer, Vector(2D/3D/4D), set, string."""

    def start(self, args):
        # type: (dict[str, object]) -> None
        """Initialize the component.

        Args:
            args (dict): The dictionary of the properties' name and value.

        Warning:
            This function must be inherited in the python component class."""

        pass

    def update(self):
        # type: () -> None
        """Process the logic of the component.

        Warning:
            This function must be inherited in the python component class."""

        pass
