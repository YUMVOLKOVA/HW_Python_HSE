import asyncio
import aiohttp

# из лекции
#####
async def download_site(url, seccion):
    async with session.get(url) as response:
        print(f"Read {response.content.total_bytes} from {url}")
        return response.content.total_bytes

asunc def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
        task = asyncio.create_task(download_site(url, session))
        tasks.append(task)
    return await asyncio.gather(*tasks)
#####


if __name__ == "__main__":
    loop = asyncio.get_event_loop)_