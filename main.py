import requests
import smtplib
from bs4 import BeautifulSoup

def send_mail(tableData):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('email', 'password')
    subject = f"Coronavirus Cases in {tableData[0]} today"
    body = f"Today in: {tableData[0]}\nTotal Cases: {tableData[1]}\nNew Cases: {tableData[2]} \
           '\nTotal Deaths: {tableData[3]}\nNew Deaths: {tableData[4]}\nRecovered: + {tableData[5]}\
           '\nActive Cases: {tableData[6]}\nCheck the link: https://www.worldometers.info/coronavirus"
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail('Coronavirus', 'emailtosendto', message)
    print(body)

    print("Email has been sent!")
    server.quit()



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

send_mail(list(UK))


