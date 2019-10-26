import requests
from bs4 import BeautifulSoup
from priceChecker import getEtsyPrice, getNordstromPrice
import smtplib
import json


url = "https://www.amazon.com/Apple-MacBook-Retina-2-8GHz-Quad-core/dp/B07SKPVDFF/ref=sr_1_1_sspa?keywords=mac&qid=1572122606&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQkNBMklFSDJFNFFQJmVuY3J5cHRlZElkPUEwNjM0MzIzSlYzWlI5SEVXVzZXJmVuY3J5cHRlZEFkSWQ9QTA3NjYwMzBGNFo4RE5XTzRNS04md2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

def compare(url, price, email):
    headers = {"User-Agents": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    soup.prettify()
#     soup.find(id="productTitle").get_text().strip()
    cur = soup.findAll("span", {"class": "_3p7kp"})[0]
    print(cur)
    cur = float(cur.get_text()[1:].replace(",",""))
    if cur <price:
        send_email(email, url)

def check_all(threshhold, query, email):
    valid_links = []
    etsyPrices = json.loads(getEtsyPrice(query))
    nordstromPrices = json.loads(getNordstromPrice(query))
    prices = etsyPrices["prices"] 
    for key in prices:
        val = int(float(prices[key]))
        if val <threshhold:
            valid_links.append(key)
    prices = nordstromPrices["prices"]       
    for key in prices:
        val = int(float(prices[key]))
        if val <threshhold:
            valid_links.append(key)
    if len(valid_links)>=1:
        send_email(email, valid_links)
        return True
    else:
        return False

def send_email(email, urls):
    print("hi")
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('wearelse.noreply@gmail.com', 'rakgfgkhljkajwak')
    subject = 'The price of your item has fallen!'
    body = "Hi! \n" 
    for u in urls:
        body+= u+"\n"
    body += "With best regards,\n"
    body += "WearElse team\n"

    message = f"Subject:{subject}\n\n{body} "
    
    # print(message)
    server.sendmail("wearelse.noreply@gmail.com", email, message)
    print("bye")
    server.quit()
    pass

# query = "Air Jordan"
# threshhold = 150

# print(check_all(threshhold, query, "sazad2@illinois.edu"))
import time
while True:
    
    f= open("price_track_database.txt")
    new_file = []
    
    
    for line in f:
        print(line)
        items = line.split(";")
        email = items[0]
        query = items[1]
        threshhold = float(items[2].replace("\n",""))
        if check_all( threshhold, query, email)!= True:
            new_file.append(line)
        
    f.close()
    
    
    new_file = list(filter(None, new_file))
    result = "".join(new_file)
    
    f = open("price_track_database.txt", 'w')
    f.write(result)
    f.close()
    
    time.sleep(12*3600)


