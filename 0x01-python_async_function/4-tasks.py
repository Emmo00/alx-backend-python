#!/usr/bin/env python3
"""asyncio example"""

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """concurrent coroutines"""
    delays = []
    for i in range(n):
        delays.append(await task_wait_random(max_delay))
    delays.sort()
    return delays