import datetime

t1 = datetime.timedelta(seconds=10)
t2 = datetime.timedelta(seconds=2)

print(t1, t2)

for operator in ['+', '-', '/', '//', '%']:
    expr = 't1'+operator+'t2'
    print(expr, eval(expr, globals(), locals()))

for operator in ['*', '/']:
    for expr in ['t1'+operator+'int(2)', 't1'+operator+'float(3.0)']:
        print(expr, eval(expr, globals(), locals()))

expr = 't1//int(2)'
print(expr, eval(expr, globals(), locals()))

print(+t1)
print(-t1)
print(abs(t1))
print(    datetime.timedelta(days=-4))
print(abs(datetime.timedelta(days=-4)))
print(str(t1))
print(repr(t1))

print((t1 + t2).total_seconds())
