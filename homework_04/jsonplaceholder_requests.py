import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_data(url):
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, url)
        return data


USERS_DATA_URL = 'https://jsonplaceholder.typicode.com/users'
POSTS_DATA_URL = 'https://jsonplaceholder.typicode.com/posts'


async def main():
    users_data_future = get_data(USERS_DATA_URL)
    posts_data_future = get_data(POSTS_DATA_URL)

    users_data, posts_data = await asyncio.gather(users_data_future, posts_data_future)

    print("Users data:", users_data)
    print("Posts data:", posts_data)


if __name__ == "__main__":
    asyncio.run(main())
