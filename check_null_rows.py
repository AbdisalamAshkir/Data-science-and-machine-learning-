
import pandas as pd

file_path = r"C:\Users\Ashkir\Documents\students data\clean data\full data\unique\student_data_2023_cleaned.xlsx"

df = pd.read_excel(file_path)

print("=" * 50)
print("STUDENT DATA QUALITY CHECK")
print("=" * 50)

# 1. Check total rows and columns
print(f"\nTotal rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")

# 2. Check null / missing values
print("\n--- NULL VALUES PER COLUMN ---")
print(df.isnull().sum())

null_rows = df[df.isnull().any(axis=1)]

print(f"\nRows containing null values: {len(null_rows)}")

# 3. Check completely empty rows
empty_rows = df.isnull().all(axis=1)

print(f"Completely empty rows: {empty_rows.sum()}")

# 4. Check rows where every cell is empty or whitespace
text_df = df.astype("string").apply(lambda col: col.str.strip())
blank_rows = text_df.isna() | text_df.eq("")
blank_row_mask = blank_rows.all(axis=1)

print(f"Completely blank rows: {blank_row_mask.sum()}")

# 5. Check zero values in numeric columns
print("\n--- ZERO VALUES PER COLUMN ---")

numeric_df = df.select_dtypes(include="number")
print((numeric_df == 0).sum())

# 6. Display rows with null values
if not null_rows.empty:
    print("\n--- ROWS CONTAINING NULL VALUES ---")
    print(null_rows.to_string(index=True))
else:
    print("\nNo null values found.")

# 7. Save rows needing review
output_path = r"C:\Users\Ashkir\Documents\students data\clean data\full data\unique\student_data_quality_issues.xlsx"

with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    null_rows.to_excel(writer, sheet_name="Null_Rows", index=False)
    df.loc[blank_row_mask].to_excel(
        writer, sheet_name="Blank_Rows", index=False
    )
    (numeric_df == 0).sum().rename("ZeroCount").to_frame().to_excel(
        writer, sheet_name="Zero_Counts"
    )

print(f"\nQuality report saved to:\n{output_path}")
