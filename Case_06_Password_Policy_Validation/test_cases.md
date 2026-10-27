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

**Evidence note:** The table provides expected outcomes, not a claim that every case has been executed. Browser automation could not enter code into the online IDE. Capture screenshots from actual local executions before marking tests as completed.
