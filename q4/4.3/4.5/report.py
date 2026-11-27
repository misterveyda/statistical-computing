import pandas as pd

# Create data frame
data = {
    'Clinic': ['A', 'A', 'B', 'B'],
    'WaitingMinutes': [10, 20, 15, 25]
}

df = pd.DataFrame(data)

# Calculate mean waiting time for each clinic
mean_waiting = df.groupby('Clinic')['WaitingMinutes'].mean()

print(mean_waiting)
