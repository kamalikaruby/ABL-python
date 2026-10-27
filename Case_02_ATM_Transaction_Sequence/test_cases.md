# Test Cases — Case Study 02: ATM Transaction Sequence Simulation

## Test table

| Test | Input scenario | Expected result |
|---|---|---|
| 1 — Deposit and withdrawal | count=2; D, 500; W, 300 | Both accepted; final balance is 1200. |
| 2 — Withdrawal exceeds balance | count=1; W, 1500 | Withdrawal rejected; final balance remains 1000. |
| 3 — Zero amount | count=1; D, 0 | Deposit rejected; final balance remains 1000. |
| 4 — Invalid transaction type | count=1; X, 100 | Invalid type recorded; final balance remains 1000. |
| 5 — Invalid transaction count | count=0 | Invalid transaction count message. |

## How to run the cases
Run `python main.py` in this folder and enter each scenario. When a case lists multiple values, enter every value in the order requested by the program.

## Evidence note
The table contains expected outcomes, not a claim that all test cases have been executed. Automated browser input to the online IDE was unsuccessful. Capture screenshots from actual local Python runs before marking tests as executed.
