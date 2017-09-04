import datetime
t = datetime.time(1, 2, 3 ,4)
print(t.strftime('%H時%M分%S.%f秒'))
print(t.strftime('%Y年%m月%d日_%H時%M分%S.%f秒'))
