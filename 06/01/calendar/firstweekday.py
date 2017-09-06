import calendar
c = calendar.LocaleTextCalendar(firstweekday=6)
for firstweekday in range(7):
    print('firstweekday', firstweekday)
    print(str(c.firstweekday), end=' ')
    c.setfirstweekday(firstweekday)
    print(c.firstweekday)

