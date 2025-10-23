##################### Hard Starting Project ######################
import datetime as dt
import smtplib
import random
import pandas
from pandas import DataFrame

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
data = pandas.read_csv('birthdays.csv')
birth_dates  = data["day"].tolist()
birth_month = data["month"].tolist()
name  = data["name"].tolist()
email = data["email"].tolist()
now = dt.datetime.now()
my_email = 'pythonsmtp8@gmail.com'
password = 'wzoh tbqz ttnv ahff'
connection = smtplib.SMTP('smtp.gmail.com', port=587)
day = now.day
month = now.month


letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
template = random.choice(letter_templates)

if day in birth_dates and month in birth_month:
    index = birth_dates.index(day)
    f = open(f"letter_templates/{template}")
    content = f.read()
    content = content.replace("[NAME]", name[index])
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: Happy Birthday\n\n{content}")
    connection.close()



#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



