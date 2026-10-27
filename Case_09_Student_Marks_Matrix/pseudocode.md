# Pseudocode — Case Study 09: Student Marks Matrix Analysis

```text
START
SET student_count = 3 and subject_count = 3
READ marks into nested list, validating each mark from 0 to 100
IF any mark is invalid
    DISPLAY invalid marks
ELSE
    FOR each student row
        CALCULATE row total
        DISPLAY student total
    END FOR
    FOR each subject column
        ADD marks from all students
        CALCULATE average = subject total / 3
        DISPLAY subject average
    END FOR
END IF
STOP
```
