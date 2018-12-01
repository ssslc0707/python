with open('我的.txt',mode='a+',encoding='utf-8') as f:
    f.seek(0)
    for i in f:
        print(i)