
#1 Thread类 代表 一个在独立控制线程中运动 的活动。
#1.1 有两种创建方式 1.1.1 向构造器传递一个可调用对象 1.1.2 在l子类中重载 run()方法。换句话说，只能重载这个类的 __init__() 和 run()方法 来创造 Thread 对象

#2. 线程对象一旦被创建，其运行必须通过 调用线程的 start()方法开始。这会在独立控制的线程中 调用run()方方法？ 那按照第一个，不会重新 新建一个对象吗？

#3. 一旦活动开始， 线程就会被认为是 存活的， 当run（）方法结束，就会死亡  is_alive()可以用来检测

#4. 其他线程可以调用 join()方法，这回阻塞调用该方法的线程，直到被调用 join()方法的线程终结

#5. 线程有名字。 名字可以传递给构造函数，也可以通过 name 属性读取或者修改

#6. run()方法引发异常的话，则会调用threading .excepthook()来处理它。

#7. 一个线程可以标记为 守护线程。当剩下的线程都是守护线程，整个python程序就会终止

#8. 有个 主线程 对象，这对应python程序里面初始的控制线程。 它不是一个守护线程

#1. class threading.Thread( group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
#1.1 group 应该为 None 保留给将来实现 ThreadGroup 类的扩展使用
#1.2 target 是用于 run()方法调用的可调用对象
#1.3 name 是线程名称
#1.4 args 用于发起调用目标函数的 参数列表或者元组
#1.5 kwargs 于调用目标函数的关键字参数字典。
#1.6 daemon 如果不=None ，那么这个Thread对象就是守护模式, None的情况下，继承当前线程的守护模式

#2. start() 开始线程活动
#2.1 它在线程活动中，只能被调用一次
#2.2 它安排对象的run()方法，在一个独立的控制线程中被调用 （它不会直接执行程序，而是一分为二，分出来的去执行，自己继续往前走
#2.3 方法调用次数 >1，会报错 RuntimeError

#3. run() 
#标准的 run()方法会 对作为 target参数 传递给该对象构造器 的 可调用对象（如果存在） 发起调用,
from threading import Thread
t = Thread( target=print, args=[1])
t.run()#将调用 print函数，并将args传入
h = Thread( target=print, args=(1,))
h.run()

#4. join( timeout=None) 等待，直到线程终结,会调用共阻塞这个方法的线程，直到调用join()的线程终结
#4.1 timeout的单位是秒
#4.2 当

#5. name

#6. getName()

#7. setName()

#8. ident 这个线程的 线程标识符

#9. native_id

#10. is_alive()

#11. daemon

#12. isDaemon()

#13. setDaemon() 被弃用

#14. 
