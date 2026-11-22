# datheon-data-engineering
# Python Data Engineering & Automation Projects
This repository contains Python projects developed as part of the Datheon Python for Data Engineering & Automation Internship.
## Project 1: Web Scraper & Data Extractor
# Description
A Python web scraper that extracts book information from Books to Scrape using Requests and BeautifulSoup.
### Features
- Scrapes paginated web pages.
- Extracts book titles, prices, availability, and ratings.
- Uses request headers and retry handling.
- Handles request errors and logs scraping activity.
- Exports collected data into CSV and JSON files.
# Dataset
- Total records collected: 1,000
- Output: books_data.csv and books_data.json
# Technologies
Python, Requests, BeautifulSoup, CSV, JSON, Logging

# Project 2: Data Cleaning & Schema Transformation
# Description
A Pandas-based data cleaning pipeline that transforms the scraped book dataset into a clean and structured dataset.
# Features
- Handles missing values.
- Removes duplicate book records.
- Cleans and converts price values into numeric format.
- Converts rating values into integers.
- Validates the final dataset schema.
- Generates an automated data quality report.
# Results
- Original records: 1,000
- Final records: 999
- Duplicate records removed: 1
- Missing values after cleaning: 0
- Schema validation: PASSED
# Technologies
Python, Pandas, CSV
## How to Run
Install the required libraries:
```bash
pip install requests beautifulsoup4 pandas
```
Run Project 1:
```bash
python project_1_web_scraper/scraper.py
```

Run Project 2:
```bash
python project_2_data_cleaning/clean_data.py
```
## Author
Python for Data Engineering & Automation Internship
