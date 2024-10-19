# Class for storing information about the data point
class DataPoint:

    def __init__(self) -> None:
        self.is_anomaly = False
        self.true_anomaly = False
    
    def set_anomaly(self, is_anomaly: bool) -> None:
        self.is_anomaly = is_anomaly
    
    def set_time(self, time: int) -> None:
        self.time = time
    
    def set_true_anomaly(self, true_anomaly: bool) -> None:
        self.true_anomaly = true_anomaly
    
    def set_value(self, value: float) -> None:
        self.value = value

    def __str__(self) -> None:
        return str(self.value)

    def __float__(self) -> float:
        return float(self.value)