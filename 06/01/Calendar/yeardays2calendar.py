import calendar

#yeardays2calendarの戻り値
#指定した年の1年間分のデータを返す。list(list(list(list(tuple()))))。width_month, month, week, tuple(日,曜日)
"""
[0, 0, 0, 0, 1, 2, 3]
[4, 5, 6, 7, 8, 9, 10]
[11, 12, 13, 14, 15, 16, 17]
[18, 19, 20, 21, 22, 23, 24]
[25, 26, 27, 28, 29, 30, 0]
"""
def yeardays2calendar(calendar): return calendar.yeardays2calendar(2017, width=3)
for calendar in [calendar.Calendar(firstweekday=0), calendar.Calendar(firstweekday=6)]:
    print('-----',calendar,'-----')
#    print(yeardays2calendar(calendar))
#    for weekday in yeardays2calendar(calendar): print(weekday)
    for width_month in yeardays2calendar(calendar):
        print('*************** width')
        for month in width_month: #月分のデータがwidth数のlistになって返ってくる
            print('========== month')
            for week in month:
                for day in week:
                    print(day)

    """
    for month in yeardays2calendar(calendar):
        print('***************')
        for week in month:
            for day in week:
                print(day)
    """
