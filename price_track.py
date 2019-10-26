import requests
from bs4 import BeautifulSoup
from priceChecker import getEtsyPrice, getNordstromPrice
import smtplib



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
    etsyPrices = getEtsyPrice(query)
    prices = etsyPrices["prices"]
    for key in prices:
        if prices[key] <threshhold:
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
    message = f"Subject:{subject}\n\n{body} "
    server.sendmail("wearelse.noreply@gmail.com", email, message)
    print("bye")
    server.quit()
    pass

query = "Air Jordan"
threshhold = 100
check_all(query, threshhold, "sazad2@illinois.edu")