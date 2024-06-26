"""AbstractDescriptor outlines the structure required by the descriptor
protocol. It is not intended to be used directly, but to be subclassed by
concrete descriptors. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod
from typing import Any

from vistutils.text import monoSpace
from vistutils.waitaminute import typeMsg


class AbstractDescriptor:
  """AbstractDescriptor outlines the structure required by the descriptor
  protocol. It is not intended to be used directly, but to be subclassed by
  concrete descriptors.

  Please note that __init__ and __init_subclass__ are reimplemented only
  to prevent the delicate object.__init__ and object.__init_subclass__ from
  raising errors when receiving scawy argz.
  """

  __field_name__ = None
  __field_owner__ = None

  def __init__(self, *args, **kwargs) -> None:
    """Why are we still here?"""
    object.__init__(self)

  def __init_subclass__(cls, **kwargs) -> None:
    """Just to suffer? Or to raise errors?"""
    super().__init_subclass__()

  def _getFieldName(self) -> str:
    """Returns the name of the field the descriptor is assigned to. """
    if self.__field_name__ is None:
      e = """The descriptor has not been assigned to a field. """
      raise AttributeError(monoSpace(e))
    if isinstance(self.__field_name__, str):
      return self.__field_name__
    e = typeMsg('__field_name__', self.__field_name__, str)
    raise TypeError(monoSpace(e))

  def _getFieldOwner(self) -> type:
    """Returns the type of the class the descriptor is assigned to. """
    if self.__field_owner__ is None:
      e = """The descriptor has not been assigned to a field. """
      raise AttributeError(monoSpace(e))
    if isinstance(self.__field_owner__, type):
      return self.__field_owner__
    e = typeMsg('__field_owner__', self.__field_owner__, type)
    raise TypeError(monoSpace(e))

  def _getPrivateName(self, ) -> str:
    """Returns the name of the private attribute used to store the inner
    object. """
    return '__%s_value__' % (self.__field_name__,)

  def __set_name__(self, owner: type, name: str) -> None:
    """The __set_name__ method is called when the descriptor is assigned to
    a class attribute. """
    self.__field_name__ = name
    self.__field_owner__ = owner

  @abstractmethod
  def __instance_get__(self, instance: object, owner: type) -> Any:
    """The __instance_get__ method is called when the descriptor is accessed
    via the owning instance. """

  def __get__(self, instance: object, owner: type) -> Any:
    """The __get__ method is called when the descriptor is accessed via the
    owning instance. Subclasses should not override this method, but should
    instead implement the __instance_get__ method. """
    if instance is None:
      return self
    return self.__instance_get__(instance, owner)

  def __set__(self, instance: object, value: Any) -> None:
    """The __set__ method is called when the descriptor is assigned a value
    via the owning instance. The default implementation raises an error."""
    e = """The '%s' descriptor class does not implement a setter!"""
    raise TypeError(e % self.__class__.__name__)

  def __delete__(self, instance: object) -> None:
    """The __delete__ method is called when the descriptor is deleted via
    the owning instance. The default implementation raises an error."""
    e = """The '%s' descriptor class does not implement a deleter!"""
    raise TypeError(e % self.__class__.__name__)
