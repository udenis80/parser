from bs4 import BeautifulSoup
import requests
import lxml

url = "https://www.kinopoisk.ru/lists/movies/top250/"
r = requests.get(url)
soup=BeautifulSoup(r.text, 'lxml')
print(soup)
