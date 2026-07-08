# Lab 02 — Command-line arguments, list comprehensions, shallow copies

## Task

Write a program that reads a variable number of `float` values from the
command line (e.g. `python3 program.py 1 -2.21 3 4.2 5`) and, printing the
result of each step:

1. Prints all input arguments as strings (excluding the program name), using
   slicing.
2. Builds a new list by casting those strings to `int`, using a list
   comprehension. Note: a direct `str -> int` cast fails on values with a
   decimal point, so values must go through `float` first.
3. Removes every `7` from that list (`remove` + a `while` loop).
4. Prints each element together with its index (`enumerate`). If the list has
   more than 10 elements, only the first 10 are printed — once with a plain
   `if`, once with an equivalent slice.
5. Builds a list of `(number, its square)` tuples for the positive even
   numbers from step 3, via a list comprehension.
6. Sorts that list of tuples in descending order by square (`sort`).
7. Restarting from the list in step 3: builds a list of `(index, element)`
   tuples for elements at even indices, in reverse order — using a single
   `for` loop over `range` only (no comprehension, `sort`, or `enumerate`).
8. Transforms the list from step 7 so the first tuple element is always
   greater than the second (swapping as needed), keeping only pairs whose
   product exceeds 10 — via a single list comprehension with both
   conditions.

## Files

- `lab02.py` — the submitted solution to the numbered task above.

## Setup

Environment setup: https://www.anaconda.com/docs/getting-started/miniconda/install/overview#quickstart-install-instructions
