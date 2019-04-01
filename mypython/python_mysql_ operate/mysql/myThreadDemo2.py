#
#
#
import threading

class Demo(threading.Thread):
    def run(self):

           print(10)
d1 = Demo()

d2 = Demo()

d1.start()
d2.start()



