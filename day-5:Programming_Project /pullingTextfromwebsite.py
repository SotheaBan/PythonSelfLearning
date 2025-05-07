import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/Telephone_numbers_in_Cambodia#Network_operators")
html = response.text

soup = BeautifulSoup(html, "html.parser")


title = soup.title.text
text = soup.get_text()

print(title)
print(text)
