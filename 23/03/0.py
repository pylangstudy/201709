import json
import pprint
from urllib.request import urlopen
with urlopen('http://pypi.python.org/pypi/Twisted/json') as url:
    http_info = url.info()
    raw_data = url.read().decode(http_info.get_content_charset())
project_info = json.loads(raw_data)
pprint.pprint(project_info)

print('------------------------------')
pprint.pprint(project_info, depth=2)

print('------------------------------')
pprint.pprint(project_info, depth=2, width=50)
