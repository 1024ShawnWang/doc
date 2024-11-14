
#awaitable asyncio.shield( aw)#防止可等待对象被屏蔽（取消）

'''
task =asyncio.create_task( something())
res =await shield( task)
'''
#上面的语句和下面的语句基本相同
#res =await something()
#但是，如果包含它的协程被取消，在something()中运行的任务并不会取消
#从something()的角度来看，取消操作并没有发生，但是它的调用者已经被取消，因为await会引发 CancelledError
#看不懂思密达
