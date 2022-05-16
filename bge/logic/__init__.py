"""Module to access logic functions, imported automatically into the python controllers namespace."""

from .. import types as _types
from ...mathutils import Vector as _Vector

# Constants
KX_TRUE = 1  # type: int
"""True value used by some modules."""

KX_FALSE = 2  # type: int
"""False value used by some modules."""

# Sensors
# Sensor Status
KX_SENSOR_INACTIVE = 0  # type: int
"""See bge.types.SCA_ISensor.status."""

KX_SENSOR_JUST_ACTIVATED = 1  # type: int
"""See bge.types.SCA_ISensor.status."""

KX_SENSOR_ACTIVE = 2  # type: int
"""See bge.types.SCA_ISensor.status."""

KX_SENSOR_JUST_DEACTIVATED = 3  # type: int
"""See bge.types.SCA_ISensor.status."""


# Armature Sensor
KX_ARMSENSOR_STATE_CHANGED = 0  # type: int
"""Detect that the constraint is changing state (active/inactive). See bge.types.KX_ArmatureSensor.type."""

KX_ARMSENSOR_LIN_ERROR_BELOW = 1  # type: int
"""Detect that the constraint linear error is below a threshold. See bge.types.KX_ArmatureSensor.type."""

KX_ARMSENSOR_LIN_ERROR_ABOVE = 2  # type: int
"""Detect that the constraint linear error is above a threshold. See bge.types.KX_ArmatureSensor.type."""

KX_ARMSENSOR_ROT_ERROR_BELOW = 3  # type: int
"""Detect that the constraint rotation error is below a threshold. See bge.types.KX_ArmatureSensor.type."""

KX_ARMSENSOR_ROT_ERROR_ABOVE = 4  # type: int
"""Detect that the constraint rotation error is above a threshold. See bge.types.KX_ArmatureSensor.type."""


# Movement Sensor
KX_MOVEMENT_ALL_AXIS = 6  # type: int
"""See bge.types.KX_MovementSensor.axis."""

KX_MOVEMENT_AXIS_NEG_X = 3  # type: int
"""See bge.types.KX_MovementSensor.axis."""

KX_MOVEMENT_AXIS_NEG_Y = 4  # type: int
"""See bge.types.KX_MovementSensor.axis."""

KX_MOVEMENT_AXIS_NEG_Z = 5  # type: int
"""See bge.types.KX_MovementSensor.axis."""

KX_MOVEMENT_AXIS_POS_X = 1  # type: int
"""See bge.types.KX_MovementSensor.axis."""

KX_MOVEMENT_AXIS_POS_Y = 0  # type: int
"""See bge.types.KX_MovementSensor.axis."""

KX_MOVEMENT_AXIS_POS_Z = 2  # type: int
"""See bge.types.KX_MovementSensor.axis."""


# Property Sensor
KX_PROPSENSOR_EQUAL = 1  # type: int
"""Activate when the property is equal to the sensor value. See bge.types.SCA_PropertySensor.type."""

KX_PROPSENSOR_NOTEQUAL = 2  # type: int
"""Activate when the property is not equal to the sensor value. See bge.types.SCA_PropertySensor.type."""

KX_PROPSENSOR_INTERVAL = 3  # type: int
"""Activate when the property is between the specified limits. See bge.types.SCA_PropertySensor.type."""

KX_PROPSENSOR_CHANGED = 4  # type: int
"""Activate when the property changes. See bge.types.SCA_PropertySensor.type."""

KX_PROPSENSOR_EXPRESSION = 5  # type: int
"""Activate when the expression matches. See bge.types.SCA_PropertySensor.type."""

KX_PROPSENSOR_LESSTHAN = 6  # type: int
"""Activate when the property is less than the sensor value. See bge.types.SCA_PropertySensor.type."""

KX_PROPSENSOR_GREATERTHAN = 7  # type: int
"""Activate when the property is greater than the sensor value. See bge.types.SCA_PropertySensor.type."""

# Radar Sensor
KX_RADAR_AXIS_POS_X = 0  # type: int
"""See bge.types.KX_RadarSensor.axis."""

KX_RADAR_AXIS_POS_Y = 1  # type: int
"""See bge.types.KX_RadarSensor.axis."""

KX_RADAR_AXIS_POS_Z = 2  # type: int
"""See bge.types.KX_RadarSensor.axis."""

KX_RADAR_AXIS_NEG_X = 3  # type: int
"""See bge.types.KX_RadarSensor.axis."""

KX_RADAR_AXIS_NEG_Y = 4  # type: int
"""See bge.types.KX_RadarSensor.axis."""

KX_RADAR_AXIS_NEG_Z = 5  # type: int
"""See bge.types.KX_RadarSensor.axis."""


# Ray Sensor
KX_RAY_AXIS_POS_X = 1  # type: int
"""See bge.types.KX_RaySensor.axis."""

KX_RAY_AXIS_POS_Y = 0  # type: int
"""See bge.types.KX_RaySensor.axis."""

