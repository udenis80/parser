import requests
from bs4 import BeautifulSoup
import fake_useragent

session = requests.Session()

link = 'https://dbdesign.online/login'
user = fake_useragent.UserAgent().random

header = {'user-agent': user}
data = {
    '_token': 'iVaYaRqHIkljYeQ5WCN4T0ncAC6NDdbiGFOI2mY3',
    'email': 'udenis80@mail.ru',
    'password': 'orbit123'
}
responce = session.post(link, data=data, headers=header)

model = 'https://dbdesign.online/user-profile?page=profile'

model_responce = session.get(model, headers=header).text
print(model_responce)
