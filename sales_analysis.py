import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# Preview data
print("First few rows:")
print(df.head())

# Handle missing values (if any)
df['Sales'] = df['Sales'].fillna(0)

# Calculate total and average sales
total_sales = np.sum(df['Sales'])
average_sales = np.mean(df['Sales'])
print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales}")

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Group by month and sum sales
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

# Plot
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='bar')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()