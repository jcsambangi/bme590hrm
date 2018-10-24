"""This is the mother file for the Heart Rate Monitor. It takes a filename input and works through processing the file with modules.
"""

import logging
import reader

filename = "test_data1.csv"


def HRM(filename):
    """This is the main function for the heart rate monitor that oversees the processing of the input file to output JSON file.

    :param filename: A string containing the file for processing.
    :returns: JSON file with the metrics dictionary
    """
    logging.basicConfig(filename="log.txt", level=logging.DEBUG, format='%(asctime)s %(message)s')
    logging.info('Started.')
    reader.validate(filename)
    logging.info('Filename: %s' % filename)
    logging.info('Finished.')


if __name__ == "__main__":
    HRM(filename)
