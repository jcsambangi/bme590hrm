"""Unit tests for cleaner.py
"""

import pytest
import numpy as np
import logging

testSomethings = [
        (1, 1, 1, 1),
        (100.098, 100.098, 100.098, 100.098),
        (301, 301, 301, "interpolate"),
        ("hello", "interpolate", "interpolate", "interpolate"),
        (True, "interpolate", "interpolate", "interpolate"),
]
testInterpolate = [
        ([[0, 1, "interpolate", 3], [50, 65, 75, 88]], 0, [[0, 1, 2, 3], [50, 65, 75, 88]]),
        ([[1, 2, 3], ["interpolate", 65, 75]], 1, [[2, 3], [65, 75]]),
        ([[0, 1, 3, "interpolate"], [50, 65, 75, 88]], 0, [[0, 1, 3], [50, 65, 75]]),
        ([[0, 1, "interpolate", "interpolate", 4], [50, 65, 75, 88, 90]], 0, [[0, 1, 2, 3, 4], [50, 65, 75, 88, 90]]),
]

@pytest.mark.parametrize("something, eFloat, eTime, eVoltage", testSomethings)
def test_cleanFloat(something, eFloat, eTime, eVoltage):
    """Tests the cleanFloat function from cleaner.py

    :returns: passes if result is as listed in testSomethings, fails otherwise
    """
    from cleaner import cleanFloat
    assert cleanFloat(something) == eFloat


@pytest.mark.parametrize("something, eFloat, eTime, eVoltage", testSomethings)
def test_cleanTime(something, eFloat, eTime, eVoltage):
    """Tests the cleanTime function from cleaner.py

    :returns: passes if result is as listed in testSomethings, fails otherwise
    """
    from cleaner import cleanTime
    assert cleanTime(something) == eTime


@pytest.mark.parametrize("something, eFloat, eTime, eVoltage", testSomethings)
def test_cleanVoltage(something, eFloat, eTime, eVoltage):
    """Tests the cleanVoltage function from cleaner.py

    :returns: passes if result is as listed in testSomethings, fails otherwise
    """
    from cleaner import cleanVoltage
    assert cleanVoltage(something) == eVoltage


@pytest.mark.parametrize("rawData, which, expected",testInterpolate)
def test_cleanInterpolate(rawData, which, expected):
    """Tests the cleanInterpolate function from cleaner.py

    :returns: passes if result is interpolated as expected, fails otherwise
    """
    from cleaner import cleanInterpolate
    assert cleanInterpolate(rawData, which) == expected


def test_cleanClipper(testData):
    """Tests the cleanClipper function from cleaner.py

    :returns: passes if data is windowed as expected, fails otherwise
    """
    testTimes = testData[0, 0:7]
    testVoltages = testData[1, 0:7]
    expectedClippedData = np.array([testTimes, testVoltages])
    logging.warning(repr(expectedClippedData))
    from cleaner import cleanClipper
    cleaned = cleanClipper(testData, 0.1)
    logging.warning(repr(cleaned))
    check = np.array_equal(cleaned, expectedClippedData)
    assert check == True
