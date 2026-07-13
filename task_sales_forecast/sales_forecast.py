"""
sales_forecast

Reads a CSV file of monthly sales data with fixed columns 'date' and
'sales', fits a Prophet model, and returns a forecast for future
periods. No external services and no environment variables are
required.
"""

import os
import pandas as pd
from prophet import Prophet


def load_sales_csv(file_path, date_col="date", sales_col="sales"):
    """
    Read a sales CSV file and return a DataFrame in the two column
    shape Prophet expects: ds (date) and y (numeric value).

    file_path: path to the CSV file
    date_col: name of the date column in the source CSV
    sales_col: name of the sales value column in the source CSV

    Returns a pandas DataFrame with columns ds and y, sorted by date,
    with rows containing missing dates or missing sales values removed.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    df = pd.read_csv(file_path)

    if date_col not in df.columns:
        raise ValueError(f"Expected date column '{date_col}' not found in CSV")
    if sales_col not in df.columns:
        raise ValueError(f"Expected sales column '{sales_col}' not found in CSV")

    df = df[[date_col, sales_col]].rename(columns={date_col: "ds", sales_col: "y"})
    df["ds"] = pd.to_datetime(df["ds"])
    df = df.dropna(subset=["ds", "y"])
    df = df.sort_values("ds").reset_index(drop=True)

    return df


def train_forecast_model(df, yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False):
    """
    Fit a Prophet model on a DataFrame with columns ds and y.

    yearly_seasonality: whether to model a yearly seasonal pattern
    weekly_seasonality: whether to model a weekly seasonal pattern
    daily_seasonality: whether to model a daily seasonal pattern

    Returns a fitted Prophet model.
    """
    model = Prophet(
        yearly_seasonality=yearly_seasonality,
        weekly_seasonality=weekly_seasonality,
        daily_seasonality=daily_seasonality,
    )
    model.fit(df)

    return model


def generate_forecast(model, periods=30, freq="MS"):
    """
    Generate a forecast from a fitted Prophet model.

    model: a fitted Prophet model
    periods: number of future periods to forecast
    freq: pandas frequency string for each period, "MS" (month start)
          by default since the source data is monthly

    Returns a DataFrame with columns ds, yhat, yhat_lower, yhat_upper,
    covering both the historical fit and the future periods.
    """
    future = model.make_future_dataframe(periods=periods, freq=freq)
    forecast = model.predict(future)

    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]


def run_sales_forecast(csv_path, date_col="date", sales_col="sales", periods=30, freq="MS"):
    """
    Load a sales CSV, fit a Prophet model, and return a forecast.

    csv_path: path to the CSV file, expected to have columns 'date' and 'sales'
    date_col: name of the date column in the source CSV
    sales_col: name of the sales value column in the source CSV
    periods: number of future periods to forecast, 30 by default
    freq: pandas frequency string for each period, "MS" (month start) by default

    Returns a DataFrame with columns ds, yhat, yhat_lower, yhat_upper.
    """
    df = load_sales_csv(csv_path, date_col=date_col, sales_col=sales_col)
    model = train_forecast_model(df)
    forecast = generate_forecast(model, periods=periods, freq=freq)

    return forecast
