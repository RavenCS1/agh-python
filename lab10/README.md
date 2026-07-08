# Lab 10 — OOP: a single-star planetary system simulation

## Task

Model a simple planetary system, focusing on Python's more advanced
class features (properties, dunder methods, class-level state, static and
class methods) rather than the classes' domain logic. Each class lives in
its own module and includes a small self-test under
`if __name__ == "__main__":`. Private attributes are prefixed with `_`.

1. `planet.py` — class `Planet` with `_name`, `_radius_km`, `_mass_kg`,
   `_distance_from_star_mkm`, each exposed read-only via `@property`
   getters of the same name (without the leading underscore).
2. Dunder methods: `__str__` (human-readable description),
   `__lt__` (orders planets by mass, enabling `<`), `__eq__` (compares all
   fields, using `math.isclose` for floats and `casefold()` for the name).
3. A regular method `orbital_period` (orbital period in Earth years, via
   Kepler's third law `T = d^1.5` with `d` in AU), a `@staticmethod`
   `gravitational_force(m1, m2, r)` (Newton's law of gravitation, converting km
   to metres), and a `@classmethod` `from_dict(cls, data)` building an
   instance from a dict of matching keys.
4. `star.py` — class `Star`, mostly copy-pasted from `Planet` with
   `_distance_from_star_mkm` replaced by `_luminosity_w` (luminosity), which
   this time is mutable: it keeps the `@property` getter but adds a matching
   `@luminosity_w.setter`. Keeps the adapted `__str__`, `__lt__`, `__eq__` and
   `from_dict`.
5. `single_star_system.py` — class `SingleStarSystem` combining one
   `Star` and a list of `Planet` (kept sorted by distance from the
   star), with read-only property getters for both. Includes a class-level
   counter of how many systems exist (incremented in `__init__`, decremented
   in `__del__`), exposed via a class method
   `single_star_system_count()`.
6. List-like behaviour on the system: `__len__`, `__contains__`,
   `__getitem__`, `__delitem__` (no `__setitem__`/insertion is required here).
7. A method to add a planet while keeping the list sorted by distance,
   plus a `from_dict` class method for the whole system.

## Files

- `planet.py`, `star.py`, `single_star_system.py` — the submitted
  solution (three modules as required above).
