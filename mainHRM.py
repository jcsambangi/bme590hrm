"""This is the main file for the Heart Rate Monitor.
"""

import logging
import reader
import analyzer

filename = "test_data32.csv"
numberOfMinutes = 0.25


def HRM(filename):
    """Oversees the processing of the input CSV file to output JSON file.

    :param filename: A string containing the file for processing.
    :returns: JSON file with the metrics dictionary
    """
    FORMAT = '%(asctime)s %(message)s'
    logging.basicConfig(filename="log.txt", level=logging.DEBUG, format=FORMAT)
    logging.info('Started.')
    reader.validate(filename)
    logging.info('Filename: %s' % filename)
    reader.existFile(filename)
    rawData = reader.readFile(filename)
    logging.info('Finished.')


if __name__ == "__main__":
    HRM(filename)
