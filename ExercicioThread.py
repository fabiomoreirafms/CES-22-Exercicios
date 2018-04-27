import threading
import time
import random

class market(object):
    lock = threading.RLock()

    def __init__(self):
        self.total_items = 0

    def add(self,n):
        self.lock.acquire()
        self.total_items = n
        self.lock.release()

    def remove(self):
        self.lock.acquire()
        saida = self.total_items
        self.lock.release()
        return saida


def producer(box, inputs, index):
    while inputs > 0:
        item = random.randint(0,256)
        print("Producer notify: item N{0} adicionado por {1}".format(item, index))
        box.add(item)
        time.sleep(1)
        inputs -= 1

def consumer(box, outputs,index):
    if outputs > 0:
        item = box.remove()
        print ("Consumer notify: {0} retirado por {1}".format(item, index))
        time.sleep(1)
        outputs-=1

if __name__=="__main__":
    inputs = 10
    box = market()
    t1 = threading.Thread(target=producer, args = (box,inputs, 1))
    t2 = threading.Thread(target=consumer, args=(box, inputs,2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()