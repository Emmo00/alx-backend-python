#!/usr/bin/env python3
"""make multiplier"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function"""
    def func(f: float) -> float:
        return f * multiplier
    return func
