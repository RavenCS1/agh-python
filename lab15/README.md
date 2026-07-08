# Lab 15 — Testing and Debugging with pytest

Given a pre-written `SalesReport` class that analyzes orders from a
JSON file, write a pytest suite covering its documented behavior,
default values, and edge cases — then use the failing tests to find and
fix the bugs in the class itself.

## Task

`SalesReport` reads a JSON array of orders (`id`, `customer`,
`product`, `quantity`, `price`, order value = `quantity * price`) and
exposes:

1. `total_sales()` — sum of all order values.
2. `average_order_value()` — mean order value, or `0` if there are no
   orders.
3. `best_selling_product()` — name of the product with the highest
   total quantity sold across all its orders, or `None` if there are no
   orders.
4. `orders_by_customer(customer)` — all orders for the given customer,
   or an empty list if the customer doesn't exist.
5. `add_order(order)` — appends a new order, raising `ValueError` if
   `quantity <= 0` or `price <= 0`.

Write tests asserting these assumptions and default behaviors, then debug
and fix the implementation to make them pass.

## Files

- `lab15.py` — the `SalesReport` class under test.
- `test_lab15.py` — the pytest suite covering it.
- `main.py`, `pyproject.toml`, `uv.lock`, `.python-version` — `uv`
  project scaffolding (`pytest` as the only dependency).
- `test.json`, `empty.json`, `Appendedtest.json` — JSON fixtures used by
  the tests (a populated order list, an empty list, and a
  post-`add_order` snapshot).
