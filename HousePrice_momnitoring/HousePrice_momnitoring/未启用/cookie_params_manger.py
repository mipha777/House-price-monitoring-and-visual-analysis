# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/11 01:53
@Desc     : 
"""
import asyncio
import time
import random
from HousePrice_momnitoring.HousePrice_momnitoring.settings import USER_AGENTS
from playwright.async_api import async_playwright

UA = random.choice(USER_AGENTS)

class CookieManager:
    def __init__(self):
        self.cookies_cache = {}

    async def create_stealth_page(self,headless: bool = False, proxy: str = None):
        playwright = await async_playwright().start()

        args = [
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-dev-shm-usage"
        ]

        if proxy:
            args.append(f'--proxy-server={proxy}')

        browser = await playwright.chromium.launch(headless=headless, args=args)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent=UA
        )

        page = await context.new_page()

        # 注入 JS 脚本进行防检测伪装
        await page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        Object.defineProperty(navigator, 'languages', {
            get: () => ['zh-CN', 'zh']
        });
        Object.defineProperty(navigator, 'plugins', {
            get: () => [1, 2, 3]
        });
        window.chrome = {
            runtime: {}
        };
        """)

        try:
            await page.goto('https://clogin.lianjia.com/login?service=https%3A%2F%2Fwww.lianjia.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttps%253A%252F%252Fxc.lianjia.com%252Fershoufang%252Fco32%252F')
            # huoqu cookie
            await page.wait_for_timeout(3000)

            input('登录后点击')


            cookies = await context.cookies()
            cookie = "; ".join([f"{c['name']}={c['value']}" for c in cookies if 'name' in c and 'value' in c])
            with open('cookies.json', 'w', encoding='utf-8') as f:
                f.write(cookie)

            # return cookie


        finally:
            await page.close()
            await context.close()
            await browser.close()




if __name__ == '__main__':
    cookie_manager = CookieManager()
    asyncio.run(cookie_manager.create_stealth_page())