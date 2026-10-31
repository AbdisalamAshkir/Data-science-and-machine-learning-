
# Import Pandas
import pandas as pd

# Create sample employee data
# Notice that one salary is missing and Ahmed appears twice
data = {
    "name": ["Ahmed", "Ali", "Ashkir", "Fatima", "Ahmed"],
    "age": [30, 25, 40, 22, 30],
    "salary": [500, 400, 800, None, 500]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# 1. Display the original data
print("\n--- Original Data ---")
print(df)

# 2. Sort by salary from highest to lowest
# ascending=False means descending order
print("\n--- Sorted by Salary (Highest First) ---") 
print(df.sort_values(by="salary", ascending=False))

# 3. Check for missing values in each column
# True means the value is missing
print("\n--- Missing Values ---")
print(df.isnull())

# 4. Count missing values in each column
print("\n--- Missing Value Counts ---")
print(df.isnull().sum())

# 5. Remove rows containing missing values
# This creates a cleaned DataFrame without changing df
clean_df = df.dropna()
print("\n--- Data Without Missing Values ---")
print(clean_df)

# 6. Remove duplicate rows
# Keep the first occurrence of identical rows
unique_df = df.drop_duplicates()
print("\n--- Data Without Duplicate Rows ---")
print(unique_df)
