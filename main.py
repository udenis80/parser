import requests
import json
from bs4 import BeautifulSoup

sp = 'https://browser-info.ru/'

def get_js(sp):
    block = sp.find('div', id='tool_padding')
    print(block.find('div', id='javascript_check').find_all('span')[1].text)

def get_cookie(sp):
    block = sp.find('div', id='tool_padding')
    print(block.find('div', id='cookie_check').find_all('span')[1].text)

def get_flash(sp):
    block = sp.find('div', id='tool_padding')
    print(block.find('div', id='flash_version').find_all('span')[1].text)

def main():
    with open('config.json') as file:
        config = json.load(file)
    responce = requests.get(sp)
    soup = BeautifulSoup(responce.text, 'lxml')

    if config['js']: get_js(soup)
    if config['cookie']: get_cookie(soup)
    if config['flash']: get_flash(soup)




if __name__ == '__main_':
    main()


