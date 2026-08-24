import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("weather.csv")

# Print the whole table
print(df)

# Find the hottest city
hottest = df["Temperature"].max()
print(f"\nThe hottest temperature is: {hottest}")

# Find the average humidity
print(f"\nThe average humidity is: {df['Humidity'].mean()}")

# Show only the rows where temperature is above 25
print("\nCities hotter than 25 degrees: ")
print(df[df["Temperature"] > 25])