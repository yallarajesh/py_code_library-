# csv_description

Reads a CSV file with pandas and returns a full description of it as a plain Python dict.

## functions exposed
- read_csv_file(file_path, **read_csv_kwargs) -> pandas.DataFrame
- get_basic_info(df) -> dict (row_count, column_count, column_names)
- get_dtypes(df) -> dict (column name to dtype string)
- get_missing_values(df) -> dict (missing_count, missing_percentage per column)
- get_unique_counts(df) -> dict (unique value count per column)
- get_numeric_summary(df) -> dict (count, mean, std, min, quartiles, max per numeric column)
- get_categorical_summary(df, top_n=5) -> dict (top frequent values per non-numeric column)
- get_memory_usage(df) -> dict (total_bytes, per_column_bytes)
- get_sample_rows(df, sample_size=5) -> list of dicts (first N rows)
- describe_csv(file_path, sample_size=5, top_n=5, read_csv_kwargs=None) -> dict (full description, combines all of the above)

## dependencies
pandas>=2.0.0

## env vars required
none

## tags
csv, pandas, data description, eda, data profiling, dataframe summary

## status
tested, passing

## path
task_csv_description/csv_description.py
