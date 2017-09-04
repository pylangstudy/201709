import datetime
t = datetime.time(1, 2, 3 ,4)
print(t)
print(t.utcoffset())

import pytz
for tz in [pytz.utc, pytz.timezone('Asia/Tokyo')]:
    print('-----', tz, '-----')
    t = datetime.time(1, 2, 3 ,4, tzinfo=tz)
    print(t)
    print(t.utcoffset())

#http://qiita.com/higitune/items/0ca244373d380cf1c060
"""
print(t.dst())
print(dir(pytz))
"""
