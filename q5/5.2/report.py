from scipy.stats import wilcoxon

# Waiting times before and after
before = [25, 30, 28, 35, 32, 26]
after = [20, 24, 23, 27, 26, 21]

# Perform Wilcoxon signed-rank test
stat, p_value = wilcoxon(before, after)

print("Wilcoxon Statistic:", stat)
print("P-value:", p_value)

# Decision at 5% significance level
if p_value < 0.05:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
