# (c) TICSIA
#
# 
import asyncio

async def my_corutine1():
    for i in range(100):
        print(f'#{i}')
        await asyncio.sleep(0.5)

async def my_corutine2():
    for i in range(100):
        print(f'*{i}')
        await asyncio.sleep(2)
        
async def main():
    task1 = asyncio.create_task(my_corutine1())
    task2 = asyncio.create_task(my_corutine2())
    await asyncio.gather(task1,task2)
    print('done')

asyncio.run(main())