from inventory import add_item, add_warehouse, total_units
from reporting import generate_report


def test_total_units_single_warehouse():
    w = add_warehouse("north", items=[])
    add_item(w, "apples", 10)
    add_item(w, "pears", 5)
    assert total_units(w) == 15


def test_report_includes_each_warehouse_name():
    a = add_warehouse("north", items=[])
    b = add_warehouse("south", items=[])
    add_item(a, "apples", 1)
    add_item(b, "bananas", 1)
    report = generate_report([a, b])
    assert "north" in report
    assert "south" in report


def test_each_warehouse_is_independent():
    """Two warehouses created with no explicit items list must not share state.

    This is the failing test. The fix lives in inventory.py, not here.
    """
    a = add_warehouse("north")
    b = add_warehouse("south")
    add_item(a, "apples", 7)
    assert total_units(a) == 7
    assert total_units(b) == 0, (
        f"warehouse 'south' should be empty but contains {b['items']!r}"
    )
