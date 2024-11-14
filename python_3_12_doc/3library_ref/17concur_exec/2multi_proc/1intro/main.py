
#1. 和多线程的api类似，但是线程共享信息，进程不会，因此增加了Pool对象，用来进程通信

from multiprocessing import Pool

def f( x):
    return x*x


if __name__=='__main__':
    with Pool( 5) as p:
        print( p.map( f, [ 1, 2, 3]))
