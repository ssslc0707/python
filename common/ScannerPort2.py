
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
from socket import *
import threading

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,startPort,endPort):
    global openNum
    for var in range(startPort,endPort):
        try:
            s = socket(AF_INET,SOCK_STREAM)
            s.connect((host,var))
            lock.acquire()
            openNum+=1
            print('[+] %d open' % var)
            lock.release()
            s.close()
        except:
            print('[+] %d close' % var)
            pass

def main():
    setdefaulttimeout(1)
    startNewThread(100,1000)

    time.sleep(20)
    print('[*] The scan is complete!')
    print('[*] A total of %d open port ' % (openNum))
def startNewThread(num,sum):
    oneDoTotal = sum//num
    for var in range(1,num-1):
        t = threading.Thread(target=portScanner,args=('192.168.1.13',(var-1)*oneDoTotal+1,var*oneDoTotal+1))
        threads.append(t)
        t.start()

    t = threading.Thread(target=portScanner,args=('192.168.1.13',(num-1)*oneDoTotal+1,sum))
    threads.append(t)
    t.start()

if __name__ == '__main__':
    x = 10
    y = 20
    print("hello", x, "ff", y)
    if x == y:
        print(True)
    else:
        print(2)