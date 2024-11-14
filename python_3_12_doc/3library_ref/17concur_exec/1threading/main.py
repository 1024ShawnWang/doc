#0. 全都是 threading模块下的变量和方法

#1. threading.active_count() 返回当前存活的Thread对象的数量。

#2. threading.current_thread() 返回当前对应调用者的控制线程的 Thread 对象

#3. threading.excepthook( args, /) 处理由 Thread.run()引发的未捕获异常

#4. threading.__excepthook__ 

#5. threading.get_ident() 返回当前线程的 “线程标识符”

#6. get_native_id() 返回内核分配给当前线程的原生集成线程ID

#7. enumerate() 返回当前存活的 Thread 对象的列表

#8. main_thread() 返回主 Thread对象

#9. settrace( func) 为所有 threading 模块开始的线程设置 追踪函数

#10. settrace_all_thread( func)

#11. gettrace() 返回由 9 设置的 追踪函数

#12. setprofile( func)

#13. setprofile_all_threads( func)

#14. getprofile( ) 对比13

#15. stack_size( [size]) 返回创建线程时 使用的 堆栈大小

#16. TIMEOUT_MAX 阻塞函数

#17. 
