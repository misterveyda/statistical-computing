import numpy as np

# Original waiting times
waiting_times = np.array([8, 10, 12, 15, 18, 20, 25, 40])

# Set random seed
np.random.seed(42)

# Perform 1000 bootstrap resamples
bootstrap_means = []

for i in range(1000):
    sample = np.random.choice(
        waiting_times,
        size=len(waiting_times),
        replace=True
    )

    bootstrap_means.append(np.mean(sample))

# Calculate bootstrap mean
bootstrap_mean = np.mean(bootstrap_means)

# Calculate 95% percentile confidence interval
lower = np.percentile(bootstrap_means, 2.5)
upper = np.percentile(bootstrap_means, 97.5)

print("Bootstrap Mean:", bootstrap_mean)
print("95% Confidence Interval:", lower, "to", upper)
