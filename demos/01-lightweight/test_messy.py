from messy import (
    first_match,
    group_by_first_letter,
    merge_counts,
    safe_divide,
    sum_evens,
    top_n,
)


def test_sum_evens():
    assert sum_evens([1, 2, 3, 4, 5, 6]) == 12
    assert sum_evens([]) == 0
    assert sum_evens([1, 3, 5]) == 0


def test_group_by_first_letter():
    result = group_by_first_letter(["Apple", "ant", "Bat", "bee", "cat"])
    assert result == {"a": ["Apple", "ant"], "b": ["Bat", "bee"], "c": ["cat"]}


def test_top_n():
    assert top_n([5, 1, 9, 3, 7], 3) == [9, 7, 5]
    assert top_n([1, 2], 5) == [2, 1]


def test_safe_divide():
    assert safe_divide(10, 2) == 5
    assert safe_divide(10, 0) is None


def test_merge_counts():
    a = {"x": 1, "y": 2}
    b = {"y": 3, "z": 4}
    assert merge_counts(a, b) == {"x": 1, "y": 5, "z": 4}


def test_first_match():
    assert first_match([1, 2, 3, 4], lambda x: x > 2) == 3
    assert first_match([1, 2], lambda x: x > 10) is None
