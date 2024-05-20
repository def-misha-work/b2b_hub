import logging
import httpx

from constants import (
    BASIC_USER_LOGIN,
    BASIC_USER_PASSWORD,
    ENDPONT_GET_COMPANY_NAME,
    DADATA_API_KEY,
)


async def get_company_name(inn):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token {DADATA_API_KEY}"
    }
    data = {"query": str(inn)}
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                ENDPONT_GET_COMPANY_NAME,
                headers=headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as exc:
            logging.error(f"Ошибка при выполнении запроса: {exc}")
            return None
        except httpx.HTTPStatusError as exc:
            logging.error(f"Ошибка HTTP: {exc}")
            return None


async def make_patch_request(url, data):
    url_params = {
        "company_inn": data["company_inn"],
        "company_name": f"'{data['company_name']}'"
    }
    async with httpx.AsyncClient() as client:
        response = await client.patch(
            url,
            params=url_params,
            # json=data,
            auth=(BASIC_USER_LOGIN, BASIC_USER_PASSWORD)
        )
        return response


async def make_post_request(url, data):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            json=data,
            auth=(BASIC_USER_LOGIN, BASIC_USER_PASSWORD)
        )
        if response.status_code != 201:
            logging.info(
                f"Заявка не создана получен ответ: {response.status_code}"
            )
        return response


async def make_get_request(url, value):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{url}{value}",
            auth=(BASIC_USER_LOGIN, BASIC_USER_PASSWORD)
        )
        if response.status_code != 200:
            logging.info(
                f"Список заявок не получен, ответ: {response.status_code}"
            )
        return response
