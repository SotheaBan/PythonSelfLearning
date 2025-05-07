import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.w3schools.com/python/trypython.asp?filename=demo_dictionary_add")
html = response.text

soup = BeautifulSoup(html, "html.parser")


print("Button:", soup.p.text)
