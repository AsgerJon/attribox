"""Main Tester Script for the project."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen

from __future__ import annotations

import os
import sys

from attribox import AttriBox


class Point:
  """This example class uses AttriBox to implement coordinates"""

  x = AttriBox[int](0)
  y = AttriBox[int](0)

  def __init__(self, x: int = 0, y: int = 0) -> None:
    print('Point.__init__ at: (%d, %d)' % (x, y))
    self.x = x
    self.y = y

  @x.ONGET
  def _notifyGet(self, value: int) -> None:
    """This method notifies when an AttriBox calls __get__"""
    print('Return value of x: %d' % value)

  @x.ONSET
  def _notifySet(self, oldVal: int, newVal: int) -> None:
    """This method notifies when an AttriBox calls __set__"""
    print('Changing x from %s to %s' % (oldVal, newVal))

  def __add__(self, other: Point) -> Point:
    """Implementation of the addition operator."""
    return Point(self.x + other.x, self.y + other.y)

  def __sub__(self, other: Point) -> Point:
    """Implementation of the subtraction operator."""
    return Point(self.x - other.x, self.y - other.y)

  def __str__(self, ) -> str:
    """String representation of the point. """
    return '(%d, %d)' % (self.x, self.y)

  def __repr__(self) -> str:
    """Code representation"""
    return '%s(%d, %d)' % (self.__class__.__name__, self.x, self.y)


class Rectangle:
  """This rectangle now uses AttriBox to define topLeft and bottomRight
  corners. """

  topLeft = AttriBox[Point](0, 0)
  bottomRight = AttriBox[Point](0, 0)

  def __init__(self, *args) -> None:
    print('%s start of __init__' % self.__class__.__name__)
    intArgs = []
    pointArgs = []
    for arg in args:
      if isinstance(arg, int):
        intArgs.append(arg)
      elif isinstance(arg, Point):
        pointArgs.append(arg)
    if len(pointArgs) == 2:
      self.topLeft.x = pointArgs[0].x
      self.topLeft.y = pointArgs[0].y
      self.bottomRight.x = pointArgs[1].x
      self.bottomRight.y = pointArgs[1].y
    elif len(intArgs) == 4:
      self.bottomRight.y = intArgs.pop()
      self.bottomRight.x = intArgs.pop()
      self.topLeft.y = intArgs.pop()
      self.topLeft.x = intArgs.pop()
    clsName = self.__class__.__name__
    print('End of %s.__init__' % (clsName,))

  def __str__(self, ) -> str:
    """String representation of the rectangle. """
    return 'Rectangle(%s, %s)' % (self.topLeft, self.bottomRight)

  def area(self) -> int:
    """Returns the area of the rectangle. """
    v = self.topLeft - self.bottomRight
    return abs(v.x * v.y)


def tester00() -> None:
  """LMAO"""
  stuff = [os, sys, 'hello world']
  for item in stuff:
    print(item)


def tester01() -> None:
  """Testing of Point class"""
  r = Rectangle(3, 4, 69, 420)
  print(r)
  r.topLeft.x = 77
  print(r)


if __name__ == '__main__':
  tester01()
