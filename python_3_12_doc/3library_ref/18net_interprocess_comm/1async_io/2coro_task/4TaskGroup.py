import asyncio

#class asyncio.TaskGroup #1
    #create_task( coro, *, name=None, context=None) #1.1直接类比asyncio.create_task也有一个创建任的方法

'''eg
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 =tg.create_task( some_coro)
        task2 =tg.create_task( some_coro)

'''

#2.如何终结一个任务组
from asyncio import TaskGroup

class TerminateTaskGroup( Exception): #继承一个异常类
    """Exception  raised to terminate a  task group."""

async def force_terminate_task_group():
    raise TerminateTaskGroup()
    
async def job( task_id, sleep_time):
    print( f'Task {task_id}: start')
    await asyncio.sleep( sleep_time)
    print( f'Task {task_id}: done')


async def main():
    try:
        async with TaskGroup() as group:
           #生成一些任务 
           group.create_task( job(1, 0.5))
           group.create_task( job(1, 1.5))
           #休眠一秒
           await asyncio.sleep( 1)
           #终结任务组
           group.create_task( force_terminate_task_group())#会抛出异常
    except* TerminateTaskGroup:#可以对异常进行一些处理
        pass
asyncio.run( main())
'''预期输出
Task 1: start
Task 2: start
Task 1: done
'''
#可以看到Task2并没有运行到结束就被结了，即使Task2任务是在终结任务前面被添加的，这是因为异步程序的原因，它存活时间线是单向无序的
#可以在往后的任何时间点开始，结束，恢复，这就是协程的意义
