"""
To visualize the dataset
"""
# Import the data frame
from basic_modules import df, plt

# Plot a bar chart showing the count of null values in each column
df.isnull().sum().plot.bar()

# Display the plot
plt.show()