KX_RAY_AXIS_POS_Z = 2  # type: int
"""See bge.types.KX_RaySensor.axis."""

KX_RAY_AXIS_NEG_X = 3  # type: int
"""See bge.types.KX_RaySensor.axis."""

KX_RAY_AXIS_NEG_Y = 4  # type: int
"""See bge.types.KX_RaySensor.axis."""

KX_RAY_AXIS_NEG_Z = 5  # type: int
"""See bge.types.KX_RaySensor.axis."""


# Actuators
# Action Actuator
KX_ACTIONACT_PLAY = 0  # type: int
"""See bge.types.BL_ActionActuator.mode."""

KX_ACTIONACT_PINGPONG = 1  # type: int
"""See bge.types.BL_ActionActuator.mode."""

KX_ACTIONACT_FLIPPER = 2  # type: int
"""See bge.types.BL_ActionActuator.mode."""

KX_ACTIONACT_LOOPSTOP = 3  # type: int
"""See bge.types.BL_ActionActuator.mode."""

KX_ACTIONACT_LOOPEND = 4  # type: int
"""See bge.types.BL_ActionActuator.mode."""

KX_ACTIONACT_PROPERTY = 6  # type: int
"""See bge.types.BL_ActionActuator.mode."""


# Armature Actuator
KX_ACT_ARMATURE_RUN = 0  # type: int
"""Just make sure the armature will be updated on the next graphic frame. This is the only persistent mode of the actuator: it executes automatically once per frame until stopped by a controller. See bge.types.BL_ArmatureActuator.type."""

KX_ACT_ARMATURE_ENABLE = 1  # type: int
"""Enable the constraint. See bge.types.BL_ArmatureActuator.type."""

KX_ACT_ARMATURE_DISABLE = 2  # type: int
"""Disable the constraint (runtime constraint values are not updated). See bge.types.BL_ArmatureActuator.type."""

KX_ACT_ARMATURE_SETTARGET = 3  # type: int
"""Change target and subtarget of constraint. See bge.types.BL_ArmatureActuator.type."""

KX_ACT_ARMATURE_SETWEIGHT = 4  # type: int
"""Change weight of constraint (IK only). See bge.types.BL_ArmatureActuator.type."""

KX_ACT_ARMATURE_SETINFLUENCE = 5  # type: int
"""Change influence of constraint. See bge.types.BL_ArmatureActuator.type."""


# Constraint Actuator
# Constants for bge.types.KX_ConstraintActuator.option
KX_CONSTRAINTACT_NORMAL = 64  # type: int
"""Activate alignment to surface. Applicable to Distance constraint. See bge.types.KX_ConstraintActuator.option."""

KX_CONSTRAINTACT_DISTANCE = 512  # type: int
"""Activate distance control. Applicable to Distance constraint. See bge.types.KX_ConstraintActuator.option."""

KX_CONSTRAINTACT_LOCAL = 1024  # type: int
"""Direction of the ray is along the local axis. Applicable to Distance constraint. See bge.types.KX_ConstraintActuator.option."""

KX_CONSTRAINTACT_DOROTFH = 2048  # type: int
"""Force field act on rotation as well. Applicable to Force field constraint. See bge.types.KX_ConstraintActuator.option."""

KX_CONSTRAINTACT_MATERIAL = 128  # type: int
"""Detect material rather than property. Applicable to both Distance and Force field constraint. See bge.types.KX_ConstraintActuator.option."""

KX_CONSTRAINTACT_PERMANENT = 256  # type: int
"""No deactivation if ray does not hit target. Applicable to both Distance and Force field constraint. See bge.types.KX_ConstraintActuator.option."""

