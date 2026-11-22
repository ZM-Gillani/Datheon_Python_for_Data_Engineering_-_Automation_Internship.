import pandas as pd
df = pd.read_csv("project_1_web_scraper/books_data.csv")
print("Original records:", len(df))
# Check missing values
missing_before = df.isna().sum().sum()

# Replace empty spaces with missing values
df = df.replace(r"^\s*$", pd.NA, regex=True)

# Clean title
df["title"] = df["title"].str.strip()

# Clean price and convert it into numeric
df["price"] = (
    df["price"]
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip()
)
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Clean availability
df["availability"] = df["availability"].str.strip()

# Convert rating words into numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["rating"] = df["rating"].str.strip().map(rating_map)

# Remove records with missing required values
df = df.dropna(
    subset=["title", "price", "availability", "rating"]
)
# Remove duplicate books
before_duplicates = len(df)
df = df.drop_duplicates(subset=["title"])
duplicates_removed = before_duplicates - len(df)

# Convert rating into integer
df["rating"] = df["rating"].astype(int)

# Save cleaned dataset
df.to_csv(
    "project_2_data_cleaning/cleaned_books.csv",
    index=False
)
# Generate quality report
missing_after = df.isna().sum().sum()

report = f"""
DATA CLEANING QUALITY REPORT

Original records: {1000}
Final records: {len(df)}
Duplicates removed: {duplicates_removed}
Missing values before cleaning: {missing_before}
Missing values after cleaning: {missing_after}

Final columns and data types:
{df.dtypes}

Schema validation:
{"PASSED" if list(df.columns) == ["title", "price", "availability", "rating"] and df["price"].notna().all() and df["rating"].notna().all() else "FAILED"}
"""
with open(
    "project_2_data_cleaning/quality_report.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(report)
print(report)
print("Cleaned CSV and quality report created successfully!")
