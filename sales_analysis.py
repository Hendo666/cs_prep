import pandas as pd

# Load the CSV
df = pd.read_csv("games_sales.csv")

# Print table
print("Full Data:")
print(df)

# Sort sales by high to low price
print("\nGames sorted by sales:")
print(df.sort_values("Sales", ascending=False))

# Calculate total sales
total_sales = df["Sales"].sum()
print(f"\nTotal sales: {total_sales} million")

# Count how many games per genre
print("\nNumber of games per genre:")
print(df["Genre"].value_counts())