import requests
from bs4 import BeautifulSoup
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
def send_email(email, url):
    print("hi")
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('wearelse.noreply@gmail.com', 'rakgfgkhljkajwak')
    subject = 'price fell'
    body = "hi \n" + url
    message = f"Subject:{subject}\n\n{body} "
    server.sendmail("wearelse.noreply@gmail.com", email, message)
    print("bye")
    server.quit()
    pass

compare(urll, 150, "sazad2@illinois.edu")