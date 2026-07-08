# Lab 06 — Functional Programming: map/filter/reduce/lambda

## Task

Implement a small customer-database toolkit using the given data
structures (`user_db` — a dict of users, `friend_groups` — a
list of friend-group ID tuples), with a strict constraint: **each
function must use a specific built-in + lambda combination**.

1. Return a list of every user's first name — `map` + lambda, cast to a
   list.
2. Filter users by email domain, returning a dict with the same
   `{id: user}` shape — `filter` + lambda, cast to `dict`.
3. Return the IDs of users within a min/max age range and a given
   employment status — chained `map` + `filter` + lambdas (filter first,
   then map to IDs).
4. Return the names of the youngest and oldest user — `min`/`max` with a
   `key=` lambda.
5. Compute the average age of all users — `reduce` + lambda.
6. Return the user dict sorted by status, then age, then name, *without*
   mutating the original — `sorted` with a tuple `key`.
7+8. For each friend group, compute each member's "influence score": the
   number of *mutual* friends shared with every other member of that group
   (a third person counts only if they appear together with **both**
   compared members in some group), summed and divided by group size.
   Store per-group results (per-member influence list + group average) in
   a dict keyed by the group tuple. Then: (a) find users whose influence
   exceeds the **global** average influence in every group they belong to;
   (b) find users whose influence exceeds the **local** (per-group)
   average in every group they belong to; (c) find users satisfying both.

## Files

- `lab06.py` — the submitted solution.
