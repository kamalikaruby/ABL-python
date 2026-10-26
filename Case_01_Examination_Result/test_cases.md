# Test Cases — Case Study 01: Examination Result and Grace-Mark Validation

## Assumptions
- There are exactly 5 subjects.
- Each mark must be an integer from 0 to 100.
- The pass mark is 40.
- For this classroom example only, if exactly one subject is below 40 and needs at most 5 marks to pass, the program adds the required grace marks. This is an illustrative rule, not a statement of college policy.

## Test table

| Test | Subject marks entered | Expected result |
|---|---|---|
| 1 — All pass | 70, 80, 65, 90, 75 | No grace marks; total 380/500; percentage 76.0%; PASS |
| 2 — Grace marks | 70, 80, 65, 90, 38 | 2 grace marks to subject 5; adjusted marks [70, 80, 65, 90, 40]; total 345/500; percentage 69.0%; PASS |
| 3 — More than one failed subject | 70, 30, 65, 90, 38 | No grace marks; total 293/500; percentage 58.6%; FAIL |
| 4 — Below zero | 70, 80, -1 | Display invalid marks message and stop input |
| 5 — Above 100 | 70, 80, 65, 101 | Display invalid marks message and stop input |
| 6 — Exactly at pass mark | 40, 40, 40, 40, 40 | No grace marks; total 200/500; percentage 40.0%; PASS |
| 7 — Grace limit boundary | 70, 80, 65, 90, 35 | 5 grace marks to subject 5; adjusted total 340/500; percentage 68.0%; PASS |
| 8 — Outside grace limit | 70, 80, 65, 90, 34 | No grace marks; total 339/500; percentage 67.8%; FAIL |

## Sample run — Test 1

```text
Enter marks for subject 1 (0-100): 70
Enter marks for subject 2 (0-100): 80
Enter marks for subject 3 (0-100): 65
Enter marks for subject 4 (0-100): 90
Enter marks for subject 5 (0-100): 75

Final marks: [70, 80, 65, 90, 75]
Total: 380 / 500
Percentage: 76.0 %
Result: PASS
```

## Sample run — Test 2

```text
Enter marks for subject 1 (0-100): 70
Enter marks for subject 2 (0-100): 80
Enter marks for subject 3 (0-100): 65
Enter marks for subject 4 (0-100): 90
Enter marks for subject 5 (0-100): 38
Grace marks awarded: 2 to subject 5

Final marks: [70, 80, 65, 90, 40]
Total: 345 / 500
Percentage: 69.0 %
Result: PASS
```

## How to verify
1. Open a terminal in this folder.
2. Run `python main.py` (or `python3 main.py`).
3. Enter the values from each test row in order.
4. Compare the actual output with the expected result.
5. Save screenshots of actual program runs in the `outputs/` folder. Do not use sample text as a substitute for genuine run screenshots.
