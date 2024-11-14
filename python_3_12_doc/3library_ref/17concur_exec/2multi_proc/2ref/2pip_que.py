#1. 使用多进程的时候，一般使用消息机制来实现进程通信，尽可能避免使用同步原语

#1.1 消息机制包括 Pipe(两个进程） 以及 Queue 队列( 上下游进程）

#1.2 与其他python队列实现的区别之一，在于 multiprocessing队列会使用 pickle来 序列化所有被放入的对象，返回的对象是重新放入的对象，它不会和原始对象共享内存 （估计是为了网路通信做准备的）

#2. multiprocessing.Pipe( [ duplex]) 返回一对 Connection 对象 ( conn1, conn2) 分别表示管道的两端

#3. class multiprocessing.Queue( [ maxsize]) 返回一个使用一个管道和少量 锁和信号量实现的共享队列实例
#当一个进程 将一个对象放进队列中， 一个写入线程会启动并将对象从缓冲区写入管道

#4. qsize() #返回队列的大致长度

#5. empty() #如果队列是空的，返回True

#6. full() #如果队列是满的，返回True

#7. put( obj[ , block[, timeout]]) 将obj放入队列

#8. put_nowait( obj) == put( obj, False)

#9. get( [ block[, timeout]]) 对比7

#10. get_nowait() 对比8

#11. close() 指示当前进程将不会再往队列中放入对象

#12. join_thread() 等待后台线程

#13. cancel_join_thread() #防止 join_thread()方法阻塞当前进程

#######################################################
#1. class multiprocessing.SimpleQueue 简化的 Queue类的实现，很像带锁的 Pipe

#2. close() 关闭队列，释放内部资源

#3. empty() 

#4. get()

#5. put( item)

##############################################################
#1. class multiprocessing.JoinableQueu( [ maxsize]) #Queue的子类，额外添加了一些方法

#2. task_done() 指出之前进入队列的任务已经完成。

#3. join() 阻塞到队列中所有的元素都被接收和处理完毕

#4. 
