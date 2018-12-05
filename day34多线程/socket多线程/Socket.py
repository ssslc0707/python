import socket
from multiprocessing import Process




def getConn(conn):
    decode = conn.recv(1024).decode('utf-8')
    print(decode)
    encode = '>>>'.encode('utf-8')

    conn.send(encode)

    conn.close()

if __name__ == '__main__':
    socket_socket = socket.socket()

    socket_socket.bind(('127.0.0.1',9090))

    print('开始监听')
    listen = socket_socket.listen()
    while True:
        print('接收链接')
        conn,addr = socket_socket.accept()

        process = Process(target=getConn,args=(conn,))

        process.start()



