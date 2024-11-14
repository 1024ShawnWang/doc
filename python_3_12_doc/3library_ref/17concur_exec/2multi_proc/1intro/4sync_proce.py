
#1.multiprocessing 中的 Lock 对象。 确保进程同步（比如可以保证一个时间h只会有一个进程打印到标准输出)

from multiprocessing import Process, Lock

def f(l, i): #Lock l
    '''
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()
    '''
    #为什么不直接用 with lock 这个语句呢
    with l:
        print('hello world', i)
        

if __name__=='__main__':
    lock = Lock() #获得一个锁对象

    for num in range( 10):
        Process( target=f, args=(lock, num)).start()
