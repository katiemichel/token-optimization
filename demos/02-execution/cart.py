def empty_cart() -> dict:
    return {"items": {}, "discount_code": None}


def add_item(cart: dict, sku: str, qty: int, unit_price_cents: int) -> dict:
    if qty <= 0:
        raise ValueError("qty must be > 0")
    if unit_price_cents < 0:
        raise ValueError("unit_price_cents must be >= 0")

    new_items = {
        existing_sku: line.copy() for existing_sku, line in cart["items"].items()
    }

    if sku in new_items:
        new_items[sku]["qty"] += qty
    else:
        new_items[sku] = {"qty": qty, "unit_price_cents": unit_price_cents}

    return {"items": new_items, "discount_code": cart["discount_code"]}


def remove_item(cart: dict, sku: str) -> dict:
    new_items = {
        existing_sku: line.copy()
        for existing_sku, line in cart["items"].items()
        if existing_sku != sku
    }
    return {"items": new_items, "discount_code": cart["discount_code"]}


def update_qty(cart: dict, sku: str, qty: int) -> dict:
    if qty <= 0:
        raise ValueError("qty must be > 0")
    if sku not in cart["items"]:
        raise KeyError(sku)

    new_items = {
        existing_sku: line.copy() for existing_sku, line in cart["items"].items()
    }
    new_items[sku]["qty"] = qty
    return {"items": new_items, "discount_code": cart["discount_code"]}


def apply_discount(cart: dict, code: str) -> dict:
    normalized = code.upper()
    if normalized not in {"SAVE10", "SAVE20"}:
        raise ValueError("unknown discount code")
    return {"items": cart["items"], "discount_code": normalized}


def subtotal_cents(cart: dict) -> int:
    return sum(
        line["qty"] * line["unit_price_cents"] for line in cart["items"].values()
    )


def total_cents(cart: dict) -> int:
    subtotal = subtotal_cents(cart)
    code = cart["discount_code"]
    if code == "SAVE10":
        return (subtotal * 90) // 100
    if code == "SAVE20":
        return (subtotal * 80) // 100
    return subtotal
