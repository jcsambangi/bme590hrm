"""This is the main file for the Heart Rate Monitor.
"""

import logging
import reader

filename = "test_data1.csv"


def HRM(filename):
    """Oversees the processing of the input file to output JSON file.

    :param filename: A string containing the file for processing.
    :returns: JSON file with the metrics dictionary
    """
    FORMAT = '%(asctime)s %(message)s'
    logging.basicConfig(filename="log.txt", level=logging.DEBUG, format=FORMAT)
    logging.info('Started.')
    reader.validate(filename)
    logging.info('Filename: %s' % filename)
    logging.info('Finished.')


if __name__ == "__main__":
    HRM(filename)
