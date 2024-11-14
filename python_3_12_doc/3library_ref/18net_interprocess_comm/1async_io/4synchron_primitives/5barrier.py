
#class asyncio.Barrier( parties)
'''
屏蔽是一个允许阻塞直到parties个任务在其上等待的简单同步原语。任务可以在wait()方法上等待，并将被阻塞直到有指定数量的任务在wait()上等待。在那时，所有正在等待的任务将同时撤销阻塞（ 水库）
'''
import asyncio
async def example_barrier():
    b =asyncio.Barrier( 3)

    #新建两个等待任务
    asyncio.create_task( b.wait())
    asyncio.create_task( b.wait())

    await asyncio.sleep( 0)
    print( b)

    await b.wait()
    print( b)
    print( 'barrier passed')

    await asyncio.sleep(0)
    print( b)

asyncio.run( example_barrier())
#没看懂思密达

#coroutine wait() #2.穿过屏障

#coroutine reset() #3.将屏障返回为默认状态

#coroutine abort() #4.使屏障处于已经被破坏状态

#parties #5.穿越屏障的数量

#n_waiting #6.执行填充时候正在等待的屏障数量

#broken #7.布尔值，值为True时表示栅栏是破损状态

#exception asyncio.BrokenBarrierError #runningtime异常的子类,在barrier对象重置时候仍有线程阻塞，和对象进入破损状态时引发
