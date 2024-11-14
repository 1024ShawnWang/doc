#1. 同步原语，不如多线程的同步原语那样重要。废话，毕竟资源又不共享，没那么多问题

#2. class multiprocessing.Barrier( parties[, action[, timeout]])

#3. class multiprocessing.BoundedSemaphore( [value])

#4. class multiprocessing.Condition( [ lock])

#5. class multiprocessing.Event

#6. class multiprocessing.Lock #原始锁，但是非递归锁
#6.1 acquire( block=True, timeout=None) #阻塞 或者非阻塞 地获得锁
#6.2 release() 释放锁

#7. class multiprocessing.RLock
#7.1 acquire( block=True, timeout=None)
#7.2 release()

#8. class multiprocessing.Semaphore( [ value]) #一种信号量对象
#类比 threading.Semaphore，但是有些不同acquire()的第一个参数名，是和 Lock.acquire()一样的block
