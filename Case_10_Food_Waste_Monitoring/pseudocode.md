# Pseudocode — Case Study 10: Food Waste Monitoring System

```text
START
SET day_count = 5 and waste_target = 10
READ prepared and leftover amounts for each day
IF prepared <= 0 OR leftover < 0 OR leftover > prepared
    DISPLAY invalid quantities
ELSE
    CALCULATE total_prepared
    CALCULATE total_leftover
    CALCULATE waste_percentage = total_leftover / total_prepared * 100
    DISPLAY totals and percentage
    IF waste_percentage <= 10
        DISPLAY target met
    ELSE
        DISPLAY target exceeded
    END IF
END IF
STOP
```
