# Lab 12 — Decorators for HTTP Request Monitoring

## Task

Build an HTTP-request monitoring toolkit for a fictional service purely
with decorators:

1. **Logging decorator** — wraps a function taking a `request`, logs the
   start (with the request's contents) and end of processing (with the
   elapsed time via `time.time()`), and must return the wrapped
   function's result unchanged.
2. **Authentication decorator** — takes an optional "required role"
   argument (`None` = allow everyone). It must check that the request
   carries a user, and that the user's role matches the required role
   (an admin is always let through). Raises a custom
   `AuthenticationError` otherwise.
3. **Retry decorator** — takes a max-retry count, retries the wrapped
   call on exception with a `time.sleep(0.5)` between attempts, and
   raises a custom `FailedRequest` once retries are exhausted.
4. **Class-level anti-spam decorator** — a decorator *factory* that,
   given a class, dynamically creates a subclass tracking a per-user
   call counter shared across all its methods. It must find all public
   (non-underscore-prefixed) callables via `dir()`/`getattr()`, wrap
   each with a rate-limiting check via `setattr()`, and raise
   `TooManyRequests` once a user exceeds the allowed number of calls —
   all without hardcoding the class's method names, so it keeps working
   if the class is later modified.

## Files

- `lab12.py` — the submitted solution. Running it produces an `http.log`
  file (not included here) via the logging decorator.