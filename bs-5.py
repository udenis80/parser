import requests
import multiprocessing



def handler(proxy):
    link = 'http://icanhazip.com/'

    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    try:
        responce = requests.get(link, proxies=proxies, timeout=2).text
        print(f'IP: {responce.strip()}')
    except:
        print('Прокси не вадный')


with open('proxy') as file:
    proxy_base = ''.join(file.readlines()).strip().split('\n')

with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
    if __name__ == '__main__':
        process.map(handler, proxy_base)

