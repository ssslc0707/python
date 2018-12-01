import time


class Foo:
    count = 0

    def __init__(self):
        Foo.count += 1


# foo = Foo()
# foo2 = Foo()
# foo3 = Foo()
# print(Foo.count)


# class F:
#     def fun(self):
#         print('func')
#
#
# f = F()
# f.fun()
# print(400*12*10)

class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
class Teacher:
    def __init__(self,birthday,person,classes):
        self.birthday = birthday
        self.person = person
        self.classes = classes
    def teach(self):
        print('%s老师开始上%s课'%(self.person.name,self.classes))
class Birthday:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def getDay(self):
        return time.strptime('%s-%s-%s'%(self.year,self.month,self.day),'%Y-%m-%d')


teacher = Teacher(Birthday('1994', '07', '07'), Person('slc', '25', '男'), 'mdzz')
teacher.teach()
print(teacher.birthday.getDay())


