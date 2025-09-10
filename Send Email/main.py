import smtplib
import datetime as dt
import  random
now = dt.datetime.now()

weekday = now.weekday()

my_email = "Your_Email"
password = "Your_Password"

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readline()
        quote = random.choice(all_quote)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(my_email,password)
        connect.sendmail(from_addr=my_email,
                        to_addrs="Your_Email",
                        msg=f"Subject:Monday Motivation\n\n{quote}"
                        )











