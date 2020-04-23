"""Module to access logic functions, imported automatically into the python controllers namespace."""

from .. import types

### Constants
KX_TRUE = 1
KX_FALSE = 2

## Sensors
# Sensor Status
KX_SENSOR_INACTIVE = 0
KX_SENSOR_JUST_ACTIVATED = 1
KX_SENSOR_ACTIVE = 2
KX_SENSOR_JUST_DEACTIVATED = 3

# Armature Sensor
KX_ARMSENSOR_STATE_CHANGED = 0
KX_ARMSENSOR_LIN_ERROR_BELOW = 1
KX_ARMSENSOR_LIN_ERROR_ABOVE = 2
KX_ARMSENSOR_ROT_ERROR_BELOW = 3
KX_ARMSENSOR_ROT_ERROR_ABOVE = 4

# Movement Sensor
KX_MOVEMENT_ALL_AXIS = 6
KX_MOVEMENT_AXIS_NEG_X = 3
KX_MOVEMENT_AXIS_NEG_Y = 4
KX_MOVEMENT_AXIS_NEG_Z = 5
KX_MOVEMENT_AXIS_POS_X = 1
KX_MOVEMENT_AXIS_POS_Y = 0
KX_MOVEMENT_AXIS_POS_Z = 2

# Property Sensor
KX_PROPSENSOR_EQUAL = 1
KX_PROPSENSOR_NOTEQUAL = 2
KX_PROPSENSOR_INTERVAL = 3
KX_PROPSENSOR_CHANGED = 4
KX_PROPSENSOR_EXPRESSION = 5
KX_PROPSENSOR_LESSTHAN = 6
KX_PROPSENSOR_GREATERTHAN = 7

# Radar Sensor
KX_RADAR_AXIS_POS_X = 0
KX_RADAR_AXIS_POS_Y = 1
KX_RADAR_AXIS_POS_Z = 2
KX_RADAR_AXIS_NEG_X = 3
KX_RADAR_AXIS_NEG_Y = 4
KX_RADAR_AXIS_NEG_Z = 5

# Ray Sensor
KX_RAY_AXIS_POS_X = 1
KX_RAY_AXIS_POS_Y = 0
KX_RAY_AXIS_POS_Z = 2
KX_RAY_AXIS_NEG_X = 3
KX_RAY_AXIS_NEG_Y = 4
KX_RAY_AXIS_NEG_Z = 5

## Actuators
# Action Actuator
KX_ACTIONACT_PLAY = 0
KX_ACTIONACT_PINGPONG = 1
KX_ACTIONACT_FLIPPER = 2
KX_ACTIONACT_LOOPSTOP = 3
KX_ACTIONACT_LOOPEND = 4
KX_ACTIONACT_PROPERTY = 6

# Armature Actuator
KX_ACT_ARMATURE_RUN = 0
KX_ACT_ARMATURE_ENABLE = 1
KX_ACT_ARMATURE_DISABLE = 2
KX_ACT_ARMATURE_SETTARGET = 3
KX_ACT_ARMATURE_SETWEIGHT = 4
KX_ACT_ARMATURE_SETINFLUENCE = 5

# Constraint Actuator
KX_CONSTRAINTACT_NORMAL = 64
KX_CONSTRAINTACT_DISTANCE = 512
KX_CONSTRAINTACT_LOCAL = 1024
KX_CONSTRAINTACT_DOROTFH = 2048
KX_CONSTRAINTACT_MATERIAL = 128
KX_CONSTRAINTACT_PERMANENT = 256
KX_CONSTRAINTACT_LOCX = 1
KX_CONSTRAINTACT_LOCY = 2
KX_CONSTRAINTACT_LOCZ = 3
KX_CONSTRAINTACT_ROTX = 4
KX_CONSTRAINTACT_ROTY = 5
KX_CONSTRAINTACT_ROTZ = 6
KX_CONSTRAINTACT_DIRNX = 10
KX_CONSTRAINTACT_DIRNY = 11
KX_CONSTRAINTACT_DIRNZ = 12
KX_CONSTRAINTACT_DIRPX = 7
KX_CONSTRAINTACT_DIRPY = 8
KX_CONSTRAINTACT_DIRPZ = 9
KX_CONSTRAINTACT_ORIX = 13
KX_CONSTRAINTACT_ORIY = 14
KX_CONSTRAINTACT_ORIZ = 15
KX_CONSTRAINTACT_FHNX = 19
KX_CONSTRAINTACT_FHNY = 20
KX_CONSTRAINTACT_FHNZ = 21
KX_CONSTRAINTACT_FHPX = 16
KX_CONSTRAINTACT_FHPY = 17
KX_CONSTRAINTACT_FHPZ = 18

