# Execution Report — Case Study 05: Repeated Transaction Detection

## Local execution results
All five scenarios in `test_cases.md` were executed locally with scripted inputs. **5 of 5 tests passed**, with no syntax or runtime errors.

| Test | Result |
|---|---|
| One repeated amount | Passed — 100 reported once |
| Two repeated amounts | Passed — 50 and 75 reported |
| No repeats | Passed — no repeated amounts found |
| Triple occurrence | Passed — 20 reported once |
| Invalid amount | Passed — invalid amount message displayed |

## Output captures
- `test_01.svg` — one repeated amount
- `test_02.svg` — no repeated amounts

These SVGs render captured local Python stdout, not browser IDE screenshots. The online IDE automation attempt could not enter code.
