"""Module to create and control physics constraints."""

from .. import types as _types


# Constants
error = ""  # type: str
"""Symbolic constant string that indicates error."""

# Debug Mode Constants
DBG_NODEBUG = 0  # type: int
"""No debug. Debug mode to be used with bge.constraints.setDebugMode()."""

DBG_DRAWWIREFRAME = 1  # type: int
"""Draw wireframe in debug. Debug mode to be used with bge.constraints.setDebugMode()."""

DBG_DRAWAABB = 2  # type: int
"""Draw Axis Aligned Bounding Box in debug. Debug mode to be used with bge.constraints.setDebugMode()."""

DBG_DRAWFREATURESTEXT = 4  # type: int
"""Draw features text in debug. Debug mode to be used with bge.constraints.setDebugMode()."""

DBG_DRAWCONTACTPOINTS = 8  # type: int
"""Draw contact points in debug. Debug mode to be used with bge.constraints.setDebugMode()."""

DBG_NOHELPTEXT = 32  # type: int
"""Debug without help text. Debug mode to be used with bge.constraints.setDebugMode()."""

DBG_DRAWTEXT = 64  # type: int
"""Draw text in debug. Debug mode to be used with bge.constraints.setDebugMode()."""

DBG_PROFILETIMINGS = 128  # type: int
"""Draw profile timings in debug. Debug mode to be used with bge.constraints.setDebugMode()."""

DBG_ENABLESATCOMPARISION = 256  # type: int
"""Enable sat comparison in debug. Debug mode to be used with bge.constraints.setDebugMode()."""

DBG_DISABLEBULLETLCP = 512  # type: int
"""Disable Bullet LCP. Debug mode to be used with bge.constraints.setDebugMode()."""

DBG_ENABLECCD = 1024  # type: int
"""Enable Continuous Collision Detection in debug. Debug mode to be used with bge.constraints.setDebugMode()."""

DBG_DRAWCONSTRAINTS = 2048  # type: int
"""Draw constraints in debug. Debug mode to be used with bge.constraints.setDebugMode()."""

DBG_DRAWCONSTRAINTSLIMITS = 4096  # type: int
"""Draw constraint limits in debug. Debug mode to be used with bge.constraints.setDebugMode()."""

DBG_FASTWIREFRAME = 8192  # type: int
"""Draw a fast wireframe in debug. Debug mode to be used with bge.constraints.setDebugMode()."""

# Create Constraints Constants
POINTTOPOINT_CONSTRAINT = 1  # type: int
"""Constraint type to be used with bge.constraints.createConstraint()."""

LINEHINGE_CONSTRAINT = 2  # type: int
"""Constraint type to be used with bge.constraints.createConstraint()."""

ANGULAR_CONSTRAINT = 3  # type: int
"""Constraint type to be used with bge.constraints.createConstraint()."""

CONETWIST_CONSTRAINT = 4  # type: int
"""Constraint type to be used with bge.constraints.createConstraint()."""

VEHICLE_CONSTRAINT = 11  # type: int
"""Constraint type to be used with bge.constraints.createConstraint()."""

GENERIC_6DOF_CONSTRAINT = 12  # type: int
"""Constraint type to be used with bge.constraints.createConstraint()."""


# Functions
def createConstraint(physicsid_1, physicsid_2, constraint_type, pivot_x=0.0, pivot_y=0.0, pivot_z=0.0, axis_x=0.0, axis_y=0.0, axis_z=0.0, flag=0):
    # type: (int, int, int, float, float, float, float, float, float, int) -> _types.KX_ConstraintWrapper
    """Creates a constraint.

    Args:
        physicsid_1 (int): The physics id of the first object in constraint.
        physicsid_2 (int): The physics id of the second object in constraint.
        constraint_type (int): The type of the constraint, see Create Constraint Constants.
        pivot_x (float): Pivot X position. (optional)
        pivot_y (float): Pivot Y position. (optional)
        pivot_z (float): Pivot Z position. (optional)
        axis_x (float): X axis angle in degrees. (optional)
        axis_y (float): Y axis angle in degrees. (optional)
        axis_z (float): Z axis angle in degrees. (optional)
        flag (int): 128 to disable collision between linked bodies. (optional)

    Returns:
        KX_ConstraintWrapper: A constraint wrapper."""

    pass


