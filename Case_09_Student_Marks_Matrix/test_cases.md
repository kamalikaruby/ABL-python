# Test Cases — Case Study 09: Student Marks Matrix Analysis

| Test | Input scenario | Expected result |
|---|---|---|
| 1 — Sequential values | Rows: 10,20,30; 40,50,60; 70,80,90 | Student totals 60, 150, 240; subject averages 40.0, 50.0, 60.0. |
| 2 — All 100 | Nine marks of 100 | Each student total 300; each subject average 100.0. |
| 3 — All zero | Nine marks of 0 | Each student total 0; each subject average 0.0. |
| 4 — Invalid mark | First mark 101 | Invalid marks message; no totals or averages. |

## How to run
Run `python main.py` and enter the scenario values in order when prompted.

**Evidence note:** These are expected outcomes, not a claim that tests were executed. Browser automation could not enter code into the online IDE. Capture screenshots from actual runs before marking tests completed.
