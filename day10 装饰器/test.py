
import time
import random
def get_runTime(fun):
    def inner(*count,**kwargs):
        start_time = time.time()
        print(start_time)
        ret = fun(*count,**kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return ret
    return inner

@get_runTime
def func(count):
    print('开始了')
    li = []
    for i in range(count):
        randint = random.randint(0, 10000)
        li.append(randint)
        #print(randint)
    li.sort()
    return 'mdzz'

def yufatang(f):

    print('语法糖测试')
    return f
@get_runTime
def func1():
    print('开始了')
    li = []
    for i in range(1000000):
        randint = random.randint(0, 10000)
        li.append(randint)
        #print(randint)
    li.sort()


def test1(*args):
    print(*args)
    print(args)
    #print(type(*args))
    print(type(args))
    def inner(*args):
        for i in args:
            print('inner ',i,type(i))
    inner(*args)
test1(1,2,2,3)
#test1(1)

for i in (1,2,3,4):
    print(i)