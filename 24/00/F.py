from enum import Enum
class UserClass:
    class Color(Enum):
        RED = 100
        GREEN = 200
        BLUE = 300

from pickle import dumps, loads
print(UserClass.Color.RED is loads(dumps(UserClass.Color.RED)))

