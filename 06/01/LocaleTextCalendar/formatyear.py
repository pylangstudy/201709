import calendar

for firstweekday in [0, 6]:#月,日
    c = calendar.LocaleTextCalendar(firstweekday=firstweekday)
    print(c.formatyear(2017, w=3, l=1, c=8, m=2))
