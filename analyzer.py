"""Analyzes raw data to produce values of interest for the metrics dictionary.
"""

import logging
import numpy as np


def produceNumpy(data):
    """Produces a 2-row numpy array from the raw data

    :param rawData: list of lists time and voltage
    :returns: numpy array
    """
    return np.array([data[0], data[1]])


def produceDuration(data):
    """Calculates time duration of the ECG strip.

    :param data: numpy array with data
    :returns: float duration of signal
    """
    return data[0, :].max()-data[0, :].min() 


def produceVoltageExtremes(data):
    """Calculates minimum and maximum lead voltages.

    :param data: numpy array with data
    :returns: tuple of floats: minimum and maximum voltages
    """
    return (data[1, :].min(), data[1, :].max())


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
