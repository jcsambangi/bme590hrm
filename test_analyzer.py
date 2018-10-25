"""Unit tests for analyzer.py.
"""

import pytest
import numpy as np


@pytest.fixture
def testNumpy():
    """Creates numpy array as fixture.

    :returns: numpy array for testing
    """
    testTimes = [0, 1, 2]
    testVoltages = [100, 50, 40]
    data = [testTimes, testVoltages]
    from analyzer import produceNumpy
    return produceNumpy(data)


def test_produceNumpy(testNumpy):
    """Tests produceNumpy function from analyzer.py

    :param testNumpy: numpy array fixture
    :returns: passes if array was produced as expected, fails otherwise
    """
    checker = False
    if testNumpy[0, 0] == 0 and testNumpy[0, 1] == 1 and testNumpy[0, 2] == 2 and testNumpy[1, 0] == 100 and testNumpy[1, 1] == 50 and testNumpy[1, 2] == 40: checker = True
    assert checker == True

def test_produceDuration(testNumpy):
    """Tests produceDuration function from analyzer.py

    :param testNumpy: numpy array fixture
    :returns: passes if duration is calculated as expected, fails otherwise
    """
    from analyzer import produceDuration
    assert produceDuration(testNumpy) == 2
