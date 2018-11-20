from pandas.core.common import array_equivalent
import pandas as pd
import numpy as np


def find_empty_columns(df, threshold=0.80):
    """A list of columns that have more > 80% missing values.

    For each column computes the number of missing values.
    If the value is greater than 80%, relative to column length,
    then column name is added to list.

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe with columns to search
    threshold : int (optional)
        threshold for deleting columns

    Returns
    -------
    empty_columns : list
        a list of columns with mostly empty values.
    """
    empty_columns = []
    for column in df:
        if df[column].isna().sum() / len(df) > threshold:
            empty_columns.append(column)
    return empty_columns


def find_low_variance(data, threshold=0.18):
     """Finds columns with low variance.

    Takes a dataframe as input. Creates a list of columns with low threshold.
    These columns can then be dropped from original dataframe.

    Parameters
    ---------------
    data : pandas.DataFrame
        dataframe with columns to search
    threshold : int (optional)
        threshold for deleting columns

    Returns
    ---------------
    low_variance_columns : list
        a list of columns with low variance.
    """
    low_variance_columns = []
    for column in data.columns:
        if (data[column].dtype == 'float64') or (data[column].dtype == 'int64'):
            if data[column].var() < threshold:
                low_variance_columns.append(column)
    return low_variance_columns


def find_low_var_categories(data, threshold=0.18):
     """Finds categorical columns with low variance.

    Takes a dataframe as input. Creates a list of columns with low threshold.
    These columns can then be dropped from original dataframe.

    Parameters
    ---------------
    data : pandas.DataFrame
        dataframe with columns to search
    threshold : int (optional)
        threshold for deleting columns

    Returns
    ---------------
    low_variance_columns : list
        a list of columns with low variance.
    """
    low_variance_columns = []
    for column in data.columns:
        if data[column].dtype == 'O':
            if pd.get_dummies(df[column]).var().sum() < threshold:
                low_variance_columns.append(column)
    return low_variance_columns


def replace_NaN(data):
    """Replace NaN values with the median from numerical column.

    Takes a dataframe as input. Iterates through the dataframe for numeric types columns.
    Replaces any NaN values with median value of column.

    Parameters
    ---------------
    data : pandas.DataFrame
        dataframe with columns to search

    Returns
    ---------------
    data : pandas.DataFrame
        dataframe with columns containing replaced NaNs.
    """

    for column in data.columns:
        if data[column].dtype != 'O':
            data[column].fillna(data[column].median(), inplace=True)

    return data


def time_like(df):
    """Finds time like columns.

    Takes a dataframe as input. Iterates through the dataframe columns.
    Returns a list of potential time like columns.

    Parameters
    ---------------
    df: pandas.DataFrame
        dataframe with columns to search

    Returns
    ---------------
    low_variance_columns : list
        a list of columns with low variance.
    """
    time_columns = []
    for column in df:
        if df[column].dtype != 'O':
            if df[column].mean() / 1000 > 1:
                time_columns.append(column)
    return time_columns

def convert_to_timestamp(df, time_columns):
    """Coverts columns in a dataframe to datetime.

    Takes a dataframe and list of columns as input.
    Converts columns in list to datetime format, depending on the length of value.
    For values longer than 6, only the year is stripped.

    Parameters
    ---------------
    df: pandas.DataFrame
        dataframe with columns to search
    time_columns: list
        list of time like columns

    Returns
    ---------------
    df: pandas.DataFrame
        dataframe with converted time columns
    """
    for column in df[time_columns]:
        # convert year
        if len(str(int(df[column][0]))) == 4:
            # convert to time stamp and then to int
            df[column] = pd.to_datetime(df[column].astype(
                int), format='%Y').astype(np.int64)

        elif len(str(int(df[column][0]))) == 5:
            # convert to time stamp and then to int
            df[column] = pd.to_datetime(df[column].astype(
                int), format='%Y%m').astype(np.int64)

        # strip the year
        elif len(str(int(df[column][0]))) == 6:
            # truncate to year month and convert to time stamp, then to int
            df[column] = df[column].astype(
                int).astype(str).apply(lambda x: x[:4])
            df[column] = pd.to_datetime(
                df[column], format='%Y').astype(np.int64)

    return df
