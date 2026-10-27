# Pseudocode — Case Study 05: Repeated Transaction Detection

```text
START
READ and validate transaction_count from 1 to 10
READ positive transaction amounts into transactions
SET repeated = empty list
SET repeated_count = 0
FOR each amount at index i
    COUNT occurrences of transactions[i] using an inner loop
    SEARCH repeated list for the same amount
    IF occurrence count > 1 AND value not already recorded
        APPEND value to repeated
        INCREASE repeated_count
    END IF
END FOR
DISPLAY transactions
IF repeated_count is 0
    DISPLAY no repeated amounts
ELSE
    DISPLAY repeated
END IF
STOP
```