# Dynamic Actuator
KX_DYN_RESTORE_DYNAMICS = 0
KX_DYN_DISABLE_DYNAMICS = 1
KX_DYN_ENABLE_RIGID_BODY = 2
KX_DYN_DISABLE_RIGID_BODY = 3
KX_DYN_SET_MASS = 4

# Game Actuator
KX_GAME_LOAD = 1
KX_GAME_START = 2
KX_GAME_RESTART = 3
KX_GAME_QUIT = 4
KX_GAME_SAVECFG = 5
KX_GAME_LOADCFG = 6

# Mouse Actuator
KX_ACT_MOUSE_OBJECT_AXIS_X = 0
KX_ACT_MOUSE_OBJECT_AXIS_X = 1
KX_ACT_MOUSE_OBJECT_AXIS_Z = 2

# Parent Actuator
KX_PARENT_REMOVE = 2
KX_PARENT_SET = 1

# Random Distributions
KX_RANDOMACT_BOOL_CONST = 1
KX_RANDOMACT_BOOL_UNIFORM = 2
KX_RANDOMACT_BOOL_BERNOUILLI = 3
KX_RANDOMACT_INT_CONST = 4
KX_RANDOMACT_INT_UNIFORM = 5
KX_RANDOMACT_INT_POISSON = 6
KX_RANDOMACT_FLOAT_CONST = 7
KX_RANDOMACT_FLOAT_UNIFORM = 8
KX_RANDOMACT_FLOAT_NORMAL = 9
KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL = 10

# Scene Actuator
KX_SCENE_RESTART = 1
KX_SCENE_SET_SCENE = 2
KX_SCENE_SET_CAMERA = 3
KX_SCENE_ADD_FRONT_SCENE = 4
KX_SCENE_ADD_BACK_SCENE = 5
KX_SCENE_REMOVE_SCENE = 6
KX_SCENE_SUSPEND = 7
KX_SCENE_RESUME = 8

# Sound Actuator
KX_SOUNDACT_PLAYSTOP = 1
KX_SOUNDACT_PLAYEND = 2
KX_SOUNDACT_LOOPSTOP = 3
KX_SOUNDACT_LOOPEND = 4
KX_SOUNDACT_LOOPBIDIRECTIONAL = 5
KX_SOUNDACT_LOOPBIDIRECTIONAL_STOP = 6

# Steering Actuator
KX_STEERING_SEEK = 1
KX_STEERING_FLEE = 2
KX_STEERING_PATHFOLLOWING = 3

# TrackTo Actuator
KX_TRACK_UPAXIS_POS_X = 0
KX_TRACK_UPAXIS_POS_Y = 1
KX_TRACK_UPAXIS_POS_Z = 2
KX_TRACK_TRAXIS_POS_X = 0
KX_TRACK_TRAXIS_POS_Y = 1
KX_TRACK_TRAXIS_POS_Z = 2
KX_TRACK_TRAXIS_NEG_X = 3
KX_TRACK_TRAXIS_NEG_Y = 4
KX_TRACK_TRAXIS_NEG_Z = 5

