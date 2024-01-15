#this program is my exercise learnings note from reading the book OReilly Introducting Python - Modern Computing in Simple Packages Chapter 13 Calendars and Clocks
import calendar

print(calendar.isleap(2009))

def leapyear(year):
    if calendar.isleap(year):
        return 'yes'
    else:
        return 'no'
    
print(f'Is year 2008 a leap year? {leapyear(2008)}')
print(f'Is year 2009 a leap year? {leapyear(2009)}')