# Case Study 01 — Test Execution Report

All 8 test input sets were executed against `main.py` using Python in an isolated execution environment. The screenshots in this folder are terminal-style SVG images generated from the captured output of those runs. TinyFish opened the online IDE but could not enter code into its editor, so these are not screenshots captured from the TinyFish browser.

| Test | Inputs | Observed result |
|---|---|---|
| 01_all_pass | 70, 80, 65, 90, 75 | PASS |
| 02_grace_marks | 70, 80, 65, 90, 38 | PASS |
| 03_two_failed_subjects | 70, 30, 65, 90, 38 | FAIL |
| 04_negative_mark | 70, 80, -1 | Invalid marks rejected |
| 05_mark_above_100 | 70, 80, 65, 101 | Invalid marks rejected |
| 06_exact_pass_mark | 40, 40, 40, 40, 40 | PASS |
| 07_grace_limit_boundary | 70, 80, 65, 90, 35 | PASS |
| 08_beyond_grace_limit | 70, 80, 65, 90, 34 | FAIL |

## Important assumption
Grace marks are an illustrative classroom rule only: up to 5 marks may be added when exactly one subject is below 40. This is not confirmed college policy.

Open each SVG file to view the corresponding test output.
