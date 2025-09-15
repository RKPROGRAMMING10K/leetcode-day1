import pandas as pd

def rename_columns(students):
    """
    Rename the columns of the students DataFrame as specified.

    Args:
    students (pd.DataFrame): DataFrame containing student information

    Returns:
    pd.DataFrame: DataFrame with renamed columns
    """
    return students.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    })

# Example usage:
# Assuming students is a DataFrame as described
# result = rename_columns(students)
# print(result)