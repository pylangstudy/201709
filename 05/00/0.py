from datetime import time, tzinfo, timedelta
class GMT1(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=1)
    def dst(self, dt):
        return timedelta(0)
    def tzname(self,dt):
        return "Europe/Prague"

t = time(12, 10, 30, tzinfo=GMT1())
print(t)
gmt = GMT1()
print(t.isoformat())
print(t.dst())
print(t.tzname())
print(t.strftime("%H:%M:%S %Z"))
print('The {} is {:%H:%M}.'.format("time", t))

