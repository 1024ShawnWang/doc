
#1.什么叫协程， 子例程的更一般形式， 协程可以在不同的点上进入，退出，和恢复
#实现：通过 async def 来实现，会返回一个coroutine对象，可能包含  await, async for 和  async with关键字
#这个就叫协程函数，返回的对象就叫协程对象

import asyncio

async def main():
    print('happy')
    await asyncio.sleep( 1)
    print('birthday')

asyncio.run( main())

#print( main()) #2.对比普通函数，这里直接调用协程，并不会执行


#3. 三种机制执行协程
import time

async def say_after( delay, what):
    await asyncio.sleep( delay)#await是关键字
    print( what)

#3.1
async def main():
    print( f'starts at {time.strftime('%X')}')
    await say_after(1, 'happy')
    await say_after(2, 'birthday')
    print( f'ends at {time.strftime('%X')}')

asyncio.run( main())   #3.1通过 asyncio.run
print(['*']*8)

#3.2
async def main1():
    task1 =asyncio.create_task( say_after(1, 'happy'))    #通过asyncio.create_task 
    task2 =asyncio.create_task( say_after(2, 'birthday'))
    print( f'starts at {time.strftime('%X')}')
    await task1
    await task2
    print( f'ends at {time.strftime('%X')}')
asyncio.run( main1()) #运行的是main1() ，并发地执行，因此要快上一秒
print(['*']*8)


#3.3
print('第三种机制')
async def main2():
    async with asyncio.TaskGroup() as tg:#通过 asyncio.TaskGroup是2更现代化代替 ，注意是调用TaskGroup()

        '''原文的这种写法当然可以，我想说的是，下面的写法也凑效 
        tk1 =
        tk2 =
        '''

        tg.create_task( say_after(1, 'happy'))
        tg.create_task( say_after(2, 'birthday'))

        print( f'starts at {time.strftime('%X')}')
    #await task隐式地执行了
    print( f'ends at {time.strftime('%X')}')
asyncio.run( main2())
