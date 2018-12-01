

dic = {'1':'s','2':'b'}

print(dic.items())
for i in dic:
    print(i + ':' + dic[i])
print('asdasd'.split())

li = [11,22,33,44,55,66,77,88,99,90]
dic = {'k1':[],'k2':[]}
for i in li:
    if i > 66:
        dic['k1'].append(i)
    else:
        dic['k2'].append(i)

print(dic)
