
import sqlite3
import pandas as pd

# Read cleaned CSV
df = pd.read_csv(
    "project_2_data_cleaning/cleaned_books.csv"
)

# Connect to SQLite database
conn = sqlite3.connect(
    "project_3_database/books.db"
)

cursor = conn.cursor()

# Create books table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT UNIQUE NOT NULL,
        price REAL NOT NULL,
        availability TEXT,
        rating INTEGER
    )
""")

print("Database connected successfully!")
print("Books table created successfully!")



# Prepare SQL query
query = """
    INSERT INTO books (title, price, availability, rating)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(title) DO UPDATE SET
        price = excluded.price,
        availability = excluded.availability,
        rating = excluded.rating
"""

# Convert DataFrame into records
records = df[
    ["title", "price", "availability", "rating"]
].to_records(index=False).tolist()

# Insert or update records
with conn:
    cursor.executemany(query, records)

print("Data inserted or updated successfully!")

# Verify database records
cursor.execute("SELECT COUNT(*) FROM books")
total_books = cursor.fetchone()[0]

print("Total books in database:", total_books)

conn.close()
print("Database connection closed.")
