import calendar

for firstweekday in [0, 6]:#月,日
    c = calendar.LocaleHTMLCalendar(firstweekday=firstweekday)
    with open(f'formatyearpage_{firstweekday}.html', mode='wb') as f:
        f.write(c.formatyearpage(2017, width=3))

