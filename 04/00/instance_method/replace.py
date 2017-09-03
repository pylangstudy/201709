import datetime
today = datetime.date.today()
print(today)
print(today.replace(1999, 12, 31))
print(today)
# インスタンスの操作ではなく、新しいインスタンスを返すらしい。インスタンスメソッドなのに。これはわかりづらい。
