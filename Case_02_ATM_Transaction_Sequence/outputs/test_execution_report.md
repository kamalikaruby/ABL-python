# Execution Report — Case Study 02: ATM Transaction Sequence Simulation

## Local execution results
The Python program was run locally with scripted inputs for all five scenarios in `test_cases.md`. **5 of 5 tests passed**, and no syntax or runtime errors occurred.

| Test | Result |
|---|---|
| Deposit and withdrawal | Passed — final balance 1200 |
| Withdrawal exceeds balance | Passed — withdrawal rejected; balance remains 1000 |
| Zero amount | Passed — deposit rejected |
| Invalid transaction type | Passed — invalid type reported |
| Invalid transaction count | Passed — invalid count reported |

## Output captures
- `test_01.svg` — deposit followed by withdrawal
- `test_02.svg` — withdrawal greater than available balance

These SVGs are terminal-style renderings of captured local Python output, not screenshots from the browser IDE. The online IDE automation attempt could not enter code into its editor.
