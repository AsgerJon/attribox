"""AttriClass and subclasses of it do not require dynamic attribute
creation when contained in an AttriBox."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any, Optional

from vistutils.waitaminute import typeMsg

from attribox import AttriBox


class AttriClass:
  """AttriClass and subclasses of it do not require dynamic attribute
  creation when contained in an AttriBox."""

  __outer_box__ = None
  __owning_instance__ = None
  __field_owner__ = None
  __field_name__ = None

  def getOuterBox(self) -> AttriBox:
    """Getter-function for the outer box"""
    if self.__outer_box__ is None:
      e = """The outer box has not been set!"""
      raise RuntimeError(e)
    if isinstance(self.__outer_box__, AttriBox):
      return self.__outer_box__
    e = typeMsg('__outer_box__', self.__outer_box__, AttriBox)
    raise TypeError(e)

  def getOwningInstance(self) -> Any:
    """Getter-function for the owning instance"""
    return self.__owning_instance__

  def getFieldName(self) -> Optional[str]:
    """Getter-function for the field name"""
    return self.__field_name__

  def getFieldOwner(self) -> Optional[type]:
    """Getter-function for the field owner"""
    return self.__field_owner__
