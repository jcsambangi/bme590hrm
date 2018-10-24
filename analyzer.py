"""Analyzes raw data to produce values of interest for the metrics dictionary.
"""

import logging
import numpy


def produceMeanHR(times, voltages, minutes):
    """Calculates mean heart rate from data.

    :param times: list of times as floats
    :param voltages: list of voltages as floats
    :returns: integer bpm over specified number of minutes
    """


def produceVoltageExtremes(voltages):
    """Calculates minimum and maximum lead voltages.

    :param voltages: list of voltages as floats
    :returns: tuple of floats: minimum and maximum voltages
    """


def produceDuration(times):
    """Calculates time duration of the ECG strip.

    :param times: list of times as floats
    :returns: float duration of signal
    """


def produceNumberOfBeats(times, voltages):
    """Calculates the number of beats in the ECG strip.

    :param times: list of times as floats
    :param voltages: list of voltages as floats
    :returns: integer number of beats in signal
    """


def produceTimesOfBeats(times, voltages):
    """Calculates timepoints at which beats occurred.

    :param times: list of times as floats
    :param voltages: list of voltages as floats
    :returns: numpy array of times at which beats occurred
    """
