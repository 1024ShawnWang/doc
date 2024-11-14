
#1.如果一个对象可以在await 语句中使用，那么它就是可等待对象，主要有三大类可等待对象：协程，任务，Future
#可等待对象，应该是对低优先级，但是必须要完成的事情的抽象，比如生活中的一日三餐

import asyncio

#1.1 可等待对象之一：协程
async def nested(): #协程函数，返回一个协程对象
    return 42

async def main():
    #nested()#类似普通函数的直接调用并不会执行协程函数，还会抛出RutimeWarning，所以我给注释 了
    print( await nested()) #e接受42，并输出
asyncio.run( main())

#1.2 可等待对象之二：任务
async def main1():
    task =asyncio.create_task( nested())
    result=await task #可以被await使用
    print( result)
asyncio.run( main1())


#1.3 可等待对象之三：Future
#特殊的低层级的可等待对象，表示一个异步操作的最终结果
#所以当 一个Future对象被await时候，它会等待Future对象在别的地方都执行完毕，那么，Future对象，不能被await两次，否则会死锁
'''
async def main():
    await function_that_return_a_future_object()

    #或者这样写
    await async.gather( function_that_return_a_future_object(), some_python_coroutine())
'''    
