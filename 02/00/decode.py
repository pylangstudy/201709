#!python3.6
#encoding:utf-8
import codecs
print('----- codecs.decode() -----')
for enc in ['utf-8', 'utf-16LE', 'utf-16BE', 'utf-32', 'shift-jis', 'euc-jp']:
    byte = '日本語'.encode(encoding=enc)
    print(byte, enc, codecs.decode(byte, encoding=enc, errors='strict'))
print('----- byte.deode() -----')
for enc in ['utf-8', 'utf-16LE', 'utf-16BE', 'utf-32', 'shift-jis', 'euc-jp']:
    byte = '日本語'.encode(encoding=enc)
    print(byte, enc, byte.decode(encoding=enc))

