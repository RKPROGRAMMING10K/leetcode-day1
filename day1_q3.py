import pandas as pd

def select_first_rows(employees):
    """
    Display the first 3 rows of the employees DataFrame.

    Args:
    employees (pd.DataFrame): DataFrame containing employee information

    Returns:
    pd.DataFrame: First 3 rows of the DataFrame
    """
    return employees.head(3)

# Example usage:
# Assuming employees is a DataFrame as described
# result = select_first_rows(employees)
# print(result)