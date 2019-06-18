import time as time
import threading as t
class MyThread(t.Thread):
    def __init__(self,tid):
        t.Thread.__init__(self)
        #self.name=name
        self.tid=tid
    def run(self):
        for i in range(5):
            time.sleep(2)
            print(self.getName())
t1=MyThread(100)
t2=MyThread(101)
t1.start()
t2.start()

    


        
