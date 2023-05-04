import requests
from bs4 import BeautifulSoup
import fake_useragent
user = fake_useragent.UserAgent().random
header = {'user-agent': user}

link = 'https://browser-info.ru/'
responce = requests.get(link, headers=header).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id='tool_padding')

# check js
check_js = block.find('div', id='javascript_check')
value_js = check_js.find_all('span')[1].text
result_js = f'value_js: {value_js}'
print(result_js)

# check flash
check_flash = block.find('div', id='flash_version')
status_flash = check_flash.find_all('span')[1].text
result_flash = f'flash: {status_flash}'
print(result_flash)

# check user-agent
check_user = block.find('div', id='user_agent').text
result_user = f'user-agent: {check_user}'
print(check_user)



