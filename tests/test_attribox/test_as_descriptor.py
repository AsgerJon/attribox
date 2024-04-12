"""TestAsDescriptor creates a custom class owning several instances of the
Attribox framework."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from unittest import TestCase

from attribox import AttriBox, scope, this


class OwnerClass:
  """Test of the AttriBox framework as a descriptor."""

  def __init__(self, *args, **kwargs) -> None:
    pass

  x = AttriBox[int](69)
  y = AttriBox[int](420)

  data = AttriBox[dict](name='John', hasSwag=True, instance=this,
                        owner=scope)

  pi = AttriBox[float](3.14159)


class ChildOwner(OwnerClass):
  """Testing if the AttriBox framework works with inheritance."""


class TestBox(TestCase):
  """Test of the AttriBox framework as a descriptor."""

  def test_00(self) -> None:
    """Test of the AttriBox framework as a descriptor."""
    instance = OwnerClass()
    self.assertEqual(instance.x, 69)
    self.assertEqual(instance.y, 420)

    otherInstance = OwnerClass()
    self.assertEqual(otherInstance.x, 69)
    self.assertEqual(otherInstance.y, 420)

    self.assertIsNot(instance.data, otherInstance.data)
    self.assertIs(instance.__class__.x, otherInstance.__class__.x)

  def test01(self) -> None:
    """Test if the owner lists the instances"""
    name = AttriBox._getOwnerListName()
    stuff = getattr(OwnerClass, name)
    self.assertIn(OwnerClass.x, stuff)
    self.assertIn(OwnerClass.y, stuff)
    self.assertIn(OwnerClass.data, stuff)
    self.assertIn(OwnerClass.pi, stuff)

  def test02(self) -> None:
    """Test if the owner lists the instances"""
    childStuff = getattr(ChildOwner, AttriBox._getOwnerListName())
    parentStuff = getattr(OwnerClass, AttriBox._getOwnerListName())
    for item in childStuff:
      self.assertIn(item, parentStuff)
    for item in parentStuff:
      self.assertIn(item, childStuff)


class TestChildBox(TestCase):
  """Testing if the AttriBox framework works with inheritance."""

  def test_00(self) -> None:
    """Testing if the AttriBox framework works with inheritance."""
    instance = ChildOwner()
    self.assertEqual(instance.x, 69)
    self.assertEqual(instance.y, 420)

    otherInstance = ChildOwner()
    self.assertEqual(otherInstance.x, 69)
    self.assertEqual(otherInstance.y, 420)
