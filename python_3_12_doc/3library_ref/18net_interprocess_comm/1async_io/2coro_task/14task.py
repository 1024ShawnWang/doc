#task任务的详细属性

#1. class asyncio.Task( coro, *, loop=None, name=None, context=None, eager_start=False) 非协程安全

#2. asyncio.create_task() / loop.creae_task() #创建

#3. cancle() #取消

#4. done() #如果Task对象已完成，就会返回True

#5. result() #返回Task结果

#6. exception() #返回Task对象的异常

#7. add_done_callback( callback, *, context=None) #添加一个回调，将在Task对象完成时被运行

#8. remove_done_callback( callback) #从回调列表中移除 callback

#9. get_stack( *, limit=None) #返回此Task对象的栈框架列表

#10. print_stack( *, limit=None, file=None)

#11. get_coro() #返回Task包装的协程对象

#12. get_context() #返回关联到该任务的 contextvars.Context对象

#13. get_name() #返回Task名称

#14. set_name()

#15. cancel( msg=None) #请求取消Task对象，在下一轮循环中将抛出CancelledError异常给被封包的协程
#看一下如何实现的
import asyncio

async def cancel_me():
    print( 'cancel_me()函数: 休眠前')

    try:
        await asyncio.sleep( 3600)#等待一小时
    except asyncio.CancelledError:
        print( 'cancle_me()函数:  取消休眠')
        raise
    finally:
        print( 'cancle_me()函数:  休眠后')

async def main():
    task =asyncio.create_task( cancel_me()) #创造 cancel_me任务

    await asyncio.sleep( 1)#休眠1秒

    task.cancel() #Task的 cancel()函数，用来取消所有未完成的任务

    try:
        await task
    except asyncio.CancelledError:
        print('main()函数中： cancel_me函数已经被取消了')

asyncio.run( main())
'''将会输出：
cancel_me()函数: 休眠前
cancle_me()函数:  取消休眠
cancle_me()函数:  休眠后
main()函数中： cancel_me函数已经被取消了
'''
#可以看到 cancel_me函数，实际上仍然被执行了一次。（毕竟是下一轮循环才能抛出异常）

#16. cancelled() #如果Task任务被取消， 就返回True（ 检查是否被取消了的）

#17. uncancel() #返回剩余的取消请求数量，没看懂思密达

#18. cancelling() #返回对此Task的挂起请求次数 == cancel()的调用次数-uncancel()的调用次数，同上，应该缺失了某些知识点，看不懂思密达
