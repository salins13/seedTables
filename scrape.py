import asyncio
from playwright.async_api import async_playwright

async def main():
    total = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        for seed in range(5, 15):
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
            print("Visiting:", url)

            await page.goto(url)
            await page.wait_for_selector("table")

            values = await page.eval_on_selector_all(
                "table td",
                "els => els.map(e => e.innerText)"
            )

            for v in values:
                try:
                    total += float(v)
                except:
                    pass

        await browser.close()

    print("FINAL TOTAL:", total)

asyncio.run(main())