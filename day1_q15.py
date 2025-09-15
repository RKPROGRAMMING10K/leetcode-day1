import pandas as pd

def find_heavy_animals(animals):
    """
    List the names of animals that weigh strictly more than 100 kilograms,
    sorted by weight in descending order.

    Args:
    animals (pd.DataFrame): DataFrame containing animal information

    Returns:
    pd.DataFrame: DataFrame with 'name' column of heavy animals sorted by weight descending
    """
    return animals[animals['weight'] > 100].sort_values('weight', ascending=False)[['name']]

# Example usage:
# Assuming animals is a DataFrame as described
# result = find_heavy_animals(animals)
# print(result)