# Pseudocode — Case Study 08: Text Compression Using Character Runs

```text
START
READ text
IF text is empty
    DISPLAY empty text message
ELSE
    SET current_character = first character
    SET run_count = 0
    SET compressed_text = empty string
    FOR each character in text
        IF character equals current_character
            INCREASE run_count
        ELSE
            APPEND current_character and run_count
            SET current_character = character
            SET run_count = 1
        END IF
    END FOR
    APPEND final character and count
    DISPLAY compressed text
END IF
STOP
```
