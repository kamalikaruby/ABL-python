# Pseudocode

```text
START
SET PASS_MARK = 40
SET GRACE_LIMIT = 5
READ marks for five subjects

IF any mark < 0 OR any mark > 100
    DISPLAY invalid marks message
ELSE
    FIND all subjects with marks below PASS_MARK
    IF exactly one subject failed AND its mark is from 35 to 39
        ADD required grace marks to make that mark 40
    END IF
    CALCULATE total and percentage
    IF every subject mark is at least PASS_MARK
        DISPLAY PASS
    ELSE
        DISPLAY FAIL
    END IF
    DISPLAY final marks, total, and percentage
END IF
STOP
```