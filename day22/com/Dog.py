class Dog:
    def __init__(self,*args):
        self.name = args[0]
        self.age = args[1]
        self.sex = args[2]
        self.hp = args[3]
        self.aggr = args[4]

    def bite(self,person):
        person.hp -= self.aggr