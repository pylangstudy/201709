from datetime import datetime, date, time
# Using datetime.combine()
d = date(2005, 7, 14)
t = time(12, 30)
print(datetime.combine(d, t))
# Using datetime.now() or datetime.utcnow()
print(datetime.now())
print(datetime.utcnow())
# Using datetime.strptime()
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt)
# Using datetime.timetuple() to get tuple of all attributes
tt = dt.timetuple()
for it in tt: print(it, end=',')
print()
# Date in ISO format
ic = dt.isocalendar()
for it in ic: print(it, end=',')
print()
# Formatting datetime
print(dt.strftime("%A, %d. %B %Y %I:%M%p"))
print('The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(dt, "day", "month", "time"))
