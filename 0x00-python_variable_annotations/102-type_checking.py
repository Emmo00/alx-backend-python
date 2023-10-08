#!/usr/bin/env python3
"""adv task"""
from typing import Tuple, Iterable, Union


def zoom_array(lst: Iterable, factor: Union[int, float] = 2) -> Tuple:
    """zoom array"""
    zoomed_in: Tuple = tuple([
        item for item in lst
        for i in range(int(factor))
    ])
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
