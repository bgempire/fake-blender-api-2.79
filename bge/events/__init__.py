"""This module holds key constants for the SCA_KeyboardSensor."""

## Functions
def EventToString(event):
	"""Return the string name of a key event. Will raise a ValueError error if its invalid.

	Parameters:
	event (int) - key event constant from bge.events or the keyboard sensor.

	Return type:
	string"""
	return "str"
	
def EventToCharacter(event, shift):
	"""Return the string name of a key event. Returns an empty string if the event cant be represented as a character.

	Parameters:	
	event (int) - key event constant from bge.events or the keyboard sensor.
	shift (bool) - set to true if shift is held.

	Return type:
	string"""
	return "str"

## Keys (Constants)
# Mouse Keys
LEFTMOUSE = 116
MIDDLEMOUSE = 117
RIGHTMOUSE = 118
WHEELUPMOUSE = 120
WHEELDOWNMOUSE = 121
MOUSEX = 122
MOUSEY = 123

# Keyboard Keys
# Alphabet Keys
AKEY = 23
BKEY = 24
CKEY = 25
DKEY = 26
EKEY = 27
FKEY = 28
GKEY = 29
HKEY = 30
IKEY = 31
JKEY = 32
KKEY = 33
LKEY = 34
MKEY = 35
NKEY = 36
OKEY = 37
PKEY = 38
QKEY = 39
RKEY = 40
SKEY = 41
TKEY = 42
UKEY = 43
VKEY = 44
WKEY = 45
XKEY = 46
YKEY = 47
ZKEY = 48

# Number Keys
ZEROKEY = 13
ONEKEY = 14
TWOKEY = 15
THREEKEY = 16
FOURKEY = 17
FIVEKEY = 18
SIXKEY = 19
SEVENKEY = 20
EIGHTKEY = 21
NINEKEY = 22

# Modifiers Keys
CAPSLOCKKEY = 49
LEFTCTRLKEY = 50
LEFTALTKEY = 51
RIGHTALTKEY = 52
RIGHTCTRL = 53
RIGHTSHIFTKEY = 54
LEFTSHIFTKEY = 55

# Arrow Keys
LEFTARROWKEY = 69
DOWNARROWKEY = 70
RIGHTARROWKEY = 71
UPARROWKEY = 72

# Numberpad Keys
PAD0 = 84
PAD1 = 77
PAD2 = 73
PAD3 = 78
PAD4 = 74
PAD5 = 79
PAD6 = 75
PAD7 = 80
PAD8 = 76
PAD9 = 71
PADPERIOD = 82
PADSLASHKEY = 83
PADASTERKEY = 9
PADMINUS = 85
PADENTER = 86
PADPLUSKEY = 87

# Function Keys
F1KEY = 88
F2KEY = 89
F3KEY = 90
F4KEY = 91
F5KEY = 92
F6KEY = 93
F7KEY = 94
F8KEY = 95
F9KEY = 96
F10KEY = 97
F11KEY = 98
F12KEY = 99
F13KEY = 100
F14KEY = 101
F15KEY = 102
F16KEY = 103
F17KEY = 104
F18KEY = 105
F19KEY = 106

# Other Keys
ACCENTGRAVEKEY = 63
BACKSLASHKEY = 65
BACKSPACEKEY = 59
COMMAKEY = 10
DELKEY = 60
ENDKEY = 113
EQUALKEY = 66
ESCKEY = 56
HOMEKEY = 110
INSERTKEY = 109
LEFTBRACKETKEY = 67
LINEFEEDKEY = 58
MINUSKEY = 11
PAGEDOWNKEY = 112
PAGEUPKEY = 111
PAUSEKEY = 108
PERIODKEY = 12
QUOTEKEY = 62
RIGHTBRACKETKEY = 68
RETKEY = 7
ENTERKEY = 7
SEMICOLONKEY = 61
SLASHKEY = 64
SPACEKEY = 8
TABKEY = 57

