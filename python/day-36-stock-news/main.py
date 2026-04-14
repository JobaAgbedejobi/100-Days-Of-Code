import requests
import datetime as dt
import smtplib
# # USING THIS TO HELP WITH ENCODED CHARACTERS SUCH AS EMOJIS AND NON-ENGLISH LETTERS
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# API KEY ONLY ALLOWS 25 REQUESTS PER DAY
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
# STOCK_API_KEY removed
# STOCK_API_KEY removed
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
TODAY = dt.date.today()
EMAIL = "os.environ.get("MY_EMAIL")"
USER = os.environ.get("MY_EMAIL")
#PASSWORD removed
PASSWORD = os.environ.get("EMAIL_PASSWORD")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY
}

news_params = {
    "q": COMPANY_NAME + "&",
    "from": f"{TODAY}&",
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": NEWS_API_KEY
}

stock_response = requests.get(url=STOCK_API_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

tsd = (stock_data["Time Series (Daily)"])
dates = list(tsd.keys())
properties = list(tsd[dates[0]].keys()) # Gets the property names for easier access

yday_price = float(tsd[dates[0]][properties[3]])
yday_2_price = float(tsd[dates[1]][properties[3]])

print(f"Yesterday's Price: {yday_price}")
print(f"Price 2 days ago: {yday_2_price}")

percentage_change = abs((yday_price-yday_2_price)/yday_price)*100
print(f"Percentage Change:{percentage_change:.2f}")
# if percentage_change >= 3:
    # print("Get News")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_response = requests.get(url=NEWS_API_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()
news = news_data["articles"][:3]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
message = ""
for article in news:
    headline = article["title"]
    brief = article["description"]
    message_text = f"headline: {headline}" + "\n" + f"brief: {brief}" + "\n\n"
    message += message_text

# Create the email message
msg = MIMEMultipart()
msg['From'] = USER
msg['To'] = EMAIL
msg['Subject'] = "TSLA Stock Alert"

# Create the body with emojis
if percentage_change > 0:
    arrow = "🔺"
else:
    arrow = "🔻"

body = f"TSLA: {arrow}{percentage_change:.2f}%\n\n{message}"
msg.attach(MIMEText(body, 'plain', 'utf-8'))

# Send the email
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=USER, password=PASSWORD)
    connection.sendmail(from_addr=USER, to_addrs=EMAIL, msg=msg.as_string())

print(message)

# # CBA TO SEND 3 SEPARATE EMAILS BUT IF I WERE TO DO IT:
# for i in range(len(news)):
#     headline = news[i]["title"]
#     brief = news[i]["description"]
#     message = f"Headline: {headline}" + "\n" + f"Brief: {brief}" + "\n\n"
#     msg = MIMEMultipart()
#     msg['From'] = USER
#     msg['To'] = EMAIL
#     msg['Subject'] = "TSLA Stock Alert"
#
#     if percentage_change > 0:
#         arrow = "🔺"
#     else:
#         arrow = "🔻"
#
#     body = f"TSLA: {arrow}{percentage_change:.2f}%\n\n{message}"
#     msg.attach(MIMEText(body, 'plain', 'utf-8'))
#
#     # Send the email
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=USER, password=PASSWORD)
#         connection.sendmail(from_addr=USER, to_addrs=EMAIL, msg=msg.as_string())

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2% 
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and 
prominent investors are required to file by the SEC The 13F filings show the funds'
 and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and 
prominent investors are required to file by the SEC The 13F filings show the funds'
and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
"""

