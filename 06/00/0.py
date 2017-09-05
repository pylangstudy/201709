import datetime

d = datetime.datetime(9876, 5, 4, 23, 34, 56, 789012)
print(d)

print('-----', 'datetime -> str' ,'-----')
for f in ['a','A','w','d','b','B','m','y','Y','H','I','p','M','S','f','z','Z','j','U','W','c','x','X','%','G','u','V']:
    print(f, d.strftime('%'+f))

print('-----', 'str -> datetime' ,'-----')
for f in ['a','A','w','d','b','B','m','y','Y','H','I','p','M','S','f','z','Z','j','U','W','c','x','X','%']:
    s = d.strftime('%'+f)
    if None is s or 0 == len(s):    print(f, s, '')
    else:                           print(f, s, datetime.datetime.strptime(s, '%'+f))

"""
for f in ['G','u','V']:
    s = str(d)
#    s = '9876-05-04 23:34:56'
    print(str(d))
    print(f, s, datetime.datetime.strptime(s, '%'+f))
#    print(f, str(d), datetime.datetime.strptime(str(d), '%'+f))


#'G'    ValueError: unconverted data remains: -05-04 23:34:56.789012
#'u'    ValueError: time data '9876-05-04 23:34:56' does not match format '%u'
#'V'    ValueError: unconverted data remains: 876-05-04 23:34:56.789012
"""
