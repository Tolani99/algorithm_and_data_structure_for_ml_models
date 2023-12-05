"""
To visualize the dataset
"""
# Import the data frame
from basic_modules import df, plt, sb

# Plot a bar chart showing the count of null values in each column
df.isnull().sum().plot.bar()

# Display the plot
# plt.show()

# Create a new figure with a specified size of 8x5 inches
plt.figure(figsize=(8, 5))

# Generate a distribution plot (histogram and kernel density estimate) for the 'target' column in the DataFrame
# sb.distplot(df['target'])

# Display the plot
# plt.show()

print(df.columns)
