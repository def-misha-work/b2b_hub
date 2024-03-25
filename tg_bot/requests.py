import httpx


async def make_post_request(url, data):
    async with httpx.AsyncClient() as client:
        return await client.post(url, json=data)
