from functools import partial
import logging

import asyncio
import requests

from utils import async_timeit


logging.basicConfig(level=logging.DEBUG)

async def get(id_, loop):
    url = f'https://fakerestapi.azurewebsites.net/api/v1/Authors/{id_}'
    headers={'accept': 'application/json; v=1.0'}

    res = await loop.run_in_executor(
        None,
        partial(requests.get, url, headers=headers)
    )
    return res.json()

@async_timeit
async def main():
    loop = asyncio.get_event_loop()
    tasks = [get(str(i), loop) for i in range(1, 11)]
    res = await asyncio.gather(*tasks)
    print([ele['id'] for ele in res])

asyncio.run(main())
