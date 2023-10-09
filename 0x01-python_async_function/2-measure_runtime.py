#!/usr/bin/env python3
"""asyncio example"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure time of wait_n async function"""
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop: float = time.time()
    return (stop - start) / n
