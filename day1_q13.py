import pandas as pd

def pivot_table(weather):
    """
    Pivot the weather DataFrame so that each row represents temperatures for a specific month,
    and each city is a separate column.

    Args:
    weather (pd.DataFrame): DataFrame containing weather data

    Returns:
    pd.DataFrame: Pivoted DataFrame
    """
    return weather.pivot(index='month', columns='city', values='temperature')

# Example usage:
# Assuming weather is a DataFrame as described
# result = pivot_table(weather)
# print(result)