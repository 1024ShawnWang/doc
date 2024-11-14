#1. coroutine asyncio.to_thread( func, /, *args, **kwargs) #在不同的线程中异步地运行函数func

import time
import asyncio

def blocking_io():
    print(f'start blocking_io at {time.strftime('%X')}')
    time.sleep(1)
    print( f'blocking_io complete at {time.strftime('%X')}')

async def main():
    print(f'started main at {time.strftime('%X')}')

    await asyncio.gather(
        asyncio.to_thread( blocking_io), #使用单独的线程，运行可能阻塞事件循环的异步函数，避免阻塞
        asyncio.sleep( 1))
    
    print( f'finished main at {time.strftime('%X')}')



started main at 21:24:37
'''实际输出
start blocking_io at 21:24:37
blocking_io complete at 21:24:38
finished main at 21:24:38
'''
#注意看耗时操作结束的实际和主程序结束的时间是一致的，这就说明单独的线程运行耗时协程确实没有阻塞循环事件
asyncio.run( main())
