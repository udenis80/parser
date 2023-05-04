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

profile_info = 'https://dbdesign.online/user-profile?page=profile'

profile_responce = session.get(profile_info, headers=header).text

cookies_dict = [
    {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
    for key in session.cookies
]
session2 = requests.Session()
for cookies in cookies_dict:
    session2.cookies.set(**cookies)

resp = session2.get(profile_info,headers=header)
print(resp.text)