import numpy as np
from scipy.stats import pearsonr

# Patient ages
ages = np.array([20, 35, 30, 45, 40, 25])

# Waiting times in minutes
waiting_minutes = np.array([25, 30, 28, 35, 32, 26])

# Calculate sample covariance
cov_minutes = np.cov(ages, waiting_minutes, ddof=1)[0, 1]

# Calculate Pearson correlation
corr_minutes, _ = pearsonr(ages, waiting_minutes)

# Convert waiting times to seconds
waiting_seconds = waiting_minutes * 60

# Calculate covariance in seconds
cov_seconds = np.cov(ages, waiting_seconds, ddof=1)[0, 1]

# Calculate correlation in seconds
corr_seconds, _ = pearsonr(ages, waiting_seconds)

# Display results
print("Covariance (minutes):", cov_minutes)
print("Correlation (minutes):", corr_minutes)

print("Covariance (seconds):", cov_seconds)
print("Correlation (seconds):", corr_seconds)
