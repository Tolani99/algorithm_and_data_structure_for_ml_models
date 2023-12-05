"""
The data which is obtained from the primary sources
is termed the raw data and required
a lot of preprocessing before we can derive
any conclusions from it or do some modeling on it. 
Those preprocessing steps are known as data cleaning
and it includes, outliers removal, null value imputation,
and removing discrepancies of any sort in the data inputs.
"""

# Importing data frame from basic modules
from basic_modules import df

# Initialize a list to store columns to be removed
to_remove = []

# Iterate through columns in the DataFrame
for col in df.columns:
    # Check if the column has only one unique value
    if df[col].nunique() == 1:
        # Add the column to the list of columns to be removed
        to_remove.append(col)

    # Check if more than 60% of the values in the column are null
    elif df[col].isnull().mean() > 0.60:
        # Add the column to the list of columns to be removed
        to_remove.append(col)

# Print the number of columns to be removed
# print(len(to_remove))

# Drop columns from the DataFrame based on the to_remove list
# print(df.drop(to_remove, axis=1, inplace=True))

# print the information
print(df.info())
