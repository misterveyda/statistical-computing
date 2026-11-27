import numpy as np
from sklearn.linear_model import LinearRegression

# Independent and dependent variables
x = np.array([10, 20, 30, 40]).reshape(-1, 1)
y = np.array([12, 16, 19, 23])

# Fit linear regression model
model = LinearRegression()
model.fit(x, y)

# Predict waiting time for 50 arrivals
prediction = model.predict([[50]])

print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])
print("Predicted waiting time:", prediction[0])
