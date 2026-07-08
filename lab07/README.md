# Lab 07 — Generators: Server Log Processing

## Task

Write a program that processes server log entries (`loaded_logs`, a
list of dicts with `ip`, `timestamp`, `method`, `page`, `status`) using
**generators** for every step. Structures must stay as default arguments,
not globals.

1. A generator yielding one log line at a time.
2. Using the generator from (1), a generator that reformats each line into
   a tuple `(ip, timestamp, method, page, status)`.
3. Using `yield from` + `filter`, a generator yielding only entries with a
   successful status (`200 <= status < 300`).
4. A generator that groups all entries internally by IP, then yields the
   list of entries for each IP address in turn.
5. Same as (4), but only yields groups whose entry count exceeds a given
   `threshold`.
6. A generator returning a random sample of logs of a given size via
   `random.sample`, where the requested sample size can be *changed
   between calls* using `.send()`. Sizes larger than the log count return
   everything; sizes `<= 0` return an empty list. (Must be written so it
   can run indefinitely — a different design than the earlier, size-fixed
   generators.)
7+8. A generator performing a **sliding-window** analysis over the logs
   with a window size fixed at creation time (not via `send`). Each step
   yields a dict mapping `method`/`page`/`status` to per-value
   occurrence counts within the current window, plus the window's
   `(start, end)` range as a tuple. The window slides one entry at a time
   until it reaches the end of the log list; a non-positive window size
   yields nothing, and a window larger than the log list is clamped to the
   full list.

## Files

- `lab07.py` — the submitted solution.
- `result.txt` — captured console output from running the solution.
