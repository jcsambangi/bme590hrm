"""Handles packaging values of interest for output.
"""

import numpy as np
import json
import logging
import analyzer


def createDictionary(data):
    """Creates dictionary fitting desired template from values of interest.

    :param data: numpy array of time and voltage data
    :returns: dictionary with values of interest assigned to appropriate keys
    """
    duration = analyzer.produceDuration(data)
    logging.info('Duration (s): {}'.format(duration))
    voltageExtremes = analyzer.produceVoltageExtremes(data)
    logging.info('Voltage Extremes (mv): {}'.format(voltageExtremes))
    beatInds = analyzer.produceBeats(data)
    numBeats = analyzer.produceNumBeats(beatInds)
    logging.info('Number of Beats: {}'.format(numBeats))
    timesOfBeats = analyzer.produceTimesOfBeats(data, beatInds)
    logging.info('Times of Beats (s): {}'.format(timesOfBeats))
    meanHR = analyzer.produceMeanHR(numBeats, duration)
    logging.info('Mean Heart Rate (bpm): {}'.format(meanHR))
    metrics = {"mean_hr_bpm": meanHR,
               "voltage_extremes": voltageExtremes,
               "duration": duration,
               "num_beats": numBeats,
               "beats": timesOfBeats}
    logging.info("Metrics dictionary created.")
    return metrics


def createJSON(metrics, inputfilename):
    """Creates JSON file with metrics dictionary.

    :param metrics: dictionary containing values of interest
    :param inputfilename: original CSV filename input to program
    :returns: name of JSON file
    """
    outputfilename = inputfilename[:-3] + "json"
    metrics["beats"] = metrics["beats"].tolist()
    with open(outputfilename, 'w') as JSONfile:
        json.dump(metrics, JSONfile)
    logging.info('Wrote JSON file: {}'.format(outputfilename))
    return outputfilename
