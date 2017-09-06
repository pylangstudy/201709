import calendar

print(calendar.HTMLCalendar())
print(calendar.HTMLCalendar(firstweekday=0))#月曜日
print(calendar.HTMLCalendar(firstweekday=6))#日曜日

for firstweekday in [0, 6]:#月,日
    c = calendar.HTMLCalendar(firstweekday=firstweekday)
    print(c.formatmonth(2017, 9, withyear=True))

for firstweekday in [0, 6]:#月,日
    c = calendar.HTMLCalendar(firstweekday=firstweekday)
    print(c.formatmonth(2017, 9, withyear=False))
