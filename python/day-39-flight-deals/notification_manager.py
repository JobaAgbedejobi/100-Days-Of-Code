import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    load_dotenv()
    def __init__(self):
        self.user = os.environ["FROM_EMAIL"]
        self.password = os.environ["EMAIL_PASSWORD"]
        self.email = os.environ["TO_EMAIL"]

    def send_notification(self, price, from_airport, to_airport,
                          out_date, return_date):
        # Create a Multipart Message
        msg = MIMEMultipart()
        msg["From"] = self.user
        msg["To"] = self.email
        msg["Subject"] = "Low Price Flight Alert"

        # Create the body of the message
        message_body = (f"Only £{price} to fly from {from_airport} to {to_airport},"
                        f" on {out_date} until {return_date}.")

        # Attach the message body
        msg.attach(MIMEText(message_body, "plain", "utf-8"))

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.user, password=self.password)
            connection.send_message(msg)
