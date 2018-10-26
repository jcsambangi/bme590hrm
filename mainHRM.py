"""This is the main file for the Heart Rate Monitor.
"""

import sys
import logging
import reader
import analyzer
import cleaner
import numpy as np
import outputter

filename = "test_data3.csv"
numberOfMinutes = None


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
    reader.existFile(filename)
    rawData = reader.readFile(filename)
    while "interpolate" in rawData[0]:
        rawData = cleaner.cleanInterpolate(rawData, 0)
    while "interpolate" in rawData[1]:
        rawData = cleaner.cleanInterpolate(rawData, 1)
    almostData = analyzer.produceNumpy(rawData)
    data = cleaner.cleanClipper(almostData, numberOfMinutes)
    metrics = outputter.createDictionary(data)
    JSONname = outputter.createJSON(metrics, filename)
    logging.info('Finished.\n')


if __name__ == "__main__":
    HRM(filename, numberOfMinutes)
