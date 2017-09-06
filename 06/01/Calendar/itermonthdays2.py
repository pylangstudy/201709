import calendar

#itermonthdays2の戻り値
#書式: (d, w)
#  d: 指定した月の日付。ただし指定月の前後月の場合は0になる
#  w: 曜日。0=月曜日, 6=日曜日
def itermonthdays2(calendar): return calendar.itermonthdays2(2017, 9)
for calendar in [calendar.Calendar(firstweekday=0), calendar.Calendar(firstweekday=6)]:
    print('-----',calendar,'-----')
    print(itermonthdays2(calendar))
    for weekday in itermonthdays2(calendar): print(weekday)

