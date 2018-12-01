from slc.day24.A import A


class B(A):
    def __init__(self,age,name,sex):
        A.__init__(self,age,name)
        self.sex = sex

    def show(self):
        A.show(self)
        self.f = 3


b = B(25, 'slc', 'nan')

b.show()
print(b.f)