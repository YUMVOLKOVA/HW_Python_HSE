# import aiohttp
import argparse
import asyncio
import pip
import time

try:
    import aiohttp
except ModuleNotFoundError:
    pip.main(['install', "aiohttp"])
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
          'dream': 1.5}


async def download_site(url, session, path):
    print(f'current url: {url}')
    async with session.get(url) as response:
        with open(f'{path}/{url.replace("https://", "").replace("/", "_").replace(".", "_")}.jpg', "bw") as f:
            f.write((await response.read()))
    time.sleep(params['dream'])


async def download_all_sites(n, path):
    async with aiohttp.ClientSession() as session:
        print('start')
        tasks = []
        for url in range(int(n)):
            task = asyncio.create_task(download_site(str(params['url']) + str(url) + '/200', session, path))
            tasks.append(task)
        print('done with create_task')
        return await asyncio.gather(*tasks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', default=1, help='number of files')
    parser.add_argument('-path', default='artifacts/easy', help='saving path')
    args = parser.parse_args()

    mysession = asyncio.get_event_loop()
    mysession.run_until_complete(download_all_sites(args.n, args.path))
