import pandas as pd

# Create a small table of data
data = {
    "Name": ["Euan", "Anna", "Ben", "Sarah", "Toby"],
    "Score": [85, 92, 78, 88, 95],
    "Passed": [True, True, False, True, True]
}

# Turn it into a Pandas DataFrame (a spreadsheet)
df = pd.DataFrame(data)

# Print the whole table
print(df)

# Print the average score
print("\nAverage score: ", df["Score"].mean())

# Print only the students who passed
print("\nStudents who passed: ")
print(df[df["Passed"] == True])