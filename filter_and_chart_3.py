import pandas as pd
import matplotlib.pyplot as plt

# Load multiple Excel files with options to select columns and skip rows
def load_files(file_paths, use_columns=None, skip_rows=2):
    dataframes = [pd.read_excel(path, usecols=use_columns, skiprows=skip_rows) for path in file_paths]
    return pd.concat(dataframes, ignore_index=True)

# General function to create bar charts
def plot_bar_chart(df, x_column, y_column, title, color="skyblue"):
    counts = df.groupby(x_column)[y_column].count()
    counts.plot(kind="bar", color=color, edgecolor="black", figsize=(10, 6))
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

# Histogram: Shots per kill
def plot_shots_per_kill(df, missile_column, effect_column):
    df[df[effect_column] == "HIT"].groupby(missile_column).size().plot(kind="hist", bins=10, color="blue", edgecolor="black", alpha=0.7, figsize=(10, 6))
    plt.xlabel("Missiles per Kill")
    plt.ylabel("Frequency")
    plt.title("Distribution of Missile Shots Per Kill")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

# Pie chart: Missile effectiveness
def plot_missile_effectiveness(df, effect_column):
    df[effect_column].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["green", "red"], startangle=90, figsize=(8, 8))
    plt.title("Proportion of Missile Outcomes")
    plt.ylabel("")
    plt.show()

# Scatter plot: Missile type vs. effectiveness
def plot_missile_effectiveness_scatter(df, missile_column, effect_column):
    effectiveness_counts = df.groupby(missile_column)[effect_column].apply(lambda x: (x == "HIT").sum() / len(x))
    plt.scatter(effectiveness_counts.index, effectiveness_counts.values, color="purple", alpha=0.7, figsize=(10, 6))
    plt.xlabel("Missile Type")
    plt.ylabel("Hit Rate")
    plt.title("Missile Type vs. Kill Effectiveness")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

# Load and analyze data
file_paths_xlsx = ["Book1.xlsx", "Book2.xlsx", "Book3.xlsx", "Book4.xlsx"]
selected_columns = ["WeaponName", "WeaponTarget", "WeaponEffect"]
df_combined = load_files(file_paths_xlsx, use_columns=selected_columns)

# Generate visualizations
plot_bar_chart(df_combined, "WeaponName", "WeaponName", "Missile Usage Count")
plot_bar_chart(df_combined, "WeaponTarget", "WeaponName", "Number of Missiles Used Per Target", "green")
plot_bar_chart(df_combined[df_combined["WeaponEffect"] == "HIT"], "WeaponTarget", "WeaponName", "Missiles Required Per Kill", "red")
plot_shots_per_kill(df_combined, "WeaponName", "WeaponEffect")
plot_missile_effectiveness(df_combined, "WeaponEffect")
plot_missile_effectiveness_scatter(df_combined, "WeaponName", "WeaponEffect")
