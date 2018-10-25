"""Analyzes raw data to produce values of interest for the metrics dictionary.
"""

import logging
import numpy as np
from scipy.signal import find_peaks
#import matplotlib.pyplot as plt


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
    return 0


def produceBeats(data):
    """Finds the beats in the ECG strip.

    :param data: numpy array with data
    :returns:
    """
    spacing = produceDuration(data)/len(data[0, :])
    maxHR = 200/60
    wait = round((1/maxHR)/spacing)
    voltages = data[1, :]
    peaks, _ = find_peaks(voltages, distance=wait, prominence=0.6)
#    plt.plot(voltages)
#    plt.plot(peaks, voltages[peaks], "x")
#    plt.show()
    return len(peaks)


def produceMeanHR(times, voltages, minutes):
    """Calculates mean heart rate from data.

    :param times: list of times as floats
    :param voltages: list of voltages as floats
    :returns: integer bpm over specified number of minutes
    """
    return 0
