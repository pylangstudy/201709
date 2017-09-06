import calendar

print(calendar.TextCalendar())
print(calendar.TextCalendar(firstweekday=0))#月曜日
print(calendar.TextCalendar(firstweekday=6))#日曜日

for firstweekday in [0, 6]:#月,日
    c = calendar.TextCalendar(firstweekday=firstweekday)
    print(c.formatmonth(2017, 9))

for firstweekday in [0, 6]:#月,日
    c = calendar.TextCalendar(firstweekday=firstweekday)
    print(c.formatmonth(2017, 9, w=4, l=2))
