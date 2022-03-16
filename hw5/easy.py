# import aiohttp
import argparse
import asyncio
import pip

try:
    import aiohttp
except:
    !pip install aiohttp
    import aiohttp

#####
# из лекции
# async def download_site(url, session):
#     async with session.get(url) as response:
#         print(f"Read {response.content.total_bytes} from {url}")
#         return response.content.total_bytes
#
# async def download_all_sites(sites):
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for url in sites:
#         task = asyncio.create_task(download_site(url, session))
#         tasks.append(task)
#     return await asyncio.gather(*tasks)
#####

params = {'url': 'https://picsum.photos/id/',
          'dream': 1}


async def download_site(url, session, path):
    async with session.get(url) as response:
        with open(f'{path}/{url}.png', "bw") as f:
            f.write((await response.content.read()))
        time.sleep(params['dream'])


async def download_all_sites(n, path):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in range(int(n)):
            task = asyncio.create_task(download_site(str(params['url']) + str(url) + '/200', session, path))
            tasks.append(task)
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', default=1, help='number of files')
    parser.add_argument('-path', default='artifacts/easy', help='saving path')
    args = parser.parse_args()

    asyncio.run(download_all_sites(args.n, args.path))
