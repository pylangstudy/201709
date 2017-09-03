import datetime
today = datetime.date.today()
print(today.isocalendar())
#2017-09-04(月)で実行した結果が以下。(ISO 年、ISO 週番号、ISO 曜日)のタプル。
#(2017, 36, 1)

