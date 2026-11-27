import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Define the Poisson distribution
lam = 3

# Calculate probabilities
p_zero = poisson.pmf(0, lam)
p_at_least_one = 1 - p_zero

print("P(X = 0):", p_zero)
print("P(X >= 1):", p_at_least_one)

# Set fixed random seed
np.random.seed(42)

# Generate 1000 independent samples of size 30
samples = np.random.poisson(lam, size=(1000, 30))

# Calculate sample means
sample_means = np.mean(samples, axis=1)

# Calculate empirical standard error
empirical_se = np.std(sample_means, ddof=1)

print("Empirical Standard Error:", empirical_se)

# Plot distribution of sample means
plt.hist(sample_means, bins=30, edgecolor='black')
plt.xlabel("Sample Means")
plt.ylabel("Frequency")
plt.title("Distribution of Sample Means")
plt.show()
