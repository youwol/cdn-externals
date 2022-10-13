import asyncio

import aiohttp

from youwol_utils import parse_json

async def execute():

    session = aiohttp.ClientSession()
    file = parse_json("./fonts.json")
    for font in file['fonts']:
        print(font['font-family'])
        url = f"https://tikzjax.com/bakoma/ttf/{font['font-family']}.ttf"
        async with await session.get(url=url) as resp:
            if resp.status == 200:
                file = open(f"./dist/ttf/{font['font-family']}.ttf", 'wb')
                file.write(await resp.read())
                file.close()
    await session.close()


loop = asyncio.get_event_loop()

asyncio.new_event_loop()
asyncio.run(execute())
