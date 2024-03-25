import httpx


async def make_post_request(url, data):
    async with httpx.AsyncClient() as client:
        return await client.post(url, json=data)


async def make_get_request(url, value):
    async with httpx.AsyncClient() as client:
        return await client.get(url.format(value))
