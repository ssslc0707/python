import socket

socket_socket = socket.socket()

connect = socket_socket.connect(('127.0.0.1', 9090))

socket_socket.send('sss'.encode('utf-8'))

socket_socket.recv(1024)

socket_socket.close()
