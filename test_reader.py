"""Unit tests for reader.py
"""

import pytest
import os
import csv

testBadFilenames = [
        ("test1.txt"),
        ("test1902try.doc"),
]


@pytest.mark.parametrize("filename", testBadFilenames)
def test_validate_true(filename):
    """Tests the function validate from reader.py.

    :param filename: inpute string with purported file name
    :returns: test passed if filename ends in '.csv', test failed for filenames not ending in '.csv'
    """
    from reader import validate
    with pytest.raises(TypeError):
        validate(filename)


def test_existFile():
    """Tests the function existFile from reader.py

    :returns: test passed if file was found, test failed if file not found
    """
    from reader import existFile
    with pytest.raises(FileNotFoundError):
        existFile("probablyNotHere.csv")


def test_readFile(mktestfile):
    """Test the function readFile from reader.py

    :returns: test passed if read data is as expected, test failed if otherwise
    """
    from reader import readFile
    assert readFile(mktestfile) == [[0.11,0.22],[0.88,0.99]]
