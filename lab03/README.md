# Lab 03 — String-only path manipulation

## Task

Write a program that receives a file path from the command line, e.g.
`python3 kod.py /moje/pliki/testowy plik/obraz1.png`, and processes it using
**only `str` methods** (no `pathlib`). Path spaces are rejoined with
`" ".join(sys.argv[1:])`. Assumptions: the path always has at least one
directory, the file always has exactly one extension, and the filename is
at least 4 characters long.

1. Count how many directories the path contains.
2. Print the path to the containing directory (i.e. without the filename).
3. Normalize the filename to lowercase.
4. Additionally replace spaces in the normalized name with underscores.
5. Check whether the path contains a directory literally named `"dokumenty"`
   **and** the extension is one of `.txt`, `.docx`, `.pdf`, `.odt` — using a
   single boolean expression (no `if/elif` chain), by checking membership
   against a collection of allowed extensions.
6. Using string formatting and `join()`, generate 10 filenames in the form
   `{folder}/{name}_copy_{n}.{extension}` for `n` in `0..9`.
7. If the full path is longer than 60 characters and has more than two
   directories, build a shortened form `first_dir/.../last_dir/filename.ext`.
8. From the normalized name (steps 3-4), build an identifier
   `PREFIX-YEAR-NR.extension`, where `PREFIX` is the first 3 letters of the
   filename, `YEAR` is the first 4-digit number found in the name (`"0000"`
   if none), and `NR` is the last number found in the name (`0` if none).

## Files

- `lab03.py` — the submitted solution. The path is split into `katalogi`
  (directory list) once up front and reused for every step instead of
  re-splitting the path each time.
