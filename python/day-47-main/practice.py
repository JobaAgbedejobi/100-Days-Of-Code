from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
from pprint import pprint

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
              "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", "
                 "\"Google Chrome\";v=\"138\"",
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
URL = "https://appbrewery.github.io/instant_pot/"
url = requests.get(URL, headers=headers)
soup = BeautifulSoup(url.text,"html.parser" )
# pprint(soup)

# # THIS WORKS BUT NOT IN THE FORMAT THEY WANT
# price_whole = soup.find(name="span", class_ = "a-price-whole").getText()
# price_fraction = soup.find(name="span", class_ = "a-price-fraction").getText()
# print(price_whole+price_fraction)

price = soup.find(class_ = "a-price aok-align-center reinventPricePriceToPayMargin "
                           "priceToPay").getText().split('$')[1]
price_as_float = float(price)

title_of_product = soup.find(name="span", id="productTitle").getText().split()
product_title = " ".join(title_of_product)

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
email = os.getenv("EMAIL")

BUY_PRICE = 100 # FOR THIS EXAMPLE
if price_as_float < BUY_PRICE:
    message = f"{product_title} is now on sale at ${price}!"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(username, password)
        connection.sendmail(from_addr=username, to_addrs=email,
            msg=f"Subject: Amazon Price Alert! \n\n{message} \n{URL}".encode("utf-8"))