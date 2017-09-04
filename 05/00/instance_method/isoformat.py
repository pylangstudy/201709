import datetime
t = datetime.time(1, 2, 3 ,4)
print(t.isoformat())#01:02:03.000004
for timespec in ['auto','hours','minutes','seconds','milliseconds','microseconds']:
    print(t.isoformat(timespec))
