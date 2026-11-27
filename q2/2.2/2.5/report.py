import numpy as np

# Define visits per year
x = 3

# Calculate log-odds
log_odds = -1 + 0.4 * x

# Calculate odds
odds = np.exp(log_odds)

# Calculate probability
p = odds / (1 + odds)

# Calculate odds ratio
odds_ratio = np.exp(0.4)

print("Probability:", p)
print("Odds:", odds)
print("Odds Ratio:", odds_ratio)
