"""Unit tests for analyzer.py.
"""

import pytest
import numpy as np


def produceNumpy():
    testTimes = [0, 1, 2]
    testVoltages = [100, 50, 40]
    data = [testTimes, testVoltages]
    from analyzer import produceNumpy
    assert produceNumpy(data) == np.array([0, 1, 2], [100, 50, 40])
