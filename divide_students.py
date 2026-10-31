from pathlib import Path
import pandas as pd

# Original cleaned Excel file
INPUT_FILE = Path(
    r"C:\Users\Ashkir\Documents\students data\clean data\full data\unique\student_data_2023_cleaned.xlsx"
)

OUTPUT_FOLDER = INPUT_FILE.parent / "students_divided_10_documents"

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Excel file not found: {INPUT_FILE}\n"
        "Update INPUT_FILE to your actual cleaned Excel filename."
    )

df = pd.read_excel(INPUT_FILE)

# Set graduation year to 2023
year_columns = {
    "".join(c.lower() for c in str(col) if c.isalnum()): col
    for col in df.columns
}

year_column = next(
    (year_columns[name] for name in
     ["graduationyear", "yearofgraduation", "year"]
     if name in year_columns),
    None
)

if year_column:
    df[year_column] = 2023
else:
    df["graduationYear"] = 2023

if len(df) < 100:
    raise ValueError(
        f"Only {len(df)} students found. "
        "There must be at least 100 for the first document."
    )

# Create output directory
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# First document: exactly 100 students
df.iloc[:100].to_excel(
    OUTPUT_FOLDER / "students_document_01.xlsx",
    index=False
)

# Split all remaining students among documents 2–10
remaining = df.iloc[100:]
base_size, extra = divmod(len(remaining), 9)
start = 0

for i in range(9):
    size = base_size + (1 if i < extra else 0)
    part = remaining.iloc[start:start + size]

    filename = OUTPUT_FOLDER / f"students_document_{i + 2:02d}.xlsx"
    part.to_excel(filename, index=False)

    print(f"{filename.name}: {len(part)} students")
    start += size

print("\n========== COMPLETE ==========")
print(f"Total students: {len(df)}")
print(f"Document 1: 100 students")
print(f"Remaining students: {len(remaining)}")
print(f"Total documents: 10")
print(f"Saved to: {OUTPUT_FOLDER}")
