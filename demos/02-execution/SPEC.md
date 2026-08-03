# Cart — spec

A tiny shopping-cart module. Pure Python, standard library only.

## Public API

All functions live in [`cart.py`](cart.py). Signatures are fixed.

```python
def add_item(cart: dict, sku: str, qty: int, unit_price_cents: int) -> dict: ...
def remove_item(cart: dict, sku: str) -> dict: ...
def update_qty(cart: dict, sku: str, qty: int) -> dict: ...
def apply_discount(cart: dict, code: str) -> dict: ...
def subtotal_cents(cart: dict) -> int: ...
def total_cents(cart: dict) -> int: ...
```

## Cart shape

A cart is a plain `dict`:

```python
{
    "items": {
        "<sku>": {"qty": int, "unit_price_cents": int},
        ...
    },
    "discount_code": str | None,
}
```

`add_item`, `remove_item`, `update_qty`, and `apply_discount` are **pure** — they return a *new* cart dict rather than mutating the input.

## Behavior

### `add_item(cart, sku, qty, unit_price_cents)`
- If `qty <= 0`, raise `ValueError("qty must be positive")`.
- If `unit_price_cents < 0`, raise `ValueError("price must be non-negative")`.
- If `sku` is already in the cart, **increment** the existing quantity by `qty`. The stored `unit_price_cents` for that sku is **not** changed.
- Otherwise add a new line item.

### `remove_item(cart, sku)`
- If `sku` is not in the cart, return the cart unchanged.
- Otherwise return a new cart without that sku.

### `update_qty(cart, sku, qty)`
- If `sku` is not in the cart, raise `KeyError(sku)`.
- If `qty <= 0`, raise `ValueError("qty must be positive")`.
- Otherwise return a new cart with the sku's `qty` replaced (not added to).

### `apply_discount(cart, code)`
- Accepted codes (case-insensitive): `"SAVE10"` → 10% off, `"SAVE20"` → 20% off.
- Any other code raises `ValueError("unknown discount code")`.
- Returns a new cart with `discount_code` set to the **uppercase** form.

### `subtotal_cents(cart)`
- Sum of `qty * unit_price_cents` across all items.
- Empty cart → `0`.

### `total_cents(cart)`
- `subtotal_cents` minus the discount, if any.
- Rounding: discounted total is computed as `(subtotal * (100 - discount_percent)) // 100`. Integer division — no floats.
- No discount → equals `subtotal_cents`.

## Empty-cart helper

A helper to construct a fresh empty cart:

```python
def empty_cart() -> dict:
    return {"items": {}, "discount_code": None}
```

This already exists in `cart.py`. Use it as your starting point.

## What "done" looks like
- `pytest demos/02-execution -q` is green.
- `ruff check demos/02-execution` is green.
- No new public functions.
- No signature changes.
