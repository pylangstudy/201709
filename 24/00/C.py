from enum import Enum
class Foo(Enum):
    def some_behavior(self):
        pass
class Bar(Foo):
    HAPPY = 1
    SAD = 2
