# Test Cases — Case Study 10: Food Waste Monitoring System

| Test | Input scenario | Expected result |
|---|---|---|
| 1 — Target met | Prepared 100 each day; leftover 5 each day | Prepared 500; leftover 25; waste 5.0%; target met. |
| 2 — Target exceeded | Prepared 100 each day; leftover 20 each day | Prepared 500; leftover 100; waste 20.0%; target exceeded. |
| 3 — No waste | Prepared 50 each day; leftover 0 each day | Waste 0.0%; target met. |
| 4 — All food left | Prepared 10 each day; leftover 10 each day | Waste 100.0%; target exceeded. |
| 5 — Invalid leftover | Day 1 prepared 20; leftover 25 | Invalid quantities message; no summary. |

## How to run
Run `python main.py` and enter the scenario values in order when prompted.


**Local verification:** All five documented test scenarios were executed locally with scripted inputs; all passed. See `outputs/test_execution_report.md`. The SVGs in `outputs/` render captured stdout and are not browser IDE screenshots.