# Constants for bge.types.KX_ConstraintActuator.limit
KX_CONSTRAINTACT_LOCX = 1  # type: int
"""Limit X coord. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_LOCY = 2  # type: int
"""Limit Y coord. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_LOCZ = 3  # type: int
"""Limit Z coord. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_ROTX = 4  # type: int
"""Limit X rotation. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_ROTY = 5  # type: int
"""Limit Y rotation. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_ROTZ = 6  # type: int
"""Limit Z rotation. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_DIRNX = 10  # type: int
"""Set distance along negative X axis. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_DIRNY = 11  # type: int
"""Set distance along negative Y axis. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_DIRNZ = 12  # type: int
"""Set distance along negative Z axis. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_DIRPX = 7  # type: int
"""Set distance along positive X axis. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_DIRPY = 8  # type: int
"""Set distance along positive Y axis. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_DIRPZ = 9  # type: int
"""Set distance along positive Z axis. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_ORIX = 13  # type: int
"""Set orientation of X axis. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_ORIY = 14  # type: int
"""Set orientation of Y axis. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_ORIZ = 15  # type: int
"""Set orientation of Z axis. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_FHNX = 19  # type: int
"""Set force field along negative X axis. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_FHNY = 20  # type: int
"""Set force field along negative Y axis. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_FHNZ = 21  # type: int
"""Set force field along negative Z axis. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_FHPX = 16  # type: int
"""Set force field along positive X axis. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_FHPY = 17  # type: int
"""Set force field along positive Y axis. See bge.types.KX_ConstraintActuator.limit."""

KX_CONSTRAINTACT_FHPZ = 18  # type: int
"""Set force field along positive Z axis. See bge.types.KX_ConstraintActuator.limit."""


# Dynamic Actuator
KX_DYN_RESTORE_DYNAMICS = 0  # type: int
"""See bge.types.KX_SCA_DynamicActuator.mode."""

KX_DYN_DISABLE_DYNAMICS = 1  # type: int
"""See bge.types.KX_SCA_DynamicActuator.mode."""

KX_DYN_ENABLE_RIGID_BODY = 2  # type: int
"""See bge.types.KX_SCA_DynamicActuator.mode."""

KX_DYN_DISABLE_RIGID_BODY = 3  # type: int
"""See bge.types.KX_SCA_DynamicActuator.mode."""

KX_DYN_SET_MASS = 4  # type: int
"""See bge.types.KX_SCA_DynamicActuator.mode."""


# Game Actuator
KX_GAME_LOAD = 1  # type: int
"""See bge.types.KX_GameActuator.mode."""

KX_GAME_START = 2  # type: int
"""See bge.types.KX_GameActuator.mode."""

KX_GAME_RESTART = 3  # type: int
"""See bge.types.KX_GameActuator.mode."""

KX_GAME_QUIT = 4  # type: int
"""See bge.types.KX_GameActuator.mode."""

KX_GAME_SAVECFG = 5  # type: int
"""See bge.types.KX_GameActuator.mode."""

KX_GAME_LOADCFG = 6  # type: int
"""See bge.types.KX_GameActuator.mode."""


# Mouse Actuator
KX_ACT_MOUSE_OBJECT_AXIS_X = 0  # type: int
"""See bge.types.KX_MouseActuator.object_axis."""

KX_ACT_MOUSE_OBJECT_AXIS_Y = 1  # type: int
"""See bge.types.KX_MouseActuator.object_axis."""

KX_ACT_MOUSE_OBJECT_AXIS_Z = 2  # type: int
"""See bge.types.KX_MouseActuator.object_axis."""


# Parent Actuator
KX_PARENT_REMOVE = 2  # type: int
"""See bge.types.KX_ParentActuator.mode."""

KX_PARENT_SET = 1  # type: int
"""See bge.types.KX_ParentActuator.mode."""


# Random Distributions
KX_RANDOMACT_BOOL_CONST = 1  # type: int
"""See bge.types.SCA_RandomActuator.distribution."""

KX_RANDOMACT_BOOL_UNIFORM = 2  # type: int
"""See bge.types.SCA_RandomActuator.distribution."""

KX_RANDOMACT_BOOL_BERNOUILLI = 3  # type: int
"""See bge.types.SCA_RandomActuator.distribution."""

KX_RANDOMACT_INT_CONST = 4  # type: int
"""See bge.types.SCA_RandomActuator.distribution."""

KX_RANDOMACT_INT_UNIFORM = 5  # type: int
"""See bge.types.SCA_RandomActuator.distribution."""

KX_RANDOMACT_INT_POISSON = 6  # type: int
"""See bge.types.SCA_RandomActuator.distribution."""

KX_RANDOMACT_FLOAT_CONST = 7  # type: int
"""See bge.types.SCA_RandomActuator.distribution."""

KX_RANDOMACT_FLOAT_UNIFORM = 8  # type: int
"""See bge.types.SCA_RandomActuator.distribution."""

KX_RANDOMACT_FLOAT_NORMAL = 9  # type: int
"""See bge.types.SCA_RandomActuator.distribution."""

KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL = 10  # type: int
"""See bge.types.SCA_RandomActuator.distribution."""


# Scene Actuator
KX_SCENE_RESTART = 1  # type: int
"""See bge.types.KX_SceneActuator.mode."""

KX_SCENE_SET_SCENE = 2  # type: int
"""See bge.types.KX_SceneActuator.mode."""

KX_SCENE_SET_CAMERA = 3  # type: int
"""See bge.types.KX_SceneActuator.mode."""

KX_SCENE_ADD_FRONT_SCENE = 4  # type: int
"""See bge.types.KX_SceneActuator.mode."""

KX_SCENE_ADD_BACK_SCENE = 5  # type: int
"""See bge.types.KX_SceneActuator.mode."""

KX_SCENE_REMOVE_SCENE = 6  # type: int
"""See bge.types.KX_SceneActuator.mode."""

KX_SCENE_SUSPEND = 7  # type: int
"""See bge.types.KX_SceneActuator.mode."""

KX_SCENE_RESUME = 8  # type: int
"""See bge.types.KX_SceneActuator.mode."""


# Sound Actuator
KX_SOUNDACT_PLAYSTOP = 1  # type: int
"""See bge.types.KX_SoundActuator.mode."""

KX_SOUNDACT_PLAYEND = 2  # type: int
"""See bge.types.KX_SoundActuator.mode."""

KX_SOUNDACT_LOOPSTOP = 3  # type: int
"""See bge.types.KX_SoundActuator.mode."""

KX_SOUNDACT_LOOPEND = 4  # type: int
"""See bge.types.KX_SoundActuator.mode."""

KX_SOUNDACT_LOOPBIDIRECTIONAL = 5  # type: int
"""See bge.types.KX_SoundActuator.mode."""

KX_SOUNDACT_LOOPBIDIRECTIONAL_STOP = 6  # type: int
"""See bge.types.KX_SoundActuator.mode."""


# Steering Actuator
KX_STEERING_SEEK = 1  # type: int
"""See bge.types.KX_SteeringActuator.behavior."""

KX_STEERING_FLEE = 2  # type: int
"""See bge.types.KX_SteeringActuator.behavior."""

KX_STEERING_PATHFOLLOWING = 3  # type: int
"""See bge.types.KX_SteeringActuator.behavior."""


# TrackTo Actuator
KX_TRACK_UPAXIS_POS_X = 0  # type: int
"""See bge.types.KX_TrackToActuator.upAxis."""

KX_TRACK_UPAXIS_POS_Y = 1  # type: int
"""See bge.types.KX_TrackToActuator.upAxis."""

KX_TRACK_UPAXIS_POS_Z = 2  # type: int
"""See bge.types.KX_TrackToActuator.upAxis."""

KX_TRACK_TRAXIS_POS_X = 0  # type: int
"""See bge.types.KX_TrackToActuator.trackAxis."""

KX_TRACK_TRAXIS_POS_Y = 1  # type: int
"""See bge.types.KX_TrackToActuator.trackAxis."""

KX_TRACK_TRAXIS_POS_Z = 2  # type: int
"""See bge.types.KX_TrackToActuator.trackAxis."""

KX_TRACK_TRAXIS_NEG_X = 3  # type: int
"""See bge.types.KX_TrackToActuator.trackAxis."""

KX_TRACK_TRAXIS_NEG_Y = 4  # type: int
"""See bge.types.KX_TrackToActuator.trackAxis."""

KX_TRACK_TRAXIS_NEG_Z = 5  # type: int
"""See bge.types.KX_TrackToActuator.trackAxis."""


# Various
# 2D Filter
RAS_2DFILTER_BLUR = 2  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""

RAS_2DFILTER_CUSTOMFILTER = 12  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""

RAS_2DFILTER_DILATION = 4  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""

RAS_2DFILTER_DISABLED = -1  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""

RAS_2DFILTER_ENABLED = -2  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""

RAS_2DFILTER_EROSION = 5  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""

RAS_2DFILTER_GRAYSCALE = 9  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""

RAS_2DFILTER_INVERT = 11  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""

RAS_2DFILTER_LAPLACIAN = 6  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""

RAS_2DFILTER_MOTIONBLUR = 1  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""

RAS_2DFILTER_NOFILTER = 0  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""

RAS_2DFILTER_PREWITT = 8  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""

RAS_2DFILTER_SEPIA = 10  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""

RAS_2DFILTER_SHARPEN = 3  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""

RAS_2DFILTER_SOBEL = 7  # type: int
"""See bge.types.SCA_2DFilterActuator.mode."""


# Armature Channel
ROT_MODE_QUAT = 0  # type: int
"""Use quaternion in rotation attribute to update bone rotation. See bge.types.BL_ArmatureChannel.rotation_mode."""

ROT_MODE_XYZ = 1  # type: int
"""Use euler_rotation and apply angles on bone's Z, Y, X axis successively. See bge.types.BL_ArmatureChannel.rotation_mode."""

