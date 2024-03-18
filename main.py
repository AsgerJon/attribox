"""Main Tester Script for the project."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import sys


def tester00() -> None:
  """Hello world"""
  stuff = [os, sys, 'hello world']
  for item in stuff:
    print(item)


if __name__ == '__main__':
  res = subprocess.run(['python3', 'test_runner.py'],
                       text=True,
                       stderr=subprocess.PIPE,
                       stdout=subprocess.PIPE, )
  if res.returncode:
    error_message = """LMAO"""
    for (key, val) in res.__dict__.items():
      error_message += f'{key}: {val}\n'
    raise RuntimeError(error_message)
  else:
    print(res.stdout)
    tester00()
