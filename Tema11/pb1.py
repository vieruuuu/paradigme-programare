from asyncio import Queue, sleep, gather, run


async def task(name, queue: Queue):
    while not queue.empty():
        n = await queue.get()

        # sleep just a bit
        await sleep(0.001)

        result = 0

        for i in range(n):
            result += i

        queue.task_done()

        print(f"task {name}: {n} => {result}")


async def main():
    queue = Queue()

    for i in range(200):
        queue.put_nowait(i)

    await gather(task("1", queue), task("2", queue), task("3", queue), task("4", queue))


if __name__ == "__main__":
    run(main())
