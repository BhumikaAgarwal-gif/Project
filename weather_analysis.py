import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("weather_data.csv")

# Preview data
print("First few rows:")
print(df.head())

# Handle missing values (if any)
df['Temperature'] = df['Temperature'].fillna(df['Temperature'].mean())
df['Rainfall'] = df['Rainfall'].fillna(0)

# Calculate average temperature and total rainfall
avg_temp = np.mean(df['Temperature'])
total_rainfall = np.sum(df['Rainfall'])
print(f"Average Temperature: {avg_temp:.2f}°C")
print(f"Total Rainfall: {total_rainfall:.2f}mm")

# Convert 'Date' to datetime and extract month
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

# Group by month
monthly_avg_temp = df.groupby('Month')['Temperature'].mean()
monthly_total_rain = df.groupby('Month')['Rainfall'].sum()

# Plot
fig, ax1 = plt.subplots(figsize=(10,5))

color = 'tab:blue'
ax1.set_xlabel('Month')
ax1.set_ylabel('Avg Temperature (°C)', color=color)
ax1.plot(monthly_avg_temp.index.astype(str), monthly_avg_temp, color=color, marker='o')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Total Rainfall (mm)', color=color)
ax2.bar(monthly_total_rain.index.astype(str), monthly_total_rain, alpha=0.3, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Monthly Average Temperature and Total Rainfall')
plt.tight_layout()
plt.show()