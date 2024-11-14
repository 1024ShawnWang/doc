
#coroutine asyncio.sleep( delay, result=None) #1.返回一个协程对象

'''
1.1 如果设置了result, 那么协程完成，将将返回给调用者
1.2 sleep()总是会挂起当前任务，以便允许其他程序运行
1.2 delay设置为0是有意义的，它将提供一个优化路径用来允许其他程序运行,避免长期运的函数阻塞事件循环
'''

import asyncio
import datetime

async def display_date():
    loop =asyncio.get_running_loop() #假设为0时刻，那么 end_time就是 时刻5, 
    print( type(loop))
    end_time = loop.time() +5.0
    while True:
        print( datetime.datetime.now())
        if (loop.time() +1.0) >= end_time: #loop.time()应该就是获取当前循环的时间，所以循环5次
            break #?没看懂过
        await asyncio.sleep( 1)
asyncio.run( display_date())
