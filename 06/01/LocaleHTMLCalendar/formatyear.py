import calendar

for firstweekday in [0, 6]:#月,日
    c = calendar.LocaleHTMLCalendar(firstweekday=firstweekday)
    print(c.formatyear(2017, width=3))

