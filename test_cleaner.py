"""Unit tests for cleaner.py
"""

import pytest

testSomethings = [
        (1, 1, 1, 1),
        (100.098, 100.098, 100.098, 100.098),
        (301, 301, 301, "interpolate"),
        ("hello", "interpolate", "interpolate", "interpolate"),
        (True, "interpolate", "interpolate", "interpolate"),
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
