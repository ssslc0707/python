import os
from multiprocessing import Process

class P:
    def __init__(self):
        print('pppp')
    def eles(self):
        print("eeee")
class MyProcess(P):

    def __init__(self,arg1):
        super().eles()
        self.arg1 = arg1
    def run(self):
        print(self.arg1)


if __name__ == '__main__':
    # print("主%s"%os.getpid())
    # process = MyProcess('adsad')
    # process.start()
    process = MyProcess(1)
    #process.start()



