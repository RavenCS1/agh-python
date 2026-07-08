# Lab 14 — Writing a Python C Extension

Write a native C extension module for CPython, use it from Python, and
benchmark it against an equivalent pure-Python implementation. The
project is managed with [`uv`](https://astral.sh/uv) instead of a plain
venv, since Python 3.13+ no longer bundles `setuptools`.

## Task

- Set up the project with `uv init`, `uv venv --python 3.14`, and
  `source .venv/bin/activate`.
- In `functions.c`, implement two C functions exposed to Python via a
  `functions` extension module (both declared `static`, since Python
  finds them through the method table, not the linker; `Python.h` must
  be included first, right after `#define PY_SSIZE_T_CLEAN`):
  1. `sum_of_squares(n)` — sum of squares of the first `n` integers,
     computed iteratively.
  2. `fibonacci(n)` — the n-th Fibonacci number, computed recursively
     (deliberately inefficient, to make the C/Python speed gap obvious).
- In `vector.c`, implement a full Python type, `Vector2D`, as a
  C struct (`PyObject_HEAD` + two `double` fields) with:
  - `__init__(self, x=0.0, y=0.0)` parsed via
    `PyArg_ParseTupleAndKeywords` with format `"|dd"`, raising
    `TypeError` on bad input.
  - `__str__` returning `"Vector2D(x, y)"`.
  - `scale(factor)` — in-place scalar multiplication, returns `None`.
  - `magnitude()` — Euclidean norm.
  - `add(other)` — in-place vector addition, taking another `Vector2D`
    via format `"O!"`.
  - The type is registered through a `PyTypeObject` (`Vector2DType`)
    and exposed via a second extension module, `vector`.
- Build both modules with `setup.py` (`python3 setup.py build`) and run
  `test.py` with `PYTHONPATH` pointing at the build output, comparing
  execution time of the C functions/class against hand-written Python
  equivalents also defined in `test.py`.

## Files

- `test_uv/functions.c` — student's C implementation of
  `sum_of_squares` and `fibonacci`.
- `test_uv/vector.c` — student's C implementation of the `Vector2D`
  type.
- `test_uv/setup.py` — `setuptools` build config defining the
  `functions` and `vector` extension modules.
- `test_uv/test.py` — benchmark script: times the C extension calls
  against equivalent pure-Python functions/classes for
  `sum_of_squares`, `fibonacci`, and `Vector2D` (`scale`, `magnitude`,
  `add`).
- `test_uv/uv.lock`, `test_uv/.python-version` — `uv` project/lockfile
  metadata.
