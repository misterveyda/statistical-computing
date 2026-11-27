from scipy.stats import chisquare

# Observed attendance
observed = [45, 30, 15]

# Expected attendance
expected = [30, 30, 30]

# Perform chi-square goodness-of-fit test
chi_stat, p_value = chisquare(
    observed,
    f_exp=expected
)

print("Expected Counts:", expected)
print("Chi-square Statistic:", chi_stat)
print("P-value:", p_value)

# Decision at 5% significance level
if p_value < 0.05:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
