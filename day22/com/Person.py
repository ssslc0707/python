from slc.day22.com.Dog import Dog


class Person:
    country = 'china'
    def __init__(self,*args):

        self.name = args[0]
        self.age = args[1]
        self.sex = args[2]
        self.hp = args[3]
        self.aggr = args[4]

    def setContry(self,c):
        self.country = c
    def attack(self,dog):
        dog.hp -= self.aggr
        print('%s受到了攻击，失去了%s点血量'%(dog.name,self.aggr))

    def getBaseInfo(self):
        return '%s,%s岁，%s'%(self.name,self.age,self.sex)
    def shangshang(self):
        print('%s,上山去砍柴'%self.getBaseInfo())
    def drive(self):
        print('%s,开车去东北'%self.getBaseInfo())
    def baoj(self):
        print('%s,最爱大保健'%self.getBaseInfo())

# person = Person('slc', 26, '男',100,1)
# dog = Dog('heipi', 26, '男', 1000, 2)
# person.attack(dog)
# print(dog.hp)
xiaom = Person('小明', 10, '男', 100, 1)
laol = Person('老李', 90, '男', 100, 1)
xiaom.shangshang()
xiaom.drive()
xiaom.baoj()
laol.shangshang()
laol.drive()
laol.baoj()
