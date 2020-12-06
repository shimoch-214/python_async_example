from time import sleep
import logging

import asyncio
import aiohttp

from utils import async_timeit

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

async def get(id_, session):
    url = f'https://fakerestapi.azurewebsites.net/api/v1/Authors/{id_}'
    headers={
        'accept': 'application/json; v=1.0'
    }
    async with session.get(url, headers=headers) as res:
        return await res.json()

async def on_request_start(session, trace_config_ctx, params):
    logger.debug(f'Start request: {params.url.host}:{params.url.port}')

async def on_request_end(session, trace_config_ctx, params):
    logger.debug(f'End request: {params.url.host}:{params.url.port} "{params.method} {params.url.path} {params.response.status}"')

@async_timeit
async def main():
    trace_config = aiohttp.TraceConfig()
    trace_config.on_request_start.append(on_request_start)
    trace_config.on_request_end.append(on_request_end)

    async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
        tasks = [get(str(i), session) for i in range(1, 11)]
        res = await asyncio.gather(*tasks)
    print([ele['id'] for ele in res])

asyncio.run(main())
