import pandas as pd

def create_bonus_column(employees):
    """
    Create a new column 'bonus' that contains the doubled values of the salary column.

    Args:
    employees (pd.DataFrame): DataFrame containing employee information with 'name' and 'salary'

    Returns:
    pd.DataFrame: DataFrame with the new 'bonus' column added
    """
    employees['bonus'] = employees['salary'] * 2
    return employees

# Example usage:
# Assuming employees is a DataFrame as described
# result = create_bonus_column(employees)
# print(result)