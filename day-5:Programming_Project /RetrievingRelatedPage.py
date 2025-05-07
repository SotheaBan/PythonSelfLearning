import requests
from bs4 import BeautifulSoup
import csv

base_url = "http://quotes.toscrape.com"
next_page = "/page/1/"

# Open CSV file for writing
with open("all_quotes.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Qu", "Author", "Tags"])  # CSV header

    while next_page:
        response = requests.get(base_url + next_page)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        for q in quotes:
            text = q.find("span", class_="text").text.strip().replace("“", "").replace("”", "")
            author = q.find("small", class_="author").text.strip()
            tags = [tag.text for tag in q.find_all("a", class_="tag")]
            writer.writerow([text, author, ", ".join(tags)])

        # Check if there's a next page
        next_btn = soup.find("li", class_="next")
        next_page = next_btn.a["href"] if next_btn else None
