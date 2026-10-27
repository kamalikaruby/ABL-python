# Test Cases — Case Study 07: String-Based Examination Answer Evaluation

| Test | Input scenario | Expected result |
|---|---|---|
| 1 — All correct | A, C, B, D, A | Score 5/5; percentage 100.0%. |
| 2 — All incorrect | B, A, D, C, B | Score 0/5; percentage 0.0%. |
| 3 — Three correct | A, C, A, D, B | Score 3/5; percentage 60.0%. |
| 4 — Invalid answer | A, C, X | Invalid answer message; no score shown. |

## Running the tests
Run `python main.py` and enter each scenario's values when prompted.


**Local verification:** All four documented test scenarios were executed locally with scripted inputs; all passed. See `outputs/test_execution_report.md`. The SVGs in `outputs/` render captured stdout and are not browser IDE screenshots.
