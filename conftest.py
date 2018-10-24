"""Configuration file for pytest.

Some code borrowed from mlp6's fem/tests/conftest.py
"""

import pytest
import csv
import os


@pytest.fixture
def mktmpdir(tmpdir_factory):
    """Creates temporary directory for unit testing-required files.

    :param tmpdir_factory:
    :returns: tmpdir object
    """
    tmpdir = tmpdir_factory.mktemp('tmp')
    return tmpdir


@pytest.fixture
def mktestfile(tmpdir):
    """Creates test file for unit testing in tmpdir

    :returns: string path of testFile
    """
    testFile = tmpdir.join('test.csv')
    testPath = testFile.strpath
    with open(testPath, 'w', newline='') as csvfile:
        testWriter = csv.writer(csvfile)
        testWriter.writerow(['0.11', '0.88'])
        testWriter.writerow(['0.22', '0.99'])
    return testPath
