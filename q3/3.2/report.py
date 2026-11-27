import pandas as pd
import matplotlib.pyplot as plt

# Convert Month column to datetime
attendance['Month'] = pd.to_datetime(attendance['Month'])

# Sort data by month
attendance = attendance.sort_values('Month')

# Plot monthly visits
plt.plot(attendance['Month'], attendance['Visits'],
         marker='o')

plt.xlabel('Month')
plt.ylabel('Number of Visits')
plt.title('Monthly Clinic Attendance')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Calculate month-to-month differences
attendance['Monthly_Difference'] = attendance['Visits'].diff()

print(attendance[['Month', 'Visits', 'Monthly_Difference']])
