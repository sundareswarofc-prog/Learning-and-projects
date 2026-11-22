# import asyncio

# --------------------------------- Example for concurrency ------------------------------------------

# async def first():
#     print("1")
#     await asyncio.sleep(1)
#     print("2")

# async def second():
#     print("3")
#     await asyncio.sleep(1)
#     print("4")

# async def main():
#     await asyncio.gather(first(),second())


# asyncio.run(main())

from multiprocessing import Process
import os
import sys

# --------------------------------- Example for Parallelism ------------------------------------------


# print(sys._is_gil_enabled())

def task_1():
    print("task_1",os.getpid())
def task_2():
    print("task_2",os.getpid())

if __name__=="__main__":
     p1=Process(target=task_1)
     p2=Process(target=task_2)

     p1.start()
     p2.start()

     p1.join()
     p2.join()