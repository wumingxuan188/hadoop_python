import _thread
import threading
import time


def hell():
    # 获取当前线程名称
    name = threading.currentThread().getName()
    # 获取当前时间
    ctime = time.ctime()

    print(ctime)
    print("hello word,"+name)

# 开启一个新线程
_thread.start_new(hell,())
_thread.start_new(hell,())

# 休眠5秒
time.sleep(5)
