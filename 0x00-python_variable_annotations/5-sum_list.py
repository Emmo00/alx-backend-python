#!/usr/bin/env python3
"""sum list module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum list"""
    sum = 0
    for n in input_list:
        sum += n
    return sum
