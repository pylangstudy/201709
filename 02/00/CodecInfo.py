import codecs
codecInfo = codecs.lookup('utf')
print(codecInfo)
print(codecInfo.name)
print(codecInfo.encode)
print(codecInfo.decode)
print(codecInfo.incrementalencoder)
print(codecInfo.incrementaldecoder)
print(codecInfo.streamwriter)
print(codecInfo.streamreader)

text = '日本語'
print(codecInfo.name, text, codecInfo.encode(text))
print(codecInfo.name, codecInfo.encode(text), codecInfo.decode(text.encode(encoding='utf-8')))
