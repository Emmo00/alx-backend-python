#!/usr/bin/env python3
"""sum mixed"""
from typing import List, Union


RealNumber = Union[int, float]
def sum_mixed_list(mxd_lst: List[RealNumber]) -> float:
    """sum mixed"""
    sum = 0
    for n in mxd_lst:
        sum += n
    return sum
