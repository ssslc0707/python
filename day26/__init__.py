class Person:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name + "ss"


person = Person("slc")

print(person._Person__name)
print(person.__dict__)