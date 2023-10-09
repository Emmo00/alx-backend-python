#!/usr/bin/env python3
"""asyncio example"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """concurrent coroutines"""
    delays: List = []
    tasks: List = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for task in tasks:
        delays.append(await task)
    delays.sort()
    return delays
