from typing import Callable, Dict, List, Optional


def sum_evens(v: List[int]) -> int:
    total = 0
    for value in v:
        if value % 2 == 0:
            total += value
    return total


def group_by_first_letter(ws: List[str]) -> Dict[str, List[str]]:
    d = {}
    for w in ws:
        k = w[0].lower()
        if k not in d:
            d[k] = []
        d[k].append(w)
    return d


def top_n(scores: List[int], n: int) -> List[int]:
    return sorted(scores, reverse=True)[:n]


def safe_divide(a: float,b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b


def merge_counts(a: Dict[str, int], b: Dict[str, int]) -> Dict[str, int]:
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
    return out


def first_match(items: List[int], pred: Callable[[int], bool]) -> Optional[int]:
    for it in items:
        if pred(it):
            return it
    return None
