from pandas.core.common import array_equivalent
import pandas as pd 
import numpy as np 


def find_duplicates(df):
    """Finds the names of duplicate columns. 

    Finds the different data types in a dataframe. 
    Creates a dictionary file with different data types as keys and the pertinent columns as keys. 
    
    
    Parameters
    ----------
    df : data : pandas.DataFrame
        dataframe to search for duplicates 


    Returns
    -------
    duplicates : list
        The list of duplicate column names.  
    """
    # emptly list to save duplicates
    duplicates = []

    # group the different data types into a dictionary
    data_groups = df.columns.to_series().groupby(df.dtypes).groups

    for group, columns in data_groups.items():

        sliced_columns_names = df[columns].columns
        sliced_df = df[columns]
        len_columns = len(sliced_columns_names)

        for position1 in range(len_columns):
            column1 = sliced_df.iloc[:, position1].values
            for position2 in range(position1 + 1, len_columns):
                column2 = sliced_df.iloc[:, position2].values
                if array_equivalent(column1, column2):
                    duplicates.append(sliced_columns_names[position1])
                    break

    return duplicates