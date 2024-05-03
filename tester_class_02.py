"""TesterClass02 lmao"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from attribox import AttriBox
from tester_class_01 import TesterClass01


class TesterClass02:
  """TesterClass02 lmao"""

  wrapped = AttriBox[TesterClass01]()

  def __str__(self) -> str:
    return 'Wrapping: %s' % self.wrapped
