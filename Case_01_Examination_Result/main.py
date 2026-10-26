# Case Study 01: Examination Result and Grace-Mark Validation
# Syllabus concepts: variables, lists, loops, operators, if-statements.

PASS_MARK = 40
GRACE_LIMIT = 5
SUBJECT_COUNT = 5

marks = []
valid_input = True

for subject in range(SUBJECT_COUNT):
    mark = int(input("Enter marks for subject " + str(subject + 1) + " (0-100): "))
    if mark < 0 or mark > 100:
        print("Invalid marks. Enter a value from 0 to 100.")
        valid_input = False
        break
    marks.append(mark)

if valid_input and len(marks) == SUBJECT_COUNT:
    failed_subjects = []
    for index in range(SUBJECT_COUNT):
        if marks[index] < PASS_MARK:
            failed_subjects.append(index)

    # Illustrative policy only: grace marks may be applied to one subject.
    if len(failed_subjects) == 1:
        index = failed_subjects[0]
        needed = PASS_MARK - marks[index]
        if needed <= GRACE_LIMIT:
            marks[index] = marks[index] + needed
            print("Grace marks awarded:", needed, "to subject", index + 1)

    total = 0
    for mark in marks:
        total = total + mark

    percentage = total / SUBJECT_COUNT
    print("\nFinal marks:", marks)
    print("Total:", total, "/", SUBJECT_COUNT * 100)
    print("Percentage:", round(percentage, 2), "%")

    all_passed = True
    for mark in marks:
        if mark < PASS_MARK:
            all_passed = False

    if all_passed:
        print("Result: PASS")
    else:
        print("Result: FAIL")