
#1.coroutine asyncio.wait( aws, *, timeout=None, return_when=ALL_COMPLETED)#并发的运行aws可迭代对象中的Futuren和Task实例，并进入阻塞状态知道满足return_when所指定的条件

#2.return_when可以选择三个常量 FIRST_COMPLETED, FIRST_EXCEPTON, ALL_COMPLETED

#3.asyncio.as_completed( aws, *, timeout=None)
