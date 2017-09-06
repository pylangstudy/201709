import calendar

#monthdayscalendarの戻り値
#1週間毎の日をlistで返す。前後月の場合、日は0となる。また、週は前月、次月を含む（必ず7日分）。
"""
[0, 0, 0, 0, 1, 2, 3]
[4, 5, 6, 7, 8, 9, 10]
[11, 12, 13, 14, 15, 16, 17]
[18, 19, 20, 21, 22, 23, 24]
[25, 26, 27, 28, 29, 30, 0]
"""
def monthdayscalendar(calendar): return calendar.monthdayscalendar(2017, 9)
for calendar in [calendar.Calendar(firstweekday=0), calendar.Calendar(firstweekday=6)]:
    print('-----',calendar,'-----')
#    print(monthdayscalendar(calendar))
    for weekday in monthdayscalendar(calendar): print(weekday)

