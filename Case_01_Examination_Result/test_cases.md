# Test Cases

| Test | Subject marks entered | Expected result |
|---|---|---|
| 1 | 70, 80, 65, 90, 75 | PASS; total 380/500; percentage 76.0% |
| 2 | 70, 80, 65, 90, 38 | 2 grace marks for subject 5; adjusted total 343/500; percentage 68.6%; PASS |
| 3 | 70, 30, 65, 90, 38 | FAIL because two subjects are below 40; no grace marks applied |
| 4 | 70, 80, -1, 90, 75 | Invalid marks message |

## Example output for Test 1

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

Run each test yourself and save terminal screenshots in an `outputs/` folder before submission.