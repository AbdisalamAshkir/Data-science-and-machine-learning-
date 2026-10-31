
import pandas as pd
import matplotlib.pyplot as plt

# Load employee data
df = pd.read_csv("employees_150_rows.csv")

# Count employees in each department
department_counts = df["department"].value_counts()

# Create the pie chart
plt.figure(figsize=(8, 8))

plt.pie(
    department_counts,
    labels=department_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

# Add a title
plt.title("Percentage of Employees by Department")

# Keep the pie chart circular
plt.axis("equal")

# Display the chart
plt.show()
