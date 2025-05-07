import requests
from bs4 import BeautifulSoup
import csv

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

# Open CSV file for writing
with open("quotes.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])  # header row

    for q in quotes:
        text = q.find("span", class_="text").text.strip().replace("“", "").replace("”", "")
        author = q.find("small", class_="author").text.strip()
        tags = [tag.text for tag in q.find_all("a", class_="tag")]
        
        writer.writerow([text, author, ", ".join(tags)])
