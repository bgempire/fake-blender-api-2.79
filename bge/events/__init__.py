"""Game Keys (bge.events)

This module holds key constants for the SCA_KeyboardSensor."""


# Functions
def EventToString(event):
    # type: (int) -> str
    """Return the string name of a key event. Will raise a ValueError error if its invalid.

    Args:
        event: key event constant from bge.events or the keyboard sensor.

    Returns:
        The key event name."""

    pass


def EventToCharacter(event, shift):
    # type: (int, bool) -> str
    """Return the string name of a key event. Returns an empty string if the event cant be represented as a character.

    Args:
        event: key event constant from bge.events or the keyboard sensor.
        shift: set to true if shift is held.

    Returns:
        The key event character."""

    pass


# Keys (Constants)
# Mouse Keys
LEFTMOUSE = 116  # type: int
MIDDLEMOUSE = 117  # type: int
RIGHTMOUSE = 118  # type: int
WHEELUPMOUSE = 120  # type: int
WHEELDOWNMOUSE = 121  # type: int
MOUSEX = 122  # type: int
MOUSEY = 123  # type: int

# Keyboard Keys
# Alphabet Keys
AKEY = 23  # type: int
BKEY = 24  # type: int
CKEY = 25  # type: int
DKEY = 26  # type: int
EKEY = 27  # type: int
FKEY = 28  # type: int
GKEY = 29  # type: int
HKEY = 30  # type: int
IKEY = 31  # type: int
JKEY = 32  # type: int
KKEY = 33  # type: int
LKEY = 34  # type: int
MKEY = 35  # type: int
NKEY = 36  # type: int
OKEY = 37  # type: int
PKEY = 38  # type: int
QKEY = 39  # type: int
RKEY = 40  # type: int
SKEY = 41  # type: int
TKEY = 42  # type: int
UKEY = 43  # type: int
VKEY = 44  # type: int
WKEY = 45  # type: int
XKEY = 46  # type: int
YKEY = 47  # type: int
ZKEY = 48  # type: int

# Number Keys
ZEROKEY = 13  # type: int
ONEKEY = 14  # type: int
TWOKEY = 15  # type: int
THREEKEY = 16  # type: int
FOURKEY = 17  # type: int
FIVEKEY = 18  # type: int
SIXKEY = 19  # type: int
SEVENKEY = 20  # type: int
EIGHTKEY = 21  # type: int
NINEKEY = 22  # type: int

# Modifier Keys
CAPSLOCKKEY = 49  # type: int
LEFTCTRLKEY = 50  # type: int
LEFTALTKEY = 51  # type: int
RIGHTALTKEY = 52  # type: int
RIGHTCTRL = 53  # type: int
RIGHTSHIFTKEY = 54  # type: int
LEFTSHIFTKEY = 55  # type: int

# Arrow Keys
LEFTARROWKEY = 69  # type: int
DOWNARROWKEY = 70  # type: int
RIGHTARROWKEY = 71  # type: int
UPARROWKEY = 72  # type: int

# Number pad Keys
PAD0 = 84  # type: int
PAD1 = 77  # type: int
PAD2 = 73  # type: int
PAD3 = 78  # type: int
PAD4 = 74  # type: int
PAD5 = 79  # type: int
PAD6 = 75  # type: int
PAD7 = 80  # type: int
PAD8 = 76  # type: int
PAD9 = 71  # type: int
PADPERIOD = 82  # type: int
PADSLASHKEY = 83  # type: int
PADASTERKEY = 9  # type: int
PADMINUS = 85  # type: int
PADENTER = 86  # type: int
PADPLUSKEY = 87  # type: int

# Function Keys
F1KEY = 88  # type: int
F2KEY = 89  # type: int
F3KEY = 90  # type: int
F4KEY = 91  # type: int
F5KEY = 92  # type: int
F6KEY = 93  # type: int
F7KEY = 94  # type: int
F8KEY = 95  # type: int
F9KEY = 96  # type: int
F10KEY = 97  # type: int
F11KEY = 98  # type: int
F12KEY = 99  # type: int
F13KEY = 100  # type: int
F14KEY = 101  # type: int
F15KEY = 102  # type: int
F16KEY = 103  # type: int
F17KEY = 104  # type: int
F18KEY = 105  # type: int
F19KEY = 106  # type: int

# Other Keys
ACCENTGRAVEKEY = 63  # type: int
BACKSLASHKEY = 65  # type: int
BACKSPACEKEY = 59  # type: int
COMMAKEY = 10  # type: int
DELKEY = 60  # type: int
ENDKEY = 113  # type: int
EQUALKEY = 66  # type: int
ESCKEY = 56  # type: int
HOMEKEY = 110  # type: int
INSERTKEY = 109  # type: int
LEFTBRACKETKEY = 67  # type: int
LINEFEEDKEY = 58  # type: int
MINUSKEY = 11  # type: int
PAGEDOWNKEY = 112  # type: int
PAGEUPKEY = 111  # type: int
PAUSEKEY = 108  # type: int
PERIODKEY = 12  # type: int
QUOTEKEY = 62  # type: int
RIGHTBRACKETKEY = 68  # type: int
ENTERKEY = 7  # type: int
SEMICOLONKEY = 61  # type: int
SLASHKEY = 64  # type: int
SPACEKEY = 8  # type: int
TABKEY = 57  # type: int

# Deprecated
RETKEY = 7  # type: int
"""Deprecated: use bge.events.ENTERKEY"""
