"""Unit tests for analyzer.py.
"""

import pytest
import numpy as np
import logging


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
    if (testNumpy[0, 0] == 0 and testNumpy[0, 1] == 1 and
            testNumpy[0, 2] == 2 and testNumpy[1, 0] == 100 and
            testNumpy[1, 1] == 50 and testNumpy[1, 2] == 40):
        checker = True
    assert checker is True


def test_produceDuration(testNumpy):
    """Tests produceDuration function from analyzer.py

    :param testNumpy: numpy array fixture
    :returns: passes if duration is calculated as expected, fails otherwise
    """
    from analyzer import produceDuration
    assert produceDuration(testNumpy) == 2


def test_produceVoltageExtremes(testNumpy):
    """Tests produceVoltageExtremes from analyzer.py

    :param testNumpy: numpy array fixture
    :returns: passes if tuple is as expected, fails otherwise
    """
    from analyzer import produceVoltageExtremes
    assert produceVoltageExtremes(testNumpy) == (40, 100)


def test_produceBeats(testData):
    """Tests produceBeats from analyzer.py

    :param testData: numpy array fixture
    :returns: passes if beats are found
    """
    from analyzer import produceBeats
    check = np.array_equal(produceBeats(testData), np.array([3, 7]))
    assert check is True


def test_produceNumBeats(testData):
    """Tests produceNumBeats from analyzer.py

    :param testData: numpy array fixture
    :returns: passes if number of beats are correct
    """
    from analyzer import produceBeats
    from analyzer import produceNumBeats
    assert produceNumBeats(produceBeats(testData)) == 2


def test_produceTimesOfBeats(testData):
    """Tests produceTimesOfBeats from analyzer.py

    :param testData: numpy array fixture
    :returns: passes if times of beats are correct
    """
    from analyzer import produceBeats
    from analyzer import produceTimesOfBeats
    pTOB = produceTimesOfBeats(testData, produceBeats(testData))
    expected == np.array([3.5, 7.5])
    check = np.array_equal(pTOB, expected)
    assert check is True


def test_produceMeanHR(testData):
    """Tests produceMeanHR from analyzer.py

    :param testData: numpy array fixture
    :returns: passes if mean heartrate in bpm is correct
    """
    from analyzer import produceBeats
    from analyzer import produceNumBeats
    from analyzer import produceDuration
    from analyzer import produceMeanHR
    numBeats = produceNumBeats(produceBeats(testData))
    duration = produceDuration(testData)
    assert produceMeanHR(numBeats, duration) == 12
