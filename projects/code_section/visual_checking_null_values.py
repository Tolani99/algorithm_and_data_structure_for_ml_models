"""
To visualize the dataset and extract unique insights
"""
# Import the data frame
from basic_modules import df, plt, sb

# Plot a bar chart showing the count of null values in each column
df.isnull().sum().plot.bar()

# Display the plot
plt.show()

