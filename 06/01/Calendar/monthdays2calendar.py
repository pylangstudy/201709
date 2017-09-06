import calendar

#monthdays2calendarの戻り値
#1週間毎の日と曜日をlist(tuple(日,曜日))で返す。tupleは前後月の場合、日は0となる。また、週は前月、次月を含む（必ず7日分）。
def monthdays2calendar(calendar): return calendar.monthdays2calendar(2017, 9)
for calendar in [calendar.Calendar(firstweekday=0), calendar.Calendar(firstweekday=6)]:
    print('-----',calendar,'-----')
#    print(monthdays2calendar(calendar))
    for weekday in monthdays2calendar(calendar): print(weekday)

