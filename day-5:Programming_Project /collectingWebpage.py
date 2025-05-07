import requests
response = requests.get("https://www.w3schools.com/python/trypython.asp?filename=demo_dictionary_add")
html = response.text

print(html)