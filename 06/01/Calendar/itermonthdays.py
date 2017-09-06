import calendar

#itermonthdaysの戻り値
#書式: d
#  d: 指定した月の日付。ただし指定月の前後月の場合は0になる
def itermonthdays(calendar): return calendar.itermonthdays(2017, 9)
for calendar in [calendar.Calendar(firstweekday=0), calendar.Calendar(firstweekday=6)]:
    print('-----',calendar,'-----')
    print(itermonthdays(calendar))
    for weekday in itermonthdays(calendar): print(weekday)

