
# Import the Pandas library and give it the short name "pd"
import pandas as pd

# Create a dictionary containing names, ages, and salaries
# Each key becomes a column, and each list contains the column values
data = {
    "name": ["Ahmed", "Ali", "Ashkir", "Fatima", "Mohamed"],
    "age": [30, 25, 40, 22, 35],
    "salary": [500, 400, 800, 350, 650]
}

# Convert the dictionary into a Pandas DataFrame (a table)
# Store the table in a variable called df
df = pd.DataFrame(data)

# Display all the data in the table
# \n adds a blank line before the heading
print("\n--- All Data ---")
print(df)

# Select and display only the name column
# df["name"] returns the values in the name column
print("\n--- Names Only ---")
print(df["name"])

# Filter the table to show people older than 30
# df["age"] > 30 checks which ages are greater than 30
# df[...] returns only the rows that satisfy this condition
print("\n--- People Older Than 30 ---")
print(df[df["age"] > 30])

# Calculate the average salary
# .mean() adds the salary values and divides by the number of people
print("\n--- Average Salary ---")
print(df["salary"].mean())

# Calculate the total salary
# .sum() adds all the salary values together
print("\n--- Total Salary ---")
print(df["salary"].sum())



print('\n show people lest then 30 years.......')
print(df[df["age"]<30])
