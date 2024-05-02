"""This file provides factory functions creating accessor functions."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from types import MethodType
from typing import Any, TYPE_CHECKING, Callable

from vistutils.text import monoSpace
from vistutils.waitaminute import typeMsg


def setterFactory(pubName: str, *args) -> Callable:
  """Returns a function that sets the attribute. """
  pvtName, type_ = None, None
  for arg in args:
    if isinstance(arg, str) and pvtName is None:
      pvtName = arg
    elif isinstance(arg, type) and type_ is None:
      type_ = arg
  pvtName = '_%s' % pubName if pvtName is None else pvtName
  type_ = object if type_ is None else type_
  setterName = 'set%s' % pubName.capitalize()

  typeAnnotations = {
    'self': 'object',
    'value': None,
    'return': 'None',
  }

  base = """Setter-function for attribute named: '%s'. The value is set
  at the private name: '%s' at the given object."""
  docText = monoSpace(base % (pubName, pvtName))

  if type_ is None:
    def func(self, value: Any) -> None:
      """Setter-function"""
      setattr(self, pvtName, value)

    typeAnnotations['value'] = 'object'
  else:
    def func(self, value: Any) -> None:
      """Setter-function"""
      if not isinstance(value, type_):
        e = typeMsg(pvtName, value, type_)
        raise TypeError(e)
      setattr(self, pvtName, value)

    typeAnnotations['value'] = type_.__name__
    typeText = """If the value given is not an instance of: '%s', it will 
    raise a TypeError. """ % type_.__name__
    docText += monoSpace(typeText)

  setattr(func, '__name__', setterName)
  setattr(func, '__qualname__', setterName)
  setattr(func, '__doc__', docText)
  setattr(func, '__annotations__', typeAnnotations)
  return func


def getterFactory(pubName: str, *args) -> Callable:
  """Returns a function that returns the attribute. """
  pvtName, type_ = None, None
  for arg in args:
    if isinstance(arg, str) and pvtName is None:
      pvtName = arg
    elif isinstance(arg, type) and type_ is None:
      type_ = arg
  pvtName = '_%s' % pubName if pvtName is None else pvtName
  type_ = object if type_ is None else type_
  getterName = 'get%s' % pubName.capitalize()

  typeAnnotations = {
    'self': 'object',
    'return': None,
  }

  base = """Getter-function for attribute named: '%s'. The value is 
  assumed to be at private name: '%s' on the object. """
  docText = monoSpace(base % (pubName, pvtName))

  if type_ is None:
    def func(self, ) -> Any:
      """Getter-function"""
      return getattr(self, pvtName)

    typeAnnotations['return'] = 'object'

  else:
    def func(self, ) -> Any:
      """Getter-function"""
      value = getattr(self, pvtName)
      if isinstance(value, type_):
        return value
      e = typeMsg(pvtName, value, type_)
      raise TypeError(e)

    typeAnnotations['return'] = type_.__name__
    typeText = """If the value found is not an instance of: '%s', it will 
    raise a TypeError. """ % type_.__name__
    docText += monoSpace(typeText)

  setattr(func, '__name__', getterName)
  setattr(func, '__qualname__', getterName)
  setattr(func, '__doc__', docText)
  setattr(func, '__annotations__', typeAnnotations)
  return func


def deleterFactory(pubName: str, *args) -> Callable:
  """Returns a function that deletes the attribute. """
  pvtName = None
  for arg in args:
    if isinstance(arg, str) and pvtName is None:
      pvtName = arg
  pvtName = '_%s' % pubName if pvtName is None else pvtName
  deleterName = 'del%s' % pubName.capitalize()

  def func(self, ) -> None:
    """Deleter-function"""
    if hasattr(self, pvtName):
      return delattr(self, pvtName)
    e = """Object: '%s' of type: '%s' has no attribute named: '%s'"""
    selfName = getattr(self, '__name__', str(self))
    clsName = getattr(self, '__class__', ).__name__
    raise AttributeError(monoSpace(e % (selfName, clsName, pvtName)))

  base = """Deleter-function for attribute named: '%s'. The value is 
  assumed to be at private name: '%s' on the object. """
  docText = monoSpace(base % (pubName, pvtName))

  typeAnnotations = {'self': 'object', 'return': 'None', }

  setattr(func, '__name__', deleterName)
  setattr(func, '__qualname__', deleterName)
  setattr(func, '__doc__', docText)
  setattr(func, '__annotations__', typeAnnotations)
  return func
