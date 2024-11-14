#1. 原始锁 是一个 锁定时 不属于 特定线程的同步基元组件

#2. 原始锁 处于“锁定” 或者 “非锁定“ 两种状态之一。创建时 非锁定。两个基本办法 acquire()和release()。 
#2.1 当状态是非锁定的时候, acquire()将锁的状态改为 锁定，并立刻返回。 
#2.2 当状态为锁定时候，acquire()将阻塞其他线程的调用
#2.3 release()只能在锁定状态下使用，它将锁的状态变为非锁定，并立刻返回

#3. 锁支持上下文管理

#4. class threading.Lock 不需要任何参数

#4.1 Lock.acquire( blocking=True, timeout=-1)

#4.2 Lock.release() 

#4.3 Lock.locked()

#
