# Test Cases — Case Study 06: Password Policy Validation

| Test | Input scenario | Expected result |
|---|---|---|
| 1 — Meets all rules | Study2026 | All four checks True; result VALID. |
| 2 — No uppercase | study2026 | Uppercase False; result INVALID. |
| 3 — No digit | StudyPython | Digit False; result INVALID. |
| 4 — Too short | Abc123 | Length False; result INVALID. |
| 5 — No lowercase | STUDY2026 | Lowercase False; result INVALID. |

## Running the tests
Run `python main.py` and enter the scenario values in the order prompted by the program.


**Local verification:** All five documented test scenarios were executed locally with scripted inputs; all passed. See `outputs/test_execution_report.md`. The SVGs in `outputs/` render captured stdout and are not browser IDE screenshots.
