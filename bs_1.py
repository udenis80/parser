import requests
from bs4 import BeautifulSoup

url = 'https://profreshenie.net/catalog/manikyur/stolyi/nedorogie-stolyi/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.find('div', class_="title"))

