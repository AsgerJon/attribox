"""Test runner! """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import unittest

from icecream import ic

ic.configureOutput(includeContext=True)

if __name__ == '__main__':
  suite = unittest.defaultTestLoader.discover('./tests', pattern='test_*.py')
  runner = unittest.TextTestRunner()
  result = runner.run(suite)
  here = os.path.dirname(__file__)
  fid = os.path.join(here, 'results.txt')
  print(result)
  with open(fid, 'w') as file:
    runner.stream = file
    runner.stream.write(str(result))

  # Exit with a specific code depending on whether the tests passed or failed
  if result.wasSuccessful():
    exit(0)
  else:
    exit(1)
