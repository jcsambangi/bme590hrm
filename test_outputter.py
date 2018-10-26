"""Tests functions in outputter.py.
"""

import pytest
import numpy as np


def test_createDictionary(testData):
    """Tests createDictionary function from outputter.py

    :returns: passes if dictionary was created as expected, fails otherwise
    """
    from outputter import createDictionary
    from analyzer import produceDuration
    from analyzer import produceVoltageExtremes
    from analyzer import produceBeats
    from analyzer import produceNumBeats
    from analyzer import produceTimesOfBeats
    from analyzer import produceMeanHR
    duration = produceDuration(testData)
    voltageExtremes = produceVoltageExtremes(testData)
    beatInds = produceBeats(testData)
    numBeats = produceNumBeats(beatInds)
    timesOfBeats = produceTimesOfBeats(testData, beatInds)
    meanHR = produceMeanHR(numBeats, duration)
    dictVals = [meanHR, voltageExtremes, duration, numBeats, timesOfBeats]
    metrics = createDictionary(dictVals)
    check = True
    if metrics.get("mean_hr_bpm") != 12:
        check = False
    if metrics.get("voltage_extremes") != (0.0, 100.0):
        check = False
    if metrics.get("duration") != 10:
        check = False
    if metrics.get("num_beats") != 2:
        check = False
    if np.array_equal(metrics.get("beats"), np.array([3.5, 7.5])) is not True:
        check = False
    assert check is True
