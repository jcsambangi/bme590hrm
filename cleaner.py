"""Checks raw data read from file to ensure smooth analysis.
"""

import logging
import math


def cleanFloat(something):
    """Ensures all members of data lists are floats.
    """
    try:
        floatSomething = float(something)
        if math.isnan(floatSomething) == True or type(something) == bool:
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
        logging.warning("ECG voltage >300 mv: " + repr(cleanedVoltage))
        return "interpolate"
    else:
        return cleanedVoltage
