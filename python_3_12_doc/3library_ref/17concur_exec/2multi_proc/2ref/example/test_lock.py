#多进程写入同一个文件，所以必须用锁

from multiprocessing import Process, Lock

def f(l, i): #l是锁对象，i是要写入的数字
    with l: #上下文管理，自动获得锁，释放锁。 == l.acquire(),finally..., , l.release()
        with open('/home/master/doc/python_3_12_doc/library_ref/17concur_exec/2multi_proc/2ref/example/test.txt', 'a') as f:
            f.write( str(i) )
            f.flush() #加上 flush()真的可以了，太南崩了

if __name__=='__main__':
    lock = Lock()

    for num in range( 10):
        Process( target=f, args=( lock, num)).start()

#查看test.txt可以看到，顺序没变，我估计是这里的写入操作都不耗时（或者说，时间差不多）
