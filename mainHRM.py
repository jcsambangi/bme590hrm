"""This is the main file for the Heart Rate Monitor.
"""

import sys
import logging
import reader
import analyzer
import cleaner
import numpy as np
import outputter

filename = "test_data1.csv"
numberOfMinutes = 0.25


def HRM(filename, numberOfMinutes):
    """Oversees the processing of the input CSV file to output JSON file.

    :param filename: A string containing the file for processing.
    :returns: JSON file with the metrics dictionary
    """
    FORMAT = '%(asctime)s %(message)s'
    DATEFMT = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                        format=FORMAT, datefmt=DATEFMT)
    logging.info('Started.')
    reader.validate(filename)
    logging.info('Input file name: {}'.format(filename))
    reader.existFile(filename)
    rawData = reader.readFile(filename)
    while "interpolate" in rawData[0]:
        rawData = cleaner.cleanInterpolate(rawData, 0)
    while "interpolate" in rawData[1]:
        rawData = cleaner.cleanInterpolate(rawData, 1)
    almostData = analyzer.produceNumpy(rawData)
    data = cleaner.cleanClipper(almostData, numberOfMinutes)
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
    dictVals = [meanHR, voltageExtremes, duration, numBeats, timesOfBeats]
    metrics = outputter.createDictionary(dictVals)
    logging.info('Metrics dictionary: {}'.format(metrics))
    logging.info('Finished.\n')


if __name__ == "__main__":
    HRM(filename, numberOfMinutes)
#    for i in range(1, 33):
#        filename = 'test_data{}.csv'.format(i)
#        HRM(filename, numberOfMinutes)
