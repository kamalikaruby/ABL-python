# Pseudocode — Case Study 07: String-Based Examination Answer Evaluation

```text
START
SET answer_key = [A, C, B, D, A]
READ five answers and validate each as A, B, C, or D
IF any answer is invalid
    DISPLAY invalid answer
ELSE
    SET score = 0
    FOR each question
        IF answer matches key at same position
            INCREASE score
        END IF
    END FOR
    CALCULATE percentage = score / 5 * 100
    DISPLAY score and percentage
END IF
STOP
```
