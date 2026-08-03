def add_warehouse(name: str, items: list = []) -> dict:
    return {"name": name, "items": items}


def add_item(warehouse: dict, sku: str, qty: int) -> None:
    warehouse["items"].append({"sku": sku, "qty": qty})


def total_units(warehouse: dict) -> int:
    return sum(item["qty"] for item in warehouse["items"])
