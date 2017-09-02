#!python3.6
#encoding:utf-8
import codecs

text = '日本語'
for enc in ['utf-8', 'utf-16LE', 'utf-16BE', 'utf-32', 'shift-jis', 'euc-jp']:
    print(enc, codecs.getreader(enc))

