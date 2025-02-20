import pandas as pd
import matplotlib.pyplot as plt

# Function to load and preprocess the data
def load_data(file_path, columns=None, skip_rows=0, filters=None):
    """
    Loads a CSV file, selects specific columns, applies row filters, and returns a DataFrame.

    Parameters:
    - file_path (str): Path to the CSV file.
    - columns (list, optional): List of columns to load. Default is None (loads all columns).
    - skip_rows (int, optional): Number of rows to skip from the top. Default is 0.
    - filters (dict, optional): Dictionary of filters {column: value} to apply.

    Returns:
    - df (DataFrame): Filtered Pandas DataFrame.
    """
    # Load the data
    df = pd.read_csv(file_path, usecols=columns, skiprows=skip_rows)

    # Apply filters if provided
    if filters:
        for col, value in filters.items():
            df = df[df[col] == value]

    return df

# Function to create a bar chart for missile usage
def plot_missile_usage(df, missile_column, target_column):
    """
    Creates a bar chart showing how many missiles were used per target.

    Parameters:
    - df (DataFrame): Processed DataFrame.
    - missile_column (str): Column containing missile type.
    - target_column (str): Column containing target ID or name.
    """
    # Count the number of missiles per target
    missile_counts = df.groupby(target_column)[missile_column].count()

    # Plot
    plt.figure(figsize=(10, 6))
    missile_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Number of Missiles Used Per Target")
    plt.xlabel("Target")
    plt.ylabel("Missile Count")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Example usage
if __name__ == "__main__":
    # File path (Modify this for different files)
    file_path = "path/to/your/data.csv"

    # Define the columns you want to load
    selected_columns = ["missile_type", "target_id", "hit_result"]

    # Define filters (Optional)
    filters = {
        "hit_result": "Destroyed"  # Example: Only keep rows where the target was destroyed
    }

    # Load the data
    df = load_data(file_path, columns=selected_columns, skip_rows=0, filters=filters)

    # Plot missile usage per target
    plot_missile_usage(df, missile_column="missile_type", target_column="target_id")
