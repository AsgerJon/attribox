"""NotifBox inherits from TypedDescriptor and provides accessor functions
with notifications."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import sys
from abc import abstractmethod
from typing import Any, Callable

from icecream import ic

from attribox import TypedDescriptor

if sys.version_info.minor < 11:
  pass
else:
  pass

ic.configureOutput(includeContext=True, )


class NotifBox(TypedDescriptor):
  """NotifBox inherits from TypedDescriptor and provides accessor functions
  with notifications."""

  __get_callbacks__ = None
  __set_callbacks__ = None
  __del_callbacks__ = None

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

  @abstractmethod
  def typeGuard(self, item: object) -> None:
    """Raises a TypeError if the item is not an instance of the inner
    class. """

  @abstractmethod
  def __get__(self, instance: object, owner: type) -> Any:
    """The __get__ method is called when the descriptor is accessed via the
    owning instance. Subclasses should not override this method, but should
    instead implement the __instance_get__ method. """

  @abstractmethod
  def __set__(self, instance: object, value: Any) -> None:
    """The __set__ method is called when the descriptor is assigned a value
    via the owning instance. """

  @abstractmethod
  def __delete__(self, instance: object) -> None:
    """The __delete__ method is called when the descriptor is deleted via
    the owning instance. """

  @abstractmethod
  def _createInnerObject(self, instance: object) -> object:
    """Creates an instance of the inner class. """

  @abstractmethod
  def _getPrivateName(self, ) -> str:
    """Returns the name of the private attribute used to store the inner
    object. """
