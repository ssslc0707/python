import random
#
# print(dir([].__iter__()))
# print([].__iter__().__dir__())
#
# print('randint' in dir( random))



li = [1,2,3,34]

iter = li.__iter__()
for i in range(iter.__length_hint__()):
    print(iter.__next__())


def myIt(li):
    iter = li.__iter__()
def myNext(li):
    for i in li:
        yield i


my_next = myNext(li)
while 1:
    print(my_next.__next__())




