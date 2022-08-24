import pandas
import datetime as dt
import smtplib
import random

date = pandas.read_csv('birthdays.csv')
bday_dict = date.to_dict(orient='records')

now = dt.datetime.now()
CURRENT_MONTH = now.month
CURRENT_DAY = now.day

USER_EMAIL = 'YourMailID'
USER_PASS = 'YourPass'
PLACEHOLDER = '[NAME]'

for day in bday_dict:
    bday_name = day['name']
    bday_email = day['email']
    bday_month = day['month']
    bday_day = day['day']

    if bday_month == CURRENT_MONTH and bday_day == CURRENT_DAY:
        random_num = random.randint(1, 3)
        with open(file=f'letter_templates/letter_{random_num}.txt') as file:
            letter = file.read()
            random_letter = letter.replace(PLACEHOLDER, bday_name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=USER_EMAIL, password=USER_PASS)
            connection.sendmail(
                from_addr=USER_EMAIL,
                to_addrs=bday_email,
                msg=f"Subject:Happy B'day\n\n{random_letter}")



