"""
csv_description

Reads a CSV file and returns a full description of it as a plain
Python dict, built entirely with pandas. No external services and
no environment variables are required.
"""

import os
import pandas as pd


def read_csv_file(file_path, **read_csv_kwargs):
    """
    Read a CSV file into a pandas DataFrame.

    file_path: path to the CSV file
    read_csv_kwargs: any extra keyword arguments forwarded to pandas.read_csv
                     (for example sep, encoding, dtype)

    Returns a pandas DataFrame.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    return pd.read_csv(file_path, **read_csv_kwargs)


def get_basic_info(df):
    """
    Return the shape and column names of a DataFrame.
    """
    return {
        "row_count": int(df.shape[0]),
        "column_count": int(df.shape[1]),
        "column_names": list(df.columns),
    }


def get_dtypes(df):
    """
    Return the pandas dtype of each column as a dict of column name to
    dtype string.
    """
    return {column: str(dtype) for column, dtype in df.dtypes.items()}


def get_missing_values(df):
    """
    Return the count and percentage of missing values for each column.
    """
    total_rows = len(df)
    missing_counts = df.isnull().sum()

    result = {}
    for column, count in missing_counts.items():
        percentage = (count / total_rows * 100) if total_rows else 0.0
        result[column] = {
            "missing_count": int(count),
            "missing_percentage": round(float(percentage), 2),
        }
    return result


def get_unique_counts(df):
    """
    Return the number of unique values for each column.
    """
    return {column: int(df[column].nunique()) for column in df.columns}


def get_numeric_summary(df):
    """
    Return descriptive statistics (count, mean, std, min, quartiles, max)
    for all numeric columns. Returns an empty dict if there are no
    numeric columns.
    """
    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        return {}

    summary = numeric_df.describe().to_dict()
    for column, stats in summary.items():
        summary[column] = {stat_name: float(value) for stat_name, value in stats.items()}

    return summary


def get_categorical_summary(df, top_n=5):
    """
    Return the most frequent values for each non-numeric column.

    top_n: how many top values to include per column
    """
    categorical_df = df.select_dtypes(exclude="number")

    if categorical_df.empty:
        return {}

    summary = {}
    for column in categorical_df.columns:
        value_counts = df[column].value_counts().head(top_n)
        summary[column] = {str(value): int(count) for value, count in value_counts.items()}

    return summary


def get_memory_usage(df):
    """
    Return memory usage in bytes for the whole DataFrame and per column.
    """
    per_column = df.memory_usage(deep=True, index=False)

    return {
        "total_bytes": int(per_column.sum()),
        "per_column_bytes": {column: int(value) for column, value in per_column.items()},
    }


def get_sample_rows(df, sample_size=5):
    """
    Return the first sample_size rows of the DataFrame as a list of dicts.
    """
    return df.head(sample_size).to_dict(orient="records")


def describe_csv(file_path, sample_size=5, top_n=5, read_csv_kwargs=None):
    """
    Read a CSV file and return a full description of it as a dict.

    file_path: path to the CSV file
    sample_size: number of sample rows to include
    top_n: number of top frequent values to include per categorical column
    read_csv_kwargs: optional dict of extra keyword arguments for pandas.read_csv

    Returns a dict with the following keys:
    basic_info, dtypes, missing_values, unique_counts, numeric_summary,
    categorical_summary, memory_usage, sample_rows
    """
    read_csv_kwargs = read_csv_kwargs or {}
    df = read_csv_file(file_path, **read_csv_kwargs)

    return {
        "basic_info": get_basic_info(df),
        "dtypes": get_dtypes(df),
        "missing_values": get_missing_values(df),
        "unique_counts": get_unique_counts(df),
        "numeric_summary": get_numeric_summary(df),
        "categorical_summary": get_categorical_summary(df, top_n=top_n),
        "memory_usage": get_memory_usage(df),
        "sample_rows": get_sample_rows(df, sample_size=sample_size),
    }
