import calendar

#yeardatescalendarの戻り値
#1週間毎の日をlistで返す。前後月の場合、日は0となる。また、週は前月、次月を含む（必ず7日分）。
"""
[0, 0, 0, 0, 1, 2, 3]
[4, 5, 6, 7, 8, 9, 10]
[11, 12, 13, 14, 15, 16, 17]
[18, 19, 20, 21, 22, 23, 24]
[25, 26, 27, 28, 29, 30, 0]
"""
def yeardatescalendar(calendar): return calendar.yeardatescalendar(2017, width=3)
for calendar in [calendar.Calendar(firstweekday=0), calendar.Calendar(firstweekday=6)]:
    print('-----',calendar,'-----')
#    print(yeardatescalendar(calendar))
#    for weekday in yeardatescalendar(calendar): print(weekday)
    for width_month in yeardatescalendar(calendar):
        print('*************** width')
        for month in width_month: #月分のデータがwidth数のlistになって返ってくる
            print('========== month')
            for week in month:
                for day in week:
                    print(day)

    """
    for month in yeardatescalendar(calendar):
        print('***************')
        for week in month:
            for day in week:
                print(day)
    """
