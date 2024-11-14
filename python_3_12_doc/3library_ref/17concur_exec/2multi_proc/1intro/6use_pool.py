
# Pool类表示一个工作进程池。 有几种不同的方式将任务分配到工作进程的办法

from multiprocessing import Pool, TimeoutError
import time
import os

def f( x):
    return x*x

if __name__ =='__main__':
    with Pool( processes=4) as pool:#启动四个线程

        print( pool.map( f, range(10)))

        for i in pool.imap_unordered( f, range(10)): #随机输出一些数字
            print( i)
        
        res = pool.apply_async( f, (20,)) #每次h只允许一个线程允许f，返回平方

        print( res.get( timeout=1))

        #eval 'os.getpid()' asynchronously
        res = pool.apply_async( os.getpid, ()) #同上
        print( res.get( timeout=1))

        multiple_results = [ pool.apply_async( os.getpid, ()) for i in range(4) ]
        print( [res.get( timeout=1) for res in multiple_results])

        res = pool.apply_async( time.sleep, (10,))

        try:
            print( res.get( timeout=1))
        except TimeoutError:
            print( 'we lacked patience and got a multiprocessing. TimeoutError')
        print( '这个时刻，pool中仍有可用的进程')

    print( 'pool关闭， 不再可用')
    
#这个包中的功能要求子进程可以导入 __main__模块。这样的话，命令行就不能运行了
