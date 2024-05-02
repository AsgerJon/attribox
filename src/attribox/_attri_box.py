"""AttriBox subclasses the TypedDescriptor class and incorporates
syntactic sugar for setting the inner class, and for the inner object
creation. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import sys
from typing import Any, Callable
from types import MethodType

from icecream import ic
from vistutils.text import monoSpace, stringList
from vistutils.waitaminute import typeMsg

from attribox import TypedDescriptor, scope, this
from morevistutils import setterFactory, getterFactory

if sys.version_info.minor < 11:
  from typing_extensions import Self
else:
  from typing import Self

ic.configureOutput(includeContext=True, )


class AttriBox(TypedDescriptor):
  """AttriBox subclasses the TypedDescriptor class and incorporates
  syntactic sugar for setting the inner class, and for the inner object
  creation. """

  __positional_args__ = None
  __keyword_args__ = None
  __get_callbacks__ = None
  __set_callbacks__ = None
  __del_callbacks__ = None

  @staticmethod
  def validateBoxed(obj: object) -> bool:
    """Tests if an object requires boxing. """
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

  @staticmethod
  def boxObject(obj: object, ) -> object:
    """This method adds to the given object the attributes and methods
    required for use with AttriBox. Please note that instances of
    subclasses of AttriClass are exempted from this."""

    names = ['__outer_box__', '__owning_instance__', '__field_owner__',
             '__field_name__']
    Names = ['OuterBox', 'OwningInstance', 'FieldOwner', 'FieldName']
    types = [TypedDescriptor, object, type, str]

    for (name, Name, type_) in zip(names, Names, types):
      setattr(obj, name, None)
      getter = MethodType(getterFactory(name, type_), obj)
      setter = MethodType(setterFactory(name, type_), obj)
      setattr(obj, 'get%s' % Name, getter)
      setattr(obj, 'set%s' % Name, setter)
    return obj

  def __init__(self, *args, **kwargs) -> None:
    """Initializes the AttriBox instance. """
    if not kwargs.get('_root', False):
      e = """The AttriBox class should not be instantiated directly!"""
      raise TypeError(e)
    if not args:
      e = """The inner class must be provided. """
      raise TypeError(e)
    innerClass = args[0]
    if not isinstance(innerClass, type):
      e = typeMsg('innerClass', innerClass, type)
      raise TypeError(e)
    self._setInnerClass(innerClass)

  def _getGetCallbacks(self) -> list[Callable]:
    """Getter-function for list of functions to be called on get."""
    if self.__get_callbacks__ is None:
      self.__get_callbacks__ = []
    return self.__get_callbacks__

  def _getSetCallbacks(self) -> list[Callable]:
    """Getter-function for list of functions to be called on set."""
    if self.__set_callbacks__ is None:
      self.__set_callbacks__ = []
    return self.__set_callbacks__

  def _getDelCallbacks(self) -> list[Callable]:
    """Getter-function for list of functions to be called on del."""
    if self.__del_callbacks__ is None:
      self.__del_callbacks__ = []
    return self.__del_callbacks__

  def notifyGet(self, callMeMaybe: Callable) -> Callable:
    """Adds given callable to list of callables to be notified on get."""
    self._getGetCallbacks().append(callMeMaybe)
    return callMeMaybe

  def notifySet(self, callMeMaybe: Callable) -> Callable:
    """Adds given callable to list of callables to be notified on set."""
    self._getSetCallbacks().append(callMeMaybe)
    return callMeMaybe

  def notifyDel(self, callMeMaybe: Callable) -> Callable:
    """Adds given callable to list of callables to be notified on del."""
    self._getDelCallbacks().append(callMeMaybe)
    return callMeMaybe

  def ONGET(self, callMeMaybe: Callable) -> Callable:
    """Decorator for adding a function to the get callbacks."""
    return self.notifyGet(callMeMaybe)

  def ONSET(self, callMeMaybe: Callable) -> Callable:
    """Decorator for adding a function to the set callbacks."""
    return self.notifySet(callMeMaybe)

  def ONDEL(self, callMeMaybe: Callable) -> Callable:
    """Decorator for adding a function to the del callbacks."""
    return self.notifyDel(callMeMaybe)

  @classmethod
  def __class_getitem__(cls, innerClass: type) -> Self:
    """Syntactic sugar for setting the inner class. """
    return cls(innerClass, _root=True)

  def __call__(self, *args, **kwargs) -> Self:
    """Syntactic sugar for creating an instance of the inner class. """
    self.__positional_args__ = args
    self.__keyword_args__ = kwargs
    return self

  def _getPrivateName(self, ) -> str:
    """Returns the name of the private attribute used to store the inner
    object. """
    return '__%s_value__' % (self._getFieldName(),)

  def _getArgs(self, instance: object) -> list:
    """Getter-function for the positional arguments. This includes 'self'
    if the 'this' object were included when instantiating the AttriBox."""
    args = []
    for arg in self.__positional_args__:
      if arg is this:
        args.append(instance)
      elif arg is scope:
        args.append(self._getFieldOwner())
      else:
        args.append(arg)
    return args

  def _getKwargs(self) -> dict:
    """Getter-function for the keyword arguments. """
    return {**self.__keyword_args__, }

  def _createInnerObject(self, instance: object) -> object:
    """Creates an instance of the inner class. """
    innerClass = self._getInnerClass()
    kwargs = self.__keyword_args__

  def _typeGuard(self, item: object) -> Any:
    """Raises a TypeError if the item is not an instance of the inner
    class. """
    innerClass = self._getInnerClass()
    if not isinstance(item, innerClass):
      e = typeMsg('item', item, innerClass)
      raise TypeError(monoSpace(e))

  def __str__(self, ) -> str:
    ownerName = self._getFieldOwner().__name__
    fieldName = self._getFieldName()
    innerName = self._getInnerClass().__name__
    return '%s.%s: %s' % (ownerName, fieldName, innerName)

  def __repr__(self, ) -> str:
    ownerName = self._getFieldOwner().__name__
    fieldName = self._getFieldName()
    innerName = self._getInnerClass().__name__
    args = ', '.join([*self.__positional_args__, *self.__keyword_args__])
    return '%s = AttriBox[%s](%s)' % (fieldName, innerName, args)

  @classmethod
  def _getOwnerListName(cls) -> str:
    """Returns the name at which the list of attribute instances of this
    type. Please note that this name is not unique to the owner as they
    are in separate scopes."""
    return '__boxes_%s__' % cls.__qualname__

  def __set_name__(self, owner: type, name: str) -> None:
    """Sets the name of the field. """
    ownerListName = self._getOwnerListName()
    TypedDescriptor.__set_name__(self, owner, name)
    existing = getattr(owner, ownerListName, [])
    if existing:
      return setattr(owner, ownerListName, [*existing, self])
    setattr(owner, ownerListName, [self, ])
    oldInitSub = getattr(owner, '__init_subclass__')

    def newInitSub(cls, *args, **kwargs) -> None:
      """Triggers the extra init"""
      oldInitSub(*args, **kwargs)
      self.applyBoxes(cls)

    setattr(owner, '__init_subclass__', classmethod(newInitSub))

  @classmethod
  def applyBoxes(cls, owner: type) -> None:
    """Applies the boxes to the owner class."""
    ownerListName = cls._getOwnerListName()
    boxes = getattr(owner, ownerListName, [])
    for box in boxes:
      if not isinstance(box, AttriBox):
        e = typeMsg('box', box, AttriBox)
        raise TypeError(e)
      boxName = box._getFieldName()
      setattr(cls, boxName, box)
      cls.__set_name__(box, owner, boxName)

  def __get__(self, instance: object, owner: type) -> Any:
    """The __get__ method is called when the descriptor is accessed via the
    owning instance. Subclasses should not override this method, but should
    instead implement the __instance_get__ method. """
    if instance is None:
      return self
    val = self.__instance_get__(instance, )
    for callMeMaybe in self._getGetCallbacks():
      callMeMaybe(instance, val)
    return val

  def __set__(self, instance: object, value: Any) -> None:
    """The __set__ method is called when the descriptor is assigned a value
    via the owning instance. """
    pvtName = self._getPrivateName()
    oldValue = getattr(instance, pvtName, None)
    self._typeGuard(value)
    setattr(instance, pvtName, value)
    for callMeMaybe in self._getSetCallbacks():
      callMeMaybe(instance, oldValue, value)

  def __delete__(self, instance: object) -> None:
    """The __delete__ method is called when the descriptor is deleted via
    the owning instance. """
    pvtName = self._getPrivateName()
    fieldName = self._getFieldName()
    oldValue = getattr(instance, pvtName, None)
    delattr(instance, pvtName)
    delattr(instance, fieldName)
    for callMeMaybe in self._getDelCallbacks():
      callMeMaybe(instance, oldValue)
