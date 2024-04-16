import logging
import httpx

from constants import (
    BASIC_USER_LOGIN,
    BASIC_USER_PASSWORD,
)


async def make_post_request(url, data):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            json=data,
            auth=(BASIC_USER_LOGIN, BASIC_USER_PASSWORD)
        )
        return response


async def make_get_request(url, value):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{url}{value}",
            auth=(BASIC_USER_LOGIN, BASIC_USER_PASSWORD)
        )
        logging.info(f"Это урл: {response.url}")
        return response
