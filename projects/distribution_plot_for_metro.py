# Import basic modules
from basic_modules import plt, sb, df

# Check if 'Metro' exists in the DataFrame
if 'Metro' in df.columns:
    # Specify the number of top categories to display
    top_categories = 10

    # Create a new figure with a specified size
    plt.figure(figsize=(12, 6))

    # Get the top N categories in the 'Metro' column
    top_metro_categories = df['Metro'].value_counts().nlargest(top_categories).index

    # Filter the DataFrame to include only the top categories
    df_top_metro = df[df['Metro'].isin(top_metro_categories)]

    # Generate a count plot for the top categories in the 'Metro' column
    sb.countplot(x='Metro', data=df_top_metro, order=top_metro_categories)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Display the plot
    plt.show()
else:
    print("'Metro' column not found in the DataFrame.")
