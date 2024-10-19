import matplotlib.pyplot as plt
from data_point import DataPoint
from data_stream_generator import generate_data_stream
from event_handler import EventHandler
from MAD_anomaly_detection import MADAnomalyDetector
from data_stream_visualiser import DataStreamVisualiser

# Metrics for accuracy and recall calculation
total_iterations = 0
true_positives = 0
true_negatives = 0
false_negatives = 0

def printAccuracy(dp: DataPoint) -> None:
    global total_iterations, true_positives, true_negatives, false_negatives

    total_iterations += 1

    if dp.is_anomaly and dp.true_anomaly:
        true_positives += 1
    elif not dp.is_anomaly and not dp.true_anomaly:
        true_negatives += 1
    elif not dp.is_anomaly and dp.true_anomaly:
        false_negatives += 1

    # Prints the report every 100 data points
    if total_iterations % 100 == 0:
        # Proportion of correctly classified instances
        accuracy = (true_positives + true_negatives) / total_iterations * 100

        # Measures how many of the actual anomalies were detected
        recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0

        print("--------------------------")
        print(f"Accuracy: {accuracy:.2f}%")
        print(f"Recall:  {recall}")

if __name__ == "__main__":
    data_stream = generate_data_stream()
    visualiser = DataStreamVisualiser()
    event_handler = EventHandler()
    visualiser.fig.canvas.mpl_connect("key_press_event", event_handler.on_key)

    mad_anomaly_detector = MADAnomalyDetector()

    # Runs the loop until 'q' pressed or user exits window
    while not event_handler.should_stop and plt.fignum_exists(visualiser.fig.number):
        dp = next(data_stream)
        updated_data_point = mad_anomaly_detector.update(dp)
        visualiser.update(dp)
        printAccuracy(dp)


