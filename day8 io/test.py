# f = open('我的.txt',mode='r',encoding='utf-8');
#
# print(f.read())
#
# f.close()
while 1:
    break_flag = 0;
    model = input("注册或者登陆,退出输入exit")
    if model == '注册':
        name = input("请输入姓名")
        password = input("请输入密码")
        print("注册成功：" ,name)
        with open('user.txt',mode='a+',encoding='utf-8') as f:
            f.write(name+' '+password+'\n')
    if model == '登陆':
        name = input('请输入用户名')
        with open('user.txt',mode='r',encoding='utf-8') as f:
            for i in f:
                split = i.split(' ')
                if name == split[0]:
                    for count in range(3):
                        password = input('输入密码')
                        if password+'\n' == split[1]:
                            print('登陆成功')
                            break_flag = 1
                            break
                        else:
                            print('密码错误！还有',2-count,'机会')
            if break_flag:
                break
            print('无此用户')
        if break_flag:
            break
    if model == 'exit':
        print('退出')
        break
