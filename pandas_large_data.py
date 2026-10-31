import pandas as pd



# Read the CSV file
df=pd.read_csv('employees_150_rows.csv')


# print first 10
print('\n --- First 10 Employees ---')
print(df.head(10))


# Count all employee records
print("\n--- Total Employees ---")
print(len(df))


# Display the column names
print("\n--- Column Names ---")
print(df.columns)

# calculate salary average 
print('\n calculte average of salary....')
print(df['salary'].mean())



# Find employees earning more than 1000
print("\n--- Employees Earning More Than 1000 ---")
print(df[df["salary"] > 1000])


# Count employees in each department
print("\n--- Employees Per Department ---")
print(df["department"].value_counts())



# Sort employees by salary, highest first
print("\n--- Top 10 Salaries ---")
print(df.sort_values(by="salary", ascending=False).head(10))

print(df)