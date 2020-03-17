import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"

webpage = requests.get(url)

soup = BeautifulSoup(webpage.text, 'html.parser')

