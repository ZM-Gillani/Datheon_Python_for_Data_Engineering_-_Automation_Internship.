# Python Data Engineering Pipeline
An end-to-end Python Data Engineering project that collects data from a website, cleans and transforms it using Pandas, and stores it in an SQLite database.
The project combines three stages into one automated pipeline.

## Project Overview
### 1. Web Scraping and Data Extraction
- Extracts book information from Books to Scrape.
- Uses Python Requests and BeautifulSoup.
- Implements pagination to collect data from multiple pages.
- Includes User-Agent headers, retry mechanism, and exception handling.
- Exports collected data into CSV and JSON files.
- Collects 1,000 book records.

### 2. Data Cleaning and Transformation
- Uses Pandas for data processing.
- Handles missing and invalid values.
- Converts book prices into numeric values.
- Transforms rating values into integers.
- Removes duplicate records.
- Validates the final data schema.
- Generates a data quality report.
- Produces 999 cleaned records.

### 3. Database Ingestion and Verification
- Uses SQLite for database storage.
- Creates a structured books table.
- Implements UPSERT to insert new records and update existing records.
- Uses batch insertion and transaction handling.
- Verifies record counts, duplicate titles, and missing values.
- Stores 999 records successfully.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas
- SQLite
- SQL
- CSV and JSON
- Git and GitHub

## Project Structure
```text
datheon-data-engineering/
│
├── project_1_web_scraper/
│   ├── scraper.py
│   ├── books_data.csv
│   └── books_data.json
│
├── project_2_data_cleaning/
│   ├── clean_data.py
│   ├── cleaned_books.csv
│   └── quality_report.txt
│
├── project_3_database/
│   ├── ingest_data.py
│   ├── verify_database.py
│   └── books.db
│
├── run_pipeline.py
├── requirements.txt
└── .gitignore
```

## Installation and Setup
1. Clone this repository:
```bash
git clone https://github.com/ZM-Gillani/datheon-data-engineering.git
```
2. Navigate to the project folder:
```bash
cd datheon-data-engineering
```
3. Create and activate a virtual environment:
```bash
python -m venv .venv
```
Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```
4. Install the required dependencies:
```bash
pip install -r requirements.txt
```
## Run the Complete Pipeline
Run the following command from the main project directory:
```bash
python run_pipeline.py
```

This command automatically executes:
1. Web scraping
2. Data cleaning and transformation
3. Database ingestion
4. Database verification

## Final Results
| Metric | Result |
|---|---:|
| Scraped records | 1,000 |
| Cleaned records | 999 |
| Duplicates removed | 1 |
| Database records | 999 |
| Missing values after cleaning | 0 |
| Database verification | PASSED |

## Learning Outcomes
Through this project, I practiced:
- Web scraping and pagination
- Data cleaning and transformation
- Data validation and quality reporting
- Relational database operations
- SQL UPSERT operations
- Automated pipeline execution
- Git and GitHub project management

## Data Source
[Books to Scrape](https://books.toscrape.com/) — a practice website for web scraping.
