
import sqlite3

conn = sqlite3.connect(
    "project_3_database/books.db"
)

cursor = conn.cursor()

# Total records
cursor.execute("SELECT COUNT(*) FROM books")
total = cursor.fetchone()[0]

# Check duplicate titles
cursor.execute("""
    SELECT title, COUNT(*)
    FROM books
    GROUP BY title
    HAVING COUNT(*) > 1
""")
duplicates = cursor.fetchall()

# Check missing required values
cursor.execute("""
    SELECT COUNT(*)
    FROM books
    WHERE title IS NULL
       OR price IS NULL
       OR availability IS NULL
       OR rating IS NULL
""")
missing = cursor.fetchone()[0]

# Display sample records
cursor.execute("""
    SELECT title, price, availability, rating
    FROM books
    LIMIT 5
""")
sample_records = cursor.fetchall()

print("DATABASE VERIFICATION REPORT")
print("Total records:", total)
print("Duplicate titles:", len(duplicates))
print("Records with missing values:", missing)

print("\nSample records:")
for record in sample_records:
    print(record)

print("\nVerification:",
      "PASSED" if total == 999 and len(duplicates) == 0 and missing == 0 else "FAILED")

conn.close()
