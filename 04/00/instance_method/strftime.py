import datetime
today = datetime.date.today()
print(today.strftime('%Y年%m月%d日_%H時%M分%S.%f秒'))
#2017-09-04(月)で実行した結果が以下。必ずゼロ埋めされる。
#2017年09月04日_00時00分00.000000秒

