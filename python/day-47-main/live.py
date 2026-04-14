from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
from pprint import pprint

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/"
              "webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome"
                 "\";v=\"138\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 "
                  "Safari/537.36",
}
URL = ("https://www.amazon.co.uk/Apple-iPhone-16e-128GB-Intelligence/dp/B0DXR93G9D/"
       "ref=sr_1_4?crid=2SK70AE192XPA&dib=eyJ2IjoiMSJ9.0bwFbTiSb1PHr5RtKTtqF6JCJ"
       "ROvuiyD_Kvn2puOSuJPhhDRZ4GMg-1FlxntKfxjEeBR939DwwwksdRUEr3pGzNLsDaTUJSEq5R0Dg"
       "-3Nujxr1ep-GD-R1T2mdJLgRXVZOFiWPGRrX-Dfa30OTt2HNfBsY1XLY3Av8895jR8Y8hwHKl0xNG"
       "ItvsuBxhixDLHxxSs_-mJ_YA2w1yAFGJpErC7QYxdMwI503OMuT7htrE.gh4y7SqGnIWzU1BiOdDk"
       "0gHCXEVKzC2gmuitxzMunvg&dib_tag=se&keywords=iphone%2B16e&qid=1755703693&"
       "sprefix=iphone%2B16e%2Caps%2C314&sr=8-4&th=1")
url = requests.get(URL, headers=headers)
soup = BeautifulSoup(url.text,"html.parser" )

price = soup.find(class_="a-price aok-align-center reinventPricePriceToPayMargin "
                         "priceToPay").getText().strip().strip("£")
price_as_float = float(price)

title_of_product = soup.find(name="span", id="productTitle").getText().strip()
product_title = title_of_product.split(":")[0]

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
email = os.getenv("EMAIL")

BUY_PRICE = 550
if price_as_float < BUY_PRICE:
    message = f"{product_title} is now on sale at £{price}!"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(username, password)
        connection.sendmail(from_addr=username, to_addrs=email,
            msg=f"Subject: Amazon Price Alert! \n\n{message} \n{URL}".encode("utf-8"))