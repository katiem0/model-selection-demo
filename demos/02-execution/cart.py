def empty_cart() -> dict:
    return {"items": {}, "discount_code": None}


def add_item(cart: dict, sku: str, qty: int, unit_price_cents: int) -> dict:
    raise NotImplementedError


def remove_item(cart: dict, sku: str) -> dict:
    raise NotImplementedError


def update_qty(cart: dict, sku: str, qty: int) -> dict:
    raise NotImplementedError


def apply_discount(cart: dict, code: str) -> dict:
    raise NotImplementedError


def subtotal_cents(cart: dict) -> int:
    raise NotImplementedError


def total_cents(cart: dict) -> int:
    raise NotImplementedError
