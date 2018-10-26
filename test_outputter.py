"""Tests functions in outputter.py.
"""

import pytest
import numpy as np
import json
import logging


def test_createDictionary(testData):
    """Tests createDictionary function from outputter.py

    :returns: passes if dictionary was created as expected, fails otherwise
    """
    from outputter import createDictionary
    metrics = createDictionary(testData)
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


def test_createJSON(testData, mktestfile):
    """Tests createJSON function from outputter.py

    :returns: passes if JSON was correctly created, fails otherwise
    """
    from outputter import createJSON
    from outputter import createDictionary
    trueDict = createDictionary(testData)
    JSONfile = createJSON(trueDict, mktestfile)
    with open(JSONfile, 'r') as readJSON:
        insideDict = json.load(readJSON)
    check = True
    if insideDict.get("mean_hr_bpm") != 12:
        check = False
    if insideDict.get("voltage_extremes") != [0.0, 100.0]:
        check = False
        logging.warning('{}'.format(insideDict.get("voltage_extremes")))
        logging.warning('{}'.format(trueDict.get("voltage_extremes")))
    if insideDict.get("duration") != 10:
        check = False
    if insideDict.get("num_beats") != 2:
        check = False
    if insideDict.get("beats") != [3.5, 7.5]:
        check = False
    assert check is True