ROT_MODE_XZY = 2  # type: int
"""Use euler_rotation and apply angles on bone's Y, Z, X axis successively. See bge.types.BL_ArmatureChannel.rotation_mode."""

ROT_MODE_YXZ = 3  # type: int
"""Use euler_rotation and apply angles on bone's Z, X, Y axis successively. See bge.types.BL_ArmatureChannel.rotation_mode."""

ROT_MODE_YZX = 4  # type: int
"""Use euler_rotation and apply angles on bone's X, Z, Y axis successively. See bge.types.BL_ArmatureChannel.rotation_mode."""

ROT_MODE_ZXY = 5  # type: int
"""Use euler_rotation and apply angles on bone's Y, X, Z axis successively. See bge.types.BL_ArmatureChannel.rotation_mode."""

ROT_MODE_ZYX = 6  # type: int
"""Use euler_rotation and apply angles on bone's X, Y, Z axis successively. See bge.types.BL_ArmatureChannel.rotation_mode."""


# Armature Constraint
CONSTRAINT_TYPE_TRACKTO = 2  # type: int
"""See bge.types.BL_ArmatureConstraint.type."""

CONSTRAINT_TYPE_KINEMATIC = 3  # type: int
"""See bge.types.BL_ArmatureConstraint.type."""

CONSTRAINT_TYPE_ROTLIKE = 8  # type: int
"""See bge.types.BL_ArmatureConstraint.type."""

