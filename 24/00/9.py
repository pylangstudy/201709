from enum import Enum
class Mood(Enum):
    FUNKY = 1
    HAPPY = 3
    def describe(self):
        # self is the member here
        return self.name, self.value
    def __str__(self):
        return 'my custom str! {0}'.format(self.value)
    @classmethod
    def favorite_mood(cls):
        # cls here is the enumeration
        return cls.HAPPY

print(Mood.favorite_mood())
#print(Mood.describe())#TypeError: describe() missing 1 required positional argument: 'self'd())
#print(Mood().describe())#TypeError: __call__() missing 1 required positional argument: 'value'
#print(Mood())#TypeError: __call__() missing 1 required positional argument: 'value'
print(str(Mood.FUNKY))
