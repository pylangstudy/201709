import calendar

for firstweekday in [0, 6]:#月,日
    c = calendar.LocaleHTMLCalendar(firstweekday=firstweekday)
    print(c.formatmonth(2017, 9, withyear=True))

for firstweekday in [0, 6]:#月,日
    c = calendar.LocaleHTMLCalendar(firstweekday=firstweekday)
    print(c.formatmonth(2017, 9, withyear=False))
