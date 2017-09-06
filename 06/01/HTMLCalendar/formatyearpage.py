import calendar

for firstweekday in [0, 6]:#月,日
    c = calendar.HTMLCalendar(firstweekday=firstweekday)
    with open(f'formatyearpage_{firstweekday}.html', mode='wb') as f:
        f.write(c.formatyearpage(2017, width=3))
#    print(c.formatyearpage(2017, width=3))

"""
for firstweekday in [0, 6]:#月,日
    c = calendar.HTMLCalendar(firstweekday=firstweekday)
    print(c.formatyearpage(2017, width=3, css=None, encoding='utf-8'))
"""
