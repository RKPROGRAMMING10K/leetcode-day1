import pandas as pd

def concatenate_tables(df1, df2):
    """
    Concatenate two DataFrames vertically into one DataFrame.

    Args:
    df1 (pd.DataFrame): First DataFrame
    df2 (pd.DataFrame): Second DataFrame

    Returns:
    pd.DataFrame: Concatenated DataFrame
    """
    return pd.concat([df1, df2], ignore_index=True)

# Example usage:
# Assuming df1 and df2 are DataFrames as described
# result = concatenate_tables(df1, df2)
# print(result)