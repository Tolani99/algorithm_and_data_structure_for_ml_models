"""
To fill missing values
"""

# Import from basic modules import data frame
from basic_modules import df, np

# Iterate through each column in the DataFrame
for col in df.columns:
    # Check if the data type of the column is 'object' (categorical)
    if df[col].dtype == 'object':
        # Fill missing values with the mode (most frequent value) for categorical columns
        df[col] = df[col].fillna(df[col].mode()[0])
    # Check if the data type of the column is numerical
    elif df[col].dtype == np.number:
        # Fill missing values with the mean for numerical columns
        df[col] = df[col].fillna(df[col].mean())

# Check the total number of missing values after filling
total_missing_values = df.isnull().sum().sum()

# Print the total missing values
print(total_missing_values)
