# [8.2. calendar — 一般的なカレンダーに関する関数群](https://docs.python.jp/3/library/calendar.html#module-calendar)

< [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/calendar.py](https://github.com/python/cpython/tree/3.6/Lib/calendar.py)

## 概要

> このモジュールは Unix の cal プログラムのようなカレンダー出力を行い、それに加えてカレンダーに関する有益な関数群を提供します。標準ではこれらのカレンダーは（ヨーロッパの慣例に従って）月曜日を週の始まりとし、日曜日を最後の日としています。 setfirstweekday() を用いることで、日曜日(6)や他の曜日を週の始まりに設定することができます。日付を表す引数は整数値で与えます。関連する機能として、 datetime と time モジュールも参照してください。

> このモジュールで提供する関数とクラスのほとんどは datetime に依存しており、過去も未来も現代のグレゴリオ暦を利用します。この方式は Dershowitz と Reingold の書籍「Calendrical Calculations」にある先発グレゴリオ暦に一致しており、同書では全ての計算の基礎となる暦としています。

* [setfirstweekday](https://docs.python.jp/3/library/calendar.html#calendar.setfirstweekday)
* [datetime](https://docs.python.jp/3/library/datetime.html#module-datetime)
* [time](https://docs.python.jp/3/library/time.html#module-time)

## 一覧

### Calendar

コンストラクタ|説明
--------------|----
class calendar.Calendar(firstweekday=0)|Calendar オブジェクトを作ります。 firstweekday は整数で週の始まりの曜日を指定するものです。 0 が月曜(デフォルト)、 6 なら日曜です。

インスタンスメソッド|説明
--------------------|----
iterweekdays()|曜日の数字を一週間分生成するイテレータを返します。イテレータから得られる最初の数字は firstweekday が返す数字と同じになります。
itermonthdates(year, month)|year 年 month (1–12) 月に対するイテレータを返します。 このイテレータはその月の全ての日、およびその月が始まる前の日とその月が終わった後の日のうち、週の欠けを埋めるために必要な日を (datetime.date オブジェクトとして) 返します。
itermonthdays2(year, month)|year 年 month 月に対する itermonthdates() と同じようなイテレータを返します。生成されるのは日付の数字と曜日を表す数字のタプルです。
itermonthdays(year, month)|year 年 month 月に対する itermonthdates() と同じようなイテレータを返します。生成されるのは日付の数字だけです。
monthdatescalendar(year, month)|year 年 month 月の週のリストを返します。週は全て七つの datetime.date オブジェクトからなるリストです。
monthdays2calendar(year, month)|year 年 month 月の週のリストを返します。週は全て七つの日付の数字と曜日を表す数字のタプルからなるリストです。
monthdayscalendar(year, month)|year 年 month 月の週のリストを返します。週は全て七つの日付の数字からなるリストです。
yeardatescalendar(year, width=3)|指定された年のデータを整形に向く形で返します。返される値は月の並びのリストです。月の並びは最大で width ヶ月(デフォルトは3ヶ月)分です。各月は4ないし6週からなり、各週は1ないし7日からなります。各日は datetime.date オブジェクトです。
yeardays2calendar(year, width=3)|指定された年のデータを整形に向く形で返します (yeardatescalendar() と同様です)。週のリストの中が日付の数字と曜日の数字のタプルになります。月の範囲外の部分の日付はゼロです。
yeardayscalendar(year, width=3)|指定された年のデータを整形に向く形で返します (yeardatescalendar() と同様です)。週のリストの中が日付の数字になります。月の範囲外の日付はゼロです。

どんなときに、どのメソッドを使えば便利なのかが非常にわかりにくい。名前から結果を想像できない。マジックナンバーを使うなど最悪の命名。

### TextCalendar

コンストラクタ|説明
--------------|----
class calendar.TextCalendar(firstweekday=0)|このクラスはプレインテキストのカレンダーを生成するのに使えます。

インスタンスメソッド|説明
--------------------|----
formatmonth(theyear, themonth, w=0, l=0)|ひと月分のカレンダーを複数行の文字列で返します。
prmonth(theyear, themonth, w=0, l=0)|formatmonth() で返されるひと月分のカレンダーを出力します。
formatyear(theyear, w=2, l=1, c=6, m=3)|m 列からなる一年間のカレンダーを複数行の文字列で返します。
pryear(theyear, w=2, l=1, c=6, m=3)|formatyear() で返される一年間のカレンダーを出力します。

### HTMLCalendar

コンストラクタ|説明
--------------|----
class calendar.HTMLCalendar(firstweekday=0)|このクラスは HTML のカレンダーを生成するのに使えます。

インスタンスメソッド|説明
--------------------|----
formatmonth(theyear, themonth, withyear=True)|ひと月分のカレンダーを HTML のテーブルとして返します。
formatyear(theyear, width=3)|一年分のカレンダーを HTML のテーブルとして返します。width の値 (デフォルトでは 3 です) は何ヶ月分を一行に収めるかを指定します。
formatyearpage(theyear, width=3, css='calendar.css', encoding=None)|一年分のカレンダーを一つの完全な HTML ページとして返します。 width の値(デフォルトでは 3 です) は何ヶ月分を一行に収めるかを指定します。 css は使われるカスケーディングスタイルシートの名前です。スタイルシートを使わないようにするために None を渡すこともできます。 encoding には出力に使うエンコーディングを指定します (デフォルトではシステムデフォルトのエンコーディングです)。

コンストラクタ|説明
--------------|----
class calendar.LocaleTextCalendar(firstweekday=0, locale=None)|この TextCalendar のサブクラスではコンストラクタにロケール名を渡すことができ、メソッドの返り値で月や曜日が指定されたロケールのものになります。このロケールがエンコーディングを含む場合には、月や曜日の入った文字列はユニコードとして返されます。
class calendar.LocaleHTMLCalendar(firstweekday=0, locale=None)|この HTMLCalendar のサブクラスではコンストラクタにロケール名を渡すことができ、メソッドの返り値で月や曜日が指定されたロケールのものになります。このロケールがエンコーディングを含む場合には、月や曜日の入った文字列はユニコードとして返されます。

注釈
これら2つのクラスの formatweekday() と formatmonthname() メソッドは、一時的に現在の locale を指定された locale に変更します。現在の locale はプロセス全体に影響するので、これらはスレッドセーフではありません。
単純なテキストのカレンダーに関して、このモジュールには以下のような関数が提供されています。

インスタンスメソッド|説明
--------------------|----
calendar.setfirstweekday(weekday)|週の最初の曜日(0 は月曜日, 6 は日曜日)を設定します。定数 MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY 及び SUNDAY は便宜上提供されています。例えば、日曜日を週の開始日に設定するときは:
import calendar
calendar.setfirstweekday(calendar.SUNDAY)
calendar.firstweekday()|現在設定されている週の最初の曜日を返します。
calendar.isleap(year)|year が閏年なら True を、そうでなければ False を返します。
calendar.leapdays(y1, y2)|範囲(y1 ... y2)指定された期間の閏年の回数を返します。ここで y1 や y2 は年を表します。
この関数は、世紀の境目をまたぐ範囲でも正しく動作します。
calendar.weekday(year, month, day)|year (1970–...), month (1–12), day (1–31) で与えられた日の曜日(0 は月曜日)を返します。
calendar.weekheader(n)|短縮された曜日名を含むヘッダを返します。n は各曜日を何文字で表すかを指定します。
calendar.monthrange(year, month)|year と month で指定された月の一日の曜日と日数を返します。
calendar.monthcalendar(year, month)|月のカレンダーを行列で返します。各行が週を表し、月の範囲外の日は0になります。それぞれの週は setfirstweekday() で設定をしていない限り月曜日から始まります。
calendar.prmonth(theyear, themonth, w=0, l=0)|month() 関数によって返される月のカレンダーを出力します。
calendar.month(theyear, themonth, w=0, l=0)|TextCalendar の formatmonth() メソッドを利用して、ひと月分のカレンダーを複数行の文字列で返します。
calendar.prcal(year, w=0, l=0, c=6, m=3)|calendar() 関数で返される一年間のカレンダーを出力します。
calendar.calendar(year, w=2, l=1, c=6, m=3)|TextCalendar の formatyear() メソッドを利用して、 3列からなる一年間のカレンダーを複数行の文字列で返します。
calendar.timegm(tuple)|カレンダーと直接は関係無いが、 time モジュールの gmtime() 関数が返す形式の時刻を表すタプルを引数に取り、1970 を基点とするエポック時刻で POSIX エンコーディングであると仮定して、対応する Unix タイムスタンプの値を返します。実際には、 time.gmtime() と timegm() はお互いの逆関数です。
calendar モジュールの以下のデータ属性を利用することができます:
calendar.day_name|現在のロケールでの曜日を表す配列です。
calendar.day_abbr|現在のロケールでの短縮された曜日を表す配列です。
calendar.month_name|現在のロケールでの月の名を表す配列です。この配列は通常の約束事に従って、1月を数字の 1 で表しますので、長さが 13 ある代わりに month_name[0] が空文字列になります。
calendar.month_abbr|現在のロケールでの短縮された月の名を表す配列です。この配列は通常の約束事に従って、1月を数字の 1 で表しますので、長さが 13 ある代わりに month_abbr[0] が空文字列になります。

参考
datetime モジュール
time モジュールと似た機能を持った日付と時間用のオブジェクト指向インタフェース。
time モジュール
時間に関連した低水準の関数群。

## Python文書の見づらさ

`calendar`がモジュールを指しているのか、インスタンスを指しているのか曖昧。

メソッドが所属する名前空間|表記
--------------------------|----
モジュール|calendar.LocaleTextCalendar.METHOD()
クラス|class calendar.LocaleTextCalendar.METHOD()
インスタンス|METHOD()

# calendarのひどい点

## Calendarクラスのメソッドが多すぎる

どんなときに、どのメソッドを使えば便利なのかが非常にわかりにくい。

### 名前が意味不明

名前から結果を想像できない。マジックナンバーを使うなど最悪の命名。

## LocaleTextCalendarが全くローカライズされていない件

```sh
06/01/LocaleTextCalendar $ python formatmonth.py 
      9月 2017
月  火  水  木  金  土  日
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30

      9月 2017
日  月  火  水  木  金  土
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
```

これはひどい。曜日のスペース数が多くてズレてしまっている。全角文字であることが考慮されていないということか？使えない……。

## HTMLCalendarの出力結果をみると高さがズレていた

HTMLCalendar.formatyearpage()の出力結果をブラウザで閲覧すると、高さがズレていた……。テーブルなのになぜ？面倒なのでHTML解析はしないが、使えない。

## 名前の重複？存在しない？

```python
import calendar
print(calendar.calendar(2017))
```
```sh
TypeError: 'module' object is not callable
```

ふつうにimportしたらモジュール名とメソッド名が重複して参照エラーになる……。

以下の3関数が実行できなかった。

* [prcal()](https://docs.python.jp/3/library/calendar.html#calendar.prcal)
* [calendar()](https://docs.python.jp/3/library/calendar.html#calendar.calendar)
* [timegm()](https://docs.python.jp/3/library/calendar.html#calendar.timegm)

以下、3属性もエラーになった。

* calendar.day_name
* calendar.day_abbr
* calendar.month_name
* calendar.month_abbr

```
AttributeError: module 'calendar' has no attribute 'calendar'
```

### 原因

追記：理解できた。私が`calendar.py`を同一階層に作成してしまったせいで、標準ライブラリの`calendar.py`がimportされなくなったせい。

自作したファイルを`_calendar.py`とリネームしておくことで解決した。

名前重複が発生しているか否か、どこで、なぜ、発生したのか。気付けない。エラーも出ない。仕様と思われる。

Pythonのimportは使いづらくわかりにくく不便。大嫌い。

# 所感

名前重複の件で疲弊した。calendarライブラリがわかりにくく使いづらい。ローカライズされない(スペース数が多くてズレる)。

Pythonは一見して便利そうなライブラリが沢山ある。しかし完成度が低いという印象が強まった。カレンダーに関しては、名前の付け方、出力結果が残念。英語圏なら使えるのかもしれない。