def createVehicle(physicsid):
    # type: (int) -> _types.KX_VehicleWrapper
    """Creates a vehicle constraint.

    Args:
        physicsid (int): The physics id of the chassis object in constraint.

    Returns:
        KX_VehicleWrapper: A vehicle constraint wrapper."""

    pass


def exportBulletFile(filename):
    # type: (str) -> None
    """Exports a file representing the dynamics world (usually using .bullet extension).
    See Bullet binary serialization.

    Args:
        filename (str): File path."""

    pass


def getAppliedImpulse(constraintId):
    # type: (int) -> float
    """Args:
        constraintId (int): The id of the constraint.

    Returns:
        float: The most recent applied impulse."""

    pass


def getVehicleConstraint(constraintId):
    # type: (int) -> _types.KX_VehicleWrapper
    """Args:
        constraintId (int): The id of the vehicle constraint.

    Returns:
        KX_VehicleWrapper: A vehicle constraint object."""

    pass


def getCharacter(gameobj):
    # type: (_types.KX_GameObject) -> _types.KX_CharacterWrapper
    """Args:
        gameobj (KX_GameObject): The game object with the character physics.

    Returns:
        KX_CharacterWrapper: Character wrapper."""

    pass


def removeConstraint(constraintId):
    # type: (int) -> None
    """Removes a constraint.

    Args:
        constraintId (int): The id of the constraint to be removed."""

    pass


def setCcdMode(ccdMode):
    # type: (int) -> None
    """Sets the CCD (Continuous Collision Detection) mode in the Physics Environment.

    Args:
        ccdMode (int): The new CCD mode.

    Note:
        Very experimental, not recommended."""

    pass


def setContactBreakingTreshold(breakingTreshold):
    # type: (float) -> None
    """Sets thresholds to do with contact point management.

    Args:
        breakingTreshold (float): The new contact breaking threshold.

    Note:
        Reasonable default is 0.02 (if units are meters)."""

    pass


def setDeactivationAngularTreshold(angularTreshold):
    # type: (float) -> None
    """Sets the angular velocity threshold.

    Args:
        angularTreshold (float): New deactivation angular threshold."""

    pass


def setDeactivationLinearTreshold(linearTreshold):
    # type: (float) -> None
    """Sets the linear velocity threshold.

    Args:
        linearTreshold (float): New deactivation linear threshold."""

    pass


def setDeactivationTime(time):
    # type: (float) -> None
    """Sets the time after which a resting rigidbody gets deactivated.

    Args:
        time (float): The deactivation time."""

    pass


def setDebugMode(mode):
    # type: (int) -> None
    """Sets the debug mode.

    Args:
        mode (int): The new debug mode, see Debug Mode Constants."""

    pass


def setGravity(x, y, z):
    # type: (float, float, float) -> None
    """Sets the gravity force.

    Args:
        x (float): Gravity X force.
        y (float): Gravity Y force.
        z (float): Gravity Z force."""

    pass


def setLinearAirDamping(damping):
    # type: (float) -> None
    """Sets the linear air damping for rigid bodies.

    Note:
        Not implemented."""

    pass


def setNumIterations(numiter):
    # type: (int) -> None
    """Sets the number of iterations for an iterative constraint solver.

    Args:
        numiter (int): New number of iterations."""

    pass


def setNumTimeSubSteps(numsubstep):
    # type: (int) -> None
    """Sets the number of sub-steps for each physics proceed. Tradeoff quality for performance.

    Args:
        numsubstep (int): New number of sub-steps."""

    pass


def setSolverDamping(damping):
    # type: (float) -> None
    """Sets the damper constant of a penalty based solver.

    Args:
        damping (float): New damping for the solver.

    Note:
        Very experimental, not recommended."""

    pass


def setSolverTau(tau):
    # type: (float) -> None
    """Sets the spring constant of a penalty based solver.

    Args:
        tau (float): New tau for the solver.

    Note:
        Very experimental, not recommended."""

    pass


def setSolverType(solverType):
    # type: (int) -> None
    """Sets the solver type.

    Args:
        solverType (int): The new type of the solver.

    Note:
        Very experimental, not recommended."""

    pass


def setSorConstant(sor):
    # type: (float) -> None
    """Sets the successive over-relaxation constant.

    Args:
        sor (float): New sor value.

    Note:
        Very experimental, not recommended."""

    pass


def setUseEpa(epa):
    # type: (bool) -> None
    """Note:
        Not implemented."""

    pass
