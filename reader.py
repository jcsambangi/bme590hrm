"""CSV file validation and reading.
"""

import csv
import logging
import numpy
import cleaner
import sys


def validate(filename):
    """Ensure that incoming file is .csv.

    :param filename: name of incoming file as string
    :returns: nothing if filename ends in .csv; raises TypeError otherwise
    """
    if not filename.lower().endswith(".csv"):
        logging.error("The input file did not have extension '.csv'\n")
        raise TypeError("The input file must have extension '.csv'.")


def existFile(filename):
    """Ensure that incoming file exists.

    :param filename: name of incoming file as string
    :returns: nothing if file existsl raises FileNotFoundError otherwise
    """
    try:
        fileHolder = open(filename, "r")
        fileHolder.close()
    except FileNotFoundError:
        logging.error("The input file could not be found.\n")
        raise FileNotFoundError("This file could not be found.")
    logging.info('Input file name: {}'.format(filename))


def readFile(filename):
    """Creates Python lists of times and voltages from CSV file.

    :param filename: name of incoming file exists
    :returns: list of lists: 0th = list of times, 1st = list of voltages
    """
    times = []
    voltages = []
    with open(filename, 'r') as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            times.append(cleaner.cleanTime(row[0]))
            voltages.append(cleaner.cleanVoltage(row[1]))
    logging.info("The input file has been read.")
    values = [times, voltages]
    return values
