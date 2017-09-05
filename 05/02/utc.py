import datetime
print(datetime.timezone.utc)
print(datetime.datetime.now())
print(datetime.datetime(1, 2, 3))
print(datetime.datetime(1, 2, 3, tzinfo=datetime.timezone.utc))
print(datetime.datetime(1, 2, 3, tzinfo=datetime.timezone(datetime.timedelta(hours=9))))
