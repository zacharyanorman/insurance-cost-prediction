import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Generate a date range for 36 months
rng = pd.date_range(start='2020-01-01', periods=36, freq='M')
print(rng)

# Create some fake sales data with a trend
np.random.seed(42)
sales = 50 + np.arange(36) * 2 + np.random.normal(0, 5, 36)

# Put months and sales into a DataFrame
df = pd.DataFrame({'Month': rng, 'Sales': sales})

# Fit an ARIMA(1,1,1) model
model = sm.tsa.ARIMA(df['Sales'], order=(1, 2, 0))
results = model.fit()

# Print the model summary
print(results.summary())

# Forecast the next 6 months
forecast = results.forecast(steps=12)

# Create a date index for the forecast
forecast_index = pd.date_range(start=df['Month'].iloc[-1], periods=13, freq='M')[1:]

# Plot the original data and the forecast
plt.plot(df['Month'], df['Sales'], label='Observed Sales')
plt.plot(forecast_index, forecast, label='Forecasted Sales', color='red', linestyle='--')
plt.legend()
plt.title("ARIMA Forecast of Sales")
plt.show()

import matplotlib.pyplot as plt

# Get residuals
residuals = results.resid

