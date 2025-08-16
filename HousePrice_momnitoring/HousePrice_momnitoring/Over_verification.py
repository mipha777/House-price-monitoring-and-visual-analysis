# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/17 02:14
@Desc     : 
"""

# human_mouse.py
import random
import asyncio
from typing import Tuple, Optional
from playwright.async_api import Page

def generate_human_like_track(
    start: Tuple[float, float],
    end: Tuple[float, float],
    steps: Optional[int] = None,
    noise: float = 1.5
) -> list:
    """
    生成一个模仿人类鼠标移动轨迹的点列表
    """
    x0, y0 = start
    x1, y1 = end
    distance = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    if steps is None:
        steps = max(int(distance / 2), 10)  # 每2px一个点，至少10点

    track = []
    for i in range(steps):
        ratio = i / steps
        x = x0 + (x1 - x0) * ratio + random.uniform(-1, 1)
        y = y0 + (y1 - y0) * ratio + random.uniform(-noise, noise)
        track.append((x, y))
    track.append((x1, y1))
    return track


async def simulate_human_mouse_move(
    page: Page,
    start: Tuple[float, float],
    end: Tuple[float, float],
    steps: Optional[int] = None,
    noise: float = 1.5,
    min_sleep: float = 0.008,
    max_sleep: float = 0.03,
    debug: bool = False,
    click_after: bool = True  # 新增参数：移动结束后是否点击
):
    """
    Playwright 模拟人类鼠标移动行为，含随机轨迹和停顿
    """
    track = generate_human_like_track(start, end, steps, noise)
    if debug:
        print(f"[DEBUG] 生成轨迹点数: {len(track)}")

    for i, (x, y) in enumerate(track):
        await page.mouse.move(x, y)
        if debug:
            print(f"[DEBUG] 移动到点 {i + 1}: ({x:.2f}, {y:.2f})")
        await asyncio.sleep(random.uniform(min_sleep, max_sleep))

    if click_after:
        # 移动结束后点击终点
        await page.mouse.click(end[0], end[1])
        if debug:
            print(f"[DEBUG] 点击终点 ({end[0]:.2f}, {end[1]:.2f})")