CONSTRAINT_TYPE_LOCLIKE = 9  # type: int
"""See bge.types.BL_ArmatureConstraint.type."""

CONSTRAINT_TYPE_MINMAX = 16  # type: int
"""See bge.types.BL_ArmatureConstraint.type."""

CONSTRAINT_TYPE_SIZELIKE = 10  # type: int
"""See bge.types.BL_ArmatureConstraint.type."""

CONSTRAINT_TYPE_LOCKTRACK = 13  # type: int
"""See bge.types.BL_ArmatureConstraint.type."""

CONSTRAINT_TYPE_STRETCHTO = 15  # type: int
"""See bge.types.BL_ArmatureConstraint.type."""

CONSTRAINT_TYPE_CLAMPTO = 18  # type: int
"""See bge.types.BL_ArmatureConstraint.type."""

CONSTRAINT_TYPE_TRANSFORM = 19  # type: int
"""See bge.types.BL_ArmatureConstraint.type."""

CONSTRAINT_TYPE_DISTLIMIT = 14  # type: int
"""See bge.types.BL_ArmatureConstraint.type."""

CONSTRAINT_IK_COPYPOSE = 0  # type: int
"""See bge.types.BL_ArmatureConstraint.ik_type."""

CONSTRAINT_IK_DISTANCE = 1  # type: int
"""See bge.types.BL_ArmatureConstraint.ik_type."""

CONSTRAINT_IK_FLAG_TIP = 1  # type: int
"""See bge.types.BL_ArmatureConstraint.ik_flag."""

CONSTRAINT_IK_FLAG_ROT = 2  # type: int
"""See bge.types.BL_ArmatureConstraint.ik_flag."""

CONSTRAINT_IK_FLAG_STRETCH = 16  # type: int
"""See bge.types.BL_ArmatureConstraint.ik_flag."""

CONSTRAINT_IK_FLAG_POS = 32  # type: int
"""See bge.types.BL_ArmatureConstraint.ik_flag."""

CONSTRAINT_IK_MODE_INSIDE = 0  # type: int
"""See bge.types.BL_ArmatureConstraint.ik_mode."""

CONSTRAINT_IK_MODE_OUTSIDE = 1  # type: int
"""See bge.types.BL_ArmatureConstraint.ik_mode."""

CONSTRAINT_IK_MODE_ONSURFACE = 2  # type: int
"""See bge.types.BL_ArmatureConstraint.ik_mode."""


# Blender Material
BL_DST_ALPHA = 8  # type: int
BL_DST_COLOR = 4  # type: int
BL_ONE = 1  # type: int
BL_ONE_MINUS_DST_ALPHA = 9  # type: int
BL_ONE_MINUS_DST_COLOR = 5  # type: int
BL_ONE_MINUS_SRC_ALPHA = 7  # type: int
BL_ONE_MINUS_SRC_COLOR = 3  # type: int
BL_SRC_ALPHA = 6  # type: int
BL_SRC_ALPHA_SATURATE = 10  # type: int
BL_SRC_COLOR = 2  # type: int
BL_ZERO = 0  # type: int


# Input Status
KX_INPUT_NONE = 0  # type: int
"""See bge.types.SCA_PythonKeyboard, bge.types.SCA_PythonMouse, bge.types.SCA_MouseSensor, bge.types.SCA_KeyboardSensor."""

KX_INPUT_JUST_ACTIVATED = 1  # type: int
"""See bge.types.SCA_PythonKeyboard, bge.types.SCA_PythonMouse, bge.types.SCA_MouseSensor, bge.types.SCA_KeyboardSensor."""

KX_INPUT_ACTIVE = 2  # type: int
"""See bge.types.SCA_PythonKeyboard, bge.types.SCA_PythonMouse, bge.types.SCA_MouseSensor, bge.types.SCA_KeyboardSensor."""

KX_INPUT_JUST_RELEASED = 3  # type: int
"""See bge.types.SCA_PythonKeyboard, bge.types.SCA_PythonMouse, bge.types.SCA_MouseSensor, bge.types.SCA_KeyboardSensor."""


# KX_GameObject
KX_ACTION_MODE_PLAY = 0  # type: int
"""Play the action once. See bge.types.KX_GameObject.playAction"""

KX_ACTION_MODE_LOOP = 1  # type: int
"""Loop the action (repeat it). See bge.types.KX_GameObject.playAction"""

KX_ACTION_MODE_PING_PONG = 2  # type: int
"""Play the action one direct then back the other way when it has completed. See bge.types.KX_GameObject.playAction"""

KX_ACTION_BLEND_BLEND = 0  # type: int
"""Blend layers using linear interpolation. See bge.types.KX_GameObject.playAction"""

KX_ACTION_BLEND_ADD = 1  # type: int
"""Adds the layers together. See bge.types.KX_GameObject.playAction"""


# Mouse Buttons
KX_MOUSE_BUT_LEFT = 116  # type: int
"""See bge.types.SCA_MouseSensor"""

