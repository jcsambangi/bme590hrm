# bme590hrm
BME 590.06: Heart Rate Monitor Assignment  
v1.0.0 released 10/26/18 by Jaydeep Sambangi (GitHub: jcsambangi, NetID: js593)

## Overview
This software analyzes ECG data from an input CSV file with lines of `time, voltage`. It outputs a JSON file of same name as the input CSV file that contains a dictionary with the following `keys`and values:
  + `mean_hr_bpm`: estimated average heart rate over a user-specified number of minutes (over the entire ECG strip if not specified),
  + `voltage_extremes`: list containing minimum and maximum lead voltages in the window,
  + `duration`: time duration of the windowed ECG strip,
  + `num_beats`: number of detected beats in the ECG window, and
  + `beats`: list of times when the beats occurred.

## Using the Software
The software can be used by running the `mainHRM.py` file. By default, the software analyzes the entire ECG strip from a file `test_data1.csv` originally derived from the [PhysioBank Database](https://physionet.org/physiobank/database/#ecg) for ECG data. The user can modify:
  + the input CSV file,
  + the number of minutes (from the start of the strip) over which to analyze the ECG, or
  + both.
The user can make these modifications in lines `12` and `13` of `mainHRM.py`, shown below, by simply modifying the assignments of the desired variable(s). 
```python
filename = "test_data1.csv"  # input file, default: "test_data1.csv"
numberOfMinutes = None  # duration to analyze (minutes), default: None
```

## Under the Hood

### Peak Detection
Peak detection is handled courtesy of the `find_peaks` [function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html) from the `scipy.signal` [module](https://docs.scipy.org/doc/scipy/reference/signal.html). In the software, peak detection is done by the function `produceBeats` (lines `36` through `51` of the `analyzer.py` module), shown below.
```python
def produceBeats(data):
    """Finds the beats in the ECG strip.

    :param data: numpy array with data
    :returns: numpy array with indices of peaks
    """
    length = data[0, :].size
    if length == 0:
        return np.array([])
    else:
        spacing = produceDuration(data)/length
    maxHR = 200/60
    wait = round((1/maxHR)/spacing)+1
    voltages = data[1, :]
    peaksInds, _ = find_peaks(voltages, distance=wait, prominence=0.6)
    return peaksInds
```
This algorithm sequentially:
  1. Finds the number of elements in the numpy array of times. If the numpy array is empty, the function exits by returning an empty numpy array for the indices of the beats.
  2. Determines the average number of seconds between samples in the strip.
  3. Specifies a variable `wait` corresponding the minimum number of samples expected between peaks.
  4. Uses the `scipy.signal.find_peaks` function with specifications for 1) the minimum number of samples between peaks and 2) a minimum desired prominence of each peak, to find the peaks in the voltage data.
  5. Returns the indices of the numpy arrays of data at which peaks were found.

### Known Issues
Some of the known shortcomings of the current release of this software are listed below.
  + Attempts to analyze any input data (does not identify bad data).
  + Double counts beats when P or T complexes of the ECG are somewhat prominent.    
