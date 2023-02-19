import smtplib
import credentials

my_email = credentials.email

connection = smtplib.SMTP(credentials.smtp_address)