import threading
import time
import random

class queue(object):
    lock = threading.RLock()
    def __init__(self):
        self.item = -1

    def add(self, n):
        self.lock.acquire()
        self.item = n
        self.lock.release()

    def remove(self):
        self.lock.acquire()
        saida = self.item
        self.item = -1
        self.lock.release()
        return saida


def producer(queue, inputs, index):
    while inputs > 0:
        item = random.randint(0,256)
        print("Producer notify: item N{0} adicionado por {1}".format(item, index))
        queue.add(item)
        time.sleep(1)
        inputs -= 1

def consumer(queue, index):
    global inputs
    while inputs > 0:
        item = queue.remove()
        if item>=0:
            print ("Consumer notify: {0} retirado por {1}".format(item, index))
        inputs-=1

if __name__=="__main__":
    inputs = 10
    queue = queue()
    t1 = threading.Thread(target=producer, args = (queue,inputs, 1))
    t2 = threading.Thread(target=consumer, args=(queue, 2))
    t3 = threading.Thread(target=consumer, args=(queue, 3))
    t4 = threading.Thread(target=consumer, args=(queue, 4))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()