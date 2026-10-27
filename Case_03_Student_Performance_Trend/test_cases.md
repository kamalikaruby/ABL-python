# Test Cases — Case Study 03: Student Performance Trend Analysis

## Test table

| Test | Input scenario | Expected result |
|---|---|---|
| 1 — Improved | 55, 60, 66, 75 | Total 256; average 64.0; trend Improved. |
| 2 — Declined | 80, 70, 72, 60 | Total 282; average 70.5; trend Declined. |
| 3 — Unchanged | 60, 70, 80, 60 | Total 270; average 67.5; trend Unchanged. |
| 4 — Invalid mark | 55, 110 | Invalid marks message; no summary. |

## How to run the cases
Run `python main.py` in this folder and enter each scenario. When a case lists multiple values, enter every value in the order requested by the program.

## Evidence note
The table contains expected outcomes, not a claim that all test cases have been executed. Automated browser input to the online IDE was unsuccessful. Capture screenshots from actual local Python runs before marking tests as executed.
