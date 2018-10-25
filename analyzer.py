"""Analyzes raw data to produce values of interest for the metrics dictionary.
"""

import logging
import numpy as np


def produceNumpy(data):
    """Produces a 2-row numpy array from the raw data

    :param rawData: list of lists time and voltage
    :returns: numpy array
    """
    return np.array(rawData[0], rawData[1])


def produceDuration(times):
    """Calculates time duration of the ECG strip.

    :param times: list of times as floats
    :returns: float duration of signal
    """
    maxTime = -1000
    for time in times:
        if time > maxTime: maxTime = time
    minTime = maxTime
    for time in times:
        if time < minTime: 


def produceVoltageExtremes(voltages):
    """Calculates minimum and maximum lead voltages.

    :param voltages: list of voltages as floats
    :returns: tuple of floats: minimum and maximum voltages
    """


def produceTimesOfBeats(times, voltages):
    """Calculates timepoints at which beats occurred.

    :param times: list of times as floats
    :param voltages: list of voltages as floats
    :returns: numpy array of times at which beats occurred
    """


def produceNumberOfBeats(times, voltages):
    """Calculates the number of beats in the ECG strip.

    :param times: list of times as floats
    :param voltages: list of voltages as floats
    :returns: integer number of beats in signal
    """


def produceMeanHR(times, voltages, minutes):
    """Calculates mean heart rate from data.

    :param times: list of times as floats
    :param voltages: list of voltages as floats
    :returns: integer bpm over specified number of minutes
    """
