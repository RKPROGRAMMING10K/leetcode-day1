import pandas as pd

def drop_missing_data(students):
    """
    Remove rows with missing values in the name column.

    Args:
    students (pd.DataFrame): DataFrame containing student information

    Returns:
    pd.DataFrame: DataFrame with rows containing missing names removed
    """
    return students.dropna(subset=['name'])

# Example usage:
# Assuming students is a DataFrame as described
# result = drop_missing_data(students)
# print(result)