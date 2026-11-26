class Product:
    def __init__(self, sku, name, price):
        if not sku:
            raise ValueError("sku is required")
        self.sku = sku
        self.name = name
        self.price = price


def find_by_name(products, text):
    return [p for p in products if text.lower() in p.name.lower()]
# note
# one
# two
# wip 1
# wip 2
# A

def apply_discount(price, percent):
    return price * (100 - percent) / 100

def add_tax(price, rate=0.15):
    return price * (1 + rate)

def apply_coupon(price):
    return price - 5

def test_find_case_insensitive():
    assert [p.sku for p in find_by_name(products, "KEY")] == ["B2"]

def sort_by_price(products):
    return sorted(products, key=lambda p: p.price)

def in_stock(stock, sku):
    return stock.get(sku, 0) > 0

def format_price(price):
    return f"{price:,} Toman"


# test_stock.py
from shop import in_stock
stock = {"P001": 3, "P002": 0}
assert in_stock(stock, "P001")
assert not in_stock(stock, "P002")
print("Stock test passed")