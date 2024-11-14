
#asyncio.run( coro, *, debug=None, loop_factory=None) 执行coro，并返回结果

import asyncio

async def main():
    await asyncio.sleep( 1)
    print( 'hello, world')

asyncio.run( main())

