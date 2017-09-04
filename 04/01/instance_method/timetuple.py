import datetime
now = datetime.datetime.now()
print(now.timetuple())
#2017-09-04(月)で実行した結果が以下。月曜日=0。
#time.struct_time(tm_year=2017, tm_mon=9, tm_mday=4, tm_hour=9, tm_min=14, tm_sec=50, tm_wday=0, tm_yday=247, tm_isdst=-1)

