import asyncio
from pyppeteer import launch

async def install_chromium():
    browser = await launch()
    await browser.close()

asyncio.get_event_loop().run_until_complete(install_chromium())