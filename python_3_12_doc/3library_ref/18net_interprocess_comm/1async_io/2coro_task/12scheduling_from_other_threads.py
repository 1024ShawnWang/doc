
# asyncio.run_coroutine_threadsafe( coro, loop) #向指定事件循环提交一个协程（ 线程安全)
# return concurrent.futures.Future 以等待来自其他os线程的结果

import asyncio

'''
coro = asyncio.sleep( 1, result=3) #新建一个协程
future =asyncio.run_coroutine_threadsafe( coro, loop)#提交coro协程到指定循环
assert future.result( timeout) ==3 #在指定超时选项情况下，等待结果？？
'''

#没看懂，下面的也没看懂，略过这个函数

