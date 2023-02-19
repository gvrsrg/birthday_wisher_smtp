import smtplib
import credentials
import datetime as dt
import random

def send_mail(text):

    my_email = credentials.email
    password = credentials.app_password
    to_address = credentials.to_address
    with smtplib.SMTP(credentials.smtp_address) as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        conn.sendmail(from_addr=my_email, to_addrs=to_address, msg=f"Subject:Hello\n\n{text}")

now = dt.datetime.now()
weekday = now.weekday()

if weekday==0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        line = random.choice(all_quotes)
        send_mail(line)

