from scipy.stats import ttest_rel

# Waiting times before and after
before = [25, 30, 28, 35, 32, 26]
after = [20, 24, 23, 27, 26, 21]

# Perform paired t-test
t_stat, p_value = ttest_rel(before, after)

# Display results
print("T-statistic:", t_stat)
print("P-value:", p_value)

# Decision at 5% significance level
if p_value < 0.05:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
