import smtplib
import credentials
import datetime as dt
import random
import pandas as pd


def send_mail(address_to, text):

    my_email = credentials.email
    password = credentials.app_password

    with smtplib.SMTP(credentials.smtp_address) as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        conn.sendmail(from_addr=my_email, to_addrs=address_to, msg=f"Subject:HBD!\n\n{text}")

now = dt.datetime.now()
weekday = now.weekday()
today = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
bd_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in bd_dict:
    bd_person = bd_dict[today]
    file_path = f"letter_templates\letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", bd_person["name"])
        send_mail(bd_person["email"], content)

#
# if weekday==0:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         line = random.choice(all_quotes)
#         send_mail(line)

