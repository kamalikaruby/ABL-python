# Pseudocode — Case Study 02: ATM Transaction Sequence Simulation

```text
START
SET balance = 1000
READ transaction_count
IF transaction_count is outside 1 to 10
    DISPLAY invalid transaction count
ELSE
    REPEAT transaction_count times
        READ transaction type and amount
        IF type is D AND amount > 0
            ADD amount to balance and record deposit
        ELSE IF type is W AND amount > 0 AND amount <= balance
            SUBTRACT amount from balance and record withdrawal
        ELSE
            DISPLAY rejection and record it
        END IF
    END REPEAT
    DISPLAY transaction history and balance
END IF
STOP
```
