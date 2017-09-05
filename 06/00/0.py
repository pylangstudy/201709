import datetime
d = datetime.datetime(9876, 5, 4, 23, 34, 56, 789012)
print(d)
for f in ['a','A','w','d','b','B','m','y','Y','H','I','p','M','S','f','z','Z','j','U','W','c','x','X','%','G','u','V']:
    print(f, d.strftime('%'+f))
