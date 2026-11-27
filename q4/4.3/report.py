import pandas as pd

# Create the data frame
data = {
    'Clinic': ['A', 'A', 'B', 'B'],
    'WaitingMinutes': [10, 20, 15, 25]
}

df = pd.DataFrame(data)

# Display the data frame
print(df)
