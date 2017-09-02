#!python3.6
#encoding:utf-8
import codecs

def text_iter():
    for i in range(5): yield f'日本語_{i}'

for byte in codecs.iterencode(text_iter(), encoding='utf-8'):
    print(byte, byte.decode())

