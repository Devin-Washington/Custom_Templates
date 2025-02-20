import pandas as pd
import matplotlib.pyplot as plt
import os
from glob import glob

# Function to load and preprocess multiple CSV files
def load_multiple_files(directory, file_pattern="*.csv", columns=None, skip_rows=0, filters=None):
    """
    Loads multiple CSV files from a directory, selects specific columns, applies row filters,
    and merges them into a single DataFrame.

    Parameters:
    - directory (str): Path to the directory containing CSV files.
    - file_pattern (str, optional): Pattern to match files (default "*.csv").
    - columns (list, optional): List of columns to load (default None, loads all columns).
    - skip_rows (int, optional): Number of rows to skip from the top (default 0).
    - filters (dict, optional): Dictionary of filters {column: value} to apply.

    Returns:
    - combined_df (DataFrame): Merged DataFrame from all loaded CSV files.
    """
    all_files = glob(os.path.join(directory, file_pattern))
    dataframes = []

    for file in all_files:
        df = pd.read_csv(file, usecols=columns, skiprows=skip_rows)
        df["source_file"] = os.path.basename(file)  # Keep track of source file name
        dataframes.append(df)

    if not dataframes:
        print("No files found in the specified directory.")
        return pd.DataFrame()  # Return empty DataFrame if no files were found

    # Merge all DataFrames
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Apply filters if provided
    if filters:
        for col, value in filters.items():
            combined_df = combined_df[combined_df[col] == value]

    return combined_df

# Function to create a bar chart for missile usage
def plot_missile_usage(df, missile_column, target_column):
    """
    Creates a bar chart showing how many missiles were used per target.

    Parameters:
    - df (DataFrame): Processed DataFrame.
    - missile_column (str): Column containing missile type.
    - target_column (str): Column containing target ID or name.
    """
    if df.empty:
        print("No data available for visualization.")
        return

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
    # Directory containing your CSV files
    data_directory = "path/to/your/csv/files"

    # Define the columns you want to load
    selected_columns = ["missile_type", "target_id", "hit_result"]

    # Define filters (Optional)
    filters = {
        "hit_result": "Destroyed"  # Example: Only keep rows where the target was destroyed
    }

    # Load multiple files
    df = load_multiple_files(data_directory, columns=selected_columns, skip_rows=0, filters=filters)

    # Plot missile usage per target
    plot_missile_usage(df, missile_column="missile_type", target_column="target_id")
