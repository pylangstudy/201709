from enum import Enum, unique
@unique
class Mistake(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 3 #ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE
