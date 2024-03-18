"""Testing the uniqueness of 'scope' and 'this'."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from unittest import TestCase

from attribox import this, scope

orphanThis = this
orphanScope = scope


class Tester:
  """Test of this and scope."""

  classThis = this
  classScope = scope

  def __init__(self, ) -> None:
    self.instanceThis = this
    self.instanceScope = scope


class TestThisScope(TestCase):
  """Test of this and scope."""

  def test_00(self) -> None:

    if orphanThis is not this:
      raise AssertionError('The orphaned this is not unique.')

    if orphanScope is not scope:
      raise AssertionError('The orphaned scope is not unique.')

    if Tester.classThis is not this:
      raise AssertionError('The class this is not unique.')

    if Tester.classScope is not scope:
      raise AssertionError('The class scope is not unique.')
