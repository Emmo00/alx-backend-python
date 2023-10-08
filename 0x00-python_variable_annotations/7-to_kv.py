#!/usr/bin/env python3
"""to kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to kv"""
    return (k, v ** 2)
