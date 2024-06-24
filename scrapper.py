import requests
from bs4 import BeautifulSoup as bs


def scrap(url : str) -> bs:
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Error {response.status_code} while trying to fetch data : {response.text}")

    # soup_data = text_to_soup(response.text)

    # return soup_data
    
    return response.text

def text_to_soup(text : str) -> bs:
    return bs(text, 'html.parser')

