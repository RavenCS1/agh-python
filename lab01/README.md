# Lab 01 — Introduction to Python

Introductory session: environment setup, basic syntax, and Python's
built-in introspection tools.

## Topics covered

- Shebang line (`#!/usr/bin/env python3`) to make a Python script directly
  executable, mirroring how it's done in Bash.
- Built-in introspection: `keyword.kwlist`, `dir(builtins)`, `dir(math)`,
  and `help(...)` for exploring what a module or object offers.
- Multi-line strings (`'''...'''`) used as block comments.
- `type()` to inspect the runtime type of a variable.
- A pointer to the `argparse` module for building command-line interfaces
  (explored further in later labs).

## Files

- `lab01.py` — solves a quadratic equation `ax² + bx + c = 0`,
  reading `a`, `b`, `c` from user input. Uses `math.sqrt` for a
  non-negative discriminant and falls back to `cmath.sqrt` for complex
  roots when the discriminant is negative.
