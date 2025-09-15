import pandas as pd

def melt_table(report):
    """
    Reshape the report DataFrame from wide to long format so that each row represents
    sales data for a product in a specific quarter.

    Args:
    report (pd.DataFrame): DataFrame containing product sales data

    Returns:
    pd.DataFrame: Reshaped DataFrame with columns 'product', 'quarter', 'sales'
    """
    return report.melt(id_vars='product', var_name='quarter', value_name='sales')

# Example usage:
# Assuming report is a DataFrame as described
# result = melt_table(report)
# print(result)