KX_MOUSE_BUT_MIDDLE = 117  # type: int
"""See bge.types.SCA_MouseSensor"""

KX_MOUSE_BUT_RIGHT = 118  # type: int
"""See bge.types.SCA_MouseSensor"""


# Navigation Mesh Draw Modes
RM_WALLS = 0  # type: int
"""Draw only the walls."""

RM_POLYS = 1  # type: int
"""Draw only polygons."""

RM_TRIS = 2  # type: int
"""Draw triangle mesh."""

# Shader
VIEWMATRIX = 0  # type: int
VIEWMATRIX_INVERSE = 10  # type: int
VIEWMATRIX_INVERSETRANSPOSE = 11  # type: int
VIEWMATRIX_TRANSPOSE = 9  # type: int
MODELMATRIX = 4  # type: int
MODELMATRIX_INVERSE = 6  # type: int
MODELMATRIX_INVERSETRANSPOSE = 7  # type: int
MODELMATRIX_TRANSPOSE = 5  # type: int
MODELVIEWMATRIX = 0  # type: int
MODELVIEWMATRIX_INVERSE = 2  # type: int
MODELVIEWMATRIX_INVERSETRANSPOSE = 3  # type: int
MODELVIEWMATRIX_TRANSPOSE = 1  # type: int
CAM_POS = 12  # type: int
"""Current camera position"""

CONSTANT_TIMER = 13  # type: int
"""User a timer for the uniform value."""

EYE = 14  # type: int
SHD_TANGENT = 1  # type: int

# States
KX_STATE1 = 1  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE2 = 2  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE3 = 4  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE4 = 8  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE5 = 16  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE6 = 32  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE7 = 64  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE8 = 128  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE9 = 256  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE10 = 512  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE11 = 1024  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE12 = 2048  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE13 = 4096  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE14 = 8192  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE15 = 16384  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE16 = 32768  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE17 = 65536  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE18 = 131072  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE19 = 262144  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE20 = 524288  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE21 = 1048576  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE22 = 2097152  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE23 = 4194304  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE24 = 8388608  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE25 = 16777216  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE26 = 33554432  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE27 = 67108864  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE28 = 134217728  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE29 = 268435456  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE30 = 536870912  # type: int
"""See bge.types.KX_StateActuator"""

KX_STATE_OP_CLR = 2  # type: int
"""Substract bits to state mask. See bge.types.KX_StateActuator.operation"""

KX_STATE_OP_CPY = 0  # type: int
"""Copy state mask. See bge.types.KX_StateActuator.operation"""

KX_STATE_OP_NEG = 3  # type: int
"""Invert bits to state mask. See bge.types.KX_StateActuator.operation"""

KX_STATE_OP_SET = 1  # type: int
"""Add bits to state mask. See bge.types.KX_StateActuator.operation"""


# Variables
globalDict = {} # type: dict
"""A dictionary that is saved between loading blend files so you can use it to store inventory and other variables you want to store between scenes and blend files. It can also be written to a file and loaded later on with the game load/save actuators.

Note:
    Only python built in types such as int/string/bool/float/tuples/lists can be saved, GameObjects, Actuators etc will not work as expected."""

keyboard = None  # type: _types.SCA_PythonKeyboard
"""The current keyboard wrapped in an SCA_PythonKeyboard object."""

mouse = None  # type: _types.SCA_PythonMouse
"""The current mouse wrapped in an SCA_PythonMouse object."""

joysticks = None  # type: _types.SCA_PythonJoystick
"""A list of attached SCA_PythonJoystick. The list size is the maximum number of supported joysticks. If no joystick is available for a given slot, the slot is set to None."""


# Functions
# General Functions
def getCurrentController():
    # type: () -> _types.SCA_PythonController
    """Gets the Python controller associated with this Python script.

    Returns:
        SCA_PythonController: python controller"""

    pass

def getCurrentScene():
    # type: () -> _types.KX_Scene
    """Gets the current Scene.

    Returns:
        KX_Scene: current scene"""

    pass

def getSceneList():
    # type: () -> list[_types.KX_Scene]
    """Gets a list of the current scenes loaded in the game engine.

    Returns:
        list: List of bge.types.KX_Scene

    Note:
        Scenes in your blend file that have not been converted wont be in this list. This list will only contain scenes such as overlays scenes."""

    pass

def loadGlobalDict():
    # type: () -> None
    """Loads bge.logic.globalDict from a file."""

    pass

def saveGlobalDict():
    # type: () -> None
    """Saves bge.logic.globalDict to a file."""

    pass

def startGame(blend):
    # type: (str) -> None
    """Loads the blend file.

    Args:
        blend (str): The name of the blend file"""

    pass

def endGame():
    # type: () -> None
    """Ends the current game."""

    pass

def restartGame():
    # type: () -> None
    """Restarts the current game by reloading the .blend file (the last saved version, not what is currently running)."""

    pass

