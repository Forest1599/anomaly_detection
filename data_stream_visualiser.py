import matplotlib.pyplot as plt
from data_point import DataPoint

# Data stream visualiser, responsible for visualising the generated data points
class DataStreamVisualiser:
    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots()
        self.xdata, self.ydata = [], []
        self.sc = self.ax.scatter(self.xdata, self.ydata)
        self.colors = []

        # Settings for the graph
        self.ax.set_xlabel("Time Step")
        self.ax.set_ylabel("Data Point Value")
        self.ax.set_title("Data Stream")
    
    def update(self, dp: DataPoint) -> None:
        # Append new values
        self.xdata.append(dp.time)
        self.ydata.append(dp.value)

        # If anomaly, set the data value dot red
        self.colors.append('red' if dp.is_anomaly else 'blue')

        # Adjust the plot limits automatically based on the data
        self.ax.set_xlim(max(0, dp.time - 100), dp.time + 10)
        self.ax.set_ylim(min(self.ydata) - 10, max(self.ydata) + 10)

        # Update scatter plot
        self.sc.set_offsets(list(zip(self.xdata, self.ydata)))
        self.sc.set_facecolors(self.colors)
        plt.draw()

        plt.pause(0.1)

