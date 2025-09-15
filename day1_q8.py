import pandas as pd

def modify_salary_column(employees):
    """
    Modify the salary column by multiplying each salary by 2.

    Args:
    employees (pd.DataFrame): DataFrame containing employee information with 'name' and 'salary'

    Returns:
    pd.DataFrame: DataFrame with salaries doubled
    """
    employees['salary'] = employees['salary'] * 2
    return employees

# Example usage:
# Assuming employees is a DataFrame as described
# result = modify_salary_column(employees)
# print(result)