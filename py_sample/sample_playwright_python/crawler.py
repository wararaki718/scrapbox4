import asyncio
from playwright.async_api import async_playwright


class SampleCrawler:
    def __init__(self) -> None:
        pass

    async def _crawling(self, url: str) -> dict:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(url)
            result = {"title": await page.title()}
            await browser.close()
        return result

    def run(self, url: str) -> dict:
        result = asyncio.run(self._crawling(url))
        return result
