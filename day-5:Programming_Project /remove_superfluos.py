import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

for q in quotes:
    text = q.find("span", class_="text").text.strip().replace("“", "").replace("”", "")
    author = q.find("small", class_="author").text.strip()
    print(f"{text} — {author}")
