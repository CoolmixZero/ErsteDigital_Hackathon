import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt


# Define the data
current_balance = 1000
data = [
    ["2023-01-01", "Groceries", -45],
    ["2023-01-01", "Utilities", -30],
    ["2023-01-02", "Rent", -500],
    ["2023-01-02", "Freelance Income", 200],
    ["2023-01-03", "Transport", -20],
    ["2023-01-04", "Dining Out", -35],
    ["2023-01-05", "Gym Membership", -25],
    ["2023-01-05", "Salary", 1000],
    ["2023-01-06", "Entertainment", -50],
    ["2023-01-07", "Groceries", -60],
    ["2023-01-08", "Healthcare", -40],
    ["2023-01-09", "Transport", -15],
    ["2023-01-10", "Utilities", -25],
    ["2023-01-11", "Clothing", -75],
    ["2023-01-12", "Freelance Income", 150],
    ["2023-01-13", "Rent", -500],
    ["2023-01-14", "Groceries", -55],
    ["2023-01-15", "Dining Out", -30],
    ["2023-01-16", "Gym Membership", -25],
    ["2023-01-18", "Entertainment", -60],
    ["2023-01-19", "Groceries", -70],
    ["2023-01-20", "Healthcare", -45],
    ["2023-01-21", "Transport", -20],
    ["2023-01-22", "Utilities", -30],
    ["2023-01-23", "Clothing", -80],
    ["2023-01-24", "Freelance Income", 250],
    ["2023-01-25", "Rent", -500],
    ["2023-01-26", "Groceries", -65],
    ["2023-01-27", "Dining Out", -40],
    ["2023-01-28", "Gym Membership", -25],
    ["2023-01-30", "Entertainment", -55],
    ["2023-01-31", "Groceries", -75],
    ["2023-01-31", "Healthcare", -50],
    ["2023-02-01", "Transport", -25],
    ["2023-02-02", "Utilities", -35],
    ["2023-02-03", "Clothing", -90],
    ["2023-02-04", "Freelance Income", 300],
    ["2023-02-05", "Rent", -550],
    ["2023-02-06", "Groceries", -50],
    ["2023-02-07", "Dining Out", -45],
    ["2023-02-08", "Gym Membership", -30],
    ["2023-02-09", "Salary", 1150],
    ["2023-02-10", "Entertainment", -70],
    ["2023-02-11", "Groceries", -80],
    ["2023-02-12", "Healthcare", -60],
    ["2023-02-13", "Transport", -30],
    ["2023-02-14", "Utilities", -40],
    ["2023-02-15", "Clothing", -100]
]

for i in range(len(data)):
    current_balance += data[i][2]
    data[i][2] = current_balance

# Convert to DataFrame
df = pd.DataFrame(data, columns=['ds', 'Category', 'y'])
df.drop(columns=['Category'], inplace=True)

# Convert the 'Date' column to datetime
df['ds'] = pd.to_datetime(df['ds'])

# Initialize a Prophet model
model = Prophet(interval_width=0.92, daily_seasonality=True)

# Fit the model on the dataset
model.fit(df)

# Create a DataFrame for future dates to predict
periods = 15
future = model.make_future_dataframe(periods=periods, freq='D')

# Predict values for future dates
forecast = model.predict(future)

# Display the forecast
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# Plot the historical data
plt.plot(df['ds'], df['y'], label='Historical Data', marker='.', linestyle='-')

# Plot the forecast
plt.plot(forecast['ds'], forecast['yhat'], label='Forecast', linestyle='--')

# Highlight the forecasted future only
plt.plot(forecast['ds'][len(df):], forecast['yhat'][len(df):], color='red', label='Future Forecast', linestyle='--')

plt.legend()
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Historical Data and Prophet Forecast')
plt.show()