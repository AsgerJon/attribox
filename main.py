"""Main Tester Script for the project."""
from __future__ import annotations

import os
import sys


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


if __name__ == '__main__':
  tester01()
