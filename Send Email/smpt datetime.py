# import smtplib
# my_email = "Your_Email"
# password = "Your_Password"
# with smtplib.SMTP("smtp.gmail.com") as connect:
#    connect.starttls()
#    connect.login(user=my_email, password=password)
#    connect.sendmail(from_addr=my_email,
#                     to_addrs="Your_email",
#                     msg="Subject:hello\n\n This is body of my email"
#                     )

import datetime as dt

now = dt.datetime.now()
year = now.year
mont = now.month
day_of_weak = now.weekday()
print(day_of_weak)
y = 2024
m = 11
d = 7
date_of_birth = dt.datetime(year=y, month=m, day=d)

