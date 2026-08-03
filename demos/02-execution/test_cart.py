import pytest

from cart import (
    add_item,
    apply_discount,
    empty_cart,
    remove_item,
    subtotal_cents,
    total_cents,
    update_qty,
)


def test_empty_cart_shape():
    c = empty_cart()
    assert c == {"items": {}, "discount_code": None}


def test_add_item_new_line():
    c = add_item(empty_cart(), "A", 2, 500)
    assert c["items"] == {"A": {"qty": 2, "unit_price_cents": 500}}


def test_add_item_increments_existing_qty_and_keeps_original_price():
    c = add_item(empty_cart(), "A", 2, 500)
    c = add_item(c, "A", 3, 999)
    assert c["items"]["A"] == {"qty": 5, "unit_price_cents": 500}


def test_add_item_is_pure():
    c1 = empty_cart()
    c2 = add_item(c1, "A", 1, 100)
    assert c1 == {"items": {}, "discount_code": None}
    assert c2 is not c1


def test_add_item_rejects_bad_qty():
    with pytest.raises(ValueError):
        add_item(empty_cart(), "A", 0, 100)
    with pytest.raises(ValueError):
        add_item(empty_cart(), "A", -1, 100)


def test_add_item_rejects_negative_price():
    with pytest.raises(ValueError):
        add_item(empty_cart(), "A", 1, -1)


def test_remove_item_present():
    c = add_item(empty_cart(), "A", 1, 100)
    c = remove_item(c, "A")
    assert c["items"] == {}


def test_remove_item_missing_is_noop():
    c = add_item(empty_cart(), "A", 1, 100)
    c2 = remove_item(c, "B")
    assert c2["items"] == c["items"]


def test_update_qty_replaces_value():
    c = add_item(empty_cart(), "A", 2, 500)
    c = update_qty(c, "A", 10)
    assert c["items"]["A"]["qty"] == 10


def test_update_qty_missing_raises():
    with pytest.raises(KeyError):
        update_qty(empty_cart(), "A", 1)


def test_update_qty_rejects_bad_qty():
    c = add_item(empty_cart(), "A", 2, 500)
    with pytest.raises(ValueError):
        update_qty(c, "A", 0)


def test_apply_discount_normalizes_case():
    c = apply_discount(empty_cart(), "save10")
    assert c["discount_code"] == "SAVE10"


def test_apply_discount_unknown_raises():
    with pytest.raises(ValueError):
        apply_discount(empty_cart(), "FREESHIP")


def test_subtotal_cents():
    c = add_item(empty_cart(), "A", 2, 500)
    c = add_item(c, "B", 1, 1000)
    assert subtotal_cents(c) == 2000


def test_subtotal_empty():
    assert subtotal_cents(empty_cart()) == 0


def test_total_cents_no_discount():
    c = add_item(empty_cart(), "A", 2, 500)
    assert total_cents(c) == 1000


def test_total_cents_with_save10():
    c = add_item(empty_cart(), "A", 2, 500)
    c = apply_discount(c, "SAVE10")
    assert total_cents(c) == 900


def test_total_cents_with_save20_uses_integer_division():
    c = add_item(empty_cart(), "A", 1, 999)
    c = apply_discount(c, "SAVE20")
    # (999 * 80) // 100 == 799
    assert total_cents(c) == 799