## Various
# 2D Filter
RAS_2DFILTER_BLUR = 2
RAS_2DFILTER_CUSTOMFILTER = 12
RAS_2DFILTER_DILATION = 4
RAS_2DFILTER_DISABLED = -1
RAS_2DFILTER_ENABLED = -2
RAS_2DFILTER_EROSION = 5
RAS_2DFILTER_GRAYSCALE = 9
RAS_2DFILTER_INVERT = 11
RAS_2DFILTER_LAPLACIAN = 6
RAS_2DFILTER_MOTIONBLUR = 1
RAS_2DFILTER_NOFILTER = 0
RAS_2DFILTER_PREWITT = 8
RAS_2DFILTER_SEPIA = 10
RAS_2DFILTER_SHARPEN = 3
RAS_2DFILTER_SOBEL = 7

# Armature Channel
ROT_MODE_QUAT = 0
ROT_MODE_XYZ = 1
ROT_MODE_XZY = 2
ROT_MODE_YXZ = 3
ROT_MODE_YZX = 4
ROT_MODE_ZXY = 5
ROT_MODE_ZYX = 6

# Armature Constraint
CONSTRAINT_TYPE_TRACKTO = 2
CONSTRAINT_TYPE_KINEMATIC = 3
CONSTRAINT_TYPE_ROTLIKE = 8
CONSTRAINT_TYPE_LOCLIKE = 9
CONSTRAINT_TYPE_MINMAX = 16
CONSTRAINT_TYPE_SIZELIKE = 10
CONSTRAINT_TYPE_LOCKTRACK = 13
CONSTRAINT_TYPE_STRETCHTO = 15
CONSTRAINT_TYPE_CLAMPTO = 18
CONSTRAINT_TYPE_TRANSFORM = 19
CONSTRAINT_TYPE_DISTLIMIT = 14
CONSTRAINT_IK_COPYPOSE = 0
CONSTRAINT_IK_DISTANCE = 1
CONSTRAINT_IK_FLAG_TIP = 1
CONSTRAINT_IK_FLAG_ROT = 2
CONSTRAINT_IK_FLAG_STRETCH = 16
CONSTRAINT_IK_FLAG_POS = 32
CONSTRAINT_IK_MODE_INSIDE = 0
CONSTRAINT_IK_MODE_OUTSIDE = 1
CONSTRAINT_IK_MODE_ONSURFACE = 2

# Blender Material
BL_DST_ALPHA = 8
BL_DST_COLOR = 4
BL_ONE = 1
BL_ONE_MINUS_DST_ALPHA = 9
BL_ONE_MINUS_DST_COLOR = 5
BL_ONE_MINUS_SRC_ALPHA = 7
BL_ONE_MINUS_SRC_COLOR = 3
BL_SRC_ALPHA = 6
BL_SRC_ALPHA_SATURATE = 10
BL_SRC_COLOR = 2
BL_ZERO = 0

# Input Status
KX_INPUT_NONE = 0
KX_INPUT_JUST_ACTIVATED = 1
KX_INPUT_ACTIVE = 2
KX_INPUT_JUST_RELEASED = 3

# KX_GameObject
KX_ACTION_MODE_PLAY = 0
KX_ACTION_MODE_LOOP = 1
KX_ACTION_MODE_PING_PONG = 2
KX_ACTION_BLEND_BLEND = 0
KX_ACTION_BLEND_ADD = 1

# Mouse Buttons
KX_MOUSE_BUT_LEFT = 116
KX_MOUSE_BUT_MIDDLE = 117
KX_MOUSE_BUT_RIGHT = 118

# Navigation Mesh Draw Modes
RM_WALLS = 0
RM_POLYS = 1
RM_TRIS = 2

# Shader
VIEWMATRIX = 0
VIEWMATRIX_INVERSE = 10
VIEWMATRIX_INVERSETRANSPOSE = 11
VIEWMATRIX_TRANSPOSE = 9
MODELMATRIX = 4
MODELMATRIX_INVERSE = 6
MODELMATRIX_INVERSETRANSPOSE = 7
MODELMATRIX_TRANSPOSE = 5
MODELVIEWMATRIX = 0
MODELVIEWMATRIX_INVERSE = 2
MODELVIEWMATRIX_INVERSETRANSPOSE = 3
MODELVIEWMATRIX_TRANSPOSE = 1
CAM_POS = 12
CONSTANT_TIMER = 13
EYE = 14
SHD_TANGENT = 1

