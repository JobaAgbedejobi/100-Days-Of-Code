##################### Extra Hard Starting Project ######################
import smtplib
import random
import datetime as dt
import csv
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("EMAIL_PASSWORD")
# 1. Update the birthdays.csv
# Changed the month from 2 digits to 1 so it matches with dt.datetime.now() format

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_month = now.month
current_day = now.day
with open(file="birthdays.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        month = int(row["month"])
        day = int(row["day"])
        if month == current_month and day == current_day:
            name = row["name"]
            email = row["email"]
            new_letter = f"Letter for {name}"
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
#             print("YES!")
            num = random.randint(1,3)
            random_letter = f"letter_{num}.txt"
            with open(file=f"letter_templates/{random_letter}", mode="r") as letter:
                content = letter.read()
                content = content.replace("[NAME]", name)

            with open(file=f"letter_templates/{new_letter}", mode="w") as letter:
                letter.write(content)

# 4. Send the letter generated in step 3 to that person's email address.
            try:
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=PASSWORD)
                    connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs=email,
                                        msg=f"Subject: Happy Birthday!\n\n{content}")
            except:
                with smtplib.SMTP("smtp.live.com") as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=PASSWORD)
                    connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs=email,
                                        msg=f"Subject: Happy Birthday!\n\n{content}")
