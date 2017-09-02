#!python3.6
#encoding:utf-8
import codecs
text = '日本語'
print('----- codecs.encode() -----')
for enc in ['utf-8', 'utf-16LE', 'utf-16BE', 'utf-32', 'shift-jis', 'euc-jp']:
    print(text, enc, codecs.encode(text, encoding=enc, errors='strict'))
print('----- str.encode() -----')
for enc in ['utf-8', 'utf-16LE', 'utf-16BE', 'utf-32', 'shift-jis', 'euc-jp']:
    print(text, enc, text.encode(encoding=enc))

