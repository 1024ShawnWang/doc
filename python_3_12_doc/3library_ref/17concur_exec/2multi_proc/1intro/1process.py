
#1. 从multiprocessing中，创建Process对象，调用start()方法来生成进程。 类比 threading.Thread

from multiprocessing import Process

'''
def f( name):
    print('hello', name)

if __name__=='__main__':
    p = Process( target=f, args=('bob',))
    p.start()
    p.join()#结束
'''

import os

def info( title):
    print( title)
    print( 'module name: ', __name__)
    print( 'parent process: ', os.getppid())  #os.getppide()获得父进程的id
    print( 'process id: ', os.getpid())

def f( name):
    info( 'function f')
    print('hello', name)

if __name__ =='__main__':
    info('main line')
    p = Process( target=f, args=('bob',))
    p.start()
    p.join()

#可以看到 p 的父进程 就是 __main__ 的进程
