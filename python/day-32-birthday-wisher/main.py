import random
import smtplib
import datetime as dt
from random import choice
#SMTP = Simple Mail Transfer Protocol
my_email = os.environ.get("MY_EMAIL") # part before @ is identity of my email account
# after the @ is identity of my email provider
# outlook is smtp.live.com, yahoo is smtp.mail.yahoo.com
password = os.environ.get("EMAIL_PASSWORD")

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
#
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="your-email@example.com",
#                     msg="Subject:Hello\n\nThis is the body of my email")#i.e. content
# connection.close()

# OR:

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="your-email@example.com",
#                         msg="Subject:Hello\n\nThis is the body of my email")


# #CHALLENGE 1: SEND MOTIVATIONAL QUOTES ON MONDAY VIA EMAIL
# #HINT 1: Use the datetime module to obtain the current day of the week
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:

# #Hint 2: Open the quotes.txt file and obtain a list of quotes
    with open (file="quotes.txt", mode="r") as file:
        content = file.read()
        # OR content = file.readlines() and can get rid of line 40

# #Hint 3: Use the random module to pick a random quote from the list of quotes
    quotes = content.splitlines()
    quote = random.choice(quotes)
    print(quote)

# #Hint 4: Use the Smtplib module to send the email to myself
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Monday Quote\n\n{quote}")