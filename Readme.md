# Efficient Data Stream Anomaly Detection

## Usage
Run the main script to start the data stream and visualise the anomaly detection in real-time.

python main.py

The data stream runs with a infinite loop unless the user stops it by closing the main window or by pressing 'q' when the window is selected.
The normal data points will be highlighted in Blue, but the detected anomalies will be highlighted in red.

NOTE:
The anomaly detection only starts after the first 100 data points have been plotted on to the graph.

# Data Generation
The generated data points are processed in a streaming fashion. The details of the data generation can be seen in data_stream_generator.py

## Median Absolute Deviation (MAD)
The MAD approach calculates the median of a rolling window of data points, that I have set to 100 data points and uses it as a measure of central tendency.

MAD is computed as the median of the absolute differences between the data points and the median.

A modified Z-score is calculated for each data point to determine if it is an anomaly, based on a defined threshold, that I have set to 3.

# Why MAD?
During the development of this project, other anomaly detection techniques were considered and tested, such as Exponential Moving Average. However, these approaches did not perform as well in handling the seasonal variations and outliers present in the data stream. After conducting research and considering the time constraints, the MAD algorithm was found to be the most effective solution for this specific context.

Unlike standard deviation, MAD is resistant to outliers, making it well suited for data streams that may have occasional exterme values.

The use of a rolling window allows the MAD algorithm to adapt to gradual changes in the data distribution.

## External Library Usage
As stated in the requirements, the use of external libraries has been kept minimal to ensure simplicity.

The main external libraries used are:
numpy: For calculating median and median absolute deviation
matplotlib: For real-time visualisation of data points and detected anomalies.

## Evaluation Metrics
To evaluate the effectiveness of the MAD anomaly detector I have collected the following metrics:

Accuraccy: The proportion of correctly classified instances agains the total plotted data points
Recall: The ratio of correctly identified anomalies to the actual anomalies present

Having executed the program for around 5 minutes, the metrics topped at:

Accuracy: 98.90%
Recall: 0.81



