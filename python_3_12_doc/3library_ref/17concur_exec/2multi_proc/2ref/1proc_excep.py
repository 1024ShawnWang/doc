
#1. class multiprocessing.Process( group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)

#1. run() 表示进程活动的办法，可以在子类中重写此方法
from multiprocessing import Process
p = Process( target=print, args=[ 1])
p.run()

#2. start() 启动进程活动， 每个方法每个进程 最多只能调用一次， 它会将对象的 run()方法安排在一个单独的进程中调用

#3. join( [ timeout])

#4. name 进程的名称。该名称是一个字符串

#5. is_alive()返回进程是否还活着

#6. daemon 进程的守护标志

#7. pid 返回进程ID

#8. exitcode 子进程的退出代码

#9. authkey 进程的身份验证密钥

#10. sentinel 系统对象的数字句柄，进程结束时候会变成ready

#11. terminate() 终结进程。

#12. kill()

#13. close()

#14. exception multiprocessing.ProcessError

#15. exception multiprocessing.BufferTooShort

#16. exception mutiprocessing.TimeoutError

#17. 
