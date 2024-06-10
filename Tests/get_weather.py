import asyncio
import pandas as pd
from pyppeteer import launch
from bs4 import BeautifulSoup



async def main():
    
    URL = "https://www.wunderground.com/history/monthly/gt/guatemala-city/MGGT/date/1996-7"
    CHROME_PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    
    # Iniciar navegador
    browser = await launch(executablePath=CHROME_PATH, headless=True)
    page = await browser.newPage()

    # Ir a pagina
    await page.goto(URL)
    await page.waitForXPath("//table")
    content = await page.content()
    await browser.close()

    soup = BeautifulSoup(content, "html.parser")
    tablas = soup.find_all("table")

    for table in tablas:
        df = pd.read_html(str(table))[0]
        print(df)
    # print(soup.prettify())

asyncio.get_event_loop().run_until_complete(main())