def LibLoad(blend, type, data=None, load_actions=False, verbose=False, load_scripts=True, asynchronous=False, scene=None):
    # type: (str, str, bytes, bool, bool, bool, bool, _types.KX_Scene) -> _types.KX_LibLoadStatus
    """Converts the all of the datablocks of the given type from the given blend.

    Args:
        blend (string): The path to the blend file (or the name to use for the library if data is supplied)
        type (string): The datablock type (currently only 'Action', 'Mesh' and 'Scene' are supported)
        data (bytes): Binary data from a blend file (optional)
        load_actions (bool): Search for and load all actions in a given Scene and not just the "active" actions (Scene type only)
        verbose (bool): Whether or not to print debugging information (e.g., 'SceneName: Scene')
        load_scripts (bool): Whether or not to load text datablocks as well (can be disabled for some extra security)
        asynchronous (bool): Whether or not to do the loading asynchronously (in another thread). Only the 'Scene' type is currently supported for this feature.
        scene (KX_Scene or string): Scene to merge loaded data to, if None use the current scene.

    Returns:
        bge.types.KX_LibLoadStatus

    Note:
        Asynchronously loaded libraries will not be available immediately after LibLoad() returns. Use the returned KX_LibLoadStatus to figure out when the libraries are ready."""

    pass

def LibNew(name, type, data):
    # type: (str, str, list[str]) -> None
    """Uses existing datablock data and loads in as a new library.

    Args:
        name (string): A unique library name used for removal later
        type (string): The datablock type (currently only "Mesh" is supported)
        data (list of strings): A list of names of the datablocks to load"""

    pass

def LibFree(name):
    # type: (str) -> None
    """Frees a library, removing all objects and meshes from the currently active scenes.

    Args:
        name (string): The name of the library to free (the name used in LibNew)"""

    pass

def LibList():
    # type: () -> list[str]
    """Returns a list of currently loaded libraries.

    Returns:
        list[str]"""

    pass

def addScene(name, overlay=1):
    # type: (str, int) -> _types.KX_Scene
    """Loads a scene into the game engine.

    Note:
        This function is not effective immediately, the scene is queued and added on the next logic cycle where it will be available from getSceneList

    Args:
        name (string): The name of the scene
        overlay (integer): Overlay or underlay (optional)"""

    pass

def sendMessage(subject, body="", to="", message_from=""):
    # type: (str, str, str, str) -> None
    """Sends a message to sensors in any active scene.

    Args:
        subject (string): The subject of the message
        body (string): The body of the message (optional)
        to (string): The name of the object to send the message to (optional)
        message_from (string): The name of the object that the message is coming from (optional)"""

    pass

def setGravity(gravity):
    # type: (_Vector) -> None
    """Sets the world gravity.

    Args:
        gravity (Vector): gravity vector"""

    pass

def getSpectrum():
    # type: () -> list[float]
    """Returns a 512 point list from the sound card. This only works if the fmod sound driver is being used.

    Returns:
        list[float], len(getSpectrum()) == 512"""

    pass

def getMaxLogicFrame():
    # type: () -> int
    """Gets the maximum number of logic frames per render frame.

    Returns:
        int: The maximum number of logic frames per render frame"""

    pass

def setMaxLogicFrame(maxlogic):
    # type: (int) -> None
    """Sets the maximum number of logic frames that are executed per render frame. This does not affect the physic system that still runs at full frame rate.

    Args:
        maxlogic (integer): The new maximum number of logic frames per render frame. Valid values: 1..5"""

    pass

def getMaxPhysicsFrame():
    # type: () -> int
    """Gets the maximum number of physics frames per render frame.

    Returns:
        int: The maximum number of physics frames per render frame"""

    pass

def setMaxPhysicsFrame(maxphysics):
    # type: (int) -> None
    """Sets the maximum number of physics timestep that are executed per render frame. Higher value allows physics to keep up with realtime even if graphics slows down the game. Physics timestep is fixed and equal to 1/tickrate (see setLogicTicRate) maxphysics/ticrate is the maximum delay of the renderer that physics can compensate.

    Args:
        maxphysics (integer): The new maximum number of physics timestep per render frame. Valid values: 1..5."""

    pass

def getLogicTicRate():
    # type: () -> float
    """Gets the logic update frequency.

    Returns:
        float: The logic frequency in Hz"""

    pass

def setLogicTicRate(ticrate):
    # type: (float) -> None
    """Sets the logic update frequency.

    The logic update frequency is the number of times logic bricks are executed every second. The default is 60 Hz.

    Args:
        ticrate (float): The new logic update frequency (in Hz)."""

    pass

def getPhysicsTicRate():
    # type: () -> float
    """Gets the physics update frequency.

    Returns:
        float: The physics update frequency in Hz"""

    pass

def setPhysicsTicRate(ticrate):
    # type: (float) -> None
    """Sets the physics update frequency

    The physics update frequency is the number of times the physics system is executed every second. The default is 60 Hz.

    Args:
        ticrate (float): The new update frequency (in Hz)."""

    pass

