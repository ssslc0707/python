import socket

s = socket.socket()

s.bind(("127.0.0.1",8000))

s.listen()


def xx(url):
    return b"hello python"


url_func = [
    ("/xx", xx),
]


# 写一个死循环,一直等待客户端来连我
while 1:
    # 获取与客户端的连接
    conn, _ = s.accept()
    # 接收客户端发来消息
    data = conn.recv(8096)
    # 把收到的数据转成字符串类型
    data_str = str(data, encoding="utf-8")  # bytes("str", enconding="utf-8")
    # print(data_str)
    # 用\r\n去切割上面的字符串
    l1 = data_str.split("\r\n")
    # print(l1[0])
    # 按照空格切割上面的字符串
    l2 = l1[0].split()
    url = l2[1]
    # 给客户端回复消息
    conn.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    # 想让浏览器在页面上显示出来的内容都是响应正文

    # 根据不同的url返回不同的内容
    # 去url_func里面找对应关系
    for i in url_func:
        if i[0] == url:
            func = i[1]
            break
    # 找不到对应关系就默认执行f404函数

    # 拿到函数的执行结果
    response = func(url)
    # 将函数返回的结果发送给浏览器
    conn.send(response)
    # 关闭连接
    conn.close()

