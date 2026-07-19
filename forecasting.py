import pandas as pd
from prophet import Prophet
import plotly.express as px
from pathlib import Path

# -----------------------------------------------------
# Create Output Directory
# -----------------------------------------------------

Path("assets/forecast").mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------
# Load Processed Dataset
# -----------------------------------------------------

df = pd.read_csv("data/processed/ferry_processed.csv")

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# -----------------------------------------------------
# Prepare Daily Activity
# -----------------------------------------------------

daily_activity = (
    df.groupby(df["Timestamp"].dt.date)["Total Activity Load"]
    .sum()
    .reset_index()
)

daily_activity.columns = ["ds", "y"]

daily_activity["ds"] = pd.to_datetime(daily_activity["ds"])

print("Dataset Ready")
print(daily_activity.head())

# -----------------------------------------------------
# Train Prophet Model
# -----------------------------------------------------

model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False
)

model.fit(daily_activity)

# -----------------------------------------------------
# Predict Next 30 Days
# -----------------------------------------------------

future = model.make_future_dataframe(periods=30)

forecast = model.predict(future)

# -----------------------------------------------------
# Save Forecast CSV
# -----------------------------------------------------

forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].to_csv(
    "assets/forecast/forecast_results.csv",
    index=False
)

print("Forecast CSV Saved")

# -----------------------------------------------------
# Forecast Plot
# -----------------------------------------------------

fig = px.line(
    forecast,
    x="ds",
    y="yhat",
    title="30-Day Passenger Demand Forecast"
)

fig.add_scatter(
    x=daily_activity["ds"],
    y=daily_activity["y"],
    mode="lines",
    name="Historical Activity"
)

fig.write_html("assets/forecast/forecast.html")

print("Forecast Chart Saved")

fig.show()

print("Forecasting Completed Successfully")