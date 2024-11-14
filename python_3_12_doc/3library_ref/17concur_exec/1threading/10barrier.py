#1. 栅栏类提供一个简单的同步原语，用于应用固定数量的线程需要彼此相互等待的情况。线程调用wait方法将阻塞，直到所有线程都调用了wait方法。此时，所有线程都将同时被释放

#2. class threading.Barrier( parties, action=None, timeout=None) 创建一个需要 parties个线程的栅栏对象。如果提供了可调用的 action参数，它会在所有线程中被释放时， 在其中一个线程自动调用

#2.1 wait( timeout=None) 冲出栅栏。当所有对象都冲出栅栏就会被一起释放

#2.2 reset()重置栅栏为默认初始态

#2.3 abort() 破坏栅栏

#2.4 parties 栅栏围住的线程数量

#2.5 n_waiting 当前时刻正在栅栏中阻塞的线程数量

#2.6 broken 一个布尔值，值为True时候表明栅栏为破损态

#2.7 exception threadign.BrokenBarrierError 异常类, RuntimError异常的子类
