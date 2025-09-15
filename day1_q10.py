import pandas as pd

def change_datatype(students):
    """
    Convert the grade column from float to int.

    Args:
    students (pd.DataFrame): DataFrame containing student information

    Returns:
    pd.DataFrame: DataFrame with grade column converted to int
    """
    students['grade'] = students['grade'].astype(int)
    return students

# Example usage:
# Assuming students is a DataFrame as described
# result = change_datatype(students)
# print(result)