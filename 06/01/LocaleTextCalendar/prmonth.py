import calendar

for firstweekday in [0, 6]:#月,日
    c = calendar.LocaleTextCalendar(firstweekday=firstweekday)
    c.prmonth(2017, 9)
