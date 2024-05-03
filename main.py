"""Main Tester Script for the project."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen

from __future__ import annotations

import os
import sys

from pyperclip import copy

from tester_class_01 import BoxInt, TesterClass01
from tester_class_02 import TesterClass02


def tester00() -> None:
  """LMAO"""
  stuff = [os, sys, 'hello world']
  for item in stuff:
    print(item)


def tester01() -> None:
  NewStr = type('NewStr', (str,), {})

  # Create an instance of NewStr
  newStr = NewStr('Hello, World!')
  oldStr = str('Goodnight World!')

  # Set a new attribute
  try:
    newStr.urMom = 'fat'
    oldStr.urMom = 'very fat'
  except AttributeError as e:
    print(e)

  print(newStr)
  print(oldStr)


def tester02() -> None:
  dunderNames = [
    '__add__', '__sub__', '__mul__', '__truediv__', '__floordiv__',
    '__mod__', '__divmod__', '__pow__', '__lshift__', '__rshift__',
    '__and__', '__xor__', '__or__', '__neg__', '__pos__', '__abs__',
    '__invert__', '__int__', '__float__', '__index__', '__round__',
    '__trunc__', '__floor__', '__ceil__', '__bool__', '__hash__',
    '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__',
    '__bool__', '__hash__', '__index__', '__round__', '__trunc__',
    '__floor__', '__ceil__', '__bool__', '__hash__', '__index__',
    '__round__', '__trunc__', '__floor__', '__ceil__', '__bool__',
    '__hash__', '__index__', '__round__', '__trunc__', '__floor__',
    '__ceil__', '__bool__', '__hash__', '__index__', '__round__',
  ]
  names = list(set(dunderNames))
  nameList = ',\n'.join(["""'%s'""" % name for name in names])
  lmaoCode = """dunderNames = [\n%s\n]""" % nameList
  copy(lmaoCode)


def tester03() -> None:
  n = BoxInt(7)
  print(n)
  n += 1
  print(n)
  n += 1
  print(n)
  n += 1
  print(n)
  n += 1
  print(n)


def tester04() -> None:
  lmao = TesterClass01()
  print(lmao)
  lmao.txt = 'Goodnight, World!'
  print(lmao)
  yolo = TesterClass02()
  print(yolo)
  yolo.wrapped.txt = 'Morning, Moon!'
  print(yolo)


if __name__ == '__main__':
  tester04()
