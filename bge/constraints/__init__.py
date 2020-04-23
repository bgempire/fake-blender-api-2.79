"""Module to create and control physics constraints."""


## Functions
def createConstraint(physicsid_1, physicsid_2, constraint_type, pivot_x=0.0, pivot_y=0.0, pivot_z=0.0, axis_x=0.0, axis_y=0.0, axis_z=0.0, flag=0):
	"""Creates a constraint.

	Parameters:	
	physicsid_1 (int) - The physics id of the first object in constraint.
	physicsid_2 (int) - The physics id of the second object in constraint.
	constraint_type (int) - The type of the constraint, see Create Constraint Constants.
	pivot_x (float) - Pivot X position. (optional)
	pivot_y (float) - Pivot Y position. (optional)
	pivot_z (float) - Pivot Z position. (optional)
	axis_x (float) - X axis angle in degrees. (optional)
	axis_y (float) - Y axis angle in degrees. (optional)
	axis_z (float) - Z axis angle in degrees. (optional)
	flag (int) - 128 to disable collision between linked bodies. (optional)

	Returns:	
	A constraint wrapper.

	Return type:
	KX_ConstraintWrapper"""
	from .. import types
	return types.KX_ConstraintWrapper()
	
def createVehicle(physicsid):
	"""Creates a vehicle constraint.
	
	Parameters:
	physicsid (int) - The physics id of the chassis object in constraint.
	
	Returns:
	A vehicle constraint wrapper.
	
	Return type:
	KX_VehicleWrapper"""
	from .. import types
	return types.KX_VehicleWrapper

def exportBulletFile(filename):
	"""Exports a file representing the dynamics world (usually using .bullet extension).

	See Bullet binary serialization.

	Parameters:
	filename (str) - File path."""
	pass
	
def getAppliedImpulse(constraintId):
	"""Parameters:
	constraintId (int) - The id of the constraint.

	Returns: The most recent applied impulse.

	Return type: float"""
	return True
	
def getVehicleConstraint(constraintId):
	"""Parameters:
	constraintId (int) - The id of the vehicle constraint.

	Returns: A vehicle constraint object.

	Return type: KX_VehicleWrapper"""
	from .. import types
	return types.KX_VehicleWrapper
	
def getCharacter(gameobj):
	"""Parameters:
	gameobj (KX_GameObject) - The game object with the character physics.

	Returns:	
	Character wrapper.

	Return type:
	KX_CharacterWrapper"""
	from .. import types
	return types.KX_CharacterWrapper
	
def removeConstraint(constraintId):
	"""Removes a constraint.

	Parameters:
	constraintId (int) - The id of the constraint to be removed."""
	pass
	
def setCcdMode(ccdMode):
	"""Note: Very experimental, not recommended

	Sets the CCD (Continous Colision Detection) mode in the Physics Environment.

	Parameters:
	ccdMode (int) - The new CCD mode."""
	pass
	
def setContactBreakingTreshold(breakingTreshold):
	"""Note: Reasonable default is 0.02 (if units are meters)

	Sets tresholds to do with contact point management.

	Parameters:
	breakingTreshold (float) - The new contact breaking treshold."""
	pass
	
def setDeactivationAngularTreshold(angularTreshold):
	"""Sets the angular velocity treshold.

	Parameters:
	angularTreshold (float) - New deactivation angular treshold."""
	pass
	
def setDeactivationLinearTreshold(linearTreshold):
	"""Sets the linear velocity treshold.

	Parameters:
	linearTreshold (float) - New deactivation linear treshold."""
	pass
	
def setDeactivationTime(time):
	"""Sets the time after which a resting rigidbody gets deactived.

	Parameters:
	time (float) - The deactivation time."""
	pass
	
def setDebugMode(mode):
	"""Sets the debug mode.

	Parameters:
	mode (int) - The new debug mode, see Debug Mode Constants."""
	pass
	
def setGravity(x, y, z):
	"""Sets the gravity force.

	Parameters:
	x (float) - Gravity X force.
	y (float) - Gravity Y force.
	z (float) - Gravity Z force."""
	pass
	
def setLinearAirDamping(damping):
	"""Note: Not implemented

	Sets the linear air damping for rigidbodies."""
	pass
	
def setNumIterations(numiter):
	"""Sets the number of iterations for an iterative constraint solver.

	Parameters:
	numiter (int) - New number of iterations."""
	pass
	
def setNumTimeSubSteps(numsubstep):
	"""Sets the number of substeps for each physics proceed. Tradeoff quality for performance.

	Parameters:
	numsubstep (int) - New number of substeps."""
	pass
	
def setSolverDamping(damping):
	"""Note: Very experimental, not recommended

	Sets the damper constant of a penalty based solver.

	Parameters:
	damping (float) - New damping for the solver."""
	pass
	
def setSolverTau(tau):
	"""Note: Very experimental, not recommended

	Sets the spring constant of a penalty based solver.

	Parameters:
	tau (float) - New tau for the solver."""
	pass
	
def setSolverType(solverType):
	"""Note: Very experimental, not recommended

	Sets the solver type.

	Parameters:
	solverType (int) - The new type of the solver."""
	pass
	
def setSorConstant(sor):
	"""Note Very experimental, not recommended

	Sets the successive overrelaxation constant.

	Parameters:
	sor (float) - New sor value."""
	pass
	
def setUseEpa(epa):
	"""Note Not implemented"""
	pass

## Constants
error = ""

# Debug Mode Constants
DBG_NODEBUG = 0
DBG_DRAWWIREFRAME = 1
DBG_DRAWAABB = 2
DBG_DRAWFREATURESTEXT = 4
DBG_DRAWCONTACTPOINTS = 8
DBG_NOHELPTEXT = 32
DBG_DRAWTEXT = 64
DBG_PROFILETIMINGS = 128
DBG_ENABLESATCOMPARISION = 256
DBG_DISABLEBULLETLCP = 512
DBG_ENABLECCD = 1024
DBG_DRAWCONSTRAINTS = 2048
DBG_DRAWCONSTRAINTSLIMITS = 4096
DBG_FASTWIREFRAME = 8192

# Create Constraints Constants
POINTTOPOINT_CONSTRAINT = 1
LINEHINGE_CONSTRAINT = 2
ANGULAR_CONSTRAINT = 3
CONETWIST_CONSTRAINT = 4
VEHICLE_CONSTRAINT = 11
GENERIC_6DOF_CONSTRAINT = 12

