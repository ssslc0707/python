# li = []
#
# while 1:
#     name = input('请输入员工名字,退出清输入 exit')
#     if name.__eq__('exit'):
#         break
#     li.append(name)
#
# print(li)

# li = ['a','b','c','d']
#
# li[0:2] = 'fr'
# print(li)

li = ['瑞源','123','abc']
li[2].upper()
print(','.join(li))
print(li[0])
li[2] = li[2].capitalize();
print(li)

# for i in range(0,10,-1):
#     print(i)

li = [1, 2, 3, 4, 5, 6, ['a', 'b', 'c', 'd'], 7]

print(type(li))
for i in li:

    if isinstance(i,list):
        for j in i:
            print(j)
        continue
    print(i)
