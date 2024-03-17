"""Main Tester Script for the project."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys

from icecream import ic

from tester_class_01 import Tester


def tester00() -> None:
  """Hello world"""
  stuff = [os, sys, 'hello world']
  for item in stuff:
    print(item)


def tester01() -> None:
  """Test of tester class"""
  lmao = Tester()
  print(lmao)


if __name__ == '__main__':
  tester01()
