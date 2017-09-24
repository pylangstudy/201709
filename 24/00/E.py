from enum import Enum
class Color(Enum):
    RED = 100
    GREEN = 200
    BLUE = 300

from pickle import dumps, loads
print(Color.RED is loads(dumps(Color.RED)))

