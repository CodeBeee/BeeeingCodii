#1 write current date a string to the text file today.txt
from datetime import date
current_date = date.today().isoformat()

with open('today.txt', 'w') as wout:
    wout.write(current_date)

#2 read the text file today.txt into the string today_string
with open('today.txt','r') as rout:
    today_string = rout.read()
print(f'read the text file today.txt into the string today_string {today_string}')

#3 parse the date from today_string
from datetime import datetime
if today_string != '':
    today_string_dt = datetime.strptime(today_string,'%Y-%m-%d')
    print(f'Date parsed from the file: {today_string_dt.date()}')

#4 date object of my birthday 
mybirthdayDt = date(1985, 9, 9)
print(f'Date object of my birthday {mybirthdayDt}')


#5 what day of the week was my birthday
print(f'Day of the week was my birthday {mybirthdayDt.isoweekday()}')

#6 when would I be 10,000 days old?
from datetime import timedelta
daysfrombirthday   = timedelta(days=10000)
tenThousandDaysOld = mybirthdayDt + daysfrombirthday
print(f' I will be or I was 10000 days old on {tenThousandDaysOld}')