# States
KX_STATE1 = 1
KX_STATE2 = 2
KX_STATE3 = 4
KX_STATE4 = 8
KX_STATE5 = 16
KX_STATE6 = 32
KX_STATE7 = 64
KX_STATE8 = 128
KX_STATE9 = 256
KX_STATE10 = 512
KX_STATE11 = 1024
KX_STATE12 = 2048
KX_STATE13 = 4096
KX_STATE14 = 8192
KX_STATE15 = 16384
KX_STATE16 = 32768
KX_STATE17 = 65536
KX_STATE18 = 131072
KX_STATE19 = 262144
KX_STATE20 = 524288
KX_STATE21 = 1048576
KX_STATE22 = 2097152
KX_STATE23 = 4194304
KX_STATE24 = 8388608
KX_STATE25 = 16777216
KX_STATE26 = 33554432
KX_STATE27 = 67108864
KX_STATE28 = 134217728
KX_STATE29 = 268435456
KX_STATE30 = 536870912
KX_STATE_OP_CLR = 2
KX_STATE_OP_CPY = 0
KX_STATE_OP_NEG = 3
KX_STATE_OP_SET = 1

## Variables
globalDict = {}
keyboard = types.SCA_PythonKeyboard()
mouse = types.SCA_PythonMouse()
joysticks = types.SCA_PythonJoystick()

## Functions
# General Functions
def getCurrentController():
	"""Gets the Python controller associated with this Python script.

	Return type:
	bge.types.SCA_PythonController"""
	value = types.SCA_PythonController
	return value
	
def getCurrentScene():
	"""Gets the current Scene.

	Return type:
	bge.types.KX_Scene"""
	value = types.KX_Scene
	return value
	
def getSceneList():
	"""Gets a list of the current scenes loaded in the game engine.

	Return type:
	list of bge.types.KX_Scene

	Note: Scenes in your blend file that have not been converted wont be in this list. This list will only contain scenes such as overlays scenes."""
	return []
	
def loadGlobalDict():
	"""Loads bge.logic.globalDict from a file."""
	pass
	
def saveGlobalDict():
	"""Saves bge.logic.globalDict to a file."""
	pass
	
def startGame(blend):
	"""Loads the blend file.

	Parameters:
	blend (string) - The name of the blend file"""
	pass
	
def endGame():
	"""Ends the current game."""
	pass
	
def restartGame():
	"""Restarts the current game by reloading the .blend file (the last saved version, not what is currently running)."""
	pass
	
def LibLoad(blend, type, data, load_actions=False, verbose=False, load_scripts=True, asynchronous=False, scene=None):
	"""Converts the all of the datablocks of the given type from the given blend.

	Parameters:	
	blend (string) - The path to the blend file (or the name to use for the library if data is supplied)
	type (string) - The datablock type (currently only 'Action', 'Mesh' and 'Scene' are supported)
	data (bytes) - Binary data from a blend file (optional)
	load_actions (bool) - Search for and load all actions in a given Scene and not just the "active" actions (Scene type only)
	verbose (bool) - Whether or not to print debugging information (e.g., 'SceneName: Scene')
	load_scripts (bool) - Whether or not to load text datablocks as well (can be disabled for some extra security)
	async (bool) - Whether or not to do the loading asynchronously (in another thread). Only the 'Scene' type is currently supported for this feature.

	Return type:
	bge.types.KX_LibLoadStatus

	Note: Asynchronously loaded libraries will not be available immediately after LibLoad() returns. Use the returned KX_LibLoadStatus to figure out when the libraries are ready."""
	value = types.KX_LibLoadStatus
	return value
	
def LibNew(name, type, data):
	"""Uses existing datablock data and loads in as a new library.

	Parameters:
	name (string) - A unique library name used for removal later
	type (string) - The datablock type (currently only "Mesh" is supported)
	data (list of strings) - A list of names of the datablocks to load"""
	pass
	
