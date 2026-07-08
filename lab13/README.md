# Lab 13 — Dataclasses and Structural Pattern Matching

## Task

Sketch a logistics system using `@dataclass` and `match`:

1. Define data structures with `@dataclass`:
   - `Driver`: `name`, `license_type`, `vehicle` — one
     license type and one assigned vehicle per driver, for simplicity.
   - `Package`: `id` (auto-generated via `uuid`, through a
     default factory), `destination`, `weight`, `priority`.
   - `Vehicle`: `registration_number`, `capacity`, `vehicle_type`,
     `parameters` (dict, defaulting to `{"GPS": "yes"}`), and `status`, a
     nested `@dataclass` `VehicleStatus` (`fueled`, `roadworthy`)
     defaulting to fueled and roadworthy.
2. A `match`-based function that prints a distinct message per package
   `priority` (`high`/`medium`/`low`), gracefully handling
   unexpected values.
3. A `match`-based function checking whether a driver may operate a
   given vehicle, for the valid combinations `C`+`truck`, `C`+`van`,
   `B`+`van` — collapsed into a single `case` via `|` alternation rather
   than one `case` per combination.
4. A function that categorizes a package by priority and weight
   (`large, priority` / `small, priority` / `regular, priority` /
   `standard`), using pattern-matching on the dataclass fields with
   guard conditions rather than a chain of `if`/`elif`.
5. A function checking whether a vehicle is ready to go (fueled and
   roadworthy, optionally also requiring GPS) using a *single* `match`
   block with exactly three `case`s.
6. The same field-matching behavior reproduced on a plain (non
   `@dataclass`) class, `WarehousePackage`, by manually declaring
   `__match_args__` — to show that pattern matching against
   positional/keyword fields isn't unique to `@dataclass`. Plus a
   routing function assigning such packages to warehouses based on
   status and weight, matching fields positionally (using `_` for
   unused ones) instead of by name.

## Files

- `lab13.py` — the submitted solution. `Package.id` uses
  `field(default_factory=lambda: str(uuid.uuid4()))` so every instance
  gets its own fresh UUID string.
