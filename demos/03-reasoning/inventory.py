def add_warehouse(name: str, items: list | None = None) -> dict:
    return {"name": name, "items": [] if items is None else items}


def add_item(warehouse: dict, sku: str, qty: int) -> None:
    warehouse["items"].append({"sku": sku, "qty": qty})


def total_units(warehouse: dict) -> int:
    return sum(item["qty"] for item in warehouse["items"])
