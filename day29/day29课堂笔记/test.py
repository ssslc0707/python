
#asdasdasdsafewgqedjuhnakjsdn去除s

list = [i for i in "asdasdasdsafewgqedjuhnakjsdn" if i !='s']
#print(list)

#123123.414safas659479.123fsdf76355.555123123 求和

import re

findall = re.findall('\d+\.\d+|\d+', "123123.414safas659479.123fsdf763555.55123123asd123")

#print(findall)
j = 0
h = 0
list = []
for i in range(1,5):
    j = i
    for x in range(1,5):
        if j == x:
            continue
        h = x
        for v1 in range(1,5):
            if v1 == j or v1 == h:
                continue
            list.append(j*100+h*10+v1)
print(list)
print(len(list))

