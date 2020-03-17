import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"

webpage = requests.get(url)

soup = BeautifulSoup(webpage.text, 'html.parser')

table_body = soup.find('tbody')

rows = table_body.find_all('tr')

UK = []

for row in rows:
    cols = row.find_all('td')
    cols = [x.text.strip() for x in cols]
    if cols[0] == 'UK':
        UK = cols

print(UK)
