import datetime
print(datetime.tzinfo.utcoffset(datetime.datetime.now()))#TypeError: descriptor 'utcoffset' requires a 'datetime.tzinfo' object but received a 'datetime.datetime'
