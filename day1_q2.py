import pandas as pd

def get_dataframe_shape(players):
    """
    Calculate and return the number of rows and columns of the players DataFrame.

    Args:
    players (pd.DataFrame): DataFrame containing player information

    Returns:
    list: [number of rows, number of columns]
    """
    return [players.shape[0], players.shape[1]]

# Example usage:
# Assuming players is a DataFrame as described
# result = get_dataframe_shape(players)
# print(result)  # Output: [10, 5]