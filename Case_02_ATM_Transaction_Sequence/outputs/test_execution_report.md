# Execution Report — Case Study 02: ATM Transaction Sequence Simulation

## Status
Source code and documentation have been prepared. Browser execution and screenshots were not completed.

## Limitation
The online IDE automation attempt could not enter code into its editor. Accordingly, this report does not claim that the tests were run in the browser or locally.

## Test scenarios prepared
1. **Deposit and withdrawal:** Both accepted; final balance is 1200.
2. **Withdrawal exceeds balance:** Withdrawal rejected; final balance remains 1000.
3. **Zero amount:** Deposit rejected; final balance remains 1000.
4. **Invalid transaction type:** Invalid type recorded; final balance remains 1000.
5. **Invalid transaction count:** Invalid transaction count message.

## Next verification step
Run `python main.py`, enter each scenario from `test_cases.md`, compare the displayed output with the expected result, then save actual screenshots in this folder.