def LibFree(name):
	"""Frees a library, removing all objects and meshes from the currently active scenes.

	Parameters:
	name (string) - The name of the library to free (the name used in LibNew)"""
	pass
	
def LibList():
	"""Returns a list of currently loaded libraries.

	Return type:
	list [str]"""
	return []
	
def addScene(name, overlay=1):
	"""Loads a scene into the game engine.

	Note: This function is not effective immediately, the scene is queued and added on the next logic cycle where it will be available from getSceneList

	Parameters:
	name (string) - The name of the scene
	overlay (integer) - Overlay or underlay (optional)"""
	pass
	
def sendMessage(subject, body="", to="", message_from=""):
	"""Sends a message to sensors in any active scene.

	Parameters:
	subject (string) - The subject of the message
	body (string) - The body of the message (optional)
	to (string) - The name of the object to send the message to (optional)
	message_from (string) - The name of the object that the message is coming from (optional)"""
	pass
	
def setGravity(gravity):
	"""Sets the world gravity.

	Parameters:
	gravity (Vector((fx, fy, fz))) - gravity vector"""
	pass
	
def getSpectrum():
	"""Returns a 512 point list from the sound card. This only works if the fmod sound driver is being used.

	Return type:
	list [float], len(getSpectrum()) == 512"""
	return []
	
def getMaxLogicFrame(maxlogic):
	"""Gets the maximum number of logic frames per render frame.

	Returns:
	The maximum number of logic frames per render frame

	Return type:
	integer"""
	return 0
	
def setMaxLogicFrame():
	"""Sets the maximum number of logic frames that are executed per render frame. This does not affect the physic system that still runs at full frame rate.

	Parameters:
	maxlogic (integer) - The new maximum number of logic frames per render frame. Valid values: 1..5"""
	pass
	
def getMaxPhysicsFrame(maxphysics):
	"""Gets the maximum number of physics frames per render frame.

	Returns:
	The maximum number of physics frames per render frame

	Return type:
	integer"""
	return 0
	
def setMaxPhysicsFrame():
	"""Sets the maximum number of physics timestep that are executed per render frame. Higher value allows physics to keep up with realtime even if graphics slows down the game. Physics timestep is fixed and equal to 1/tickrate (see setLogicTicRate) maxphysics/ticrate is the maximum delay of the renderer that physics can compensate.

	Parameters:
	maxphysics (integer) - The new maximum number of physics timestep per render frame. Valid values: 1..5."""
	pass
	
def getLogicTicRate():
	"""Gets the logic update frequency.

	Returns:
	The logic frequency in Hz

	Return type:
	float"""
	return 0.0
	
def setLogicTicRate(ticrate):
	"""Sets the logic update frequency.

	The logic update frequency is the number of times logic bricks are executed every second. The default is 60 Hz.

	Parameters:
	ticrate (float) - The new logic update frequency (in Hz)."""
	pass
	
def getPhysicsTicRate():
	"""Gets the physics update frequency

	Returns:
	The physics update frequency in Hz

	Return type:
	float"""
	return 0.0
	
def setPhysicsTicRate(ticrate):
	"""Sets the physics update frequency

	The physics update frequency is the number of times the physics system is executed every second. The default is 60 Hz.

	Parameters:
	ticrate (float) - The new update frequency (in Hz)."""
	pass
	
def getAnimRecordFrame():
	"""Gets the current frame number used for recording animations. This number is incremented automatically by Blender when the "Record animation" feature is turned on.

	Return type:
	int"""
	return 0
	
def setAnimRecordFrame():
	"""Sets the current frame number used for recording animations. This number is automatically incremented by Blender when the "Record animation" feature is turned on.

	The frame number Must be non-negative, unless Blender has bpy.types.UserPreferencesEdit.use_negative_frames enabled in its user preferences. Only use non-negative numbers to be on the safe side, unless you know what you are doing.

	Parameters:
	framenr (int) - The new frame number."""
	pass
	
def getExitKey():
	"""Gets the key used to exit the game engine

	Returns:
	The key (defaults to bge.events.ESCKEY)

	Return type:
	int"""
	return 0
	
