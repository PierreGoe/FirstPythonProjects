"""https://miyakogi.github.io/pyppeteer/"""

import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://www.google.com')
    await page.screenshot({'path': 'example.png', 'fullPage':'True'})#choisir emplacement
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

