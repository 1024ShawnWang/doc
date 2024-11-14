
#asyncio.timeout( delay)#1.返回一个可被用于限制等待某个操作所耗费时间的 异步上下文管理器
'''
async def main():
    async with asyncio.timeout( 10):
        await long_running_task()
'''
#如果 long_running_task()耗费十秒以上完成，该上下文管理器将取消当前任务，并在内部处理引发的 asyncio.CancelledError，并将其转为可被捕获和处理的异常 TimeoutError
'''
async def main():
    try:
        async with asyncio.timeout( 10):
            await long_running_task()
    except TimeoutError:
        print( '长操作已经超时了，但是我们已经处理了')
    print('好了，这下语句无论如何都执行了')
'''

#2.class asyncio.Timeout( when)#2.撤销已过期的 异步上下文管理器
'''
async def main():
    try:
        async with asyncio.timeout( None) as cm:
            new_deadline = get_running_loop().time() +10
            cm.reschedule( new_deadline) #reschedule( when:float |None) 重新安排超时

            await long_running_task()
    except TimeoutError:
        pass

    if cm.expired():#expired() -> bool 返回上下文管理器是否超出时限
        print('looks like we haven't finished on time')
'''

#3.asyncio.timeout_at( when)
#类似于 asyncio.timeout() 不同之处在于when是停止等待的绝对时间，或者为None
'''
async def main():
    loop = get_running_loop() #获得当前协程绑定的循环事件
    deadline =loop.time() +20
    try:
        async with asyncio.timeout_at( deadline):
            await long_running_task()
    except TimeoutError:
        print('The long operation timed out, but we've handled it.')
    print( 'This statement will run regardless')
'''

#4. coroutine asyncio.wait_for( aw, timeout)等待aw可等待对象完成，指定timeout秒后超时
#如果timeout=None,那么会一直等到任务完成
'''
async def eternity():
    await asyncio.sleep( 3600)#休眠一小时
    print('yay!')

async def main():
    try:
        await asyncio.wait_for( eternity(), timeout=1.0) #由于timeout=1.0，那么最多等待一秒
    except TimeoutError:
        print('timeout')
asyncio.run( main())
'''
