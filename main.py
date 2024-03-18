"""Main Tester Script for the project."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys

from PySide6.QtWidgets import QApplication

from ezqt.windows import MainWindow


def tester00() -> None:
  """Hello world"""
  stuff = [os, sys, 'hello world']
  for item in stuff:
    print(item)


def tester01() -> None:
  """Test of tester class"""
  app = QApplication(sys.argv)
  main = MainWindow()
  main.show()
  app.exec()


if __name__ == '__main__':
  tester01()
