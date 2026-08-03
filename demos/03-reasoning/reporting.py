from inventory import total_units


def generate_report(warehouses: list[dict]) -> str:
    lines = [f"Inventory report ({len(warehouses)} warehouses)"]
    for w in warehouses:
        lines.append(f"  {w['name']}: {total_units(w)} units across {len(w['items'])} skus")
    return "\n".join(lines)
