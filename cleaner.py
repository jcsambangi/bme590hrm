"""Checks raw data read from file to ensure smooth analysis.
"""

import logging
import math
import numpy as np


def cleanFloat(something):
    """Investigates things for possible casting to float and does so if possible.
    """
    try:
        floatSomething = float(something)
        if math.isnan(floatSomething) is True or type(something) == bool:
            raise ValueError
    except ValueError:
        logging.warning("Not a float: " + repr(something))
        floatSomething = "interpolate"
    return floatSomething


def cleanTime(something):
    """Ensures time that will be appended to list is appopriate.
    """
    cleanedTime = cleanFloat(something)
    return cleanedTime


def cleanVoltage(something):
    """Ensures voltage that will be appended to list is appropriate.
    """
    cleanedVoltage = cleanFloat(something)
    if type(cleanedVoltage) is not float:
        return cleanedVoltage
    elif cleanedVoltage > 300:
        try:
            raise ValueError
        except ValueError:
            logging.warning("ECG voltage >300 mv: " + repr(cleanedVoltage))
        return "interpolate"
    else:
        return cleanedVoltage


def cleanInterpolate(rawData, which):
    """Replaces 'interpolate' with appropriately interpolated value.

    :param rawData: incoming list of lists of times and voltages
    :param which: integer designation of which list to clean
    :returns: list of lists of times and voltages, cleaner than before
    """
    modList = rawData[which]
    otherList = rawData[1-which]
    ind = modList.index("interpolate")
    if ind == 0 or ind == (len(modList)-1):
        modList.pop(ind)
        otherList.pop(ind)
        logging.warning("1 data point removed.")
    else:
        num = 1
        indHold = ind
        while modList[indHold+1] == "interpolate":
            num += 1
            indHold += 1
        logging.warning("%f point(s) interpolated." % num)
        increment = (modList[ind+num]-modList[ind-1])/(num+1)
        for i in range(0, num):
            modList[ind+i] = modList[ind+i-1]+increment
    newRawData = []
    newRawData.insert(which, modList)
    newRawData.insert(1-which, otherList)
    return newRawData


def cleanClipper(data, endTime):
    """Clips times and voltages to reflect user-specified end time

    :param data: numpy array of raw data
    :param endTime: user-specified end time in minutes
    :returns: numpy array of appropriately windowed data
    """
    times = data[0, :]
    if endTime is None: return data
    try:
        endTime = float(endTime)
        if (math.isnan(endTime) is True or type(endTime) == bool or
                endTime == 0 or endTime > np.amax(times)):
            logging.info("User entered inappropriate time: "+repr(endTime))
            raise ValueError
    except (TypeError, ValueError):
        return data
    endTime = endTime*60
    voltages = data[1, :]
    indRetain = []
    i = 0
    for x in times:
        if x <= endTime:
            indRetain.append(i)
        i += 1
    clippedData = np.array([times[indRetain], voltages[indRetain]])
    return clippedData
