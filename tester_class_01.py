"""TesterClass01"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any, Self

from vistutils.parse import maybe

from attribox import AttriClass, AttriBox


class BoxInt(AttriClass):
  """Integer valued class great for AttriBox!"""
  __inner_value__ = None

  def __init__(self, value: int = None) -> None:
    self.__inner_value__ = maybe(value, 0)

  def __iadd__(self, other) -> Self | int:
    self.__inner_value__ += other
    return self

  def __isub__(self, other) -> Self | int:
    self.__inner_value__ -= other
    return self

  def __imul__(self, other) -> Self | int:
    self.__inner_value__ *= other
    return self

  def __add__(self, other) -> Self | int:
    return BoxInt(self.__inner_value__ + other)

  def __sub__(self, other) -> Self | int:
    return BoxInt(self.__inner_value__ - other)

  def __mul__(self, other) -> Self | int:
    return BoxInt(self.__inner_value__ * other)

  def __radd__(self, other) -> Self | int:
    return BoxInt(self.__inner_value__ + other)

  def __rsub__(self, other) -> Self | int:
    return BoxInt(self.__inner_value__ - other)

  def __rmul__(self, other) -> Self | int:
    return BoxInt(self.__inner_value__ * other)

  def __str__(self, ) -> str:
    """String representation of the inner value."""
    return '%d' % self.__inner_value__

  def __repr__(self, ) -> str:
    """Code representation"""
    return '%s(%d)' % (self.__class__.__name__, self.__inner_value__)

  def __eg__(self, other) -> bool:
    return False if self - other else True

  def __ne__(self, other) -> bool:
    return True if self - other else False

  def __lt__(self, other) -> bool:
    return True if (other - self) > 0 else False

  def __le__(self, other) -> bool:
    return self == other or self < other

  def __gt__(self, other) -> bool:
    return True if (self - other) > 0 else False

  def __ge__(self, other) -> bool:
    return self == other or self > other

  def __pow__(self, other) -> Self | int:
    return BoxInt(self.__inner_value__ ** other)

  def __rpow__(self, other) -> Self | int:
    return BoxInt(other ** self.__inner_value__)

  def __mod__(self, other) -> Self | int:
    return BoxInt(self.__inner_value__ % other)

  def __rmod__(self, other) -> Self | int:
    return BoxInt(other % self.__inner_value__)

  def __divmod__(self, other) -> tuple[Self | int, Self | int]:
    out = divmod(self.__inner_value__, other)
    return BoxInt(out[0]), BoxInt(out[1])

  def __int__(self) -> int:
    return self.__inner_value__

  def __float__(self, ) -> float:
    return float(self.__inner_value__)

  def __complex__(self, ) -> complex:
    return float(self) + 0j


class TesterClass01:
  """TesterClass01"""

  x = AttriBox[BoxInt](3)
  y = AttriBox[BoxInt](4)
  txt = AttriBox[str]('Hello, World!')

  def __str__(self, ) -> str:
    return '%s: %d, %d' % (self.txt, self.x, self.y)
