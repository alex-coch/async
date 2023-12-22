import asyncio
from asyncio import Runner
from asyncio import sleep


async def main():
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")


async def task_coro1():
    print("Hello from first coro")
    await sleep(1)


# another example coroutine
async def task_coro2():
    print("Hello from second coro")
    await sleep(1)


if __name__ == "__main__":
    asyncio.run(main())

    # entry point of the program
    with Runner() as runner:
        # execute the first coroutine
        runner.run(task_coro1())
        # execute the second coroutine
        runner.run(task_coro2())
