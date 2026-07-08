"""
Library for handling an online shop
"""

__version__ = "1.0"

__all__ = [
    "receive_order",
    "print_customers",
    "print_orders"
]

def _initialize():
    import csv
    import uuid
    from .helpers.data import _orders_in_progress, _registered_customers
    try:
        _registered_customers.clear()
        with open("customers.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                login = row.pop("login")
                _registered_customers[login] = dict(row)
        _orders_in_progress.clear()
        with open("orders.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                order_id = uuid.UUID(row.pop("id"))
                row["products"] = [uuid.UUID(id.strip()) for id in row["products"].strip().split(";")]
                _orders_in_progress[order_id] = dict(row)
    except Exception as e:
        raise RuntimeError(f"shop package initialization failed - error: {e}")

_initialize()

from .shop import receive_order, print_customers, print_orders
