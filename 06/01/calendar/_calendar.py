#import calendar
#print(calendar)
#print(calendar.calendar)
#print(calendar.calendar.calendar)
#print(calendar.calendar.calendar.calendar)
#print(calendar.calendar(2017))
#TypeError: 'module' object is not callable
#これはひどい。ふつうにimportしたらモジュール名とメソッド名が重複して参照エラーになる。

#別名を付与してみたが、存在しないエラー。謎
import calendar as c
print(c)
print(dir(c))
print(c.calendar(2017))#AttributeError: module 'calendar' has no attribute 'calendar'
#print(c.calendar(2017))
#存在しないエラーだが、以下文書にはある。
#https://docs.python.jp/3/library/calendar.html#calendar.calendar

