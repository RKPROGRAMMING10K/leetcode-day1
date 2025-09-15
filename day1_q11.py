import pandas as pd

def fill_missing_values(products):
    """
    Fill missing values in the quantity column with 0.

    Args:
    products (pd.DataFrame): DataFrame containing product information

    Returns:
    pd.DataFrame: DataFrame with missing quantity values filled with 0
    """
    products['quantity'] = products['quantity'].fillna(0)
    return products

# Example usage:
# Assuming products is a DataFrame as described
# result = fill_missing_values(products)
# print(result)