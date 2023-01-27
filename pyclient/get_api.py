import aiohttp
import asyncio
import time
import schedule

start_time = time.time()



async def get_pokemon(session, url):
    async with session.get(url) as resp:
        print(resp.status)
        return resp.status


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, 10):
            await asyncio.sleep(0.1)
            url = 'https://varzesh3.com/'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)

def job(a):
    asyncio.run(main())
schedule.every().minutes.do(job)

while True:
    b=schedule.run_pending()
    print(b)
    print("--- %s seconds ---" % (time.time() - start_time))




# import aiohttp
# import asyncio
# import time

# start_time = time.time()



# async def main():

#     async with aiohttp.ClientSession() as session:

#         for url in urls:
#             async with session.get(url) as resp:
#                 print(resp.status)

# asyncio.run(main())
# print("--- %s seconds ---" % (time.time() - start_time))
