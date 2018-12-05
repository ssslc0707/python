from multiprocessing import Process
import os
def funx(file,count):
    with open(file=file,mode='w') as f:
        f.write(count*10*'*')
if __name__ == '__main__':
    list = []

    for i in range(5):
        process = Process(target=funx, args=("file%s"%i, i))
        list.append(process)
        process.start()
    for p in list:p.join()

    print([i for i in os.walk('E:\pythonC\day34')])
