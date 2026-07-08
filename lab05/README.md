# Lab 05 — Sensor Simulation (Mutable Defaults & Variadic Arguments)

## Task

Write a small simulation of a group of sensors, starting from a
pre-built data structure (`sensor_group`, a dict of sensors) and two
queues (`data_queue` for incoming readings, `command_queue` for
commands). The exercise deliberately avoids relying on global variables:
every structure must be passed in as a default argument value, so a
function can be called with no arguments (using the shared default) or
with an explicit alternative structure.

Implement:

1. `last_reading(sensors, id) -> (found: bool, value|None)` — last
   reading of a sensor by ID.
2. `add_value(sensors, id, value) -> bool` — append a new reading,
   validating the value is `int`/`float`/`bool` via `isinstance`.
3. A predicate function `(value, condition) -> bool` that uses `eval()`
   to check whether a value satisfies a condition string (e.g.
   `(50, "x > 20")` → `True`).
4. `distribute_data(sensors, data)` — drain the reading queue into the
   matching sensor buffers via function 2, logging an error message for
   any reading whose sensor ID isn't known.
5. `toggle_status(sensors, *sensor_ids)` — flip the active/inactive
   flag for an arbitrary number of sensor IDs, passed as **positional**
   varargs (not a list/tuple/dict).
6. A filter function accepting sensor criteria as **keyword** arguments
   (arbitrary number), returning a new dict of only the matching
   sensors.
7. `emulate_readings(sensors, data)` — generate one new random reading
   per active sensor (type-appropriate ranges/values) and append them to
   the queue in shuffled order.
8. An event loop that pops commands off `command_queue` one at a time,
   dispatching to the functions above, until it hits a `"stop"` command
   or runs out of commands.

## Files

- `lab05.py` — the submitted solution.
