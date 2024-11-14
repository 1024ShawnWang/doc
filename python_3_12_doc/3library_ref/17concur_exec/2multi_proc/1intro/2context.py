
#1. 根据不同的平台， multiprocessing 支持三种启动进程的方法

#1.1 spawn
#1.2 fork
#1.3 forkserver

import multiprocessing as mp

def foo( q):
    q.put('hello')

'''1.
if __name__=='__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process( target=foo, args=(q,))

    p.start()
    print( q.get())
    p.join()
'''

#2
if __name__=='__main__':
    ctx = mp.get_context( 'spawn')
    q = ctx.Queue()

    p = ctx.Process( target=foo, args=(q,))
    p.start()
    print( q.get())
    p.join()

