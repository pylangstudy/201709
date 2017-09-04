import datetime
import time
#print(datetime.datetime.fromordinal(0))#ValueError: ordinal must be >= 1
print(datetime.datetime.fromordinal(1))     #0001-01-01
print(datetime.datetime.fromordinal(365))   #0001-12-31
print(datetime.datetime.fromordinal(365*2)) #0002-12-31
print(datetime.datetime.fromordinal(730920))#2002-03-11

