# Lab 11 — Inheritance, Iterators and Mixins

## Task

Extend a small online-library toy application using inheritance and custom iterators:

- Add `DigitalBook`, a subclass of the base `Book` class that adds a
  `file_size` field, calling the base class's `__init__` for the shared
  fields.
- Add `PrintedBook`, another `Book` subclass that adds an `edition` field.
- Implement `LibraryIterator`, an iterator over the library's book
  list: takes the list in `__init__`, implements `__iter__` (returns
  `self`) and `__next__` (returns the next book, raising `StopIteration`
  at the end).
- Implement `BookTypeIterator`, a variant that only yields books of a
  given type — same shape as above, but `__next__` skips books that
  don't match the requested type.
- Wire both iterators into the `Library` class: default
  iteration (`__iter__`) walks all books, while a second method,
  `iterate_by_type`, exposes the type-filtered
  iterator — since a class can only have one "official" `__iter__`.
- Implement a mixin class `Borrowable` that can be
  added to other classes without being part of their main inheritance
  chain. It tracks a `borrowed` boolean, and exposes
  `borrow`/`return_book` methods plus an `is_borrowed`
  property. Both methods raise a custom `BorrowError` exception
  (subclassing `Exception`, with a custom `__str__`) if called in the
  wrong state (e.g. borrowing an already-borrowed book).
- Combine the pieces into `BorrowablePrintedBook`, using only the
  classes built above (no extra state), which must initialize both
  parent classes.

## Files

- `lab11.py` — the submitted solution.
