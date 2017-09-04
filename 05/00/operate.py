import datetime
import pytz
t = datetime.time(1, 2, 3, 4)
t2 = datetime.time(1, 2, 4, 5)
td = datetime.timedelta(seconds=1)

print(f't:{t}')
print(f'timedelta:{td}')
#print('----- 加算（timedelta）-----')
#print(f'{t} + {td}: = {t + td}')#TypeError: unsupported operand type(s) for +: 'datetime.time' and 'datetime.timedelta'
#print('----- 減算（timedelta）-----')
#print(f'{t} - {td}: = {t - td}')#TypeError: unsupported operand type(s) for -: 'datetime.time' and 'datetime.timedelta'
print('----- 比較 -----')
print(f'{t} < {t2}: = {t < t2}')
print(f'{t} > {t2}: = {t > t2}')
print(f'{t} == {t2}: = {t == t2}')
print(f'{t} != {t2}: = {t != t2}')
#print('----- 差 -----')
#print(datetime.datetime.now() - t)#TypeError: unsupported operand type(s) for -: 'datetime.datetime' and 'datetime.time'
