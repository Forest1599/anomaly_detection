import random
from data_point import DataPoint
import math

# Constant values for data stream generation
MEAN = 50
AMPLITUDE = 10
NOISE_LEVEL = 5
ANOMALY_CHANCE = 0.05
SEASONAL_FREQUENCY = 70
ANOMALY_MIN_AMPLITUDE = 20
ANOMALY_MAX_AMPLITUDE = 40

# Generates a continous data stream with seasonal pattern as the sin wave, random noise and random anomalies
def generate_data_stream():

    t = 0 # Time step to control the seasonal pattern (increments with each new data point)
    while True:
        
        # Seasonal pattern following the sine wave
        seasonal_value = MEAN + AMPLITUDE * math.sin(2 * math.pi * (t / SEASONAL_FREQUENCY))

        # Gets a random value for noise level, either negative or positive value
        noise = random.uniform(-NOISE_LEVEL, NOISE_LEVEL)
        data_point = seasonal_value + noise

        dp = DataPoint()
        # If a random number falls below the set anomaly_chance, an anomaly data point is generated
        if random.random() < ANOMALY_CHANCE:
            # anomaly value generated where the amplitude is randomly selected and either positive or negative value is set
            anomaly_magnitude = random.choice([-1, 1]) * random.uniform(ANOMALY_MIN_AMPLITUDE, ANOMALY_MAX_AMPLITUDE) 
            data_point += anomaly_magnitude

            dp.set_true_anomaly(True)

        # Time increment
        t += 1

        dp.set_value(data_point)
        dp.set_time(t)
        
        yield dp