import datetime
today = datetime.date.today()
print(today.timetuple())
#2017-09-04(月)でじっこうした結果が以下。月曜日=0。
#time.struct_time(tm_year=2017, tm_mon=9, tm_mday=4, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=247, tm_isdst=-1)

