
import pandas as pd
import matplotlib.pyplot as plt

# Load the employee dataset
df = pd.read_csv("employees_150_rows.csv")

# Calculate average salary for each department
average_salary = df.groupby("department")["salary"].mean()

# Create a bar chart
average_salary.plot(kind="bar")

# Add chart labels and title
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=45)

# Adjust layout and display chart
plt.tight_layout()
plt.show()
