import datetime
import pytz
for tz in [pytz.utc, pytz.timezone('Asia/Tokyo')]:
    print('-----', tz, '-----')
    t = datetime.time(1, 2, 3 ,4, tzinfo=tz)
    print(t)
    print(t.dst())

