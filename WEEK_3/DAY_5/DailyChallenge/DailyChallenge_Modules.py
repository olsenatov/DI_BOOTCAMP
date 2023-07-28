import requests
import time

def get_page_load_timer(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        response.raise_for_status()
        
        end_time = time.time()
        load_time = end_time - start_time
        return load_time
    
    except requests.exceptions.RequestException as err:
        print(f"Error occurred while fetching {url}:{err}")
        return None
    
wpages = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]  #for imdb.com there's error 403 - demonstrates not fetching

for wpage in wpages:
    load_time = get_page_load_timer(wpage)
    if load_time is not None:
        print(f"Load time for {wpage} is : {load_time} seconds")