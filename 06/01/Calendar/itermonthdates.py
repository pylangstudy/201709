import calendar

def itermonthdates(calendar): return calendar.itermonthdates(2017, 9)

for calendar in [calendar.Calendar(), calendar.Calendar(firstweekday=0), calendar.Calendar(firstweekday=6)]:
    print('-----',calendar,'-----')
    print(itermonthdates(calendar))
    for weekday in itermonthdates(calendar): print(weekday)
#print(calendar.Calendar())
#print(calendar.Calendar(firstweekday=0))#月曜日
#print(calendar.Calendar(firstweekday=6))#日曜日

