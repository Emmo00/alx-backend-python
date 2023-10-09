#!/usr/bin/env python3
"""asyncio example"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """concurrent coroutines"""
    delays: List = []
    for i in range(n):
        delays.append(await asyncio.create_task(wait_random(max_delay)))
    delays.sort()
    return delays
