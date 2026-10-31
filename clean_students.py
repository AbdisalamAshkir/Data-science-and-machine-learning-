
from pathlib import Path
import pandas as pd

# Your actual Excel file
FILE_PATH = Path(
    r"C:\Users\Ashkir\Documents\students data\clean data\full data\unique\student_data_2023_unique_students.xlsx"
)

# Graduation year for every student
GRADUATION_YEAR = 2023

# Check the file
if not FILE_PATH.exists():
    raise FileNotFoundError(f"File not found: {FILE_PATH}")

# Load Excel data
df = pd.read_excel(FILE_PATH)

print("\n========== STUDENT DATA ANALYSIS ==========")
print("Total records:", len(df))
print("\nColumns:")
print(df.columns.tolist())
print("\nMissing values:")
print(df.isna().sum().to_string())

# Normalize column names for matching
def normalize(name):
    return "".join(c.lower() for c in str(name) if c.isalnum())

columns = {normalize(c): c for c in df.columns}

# Find a student identifier, if available
id_candidates = [
    "studentid", "studentnumber", "studentno",
    "rollnumber", "rollno", "registrationnumber",
    "registrationno", "admissionnumber", "admissionno"
]

id_column = next(
    (columns[c] for c in id_candidates if c in columns),
    None
)

# Detect and remove duplicates
if id_column:
    ids = df[id_column].astype("string").str.strip()
    valid_ids = ids.notna() & ids.ne("")

    duplicate_mask = pd.Series(False, index=df.index)
    duplicate_mask.loc[valid_ids] = ids.loc[valid_ids].duplicated(
        keep="first"
    )

    print(f"\nDuplicate detection: {id_column}")
else:
    # Only remove rows that are identical in every column
    duplicate_mask = df.duplicated(keep="first")
    print("\nNo recognized student ID column.")
    print("Removing only completely identical rows.")

duplicates = df.loc[duplicate_mask].copy()
cleaned = df.loc[~duplicate_mask].copy()

print("Duplicate records found:", len(duplicates))

# Set graduation year to 2023
year_candidates = [
    "graduationyear", "yearofgraduation",
    "graduation_year", "year"
]

cleaned_columns = {normalize(c): c for c in cleaned.columns}

year_column = next(
    (cleaned_columns[normalize(c)]
     for c in year_candidates
     if normalize(c) in cleaned_columns),
    None
)

if year_column:
    cleaned[year_column] = GRADUATION_YEAR
else:
    year_column = "graduationYear"
    cleaned[year_column] = GRADUATION_YEAR

# Save results in the same folder as the original
output_file = FILE_PATH.with_name(
    "student_data_2023_cleaned.xlsx"
)

duplicates_file = FILE_PATH.with_name(
    "student_data_duplicates_review.xlsx"
)

report_file = FILE_PATH.with_name(
    "student_data_2023_analysis.txt"
)

cleaned.to_excel(output_file, index=False)
duplicates.to_excel(duplicates_file, index=False)

# Generate analysis report
with open(report_file, "w", encoding="utf-8") as f:
    f.write("STUDENT DATA ANALYSIS REPORT\n")
    f.write("=" * 35 + "\n")
    f.write(f"Original records: {len(df)}\n")
    f.write(f"Duplicates found: {len(duplicates)}\n")
    f.write(f"Final student records: {len(cleaned)}\n")
    f.write(f"Graduation year: {GRADUATION_YEAR}\n")
    f.write(f"Year column: {year_column}\n")
    f.write(f"Duplicate identifier: {id_column or 'Full-row match'}\n")
    f.write(f"Cleaned file: {output_file}\n")

print("\n========== COMPLETED ==========")
print("Original students:", len(df))
print("Duplicates removed:", len(duplicates))
print("Final students:", len(cleaned))
print("Graduation year:", GRADUATION_YEAR)
print("\nCleaned Excel:", output_file)
print("Duplicates for review:", duplicates_file)
print("Analysis report:", report_file)
