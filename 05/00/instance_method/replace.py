import datetime
t = datetime.time(1, 2, 3, 4)
print(t)
print(t.replace(5, 6, 7, 8))
# インスタンスの操作ではなく、新しいインスタンスを返すらしい。インスタンスメソッドなのに。これはわかりづらい。
