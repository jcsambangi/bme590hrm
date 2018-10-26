"""Handles packaging values of interest for output.
"""

import numpy as np


def createDictionary(dictVals):
    """Creates dictionary fitting desired template from values of interest.

    :param dictVals: Python list containing 5 values of interest
    :returns: dictionary with values of interest assigned to appropriate keys
    """
    metrics = {"mean_hr_bpm": dictVals[0],
                "voltage_extremes": dictVals[1],
                "duration": dictVals[2],
                "num_beats": dictVals[3],
                "beats": dictVals[4]}
    return metrics
