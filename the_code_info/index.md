<!--
One line per task. Format:
<task_name> | <one-line description> | tags: <tag1, tag2, ...> | task_<task_name>/

This file is read first, before any full doc or source code, to check
whether a task already exists before building it again.
-->

csv_description | reads a CSV file with pandas and returns a full description as a dict (shape, dtypes, missing values, unique counts, numeric and categorical summaries, memory usage, sample rows) | tags: csv, pandas, data description, eda, data profiling, dataframe summary | task_csv_description/
sales_forecast | reads a monthly sales CSV (date, sales columns) and returns a Prophet forecast for future periods | tags: forecasting, prophet, sales, time series, monthly data, pandas | task_sales_forecast/
test_postgres_connection | reads a Postgres URL from an environment variable and tests the connection with psycopg2, returning status, version, and connection details | tags: postgres, psycopg2, database, connection test, sql | task_test_postgres_connection/