def setExitKey(key):
	"""Sets the key used to exit the game engine

	Parameters:
	key (int) - A key constant from bge.events"""
	pass
	
def NextFrame():
	"""Render next frame (if Python has control)"""
	pass

def setRender(render):
	"""Sets the global flag that controls the render of the scene. If True, the render is done after the logic frame. If False, the render is skipped and another logic frame starts immediately.
	
	Parameters:
	render (bool) – the render flag"""
	pass

def getRender():
	"""Get the current value of the global render flag
	
	Returns:
	The flag value
	
	Return type:
	bool"""
	return False

# Time related functions
def getClockTime():
	"""Get the current BGE render time, in seconds. The BGE render time is the simulation time corresponding to the next scene that will be rendered.
	
	Return type:
	double"""
	return 0.0

def getFrameTime():
	"""Get the current BGE frame time, in seconds. The BGE frame time is the simulation time corresponding to the current call of the logic system. Generally speaking, it is what the user is interested in.
	
	Return type:
	double"""
	return 0.0

def getRealTime():
	"""Get the number of real (system-clock) seconds elapsed since the beginning of the simulation."""
	return 0.0

def getTimeScale():
	"""Get the time multiplier between real-time and simulation time. The default value is 1.0. A value greater than 1.0 means that the simulation is going faster than real-time, a value lower than 1.0 means that the simulation is going slower than real-time.
	
	Return type:
	double"""
	return 0.0

def setTimeScale(time_scale):
	"""Set the time multiplier between real-time and simulation time. A value greater than 1.0 means that the simulation is going faster than real-time, a value lower than 1.0 means that the simulation is going slower than real-time. Note that a too large value may lead to some physics instabilities.

	Parameters:
	time_scale – The new time multiplier."""
	pass

def getUseExternalClock():
	"""Get if the BGE use the inner BGE clock, or rely or on an external clock. The default is to use the inner BGE clock.
	
	Return type:
	bool"""
	return False

def setUseExternalClock(use_external_clock):
	"""Set if the BGE use the inner BGE clock, or rely or on an external clock. If the user selects the use of an external clock, he should call regularly the setClockTime method.
	
	Parameters:
	use_external_clock – the new setting"""
	pass

def setClockTime(new_time):
	"""Set the next value of the simulation clock. It is preferable to use this method from a custom main function in python, as calling it in the logic block can easily lead to a blocked system (if the time does not advance enough to run at least the next logic step).

	Parameters:
	new_time – the next value of the BGE clock (in second)."""
	pass

# Utility Functions
def expandPath(path):
	"""Converts a blender internal path into a proper file system path.

	Use / as directory separator in path You can use '//' at the start of the string to define a relative path; Blender replaces that string by the directory of the current .blend or runtime file to make a full path name. The function also converts the directory separator to the local file system format.

	Parameters:
	path (string) - The path string to be converted/expanded.

	Returns:
	The converted string

	Return type:
	string"""
	return "str"
	
def getAverageFrameRate():
	"""Gets the estimated/average framerate for all the active scenes, not only the current scene.

	Returns:	
	The estimated average framerate in frames per second

	Return type:
	float"""
	return 0.0
	
def getBlendFileList(path = "//"):
	"""Returns a list of blend files in the same directory as the open blend file, or from using the option argument.

	Parameters:
	path (string) - Optional directory argument, will be expanded (like expandPath) into the full path.

	Returns:
	A list of filenames, with no directory prefix

	Return type:
	list"""
	return []
	
def getRandomFloat():
	"""Returns a random floating point value in the range [0 - 1)"""
	return 0.0
	
def PrintGLInfo():
	"""Prints GL Extension Info into the console"""
	pass
	
def PrintMemInfo():
	"""Prints engine statistics into the console"""
	pass
	
def getProfileInfo():
	"""Returns a Python dictionary that contains the same information as the on screen profiler. The keys are the profiler categories and the values are tuples with the first element being time taken (in ms) and the second element being the percentage of total time."""
	return {}

