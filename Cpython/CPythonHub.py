from __future__ import annotations
import time
from matplotlib import pyplot as plt
import math
# run code in python
class CPythonHub:
    "Cpython as a hub"
    def __init__(self):
        """CPythonHub Simulated hub
        """
    pass
    class system:
        def set_stop_button(self):
            pass
        def storage(*args, **kwargs):
            return bytes(1)
            
    class display:
        def char(c):
            print (c)
            
    class buttons:
        alreadyPressed = False
        def pressed():
            if not CPythonHub.buttons.alreadyPressed:
                CPythonHub.buttons.alreadyPressed = True
                return input("press 1 for Left, 2 for Center, and 3 for Right:")
            else:
                CPythonHub.buttons.alreadyPressed = False
                return None
            
            
    class light:
        def on(color):
            pass
    
def wait(millisconds):
    time.sleep(millisconds/1000)
    
class Button:
    RIGHT = "3"
    LEFT =  "1"
    CENTER = "2"

class Pose:
    def __init__(self,x,y,a):
        self.x =x
        self.y =y
        self.a =a
    def copy(self):
        return Pose(self.x,self.y,self.a)

class DriveBase:
    position =Pose(0,0,0)
    def __init__(self,*args):
        plt.ion
    def straight(self,distance,**kwargs):
        oldPosition = self.position.copy()
        self.position.x += distance * math.cos(math.degrees(self.position.a))
        self.position.y += distance* math.sin(math.degrees(self.position.a))
        print([oldPosition.x,self.position.x],[oldPosition.y,self.position.y])
        plt.plot([oldPosition.x,self.position.x],[oldPosition.y,self.position.y])
        time.sleep(0.2)
    def turn(self,angle,**kwargs):
        self.position.a += angle
    def done(self): return True


from enum import Enum
from typing import Union, TYPE_CHECKING
import os

if TYPE_CHECKING or os.environ.get("SPHINX_BUILD") == "True":
    Number = Union[int, float]
    """
    Numbers can be represented as integers or floating point values:

        * Integers (:class:`int <ubuiltins.int>`) are whole numbers
          like ``15`` or ``-123``.
        * Floating point values (:class:`float <ubuiltins.float>`) are decimal
          numbers like ``3.14`` or ``-123.45``.

    If you see :class:`Number` as the argument type, both
    :class:`int <ubuiltins.int>` and :class:`float <ubuiltins.float>` may be used.

    For example, :func:`wait(15) <pybricks.tools.wait>` and
    :func:`wait(15.75) <pybricks.tools.wait>` are both allowed. In most functions,
    however, your input value will be truncated to a whole number anyway. In this
    example, either command makes the program pause for just 15 milliseconds.

    .. note::
        The BOOST Move hub doesn't support floating point numbers due to
        limited system resources. Only integers can be used on that hub.
    """


class _PybricksEnumMeta(type(Enum)):
    @classmethod
    def __dir__(cls):
        yield "__class__"
        yield "__name__"
        for member in cls:
            yield member.name


class _PybricksEnum(Enum, metaclass=_PybricksEnumMeta):
    def __dir__(self):
        yield "__class__"
        for member in type(self):
            yield member.name

    def __str__(self):
        return "{}.{}".format(type(self).__name__, self.name)

    def __repr__(self):
        return str(self)


class Color:
    """Light or surface color."""

    NONE: Color = ...
    BLACK: Color = ...
    GRAY: Color = ...
    WHITE: Color = ...
    RED: Color = ...
    ORANGE: Color = ...
    BROWN: Color = ...
    YELLOW: Color = ...
    GREEN: Color = ...
    CYAN: Color = ...
    BLUE: Color = ...
    VIOLET: Color = ...
    MAGENTA: Color = ...

    def __init__(self, h: Number, s: Number = 100, v: Number = 100):
        """Color(h, s=100, v=100)

        Arguments:
            h (Number, deg): Hue.
            s (Number, %): Saturation.
            v (Number, %): Brightness value.
        """

        self.h = int(h) % 360
        """
        The hue.
        """

        self.s = max(0, min(int(s), 100))
        """
        The saturation.
        """

        self.v = max(0, min(int(v), 100))
        """
        The brightness value.
        """

    def __repr__(self):
        return "Color(h={}, s={}, v={})".format(self.h, self.s, self.v)

    def __eq__(self, other: Color) -> bool:
        ...

    def __mul__(self, scale: float) -> Color:
        v = max(0, min(self.v * scale, 100))
        return Color(self.h, self.s, int(v), self.name)

    def __rmul__(self, scale: float) -> Color:
        return self.__mul__(scale)

    def __truediv__(self, scale: float) -> Color:
        return self.__mul__(1 / scale)

    def __floordiv__(self, scale: int) -> Color:
        return self.__mul__(1 / scale)


Color.NONE = Color(0, 0, 0)
Color.BLACK = Color(0, 0, 10)
Color.GRAY = Color(0, 0, 50)
Color.WHITE = Color(0, 0, 100)
Color.RED = Color(0, 100, 100)
Color.ORANGE = Color(30, 100, 100)
Color.BROWN = Color(30, 100, 50)
Color.YELLOW = Color(60, 100, 100)
Color.GREEN = Color(120, 100, 100)
Color.CYAN = Color(180, 100, 100)
Color.BLUE = Color(240, 100, 100)
Color.VIOLET = Color(270, 100, 100)
Color.MAGENTA = Color(300, 100, 100)
