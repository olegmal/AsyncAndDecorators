import asyncio
from time import time


async def to_do_something(sec):
    await asyncio.sleep(sec)
    print("Result is", sec)


async def print_something(sec):
    await asyncio.sleep(sec)
    print(sec)
    await to_do_something(sec)

async def main():
    async  with asyncio.TaskGroup() as tg:
        for i in range(1, 10):
            tg.create_task(print_something(i))


start = time()
asyncio.run(main())
print(f"Це зайняло {time() - start} секунд часу ")
