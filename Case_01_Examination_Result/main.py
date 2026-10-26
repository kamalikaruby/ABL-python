# Case Study 01: Examination Result and Grace-Mark Validation
# Syllabus concepts: variables, input/output, data types, operators,
# conditional statements, while loops, strings, and lists.

PASS_MARK = 40
GRACE_LIMIT = 5
SUBJECT_COUNT = 5

marks = []
subject = 1
valid_input = True

while subject <= SUBJECT_COUNT and valid_input:
    mark = int(input("Enter marks for subject " + str(subject) + " (0-100): "))

    if mark < 0 or mark > 100:
        print("Invalid marks. Enter a value from 0 to 100.")
        valid_input = False
    else:
        marks.append(mark)
        subject = subject + 1

if valid_input:
    failed_count = 0
    failed_index = 0
    index = 0

    while index < SUBJECT_COUNT:
        if marks[index] < PASS_MARK:
            failed_count = failed_count + 1
            failed_index = index
        index = index + 1

    # Illustrative classroom rule only, not an official college policy.
    if failed_count == 1:
        needed = PASS_MARK - marks[failed_index]

        if needed <= GRACE_LIMIT:
            marks[failed_index] = marks[failed_index] + needed
            print("Grace marks awarded:", needed, "to subject", failed_index + 1)

    total = 0
    index = 0

    while index < SUBJECT_COUNT:
        total = total + marks[index]
        index = index + 1

    percentage = total / SUBJECT_COUNT

    print("\nFinal marks:", marks)
    print("Total:", total, "/", SUBJECT_COUNT * 100)
    print("Percentage:", percentage, "%")

    all_passed = True
    index = 0

    while index < SUBJECT_COUNT:
        if marks[index] < PASS_MARK:
            all_passed = False
        index = index + 1

    if all_passed:
        print("Result: PASS")
    else:
        print("Result: FAIL")
