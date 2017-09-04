import datetime
now = datetime.datetime.now()
print(now)
print(now.replace(1999, 12, 31))
print(now)
# インスタンスの操作ではなく、新しいインスタンスを返すらしい。インスタンスメソッドなのに。これはわかりづらい。
