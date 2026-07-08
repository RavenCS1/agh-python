# Lab 04 — Dictionaries, dict comprehensions, permutations

## Task

Write a program that reads a sequence of integers from the command line
(e.g. `python3 kod.py 1 5 9 2 4 7 22 11 37 42 2 5`). Wherever possible, use
dictionary comprehensions.

1. Build a dict mapping each number in the sequence to its frequency (`0`
   for numbers not present); reuse `count`.
2. Randomly pick two numbers from the input (possibly duplicates) and remove
   them from the frequency dict (not from the list). Then overwrite the
   input list with the dict's remaining keys. From here on, use this
   shortened list.
3. Split the (shortened) list into two dicts under keys `"even"` (even
   index) and `"odd"` (odd index); a number appearing at both an even
   and odd index belongs in both.
4. Combine the previous two results (without recomputing from scratch) into
   a two-level dict: outer keys `"even"`/`"odd"`, inner value is
   the frequency dict (from step 1) restricted to that group's numbers.
5. Build a dict keyed by `(i, i+1)` index pairs of neighboring elements,
   valued by their difference.
6. Using a loop over the dict from step 5 (values only, no `dict[key]`
   lookups), build a new dict with the same keys but values collapsed to
   `+1`/`0`/`-1` by sign, then write it back into the original dict with
   `update`.
7. From the sorted, de-duplicated elements (`sorted(set(numbers))`), build
   three random permutations as dicts (each mapping an element to where it
   goes). Compose them into a single mapping `s = s3 . s2 . s1` (enter
   through `s1`, exit through `s3`), then decompose `s` into its permutation
   cycles by walking the mapping until returning to the starting element.
   Report the result as a dict: `{"permutation": s, 1: [cycles of length 1],
   2: [cycles of length 2], ...}`, with cycles as tuples.

## Files

- `lab04.py` — the submitted solution.
