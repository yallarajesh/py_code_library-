# sales_forecast

Reads a monthly sales CSV file (fixed columns date and sales) and returns a Prophet forecast for future periods.

## functions exposed
- load_sales_csv(file_path, date_col="date", sales_col="sales") -> pandas DataFrame with columns ds, y
- train_forecast_model(df, yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False) -> fitted Prophet model
- generate_forecast(model, periods=30, freq="MS") -> pandas DataFrame with columns ds, yhat, yhat_lower, yhat_upper
- run_sales_forecast(csv_path, date_col="date", sales_col="sales", periods=30, freq="MS") -> pandas DataFrame with columns ds, yhat, yhat_lower, yhat_upper

## dependencies
pandas
prophet

## env vars required
none

## tags
forecasting, prophet, sales, time series, monthly data, pandas

## status
tested, passing

## path
task_sales_forecast/sales_forecast.py
