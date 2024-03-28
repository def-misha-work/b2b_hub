import logging
import httpx


async def make_post_request(url, data):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
        return response


async def make_get_request(url, value):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{url}{value}")
        logging.info(f"Это урл: {response.url}")
        return response
