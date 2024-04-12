"""Testing the errors of the AttriBox framework."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from unittest import TestCase

from attribox import scope, this, AttriBox


class OwnerClass:
  """Class owning AttriBox instances."""

  x = AttriBox[int](69)
  y = AttriBox[int](420)

  data = AttriBox[dict](name='John', hasSwag=True, instance=this,
                        owner=scope)

  pi = AttriBox[float](3.14159)


class TestErrors(TestCase):
  """Testing the errors of the AttriBox framework."""

  def test_00(self) -> None:
    """Testing the errors of the AttriBox framework."""
    with self.assertRaises(TypeError):
      AttriBox()

  def test_01(self) -> None:
    """Testing the errors of the AttriBox framework."""
    with self.assertRaises(NotImplementedError):
      instance = OwnerClass()
      instance.x = 69

  def test_02(self) -> None:
    """Testing the errors of the AttriBox framework."""
    with self.assertRaises(NotImplementedError):
      instance = OwnerClass()
      del instance.x
