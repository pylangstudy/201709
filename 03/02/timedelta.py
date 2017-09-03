import datetime
print(datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0))
print(datetime.timedelta(days=1, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0))
print(datetime.timedelta(days=0, seconds=1, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0))
print(datetime.timedelta(days=0, seconds=0, microseconds=1, milliseconds=0, minutes=0, hours=0, weeks=0))
print(datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=1, minutes=0, hours=0, weeks=0))
print(datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=1, hours=0, weeks=0))
print(datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=1, weeks=0))
print(datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=1))
print(datetime.timedelta(microseconds=-1))#>負の値を正規化すると、一見混乱するような値になります。

td = datetime.timedelta(days=1)
print(td)
print(td.min)
print(td.max)
print(td.resolution)

print(td.days)
print(td.seconds)
print(td.microseconds)

#なぜ入力できて出力できないのか…謎仕様
#print(td.milliseconds)#AttributeError: 'datetime.timedelta' object has no attribute 'milliseconds'
#print(td.hours)#AttributeError: 'datetime.timedelta' object has no attribute 'hours'
#print(td.weeks)#AttributeError: 'datetime.timedelta' object has no attribute 'weeks'

