import smtplib
import credentials

my_email = credentials.email
password = credentials.password
to_address = credentials.to_address

connection = smtplib.SMTP(credentials.smtp_address)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=to_address, msg="Hello")
connection.close()