import calendar

for firstweekday in [0, 6]:#月,日
    c = calendar.LocaleTextCalendar(firstweekday=firstweekday)
    print(c.formatmonth(2017, 9))

for firstweekday in [0, 6]:#月,日
    c = calendar.LocaleTextCalendar(firstweekday=firstweekday)
    print(c.formatmonth(2017, 9, w=4, l=2))
