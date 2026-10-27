# Test Cases — Case Study 08: Text Compression Using Character Runs

| Test | Input scenario | Expected result |
|---|---|---|
| 1 — Repeated runs | aaabbc | Compressed text: a3b2c1. |
| 2 — No repeating characters | abcd | Compressed text: a1b1c1d1. |
| 3 — One repeated character | xxxxx | Compressed text: x5. |
| 4 — Alternating characters | abab | Compressed text: a1b1a1b1. |
| 5 — Empty text | press Enter without text | No text entered. |

## Running the tests
Run `python main.py` and enter each scenario's values when prompted.


**Local verification:** All five documented test scenarios were executed locally with scripted inputs; all passed. See `outputs/test_execution_report.md`. The SVGs in `outputs/` render captured stdout and are not browser IDE screenshots.
