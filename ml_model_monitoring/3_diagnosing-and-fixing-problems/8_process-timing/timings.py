import os
import timeit
import numpy as np

# Import the scripts to be timed
from src import training
from src import ingestion

def ingestion_timing():
    """Measure the time it takes to run ingestion.py."""
    start_time = timeit.default_timer()
    os.system('python3 ingestion.py')
    elapsed_time = timeit.default_timer() - start_time
    return elapsed_time

def training_timing():
    """Measure the time it takes to run training.py."""
    start_time = timeit.default_timer()
    os.system('python3 training.py')
    elapsed_time = timeit.default_timer() - start_time
    return elapsed_time

def measure_and_save_timings():
    """Measure timings for ingestion and training scripts and return statistics."""
    # Measure ingestion timings
    ingestion_times = [ingestion_timing() for _ in range(20)]
    ingestion_mean = np.mean(ingestion_times)
    ingestion_std = np.std(ingestion_times)
    ingestion_min = np.min(ingestion_times)
    ingestion_max = np.max(ingestion_times)

    # Measure training timings
    training_times = [training_timing() for _ in range(20)]
    training_mean = np.mean(training_times)
    training_std = np.std(training_times)
    training_min = np.min(training_times)
    training_max = np.max(training_times)

    # Return the results as a list
    return [
        ingestion_mean, ingestion_std, ingestion_min, ingestion_max,
        training_mean, training_std, training_min, training_max
    ]


