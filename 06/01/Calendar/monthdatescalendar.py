import calendar

#monthdatescalendarの戻り値
#1週間毎のdateをlistで返す。週のdateを網羅する。ただし前月のdateを含み、次月のdateを含まない。
def monthdatescalendar(calendar): return calendar.monthdatescalendar(2017, 9)
for calendar in [calendar.Calendar(firstweekday=0), calendar.Calendar(firstweekday=6)]:
    print('-----',calendar,'-----')
#    print(monthdatescalendar(calendar))
    for weekday in monthdatescalendar(calendar): print(weekday)

