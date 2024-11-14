
#class asyncio.Event #1.事件对象
import asyncio

async def waiter( event): #传入一个事件对象
    print( 'Waiting for it ...')
    await event.wait() #2.wait()方法产生阻塞，除非使用set()方法将flag设置为True
    print( '... got it')

async def main():
    event =asyncio.Event() #创建一个Event对象
    waiter_task =asyncio.create_task( waiter( event))
    await asyncio.sleep(1)
    event.set()#3.Event对象会管理一个内部flag，初始状态为False，wait（）会产生阻塞，除非该flag==True, set()可以将其设置为True, clear()办法可以重置为False
    await waiter_task
asyncio.run( main())
#没看懂思密达，按理说 event.wait()产生了阻塞，set（）办法在其后面执行，肯定会一直阻塞，怎么还能打印出来 '...got it'呢。 难道这就是异步编程的魅力？整个时间线完全是无序的，每一步都可以出现在向后的任意一个时间点？

#4 clear()清空（取消）事件

#5. is_set() 检查事件是否被设置

