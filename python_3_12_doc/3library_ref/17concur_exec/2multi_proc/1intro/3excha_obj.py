
#1. mutiprocessing.Queue 用于在不同线程中交换消息的对象

'''1.1
from multiprocessing import Queue, Process

def f( q):
    q.put( [42, None, 'hello'])

if __name__=='__main__':
    q = Queue()

    p = Process( target=f, args=(q,))
    p.start()

    print( q.get()) #Queue的get()方法
    p.join()
'''

#2
from multiprocessing import Process, Pipe
def f( conn):
    conn.send( [42, None, 'hello'])
    conn.close()

if __name__=='__main__':
    parent_conn, child_conn =Pipe() #返回一个由管道连接的连接对象，默认是双工（双向的）。
    #p = Process( target=f, args=( child_conn))#进程由child_conn发送了一个列表 #child_conn要加逗号，不然不是一个元组了
    p = Process( target=f, args=( child_conn,))#进程由child_conn发送了一个列表
    p.start() #正式开始进程

    print( parent_conn.recv()) # 父端（另一端） 接收
    
    p.join() #让主进程等待自己结束

