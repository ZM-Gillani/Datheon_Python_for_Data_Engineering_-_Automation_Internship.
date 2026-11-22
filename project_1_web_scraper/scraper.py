import requests
import json
import csv
import logging

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Logging setup
logging.basicConfig(
    filename="scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
base_url = "https://books.toscrape.com/"
current_url = base_url

headers = {
    "User-Agent": "Mozilla/5.0"
}
# Retry configuration
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)

session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)
session.headers.update(headers)
all_books = []
# Scraping with pagination
while current_url:
    print("Scraping:", current_url)
    try:
        response = session.get(current_url, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print("Request failed:", error)
        logging.error("Request failed: %s", error)
        break
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.h3.a["title"]
        price = book.find(
            "p", class_="price_color"
        ).get_text(strip=True)
        availability = book.find(
            "p", class_="instock availability"
        ).get_text(strip=True)
        rating = book.find(
            "p", class_="star-rating"
        )["class"][1]
        book_data = {
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating
        }
        all_books.append(book_data)
    logging.info(
        "Collected %s books from %s",
        len(books),
        current_url
    )
    next_button = soup.find("li", class_="next")
    if next_button:
        next_page = next_button.a["href"]
        current_url = urljoin(current_url, next_page)
    else:
        current_url = None
# Data validation
required_fields = ["title", "price", "availability", "rating"]
missing_records = []
for book in all_books:
    if any(not book.get(field) for field in required_fields):
        missing_records.append(book)
unique_titles = set(book["title"] for book in all_books)
duplicate_count = len(all_books) - len(unique_titles)

print("\nScraping completed!")
print("Total books collected:", len(all_books))
print("Records with missing fields:", len(missing_records))
print("Duplicate records:", duplicate_count)

logging.info("Total records: %s", len(all_books))
logging.info("Missing records: %s", len(missing_records))
logging.info("Duplicate records: %s", duplicate_count)
# Save JSON
with open("books_data.json", "w", encoding="utf-8") as file:
    json.dump(all_books, file, indent=4, ensure_ascii=False)
# Save CSV
with open("books_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=required_fields
    )
    writer.writeheader()
    writer.writerows(all_books)
print("JSON and CSV files created successfully!")
logging.info("JSON and CSV export completed.")