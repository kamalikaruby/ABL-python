# Pseudocode — Case Study 06: Password Policy Validation

```text
START
READ password
SET character_count = 0
SET uppercase_found, lowercase_found, digit_found = false
FOR each character in password
    INCREASE character_count
    IF character is between A and Z, set uppercase_found = true
    IF character is between a and z, set lowercase_found = true
    IF character is between 0 and 9, set digit_found = true
END FOR
SET length_ok = character_count >= 8
DISPLAY all checks
IF length_ok AND uppercase_found AND lowercase_found AND digit_found
    DISPLAY VALID
ELSE
    DISPLAY INVALID
END IF
STOP
```
