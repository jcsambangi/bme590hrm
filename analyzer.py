"""Analyzes raw data to produce values of interest for the metrics dictionary.
"""

import logging
import numpy as np
from scipy.signal import find_peaks


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


def produceBeats(data):
    """Finds the beats in the ECG strip.

    :param data: numpy array with data
    :returns: numpy array with indices of peaks
    """
    length = data[0, :].size
    if length == 0:
        return np.array([])
    else:
        spacing = produceDuration(data)/length
    maxHR = 200/60
    wait = round((1/maxHR)/spacing)+1
    voltages = data[1, :]
    peaksInds, _ = find_peaks(voltages, distance=wait, prominence=0.6)
    return peaksInds


def produceNumBeats(peakInds):
    """Counts the number of beats in the ECG strip.

    :param peakInds: numpy array with indices of peaks
    :returns: integer number of beats in ECG strip
    """
    return len(peakInds)


def produceTimesOfBeats(data, peakInds):
    """Calculates timepoints at which beats occurred.

    :param data: numpy array with data
    :param peakInds: nump array with indices of peaks
    :returns: numpy array of times at which beats occurred
    """
    times = data[0, :]
    return times[peakInds]


def produceMeanHR(numBeats, duration):
    """Calculates mean heart rate from data.

    :param numBeats: integer number of beats in ECG strip
    :param duration: float duration of strip
    :returns: mean heart rate as integer beats per minute
    """
    if duration == 0:
        return 0
    else:
        return round(numBeats/(duration/60))
