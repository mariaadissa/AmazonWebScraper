# used libraries
import requests
import time
import datetime
import csv
from bs4 import BeautifulSoup
# for sending emails
import smtplib

def check_price():
    URL = 'https://www.amazon.com/Currently-Unsupervised-Novelty-Graphic-Sarcasm/dp/B01HFFYP8A/ref=sr_1_15?dchild=1&keywords=data%2Btshirt&qid=1633430723&sr=8-15&th=1&psc=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers = headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

    title = soup2.find(id='productTitle').get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()

    price = price.strip()[1:] 
    title = title.strip()
    today = datetime.date.today()
    header = ['Title', 'Price','Date']
    data = [title, price,today]
    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    

# Creating the csv file for the first time
URL = 'https://www.amazon.com/Currently-Unsupervised-Novelty-Graphic-Sarcasm/dp/B01HFFYP8A/ref=sr_1_15?dchild=1&keywords=data%2Btshirt&qid=1633430723&sr=8-15&th=1&psc=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
page = requests.get(URL, headers = headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(),"html.parser")
title = soup2.find(id='productTitle').get_text()
price = soup2.find(id="priceblock_ourprice").get_text()
price = price.strip()[1:] 
title = title.strip()
today = datetime.date.today()
header = ['Title', 'Price','Date']
data = [title, price,today]
with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)  

# repeating the process each day
while(True):
    check_price()
    time.sleep(86400) #checking the price everyday

# sending email function
def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('myemail@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Maria, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Currently-Unsupervised-Novelty-Graphic-Sarcasm/dp/B01HFFYP8A/ref=sr_1_15?dchild=1&keywords=data%2Btshirt&qid=1633430723&sr=8-15&th=1&psc=1"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'myemail@gmail.com',
        msg
    )