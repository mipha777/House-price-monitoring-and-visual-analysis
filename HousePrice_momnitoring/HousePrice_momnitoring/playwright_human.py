# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/17 02:25
@Desc     : 
"""
import asyncio

from playwright.async_api import Playwright
from Over_verification import simulate_human_mouse_move,generate_human_like_track
async def anjuke_302_verification(
    url: str,
    proxy: str = None,
    start: tuple[float,float] = (100,200),
    end: tuple[float,float] = (300,200),
    debug: bool = False
):
    """
    Playwright 自动化处理 302 验证页面
    参数:
    - url: 验证页面 URL
    - proxy: 使用的代理，格式 http://IP:PORT
    - start, end: 鼠标起点和终点坐标
    - debug: 是否打印轨迹信息
    """
    from playwright.async_api import async_playwright
    from Over_verification import simulate_human_mouse_move
    from playwright_stealth import stealth

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )

        context_args = {}
        if proxy:
            context_args['proxy'] = {"server": proxy}

        context = await browser.new_context(
            **context_args,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            viewport={"width":1366,"height":768},
            locale="zh-CN"
        )

        page = await context.new_page()
        await page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        Object.defineProperty(navigator, 'languages', {get: () => ['en-US','en']});
        Object.defineProperty(navigator, 'plugins', {get: () => [1,2,3,4,5]});
    """)
        await page.goto(url)
        # 模拟点击
        import random
        element = await page.query_selector("#btnSubmit")
        box = await element.bounding_box()
        viewport = page.viewport_size  # 获取页面窗口大小
        start = (random.uniform(0, viewport["width"]), random.uniform(0, viewport["height"])) # suiji鼠标起点
        end = (box["x"] + box["width"] / 2, box["y"] + box["height"] / 2) # 鼠标重点

        await simulate_human_mouse_move(page, start, end, debug=debug)

        await asyncio.sleep(1)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(anjuke_302_verification('https://hangzhou.anjuke.com/sale/p11/?from=HomePage_TopBar'))
