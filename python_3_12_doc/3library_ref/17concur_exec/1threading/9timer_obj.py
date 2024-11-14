
#1. 定时器对象用来控制一个操作在等待一定时间后运行 Timer类是Thread类的子类

#2. 既然是子类，就会有相同的办法 通过Timer.start方法启动，通过cancel()方法来停止，定时器在执行其行动之前要等待的时间间隔 可能与程序员指定的时间间隔 不一定相同

from threading import Timer

def hello():
    print('hello, world')

t =Timer( 30.0, hello)
t.start()

#3. cancel() 停止定时器，并取消执行计时器将要执行的操作
