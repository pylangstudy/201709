from datetime import date
d = date.fromordinal(730920) # 730920th day after 1. 1. 0001
print(d)
t = d.timetuple()
for i in t: print(i, end=', ')
print()
ic = d.isocalendar()
for i in ic: print(i, end=', ')
print()

print(d.isoformat())
print(d.strftime("%d/%m/%y"))
print(d.strftime("%A %d. %B %Y"))
print('The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month"))

