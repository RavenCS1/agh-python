# Lab 08 — File I/O: sensor readings and tank phase data

## Task

Given experimental measurements for four liquid tanks, write functions that
read, parse and reshape the raw data files into structured, in-memory data,
then use that data to generate derived reports.

- Data files are named `tank_{X}.dat` and each line holds: measurement
  time (float), temperature (float), pressure (float) and observed phase
  (string: `"ciało stałe"`/`"ciecz"`/`"gaz"`/`"mieszana"` — solid/liquid/gas/mixed).
- `sensors.csv` is a sensor database: sensor id, name, tank, type
  (temperature/pressure), unit, measurement frequency, cycle length,
  accuracy, scaling factor, and min/max operating range.
- Every file must be opened and closed with its own `with` block — no
  globally-open files.
- Values must be converted to their proper types on read (numbers must not
  stay as strings), so they can be used directly in calculations.

Required functions:
1. Read a single `.dat` file (filename as argument) and return a list of
   dicts: `[{"time": ..., "temperature": ..., "pressure": ..., "phase": ...}, ...]`.
2. Discover all `.dat` files in the working directory and build
   `{tank_name: {"readings": [...]}, ...}` using function 1.
3. Read `sensors.csv` and enrich the structure from step 2 with
   per-tank accuracy: `{"readings": [...], "accuracy": {"temperature": ..., "pressure": ...}}`.
4. For every tank, select the readings where
   `273.14 <= temperature <= 273.18` K and `610.657 <= pressure <= 612.657` Pa,
   and write them to `{tank_name}_selection.csv` (same columns/header as the
   source `.dat` files).
5. Count, per tank, how many of the selected readings have phase `"mieszana"`
   (mixed) and write a `phase_report.txt` report with a header and one row per
   tank (tank name, count of mixed-phase observations).
6. Re-open `phase_report.txt` in append mode and add (without overwriting) the
   contents of a previously generated `previous_phase_report.txt`.
7. Read `sensors.csv` and, for every row, generate a
   `sensor_{sensor_id}_config.yaml` file following a fixed
   identifier/configuration/operating-point template.

Headers and file names are in English; the actual measured values (sensor
type `"temperatura"`/`"ciśnienie"`, phase `"ciało stałe"`/`"ciecz"`/`"gaz"`/
`"mieszana"`) are left as originally recorded, since the code branches on
those exact strings.

## Files

- `lab08.py` — the submitted solution implementing all of the above.
- `tank_A.dat` … `tank_D.dat` — raw tank measurement files (input).
- `sensors.csv` — sensor metadata database (input).

Steps 4–7 write their outputs (`*_selection.csv`, `phase_report.txt`,
`sensor_*_config.yaml`) at runtime rather than shipping them pre-generated;
step 6 additionally expects a `previous_phase_report.txt` to already exist,
which isn't included here.
