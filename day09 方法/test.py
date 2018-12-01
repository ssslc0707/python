#
# def F(*args):
#     print(args)
#
# li = [11,22,33,44]
# F(li)
# F(*li)
# F()

def my_max(a,b):
    return a if a > b else b


#函数嵌套
# def func():
#     a=1
#     def funx():
#         a=2
#         def funz():
#             nonlocal a
#             print(a)
#
#         funz()
#     funx()
# func()

def closure():
    a = 1
    def inner():
        return a + 1
    return inner()
print(closure())
