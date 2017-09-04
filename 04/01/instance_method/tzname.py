import datetime
now = datetime.datetime.now()
print(now)
print(now.tzname())

import pytz
now = datetime.datetime.now(tz=pytz.utc)
print(now)
print(now.tzname())

