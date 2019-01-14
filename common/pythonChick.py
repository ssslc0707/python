import threading
from time import sleep

import pyHook
import pythoncom
from pymouse import PyMouse



def chick():
    mouse = PyMouse()
    position = mouse.position()
    print(position)
    while 1:
        mouse.click(position[0],position[1])
        sleep(1)
def onKeyboardEvent(event):
    if str(event.Key) == 'S': #按下键盘S启动自动点击
        t = threading.Thread(target=chick)
        t.setDaemon(True) #设置主线程结束时自动杀死子线程
        t.start()
    if str(event.Key) == 'E': #按下键盘E退出程序
        exit()
    return True
hm = pyHook.HookManager()
hm.KeyDown = onKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()

#需要安装PyMouse pyHook