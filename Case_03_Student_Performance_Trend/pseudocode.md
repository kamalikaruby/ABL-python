# Pseudocode — Case Study 03: Student Performance Trend Analysis

```text
START
SET assessment_count = 4
READ and validate four marks
IF any mark is outside 0 to 100
    DISPLAY invalid marks
ELSE
    CALCULATE total using a loop
    CALCULATE average = total / 4
    IF last mark > first mark
        SET trend = improved
    ELSE IF last mark < first mark
        SET trend = declined
    ELSE
        SET trend = unchanged
    END IF
    DISPLAY marks, total, average, trend
END IF
STOP
```
