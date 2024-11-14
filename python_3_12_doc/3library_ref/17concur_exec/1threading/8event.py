
#1. 事件对象，用于线程通信，一个线程发出事件信号，其他线程等待该信号

#2. 一个事件对象管理一个内部标识，调用set()办法，可将其设置为true。调用clear()方法可以将其设置为false
#调用wait()f办法，将进入阻塞直到标识为true

#3. class threading.Event实现事件对象的类

#3.1 is_set() 内部标识==true，就返回True

#3.2 set() 将内部标识设置为true，正在等待这个事件的线程将被唤醒

#3.3 clear() 将内部标识设置为 false

#3.4 wait( timeout=None) 只要内部标识==false，并且没有超出给定的timeout就保持阻塞

#3.5 
