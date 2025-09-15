import pandas as pd

def drop_duplicate_emails(customers):
    """
    Remove duplicate rows based on the email column, keeping only the first occurrence.

    Args:
    customers (pd.DataFrame): DataFrame containing customer information

    Returns:
    pd.DataFrame: DataFrame with duplicates removed based on email
    """
    return customers.drop_duplicates(subset='email')

# Example usage:
# Assuming customers is a DataFrame as described
# result = drop_duplicate_emails(customers)
# print(result)