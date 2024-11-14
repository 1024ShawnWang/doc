#1. multiprocessing.active_children() 返回当前进程存活的子进程的列表

#2. multiprocessing.cpu_count() 返回系统的cpu数量
import multiprocessing
print( multiprocessing.cpu_count())

#3. multiprocessing.current_process() 返回与当前进程相对应的 process 对象

#4. multiprocessing.parent_process()

#5. multiprocessing.freeze_support() 为了使用 multiprocessing的程序，提供冻结以产生windows可执行文件的支持

#6. get_all_start_methods() 返回由受支持的启动方法组成的列表

#7. get_context( method=None) 返回一个Context对象

#8. multiprocessing.get_start_method( allow_none=False) 返回启动进程时使用的启动方法名

#9. set_executable( exe) #设置在启动子进程时要使用的 python解释器

#10. set_forkserver_preload( module_names)

#11. set_start_method( method, force=False)

#12. 
