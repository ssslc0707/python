# def generator():
#     print(1)
#     num = yield 'a'
#     print(num)
#     print(2)
#     num2 = yield 'b'
#     yield
#
# g = generator()
#
#
# print(g.__next__())
# print(g.send(111))
# print(g.send(111))

# def init(fun):
#     def inner(*args,**kwargs):
#
#         f = fun(*args,**kwargs)
#         f.__next__()
#         return f
#     return inner
#
# @init
# def getDyAvg():
#     sum = 0
#     count = 0
#     avg = 0
#     while 1:
#
#         num = yield avg
#
#         sum += num
#         count += 1
#         avg = sum/count
#
#
# avg = getDyAvg()
# print(avg)
# print(avg.send(10))
#
# print(avg.send(20))
#
# print(avg.send(30))
#
# print(avg.send(0))
# print(avg.send(10))
# g = (i*i for i in range(10))
#
# for i in g:
#     print(i)
# def demo():
#     for i in range(4):
#         yield i
#
# g=demo()
#
# g1=(i for i in g)
# g2=(i for i in g1)
# for i in g1:
#     print(i)
# print(type(g1))
# print(list(g1))
# print(list(g2))

def add(n,i):
    print(n,i)
    return n+i

def test():
    for i in range(4):
        yield i

g=test()
for n in [1,10]:
    #print(n)    #1,2,3,4     11,12,13,14
    g=(add(n,i) for i in g)
    print('退出',n)
    #print(n,list(g))

print('zuihou',list(g))
