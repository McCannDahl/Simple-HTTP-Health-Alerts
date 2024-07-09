import requests
import time
import beepy as beep
from config import urls, interval

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

def check_urls():
    for url in urls:
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()  # Raise an exception for HTTP errors
            prGreen(f'{url} is up')
        except requests.RequestException as e:
            prRed(f'Error accessing {url}: {e}')
            return False
    return True

while True:
    if not check_urls():
        beep.beep('error')
    print('--------------')
    time.sleep(interval * 60)  # Convert minutes to seconds
