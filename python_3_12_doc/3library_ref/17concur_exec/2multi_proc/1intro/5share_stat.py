
#1. 并发编程，使用多线程的时候，应该尽量避免进程共享信息（ 不如用多线程了）
#2. 非要共享一些数据的时候， multiprocessing提供了两个办法
#2.1 使用 Value，或者 Array将数据存储在共享内存映射中
#2.2 使用 Server process

from multiprocessing import Process, Value, Array

'''
def f(n, a):
    n.value = 3.1415926
    for i in range( len(a)):
        a[i] = -a[i]

if __name__ =='__main__':
    num = Value( 'd', 0.0)  # 'd'和'i' 参数是 array模块 使用的类型的 typecode : 'd'是双精度，'i'表示有符号整数
    arr = Array( 'i', range( 1))

    p = Process( target=f, args=(num, arr))
    p.start()
    p.join()

    print( num.value)
    print( arr[:])
'''

#2 server process
#由 Manager()返回的管理器对象控制一个服务进程，该进程保存python对象，并允许其他进程使用代理操作它们
#返回的管理器支持类型： list, dict, Namespace, Lock, Rlock,

from multiprocessing import Process, Manager
def f(d, l): #传入一个字典和列表
    d[1] ='1'
    d['2'] =2
    d[0.25] =None
    l.reverse()

if __name__=='__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list( range(10))

        p = Process( target=f, args=(d,l)) #改变d, l的内容
        p.start()
        p.join()

        print( d)
        print( l)
