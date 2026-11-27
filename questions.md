QUESTION ONE (20 MARKS)
The clinic network models arrivals for staffing decisions and estimates uncertainty in waiting times. At one
small clinic, daily arrivals are modelled as Poisson with mean 3 per day.
1. Explain why increasing the sample size reduces the variation of sample means under independent
sampling. (2 marks)
2. Write Python or R code to calculate P(X = 0) and P(X ≥ 1) (2 marks). Using a fixed seed, draw 1,000
independent samples of 30 daily counts, store their means, plot their distribution and calculate their
empirical standard error
3. Observed daily counts have mean 3 and variance 12. Analyse the departure from the Poisson model
and identify one possible explanation and one data check.
4. Design a bootstrap study to estimate uncertainty in the mean of waiting times = [8, 10, 12, 15, 18, 20,
25, 40]. Justify the sampling unit, and provide Python or R code for 1,000 bootstrap means and a
percentile confidence interval.
QUESTION TWO (20 MARKS)
For service planning, daily arrivals x = [10, 20, 30, 40] and corresponding mean waiting times y = [12, 16, 19,
23] minutes are modelled. The data frame patients contains Age, WaitingMinutes and VisitsPerYear. The
covariance matrix in part (b) describes two numerical patient-profile variables.
1. Explain the role of the intercept and the meaning of a fitted waiting time in the clinic’s regression
model.
2. Write Python or R code to fit an intercept-and-slope least-squares model and predict mean waiting
time when daily arrivals x = 50
3. A regression residual plot has a pronounced curved pattern. Analyse what this suggests about the
model and propose a modification, including one way to assess the improvement.
4. Design a principal component analysis workflow in Python or R for Age, WaitingMinutes and
VisitsPerYear in patients.
5. The network models high satisfaction as log(p / (1 − p)) = −1 + 0.4x, where p is the probability of a
satisfaction rating of at least 4 on a five-point scale and x is visits per year. A report says each extra
visit adds 0.4 directly to probability. Evaluate this statement and show how to calculate the probability
and odds ratio correctly.
1
QUESTION THREE (20 MARKS)
The network forecasts attendance using a data frame attendance with Month and Visits for 36 consecutive
months. A simplified forecast-calibration cost is g(θ) = (θ + 2)² + 5, where θ is an additive forecast adjustment
that may be positive or negative.
1. Explain autocorrelation and its relevance to time-series forecasting.
2. Write Python or R code to plot monthly visits and calculate month-to-month differences
3. Missing attendance values cluster during a service disruption. Analyse why deleting those months may
bias the report,
4. The clinic attendance forecast uses information from future months when constructing predictors and
omits its prediction interval. Evaluate the effect on reported performance and the usefulness of the
forecast for planning.
QUESTION FOUR (20 MARKS)
A clinic network evaluates service performance to reduce waiting times and plan staffing. Anonymised records
contain PatientID, Clinic, Age, WaitingMinutes and SatisfactionRating. Questions One to Five use different
samples and models from this study; each question supplies the data needed to answer it.
1. Discuss why the median may be preferred to the mean for highly skewed waiting times.
2. Explain why synthetic patient records used in the service study must be labelled and their generation
documented.
3. Write Python or R code to create a data frame with Clinic = [A, A, B, B] and WaitingMinutes = [10,
20, 15, 25].
4. For waiting times = [10, 12, 15, 18, 45], write Python or R code to calculate the median, sample
standard deviation and interquartile range.
5. Using the data frame in part (i), write Python or R code to calculate the mean waiting time for each
clinic.
QUESTION FIVE (20 MARKS)
The network evaluates a new appointment system. Waiting times in minutes for the same six patients are
Before = [25, 30, 28, 35, 32, 26] and After = [20, 24, 23, 27, 26, 21]. It also compares attendance patterns and
waiting times across clinics. Use a 5% significance level.
1. Explain the null and two-sided alternative hypotheses for the mean within-participant change.
2. Write Python or R code to perform a paired t-test and display its statistic and p-value
3. . A clinic expects equal attendance on three days but observes [45, 30, 15]. Perform a chi-square
goodness-of-fit test and display expected counts (3 marks).
2
4. The six patients have ages [20, 35, 30, 45, 40, 25], paired in order with the Before waiting times. Write
Python or R code to calculate sample covariance and Pearson correlation between age and waiting
time, then repeat after converting minutes to seconds. Analyse why covariance changes while
correlation remains unchanged.
5. Evaluate whether an independent-samples test is appropriate for the Before and After data, and justify
your judgement using the study design.
6. Paired differences are strongly skewed and contain an extreme value. Select a suitable paired
non-parametric alternative, justify your choice and state one assumption.