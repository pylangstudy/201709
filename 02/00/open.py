#!python3.6
#encoding:utf-8
import codecs
text = '日本語'
print('----- codecs.encode() -----')
for enc in ['utf-8', 'utf-16LE', 'utf-16BE', 'utf-32', 'shift-jis', 'euc-jp']:
    print(text, enc, codecs.encode(text, encoding=enc, errors='strict'))
    with open(f'test_files/{enc}.txt', 'wb') as f:
        f.write(codecs.encode(text, encoding=enc, errors='strict'))
print('----- codecs.open() -----')
for enc in ['utf-8', 'utf-16LE', 'utf-16BE', 'utf-32', 'shift-jis', 'euc-jp']:
    with codecs.open(f'test_files/{enc}.txt', encoding=enc) as f:
        print(f.read())

