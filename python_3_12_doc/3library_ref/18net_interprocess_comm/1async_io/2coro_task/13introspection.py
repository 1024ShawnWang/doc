
#内省--自我省察

#1. asyncio.current_task( loop=None) #返回当前运行的Task实例，如果没有正在运行的任务就返回None

#2. asyncio.all_task( loop=None) #返回事件循环所运行的未完成的 Task对象集合

#3. asyncio.iscoroutine( obj) #obj要是协程对象就返回True否则False
