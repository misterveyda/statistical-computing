import numpy as np
from scipy.stats import iqr

# Waiting times
waiting_times = [10, 12, 15, 18, 45]

# Calculate median
median_value = np.median(waiting_times)

# Calculate sample standard deviation
std_value = np.std(waiting_times, ddof=1)

# Calculate interquartile range
iqr_value = iqr(waiting_times)

print("Median:", median_value)
print("Sample Standard Deviation:", std_value)
print("Interquartile Range:", iqr_value)
