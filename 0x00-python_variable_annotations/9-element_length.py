#!/usr/bin/env python3
"""element length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence[Sequence]]) -> List[Tuple[Sequence, int]]:
    """element length"""
    return [(i, len(i)) for i in lst]