def getAnimRecordFrame():
    # type: () -> int
    """Gets the current frame number used for recording animations. This number is incremented automatically by Blender when the "Record animation" feature is turned on.

    Returns:
        int"""

    pass

def setAnimRecordFrame(framenr):
    # type: (int) -> None
    """Sets the current frame number used for recording animations. This number is automatically incremented by Blender when the "Record animation" feature is turned on.

    The frame number Must be non-negative, unless Blender has bpy.types.UserPreferencesEdit.use_negative_frames enabled in its user preferences. Only use non-negative numbers to be on the safe side, unless you know what you are doing.

    Args:
        framenr (int): The new frame number."""

    pass

def getExitKey():
    # type: () -> int
    """Gets the key used to exit the game engine.

    Returns:
        int: The key (defaults to bge.events.ESCKEY)"""

    pass

def setExitKey(key):
    # type: (int) -> None
    """Sets the key used to exit the game engine.

    Args:
        key (int): A key constant from bge.events"""

    pass

def NextFrame():
    # type: () -> None
    """Render next frame (if Python has control)"""

    pass

def setRender(render):
    # type: (bool) -> None
    """Sets the global flag that controls the render of the scene. If True, the render is done after the logic frame. If False, the render is skipped and another logic frame starts immediately.

    Args:
        render (bool): the render flag"""

    pass

def getRender():
    # type: () -> bool
    """Get the current value of the global render flag.

    Returns:
        bool: The flag value"""

    pass

# Time related functions
def getClockTime():
    # type: () -> float
    """Get the current BGE render time, in seconds. The BGE render time is the simulation time corresponding to the next scene that will be rendered.

    Returns:
        float"""

    pass

def getFrameTime():
    # type: () -> float
    """Get the current BGE frame time, in seconds. The BGE frame time is the simulation time corresponding to the current call of the logic system. Generally speaking, it is what the user is interested in.

    Returns:
        double"""

    pass

def getRealTime():
    # type: () -> float
    """Get the number of real (system-clock) seconds elapsed since the beginning of the simulation."""

    pass

def getTimeScale():
    # type: () -> float
    """Get the time multiplier between real-time and simulation time. The default value is 1.0. A value greater than 1.0 means that the simulation is going faster than real-time, a value lower than 1.0 means that the simulation is going slower than real-time.

    Returns:
        float"""

    pass

def setTimeScale(time_scale):
    # type: (float) -> None
    """Set the time multiplier between real-time and simulation time. A value greater than 1.0 means that the simulation is going faster than real-time, a value lower than 1.0 means that the simulation is going slower than real-time. Note that a too large value may lead to some physics instabilities.

    Args:
        time_scale: The new time multiplier."""

    pass

def getUseExternalClock():
    # type: () -> bool
    """Get if the BGE use the inner BGE clock, or rely or on an external clock. The default is to use the inner BGE clock.

    Returns:
        bool"""

    pass

def setUseExternalClock(use_external_clock):
    # type: (bool) -> None
    """Set if the BGE use the inner BGE clock, or rely or on an external clock. If the user selects the use of an external clock, he should call regularly the setClockTime method.

    Args:
        use_external_clock (bool): the new setting"""

    pass

def setClockTime(new_time):
    # type: (float) -> None
    """Set the next value of the simulation clock. It is preferable to use this method from a custom main function in python, as calling it in the logic block can easily lead to a blocked system (if the time does not advance enough to run at least the next logic step).

    Args:
        new_time: the next value of the BGE clock (in second)."""

    pass

# Utility Functions
def expandPath(path):
    # type: (str) -> str
    """Converts a blender internal path into a proper file system path.

    Use / as directory separator in path You can use '//' at the start of the string to define a relative path; Blender replaces that string by the directory of the current .blend or runtime file to make a full path name. The function also converts the directory separator to the local file system format.

    Args:
        path (string): The path string to be converted/expanded.

    Returns:
        str: The converted string"""

    pass

def getAverageFrameRate():
    # type: () -> float
    """Gets the estimated/average framerate for all the active scenes, not only the current scene.

    Returns:
        float: The estimated average framerate in frames per second"""

    pass

def getBlendFileList(path = "//"):
    # type: (str) -> list[str]
    """Returns a list of blend files in the same directory as the open blend file, or from using the option argument.

    Args:
        path (string): Optional directory argument, will be expanded (like expandPath) into the full path.

    Returns:
        list: A list of filenames, with no directory prefix"""

    pass

def getRandomFloat():
    # type: () -> float
    """Returns a random floating point value in the range [0 - 1)"""

    pass

def PrintGLInfo():
    # type: () -> None
    """Prints GL Extension Info into the console"""

    pass

def PrintMemInfo():
    # type: () -> None
    """Prints engine statistics into the console"""

    pass

def getProfileInfo():
    # type: () -> dict[str, tuple[float, float]]
    """Returns a Python dictionary that contains the same information as the on screen profiler. The keys are the profiler categories and the values are tuples with the first element being time taken (in ms) and the second element being the percentage of total time."""

    pass
