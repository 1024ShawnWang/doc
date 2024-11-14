
#class asyncio.Runner( *, debug=None, loop_factory=None)

import asyncio

async def main():
    await asyncio.sleep( 1)
    print('hello')

with asyncio.Runner() as runner:
    runner.run( main())

#2. run(coro, *, context=None) #如上

#3. close() #关闭运行器

#4. get_loop() #返回关联到运行器的循环事件上


#处理键盘中断
#没看懂思密达
