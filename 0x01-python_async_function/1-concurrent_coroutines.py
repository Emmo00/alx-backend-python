#!/usr/bin/env python3
"""asyncio example"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """concurrent coroutines"""
    delays = []
    for i in range(n):
        delays.append(await asyncio.create_task(wait_random(max_delay)))
    delays.sort()
    return delays
