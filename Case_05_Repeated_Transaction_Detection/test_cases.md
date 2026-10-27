# Test Cases — Case Study 05: Repeated Transaction Detection

| Test | Input scenario | Expected result |
|---|---|---|
| 1 — One repeated amount | 5; 100, 200, 100, 300, 400 | Repeated amounts: [100]. |
| 2 — Two repeated amounts | 6; 50, 50, 75, 75, 90, 100 | Repeated amounts: [50, 75]. |
| 3 — No repeats | 4; 100, 200, 300, 400 | No repeated amounts found. |
| 4 — Triple occurrence | 4; 20, 20, 20, 50 | Repeated amounts: [20] only once. |
| 5 — Invalid amount | 3; 100, 0 | Invalid amount message; no summary. |

## Running the tests
Run `python main.py` and enter the scenario values in the order prompted by the program.

**Evidence note:** The table provides expected outcomes, not a claim that every case has been executed. Browser automation could not enter code into the online IDE. Capture screenshots from actual local executions before marking tests as completed.
