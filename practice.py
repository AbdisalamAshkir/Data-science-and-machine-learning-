import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('employees_150_rows.csv')


plt.figure(figsize=(8,8))

department_count=df["department"].value_counts()

plt.pie(
department_count,
labels=department_count.index,
autopct="%1.1f%%",
startangle=90
)

plt.title('percentage of employee departments ')

plt.axis("equal")


plt.show()
