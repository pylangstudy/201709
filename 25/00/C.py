from enum import Enum
class FieldTypes(Enum):
    name = 0
    value = 1
    size = 2
print(FieldTypes.value.size)
print(FieldTypes.size.value)
