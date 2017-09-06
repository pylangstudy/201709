import calendar
for firstweekday in range(7):
    print('firstweekday', firstweekday)
    print(str(calendar.firstweekday()), end=' ')
    calendar.setfirstweekday(firstweekday)
    print(calendar.firstweekday())
"""
c = calendar.LocaleTextCalendar(firstweekday=6)
for firstweekday in range(7):
    print('firstweekday', firstweekday)
    print(str(c.firstweekday), end=' ')
    c.setfirstweekday(firstweekday)
    print(c.firstweekday)
"""
