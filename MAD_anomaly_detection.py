from data_point import DataPoint
from collections import deque
import numpy as np

WINDOW_SIZE = 100
MAD_THERSHOLD = 3

"""
This class implements the Median Absolute Deviation algorithm for anomaly detection.
The MAD algorithm calculates the median of a rolling window of data points and determines
whether a new data point is an anomaly based on its deviation from the median.

More details can be found on Readme.md
"""
class MADAnomalyDetector:
    def __init__(self) -> None:
        self.window_size = WINDOW_SIZE
        self.data_window = deque(maxlen=WINDOW_SIZE)
        self.mad_threshold = MAD_THERSHOLD

    def update(self, dp: DataPoint) -> DataPoint:
        # Add the new data point value to the rolling window
        self.data_window.append(dp.value)

        # Only start detecting anomalies once we have enough data for the window
        if len(self.data_window) == self.window_size:
            # Calculate the median of the current window
            median_value = np.median(self.data_window)
            # Calculate the Median Absolute Deviation (MAD)
            mad = np.median([abs(x - median_value) for x in self.data_window])

            # Calculate the modified Z-score for the latest data point
            if mad == 0:
                dp.set_anomaly(False)  # If no variance, not an anomaly
            else:
                modified_z_score = abs(dp.value - median_value) / mad
                dp.set_anomaly(modified_z_score > self.mad_threshold)

        return dp