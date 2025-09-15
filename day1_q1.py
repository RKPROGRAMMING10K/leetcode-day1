import pandas as pd

def create_dataframe(student_data):
    """
    Create a DataFrame from a 2D list containing student IDs and ages.

    Args:
    student_data (list of lists): 2D list where each sublist is [student_id, age]

    Returns:
    pd.DataFrame: DataFrame with columns 'student_id' and 'age'
    """
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

# Example usage:
# student_data = [
#   [1, 15],
#   [2, 11],
#   [3, 11],
#   [4, 20]
# ]
# df = create_dataframe(student_data)
# print(df)