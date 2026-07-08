# Lab 09 — Package structure and exception handling: an online shop skeleton

## Task

Build the skeleton of an online-shop library, focusing on package layout and
exception-based error handling rather than business logic, then exercise it
from a top-level `main.py`.

- Package layout: `main.py` (test/driver script) at the
  top and a `shop/` package holding the implementation. Internal helper
  names are prefixed with `_`; only unprefixed names are meant to be part of
  the public interface. All imports inside the package must be relative
  (start with a dot), e.g. `from .helpers.validation import _validate_customer_data`.
- Order/product IDs are generated with `uuid.uuid4()`; customers are
  identified by their (string) login.
1. `shop/helpers/validation.py`: `_validate_order(order)`
   validates that an order is a dict with a non-empty string `"customer"` key
   and a non-empty `"products"` list of `uuid.UUID`s; a companion
   `_validate_customer_data(data)` validates a customer dict (`"email"`,
   `"address"` non-empty strings). Invalid input raises `TypeError`, `KeyError`
   or `ValueError` with a descriptive message (any "wrong type/empty" case
   is simplified down to `ValueError`).
2. `shop/helpers/data.py`: module-level dicts `_orders_in_progress`
   (keyed by order id) and `_registered_customers` (keyed by login), each
   pre-seeded with one sentinel/test entry keyed by an impossible value
   (e.g. `-1`).
3. `shop/shop.py`: core logic —
   - `_register_customer(login, customer_data)` — returns the login if the
     customer already exists, otherwise validates and registers them.
   - `_register_order(order)` — validates the order, checks the
     referenced customer exists (else `KeyError`), generates a new order id
     and stores it.
   - `receive_order(order, new_customer_data=None)` — the public
     entry point: optionally registers a new customer, then registers the
     order, catching every exception internally so callers only ever see
     `(login, order_id)` on success or `(None, None)` / `(login, None)` on
     partial/total failure.
   - `print_customers()` / `print_orders()` — simple debug printers.
4. `shop/__init__.py` — exposes only `receive_order`, `print_customers`
   and `print_orders` (via `__all__` and a package docstring/`__version__`).
5. Logging: `shop/helpers/logger.py` creates a shared logger
   writing `WARNING`+ to `shop.log`; every place that previously raised/caught
   an exception also logs a matching warning.
6. `__init__.py` gains an `_initialize()` function (called on import) that
   loads pre-existing customers/orders from the bundled `customers.csv`
   and `orders.csv` via `csv.DictReader`, replacing the sentinel
   test entries, and raises `RuntimeError` if initialization fails.

## Files

- `main.py` — driver/test script exercising the package with sample data.
- `shop/__init__.py`, `shop/shop.py` — public package surface and core logic.
- `shop/helpers/validation.py`, `shop/helpers/data.py`,
  `shop/helpers/logger.py` — internal helpers (validation, data store, logger).
- `customers.csv`, `orders.csv` — seed data loaded at import time.

Running `main.py` produces a `shop.log` file, not included here.
