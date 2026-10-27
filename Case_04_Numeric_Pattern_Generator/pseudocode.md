# Pseudocode — Case Study 04: Numeric Pattern Generator

```text
START
READ rows
IF rows < 1 OR rows > 10
    DISPLAY invalid row count
ELSE
    SET row = 1
    WHILE row <= rows
        SET column = 1
        SET line = empty string
        WHILE column <= row
            ADD column and a space to line
            INCREASE column
        END WHILE
        DISPLAY line
        INCREASE row
    END WHILE
END IF
STOP
```
