"""Tester class """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from attribox import AttriBox


class Tester:
  """Tester class """

  x = AttriBox[int](69)
  y = AttriBox[int](420)

  def __str__(self) -> str:
    return '(%s, %s)' % (self.x, self.y)
