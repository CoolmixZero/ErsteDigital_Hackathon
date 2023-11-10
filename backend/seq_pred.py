import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import numpy as np


# Generate more random data for the example
# Let's create a dataset with a slightly more complex pattern
np.random.seed(42)  # for reproducibility

# Generate random data with a trend and some seasonality
days = pd.date_range(start='2020-01-01', periods=2000, freq='D')
data = np.random.normal(loc=0, scale=5, size=2000).cumsum()
seasonality = np.sin(np.linspace(0, 20, 2000)) * 20
noise = np.random.normal(loc=0, scale=2, size=2000)

# Combine trend, seasonality, and noise
y = 50 + data + seasonality + noise

# Create the DataFrame
df = pd.DataFrame({'ds': days, 'y': y})

print(df.tail())

# Initialize a Prophet model
model = Prophet(interval_width=0.92, daily_seasonality=True)

# Fit the model on the dataset
model.fit(df)

# Create a DataFrame for future dates to predict
periods = 60
future = model.make_future_dataframe(periods=periods)

# Predict values for future dates
forecast = model.predict(future)

# Display the forecast
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

fig = model.plot(forecast)

plt.title('Prophet Forecast')
plt.ylabel('Predicted Value')
plt.xlabel('Date')
plt.xlim(days[-300], days[-1] + pd.DateOffset(days=periods))

plt.show()