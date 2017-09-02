#!python3.6
#encoding:utf-8
import codecs

def byte_iter():
    for i in range(5): yield f'日本語_{i}'.encode()

for text in codecs.iterdecode(byte_iter(), encoding='utf-8'):
    print(text, text.encode())

