
"""
Exploratory Data Analysis (EDA) is an analytical approach that employs 
visual techniques to examine and understand data. It plays a crucial
role in uncovering trends, patterns, and relationships within the dataset,
as well as validating assumptions through the use of statistical summaries
and graphical representations. EDA is an essential step in the
data analysis process, providing insights that can guide further analysis,
model building, and decision-making.
"""

# importing df from basic modules
from basic_modules import df, np

# Iterate through each column in the DataFrame
for col in df.columns:
    # Check if the data type of the column is 'object' (typically categorical)
    if df[col].dtype == 'object':
        # Fill missing values in categorical columns with the mode (most frequent value)
        df[col] = df[col].fillna(df[col].mode()[0])

    # Check if the data type of the column is numeric
    elif np.issubdtype(df[col].dtype, np.number):
        # Fill missing values in numeric columns with the mean
        df[col] = df[col].fillna(df[col].mean())

# Check the total number of remaining null values in the DataFrame
total_nulls = df.isnull().sum().sum()

# print("Total null values after imputation:", total_nulls)

# Initialize empty lists to store column names based on data types
ints, objects, floats = [], [], []

# Iterate through each column in the DataFrame
for col in df.columns:
    # Check if the data type of the column is float
    if df[col].dtype == float:
        # Add the column to the list of float columns
        floats.append(col)
    
    # Check if the data type of the column is int
    elif df[col].dtype == int:
        # Add the column to the list of integer columns
        ints.append(col)
    
    # If the data type is neither float nor int, assume it's an object
    else:
        # Add the column to the list of object columns
        objects.append(col)

# Print the counts of columns for each data type
print("Number of integer columns:", len(ints))
print("Number of float columns:", len(floats))
print("Number of object columns:", len(objects))

