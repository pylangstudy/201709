import calendar

def iterweekdays(calendar): return calendar.iterweekdays()

for calendar in [calendar.Calendar(), calendar.Calendar(firstweekday=0), calendar.Calendar(firstweekday=6)]:
    print('-----',calendar,'-----')
    print(iterweekdays(calendar))
    for weekday in iterweekdays(calendar): print(weekday, end=',')
    print()
#print(calendar.Calendar())
#print(calendar.Calendar(firstweekday=0))#月曜日
#print(calendar.Calendar(firstweekday=6))#日曜日

