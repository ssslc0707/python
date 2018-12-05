class A:
    def __init__(self):
        self.x = 1
        print('in init function')
    def __new__(cls, *args, **kwargs):
        print('in new function')
        return object.__new__(A, *args, **kwargs)


# a = A()
#
# b = A()
class sing:
    single = None
    def __init__(self):
        print("init")
    def __new__(cls, *args, **kwargs):
        if cls.single == None:
            cls.single = object.__new__(A, *args, **kwargs)

        return cls.single
    def __iter__(self):
        return self
    def next(self):
        return self.single
max(sing)

# s = sing()
# s1 = sing()
# print(s)
# print(s1)
# print(s.__eq__(s1))
#
import hashlib
with open(file='2.进阶.py',mode='r+',encoding='utf-8') as f:
    str = ''
    for i in f:
        str+=i

md5 = hashlib.md5()
md5.update(bytes(str,'utf-8'))
print(md5.hexdigest())

