import multiprocessing
import threading
import time
import random

def comparador(func, *args):
    t1 = time.time()
    m1 = multiprocessing.Process(target=func, args=(args))
    m2 = multiprocessing.Process(target=func, args=(args))
    m1.start()
    m2.start()
    m1.join()
    m2.join()
    t2 = time.time()

    t3 = time.time()
    T1 = threading.Thread(target=func, args=(args))
    T2 = threading.Thread(target=func, args=(args))
    T1.start()
    T2.start()
    T1.join()
    T2.join()
    t4 = time.time()

    return [t2-t1, t3-t4]

def square (array):
    for i,num in enumerate (array):
        array[i] = num*num

def saque (valor):
    global conta
    conta -= valor
    print (conta)

conta = 500
if __name__ == '__main__':
    vetor=[]
    for i in range (200):
        vetor.append(random.randint(0, 200))
    print (comparador(square, vetor))

    print (comparador(saque, 200))