import pandas as pd

def select_data(students):
    """
    Select the name and age of the student with student_id = 101.

    Args:
    students (pd.DataFrame): DataFrame containing student information

    Returns:
    pd.DataFrame: DataFrame with columns 'name' and 'age' for student_id 101
    """
    return students[students['student_id'] == 101][['name', 'age']]

# Example usage:
# Assuming students is a DataFrame as described
# result = select_data(students)
# print(result)