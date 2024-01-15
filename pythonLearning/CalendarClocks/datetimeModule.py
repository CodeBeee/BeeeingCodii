
#datetime module has 4 methods - 
#1 date for years, months and days
#2 time for hours, minutes, secods & fractions
#3 datetime for dates and times together
#4 timedelta for date and/or time intervals

#create a date object using year, month and day. 
from datetime import date
halloween = date(2019, 10, 31)
print(halloween)
print(halloween.isoformat())

#time intervals
from datetime import timedelta
today    = date.today()
one_day  = timedelta(days=1)
tomorrow = today + one_day
print(f'if today is {today}; then, tomorrow is {tomorrow}')

#time
from datetime import time
noon = time(12,0,0)
print(f'what time is noon? it is {noon}')

#datetime object includes both the date and time of the day. 
from datetime import datetime
some_day = datetime(2008, 2, 10, 7, 45, 45, 8)
print(some_day)

#can combine date and time object using combine().
today_noon = datetime.combine(today, noon)
print(f'what time was it at noon today {today_noon}')

#time's time module; 
import time as t
now_inEpoch = t.time()

print(f'current time in epoch format (unix time) is {now_inEpoch}')
print(f'converting that current time in epoch to a string would be {t.ctime(now_inEpoch)}')
print(f'current time in local time zone as structtime object of time  {t.localtime(now_inEpoch)}')
print(f'current time in UTC as structtime object of time {t.gmtime(now_inEpoch)}')
print(f'current time in UTC in unix time with from structtime object of time {t.mktime(t.gmtime(now_inEpoch))}')

#use strftime for all modules to convert time to a string. 
import time
formatstring = "its a %A, %B %d, %Y, local time %I:%M:%S%p" 
ataha = t.localtime()
print(f'current local time in a the format requested {t.strftime(formatstring,ataha)}') #time
print(f'some day in a the format requested {some_day.strftime(formatstring)}') #date
print(f'noon the format requested {noon.strftime(formatstring)}') #time of datetime ; ignore day part of the time as it is meaningless.

#use strptime to convert a string to a date object by specifying the format the string appears for date parsing
fmt = '%Y-%m-%d' #the string passed should be in exact format including the dashes. The numbers should be within the bounds (for months, values ranging 1-12)
print(f'converting a string into a time object {t.strptime("2019-10-31",fmt)}') #time
