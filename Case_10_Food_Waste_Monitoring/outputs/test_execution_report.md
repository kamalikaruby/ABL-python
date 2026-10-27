# Execution Report — Case Study 10: Food Waste Monitoring System

## Local execution results
All five scenarios in `test_cases.md` were executed locally with scripted inputs. **5 of 5 tests passed**, with no syntax or runtime errors.

| Test | Result |
|---|---|
| Target met | Passed — 500 prepared, 25 leftover, 5.0% waste |
| Target exceeded | Passed — 500 prepared, 100 leftover, 20.0% waste |
| No waste | Passed — 0.0% waste; target met |
| All food left | Passed — 100.0% waste; target exceeded |
| Invalid leftover | Passed — invalid quantities rejected |

## Output captures
- `test_01.svg` — waste percentage within target
- `test_02.svg` — invalid leftover quantity

These SVGs render captured local Python stdout; they are not browser IDE screenshots. The online IDE automation attempt could not enter code. The 10% target is an illustrative classroom assumption.
