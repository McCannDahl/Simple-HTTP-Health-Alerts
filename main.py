import requests
import time
import beepy as beep
from config import urls, interval

def check_urls():
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            print(f'{url} is up')
        except requests.RequestException as e:
            print(f'Error accessing {url}: {e}')
            return False
    return True

while True:
    if not check_urls():
        beep.beep('error')
    print('--------------')
    time.sleep(interval * 60)  # Convert minutes to seconds
