import datetime
import time
#print(datetime.datetime.combine(datetime.date.today(), time.time()))#TypeError: combine() argument 2 must be datetime.time, not float
print(datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()))
