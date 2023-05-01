from bs4 import BeautifulSoup
import requests
import lxml
data = []
url = "https://www.kinopoisk.ru/lists/movies/top250/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
# for film in range:
print(soup.find('div', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj'))
print(soup.find('a', class_='base-movie-main-info_link__YwtP1'))
