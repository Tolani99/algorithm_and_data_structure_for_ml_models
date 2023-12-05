# Importing the basic modules
from basic_modules import plt, sb, df

# Create a new figure with a specified size of 8x5 inches
plt.figure(figsize=(8, 5))

# Generate a horizontal bar plot for the counts of each category in the 'Metro' column
sb.countplot(y='Metro', data=df)

# Display the plot
plt.show()
