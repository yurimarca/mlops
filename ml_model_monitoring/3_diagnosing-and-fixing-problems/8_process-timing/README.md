Speed is not only something that helps us finish work on time, it's also a natural feature of ML projects that are functioning correctly. If your ML pipeline slows down significantly, it can be a sign that there are serious problems you need to address. That's why timing our processes can be extremely important.

In this exercise, we provided you a python script called `timings.py` in `/L4/` directory. You will write functions in this script that help you record and monitor the speed of important ML pipeline processes.

## Instructions

First, make sure you're familiar with the scripts whose timing we'll be measuring. We'll be monitoring the timing of two ML scripts:

- `ingestion.py`
- `training.py`

Both of them are stored in your workspace under `/L4/` directory, and you'll need to import both of these into your timing script.

You need to create two crucial functions for your script:

- a function called `ingestion_timing()` that measures the time it takes Python to run `ingestion.py`, in seconds
- a function called `training_timing()` that measures the time it takes Python to run `training.py`, in seconds

After creating these functions, you should create one final function called `measure_and_save_timings()`. This function should accomplish the following:

- Run `ingestion_timing()`20 times, obtaining 20 different timing measurements. Calculate the mean, standard deviation, minimum, and maximum of these timings (four final measurements)
- Run `training_timing()` 20 times, obtaining 20 different timing measurements. Calculate the mean, standard deviation, minimum, and maximum of these timings (four more final measurements)
- Return a Python list containing all eight final measurements.

The list that your script returns as its final output should have eight elements, in this order:

- the mean of 20 `ingestion_timing()` outputs
- the standard deviation of 20 `ingestion_timing()` outputs
- the minimum of 20 `ingestion_timing()` outputs
- the maximum of 20 `ingestion_timing()` outputs
- the mean of 20 `training_timing()` outputs
- the standard deviation of 20 `training_timing()` outputs
- the minimum of 20 `training_timing()` outputs
- the maximum of 20 `training_timing()` outputs
