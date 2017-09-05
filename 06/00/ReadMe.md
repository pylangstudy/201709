# [8.1.8. strftime() と strptime() の振る舞い](https://docs.python.jp/3/library/datetime.html#strftime-and-strptime-behavior)

< [8.1. datetime — 基本的な日付型および時間型](https://docs.python.jp/3/library/datetime.html#module-datetime) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/datetime.py](https://github.com/python/cpython/tree/3.6/Lib/datetime.py)

文字列→日付、日付→文字列、に相互変換できる。

## 概要

> date, datetime,および time オブジェクトは全て、明示的な書式文字列でコントロールして時刻表現文字列を生成するための strftime(format) メソッドをサポートしています。大雑把にいうと、 d.strftime(fmt) は time モジュールの time.strftime(fmt, d.timetuple()) のように動作します。ただし全てのオブジェクトが timetuple() メソッドをサポートしているわけではありません。

> 逆に datetime.strptime() クラスメソッドは日付や時刻に対応する書式文字列から datetime オブジェクトを生成します。 datetime.strptime(date_string, format) は datetime(*(time.strptime(date_string, format)[0:6])) と等価です。

> time オブジェクトでは、年、月、日の値がないため、それらの書式化コードを使うことができません。無理矢理使った場合、年は 1900 に置き換えられ、月と日は 1 に置き換えられます。

> date オブジェクトでは、時、分、秒、マイクロ秒の値がないため、それらの書式化コードを使うことができません。無理矢理使った場合、これらの値は 0 に置き換えられます。

> Python はプラットフォームの C ライブラリの strftime() 関数を呼び出していて、プラットフォームごとにその実装が異なるのはよくあることなので、サポートされるフォーマット記号全体はプラットフォームごとに様々です。プラットフォームでサポートされているフォーマット記号全体を見るには、 strftime(3) のドキュメントを参照してください。

> 以下のリストはC標準(1989年版)が要求する全ての書式化コードで、標準C実装があれば全ての環境で動作します。1999 年版の C 標準では書式化コードが追加されているので注意してください。

* [datetime](https://docs.python.jp/3/library/datetime.html#datetime.datetime)
* [date](https://docs.python.jp/3/library/datetime.html#datetime.date)
* [time](https://docs.python.jp/3/library/datetime.html#datetime.time)

### ポイント

* 上記3型のうち、相互変換できるのはdatetimeのみ。datetimeさえ覚えればOK
* 書式はプラットフォームのC言語ライブラリstrftime()の実装ごとに異なる

書式が共通化されず実行環境ごとに異なるのは残念。

## ディレクティブ

ディレクティブ|意味|使用例|注釈
--------------|----|------|----
%a|ロケールの曜日名を短縮形で表示します。|Sun, Mon, ..., Sat (en_US);So, Mo, ..., Sa (de_DE)|(1)
%A|ロケールの曜日名を表示します。Sunday, Monday, ..., Saturday (en_US);<br>Sonntag, Montag, ..., Samstag (de_DE)|(1)
%w|曜日を10進表記した文字列を表示します。0 が日曜日で、6 が土曜日を表します。|0, 1, ..., 6| 
%d|0埋めした10進数で表記した月中の日にち。|01, 02, ..., 31| 
%b|ロケールの月名を短縮形で表示します。Jan, Feb, ..., Dec (en_US);<br>Jan, Feb, ..., Dez (de_DE)|(1)
%B|ロケールの月名を表示します。January, February, ..., December (en_US);<br>Januar, Februar, ..., Dezember (de_DE)|(1)
%m|0埋めした10進数で表記した月。|01, 02, ..., 12| 
%y|0埋めした10進数で表記した世紀ありの年。|00, 01, ..., 99| 
%Y|西暦 ( 4桁) の 10 進表記を表します。|0001, 0002, ..., 2013, 2014, ..., 9998, 9999|(2)
%H|0埋めした10進数で表記した時 (24時間表記)。|00, 01, ..., 23| 
%I|0埋めした10進数で表記した時 (12時間表記)。|01, 02, ..., 12| 
%p|ロケールの AM もしくは PM と等価な文字列になります。AM, PM (en_US);<br>am, pm (de_DE)|(1), (3)
%M|0埋めした10進数で表記した分。|00, 01, ..., 59| 
%S|0埋めした10進数で表記した秒。|00, 01, ..., 59|(4)
%f|10進数で表記したマイクロ秒 (左側から0埋めされます)。|000000, 000001, ..., 999999|(5)
%z|UTCオフセットを +HHMM もしくは -HHMM の形式で表示します (オブジェクトがnaiveであれば空文字列)。|(空文字列), +0000, -0400, +1030|(6)
%Z|タイムゾーンの名前を表示します (オブジェクトがnaiveであれば空文字列)。|(空文字列), UTC, EST, CST| 
%j|0埋めした10進数で表記した年中の日にち。|001, 002, ..., 366| 
%U|0埋めした10進数で表記した年中の週番号 (週の始まりは日曜日とする)。新年の最初の日曜日に先立つ日は 0週に属するとします。|00, 01, ..., 53|(7)
%W|0埋めした10進数で表記した年中の週番号 (週の始まりは月曜日とする)。新年の最初の月曜日に先立つ日は 0週に属するとします。|00, 01, ..., 53|(7)
%c|ロケールの日時を適切な形式で表します。Tue Aug 16 21:30:00 1988 (en_US);<br>Di 16 Aug 21:30:00 1988 (de_DE)|(1)
%x|ロケールの日付を適切な形式で表します。08/16/88 (None);<br>08/16/1988 (en_US);<br>16.08.1988 (de_DE)|(1)
%X|ロケールの時間を適切な形式で表します。21:30:00 (en_US);<br>21:30:00 (de_DE)|(1)
%%|文字 '%' を表します。|%| 

> Several additional directives not required by the C89 standard are included for convenience. These parameters all correspond to ISO 8601 date values. These may not be available on all platforms when used with the strftime() method. The ISO 8601 year and ISO 8601 week directives are not interchangeable with the year and week number directives above. Calling strptime() with incomplete or ambiguous ISO 8601 directives will raise a ValueError.

> 便宜上、C89標準では不要な追加の指令がいくつか含まれています。これらのパラメータはすべてISO 8601の日付値に対応します。これらは、strftime（）メソッドと一緒に使用すると、すべてのプラットフォームで利用できるわけではありません。 ISO 8601年およびISO 8601の週の指令は、上記の年および週番号の指令と入れ替えることはできません。不完全またはあいまいなISO 8601指令でstrptime（）を呼び出すと、ValueErrorが発生します。

ディレクティブ|意味|使用例|注釈
--------------|----|------|----
%G|ISO 8601年のうち、ISOの週の大部分（％V）を含む年を表す年。(ISO 8601 year with century representing the year that contains the greater part of the ISO week (%V).)|0001, 0002, ..., 2013, 2014, ..., 9998, 9999|(8)
%u|ISO 8601の曜日を10進数で表し、1は月曜日を表します。(ISO 8601 weekday as a decimal number where 1 is Monday.)|1, 2, ..., 7| 
%V|月曜日を週の最初の曜日とする10進数のISO 8601週。週01は1月4日を含む週です。(ISO 8601 week as a decimal number with Monday as the first day of the week. Week 01 is the week containing Jan 4.)|01, 02, ..., 53|(8)

> バージョン 3.6 で追加: %G, %u and %V were added.

```python
import datetime
d = datetime.datetime(9876, 5, 4, 23, 34, 56, 789012)
print(d)
for f in ['a','A','w','d','b','B','m','y','Y','H','I','p','M','S','f','z','Z','j','U','W','c','x','X','%','G','u','V']:
    print(f, d.strftime('%'+f))
```
```sh
$ python 0.py 
9876-05-04 23:34:56.789012
a Thu
A Thursday
w 4
d 04
b May
B May
m 05
y 76
Y 9876
H 23
I 11
p PM
M 34
S 56
f 789012
z 
Z 
j 125
U 18
W 18
c Thu May  4 23:34:56 9876
x 05/04/76
X 23:34:56
% %
G 9876
u 4
V 18
```

