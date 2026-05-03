import asyncio


async def q():
    print("Why cant programmers tell jokes?")
    await asyncio.sleep(3)


async def a():
    print("Timing!")


async def main():
    await asyncio.gather(q(), a())


asyncio.run(main())
