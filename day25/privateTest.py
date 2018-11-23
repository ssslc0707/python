class Person:
    __key = 123
    def __init__(self,name,password):
        self.name = name
        self.__password = password


    def __getPassword(self):
        return self.__password


person = Person('slc', '123123')

print(person._Person.__password)

