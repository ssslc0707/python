#fun = lambda x,y:x+y

#print(fun(1,2))



# fun = lambda x,y:list({x[i]:y[i]}for i in range(len(x)))
#
# print(fun((('a'),('b')),(('c'),('d'))))
# fu = lambda x:{x:x+1}
#
# print(list(map(fu,[1,2,3,3])))
#
# def m():
#     return (lambda x:i*x for i in range(4))  #[]和()的区别
# print([mu(2) for mu in m()])
# print(m())
t=((0,),)
print(t[0][0])