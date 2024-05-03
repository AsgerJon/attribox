"""The 'testBox' function receives an object and tests if its namespace is
ready for use in AttriBox."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations


def testBox(obj: object) -> bool:
  """The 'testBox' function receives a class and tests if its namespace is
  ready for use in AttriBox."""
  names = ['__outer_box__', '__owning_instance__', '__field_owner__',
           '__field_name__']
  Names = ['OuterBox', 'OwningInstance', 'FieldOwner', 'FieldName']
  testNames = []
  for (name, Name) in zip(names, Names):
    testNames.append(name)
    testNames.append('get%s' % Name)
    testNames.append('set%s' % Name)
  for testName in testNames:
    if not hasattr(obj, testName):
      return False
  return True
