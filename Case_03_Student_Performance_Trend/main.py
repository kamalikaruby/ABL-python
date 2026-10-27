# Case Study 03: Student Performance Trend Analysis
# Syllabus: variables, lists, operators, if-statements, and loops.

ASSESSMENT_COUNT = 4
marks = []
assessment = 1
valid_input = True

while assessment <= ASSESSMENT_COUNT and valid_input:
    mark = int(input("Enter marks for assessment " + str(assessment) + " (0-100): "))

    if mark < 0 or mark > 100:
        print("Invalid marks. Enter a value from 0 to 100.")
        valid_input = False
    else:
        marks.append(mark)
        assessment = assessment + 1

if valid_input:
    total = 0
    index = 0

    while index < ASSESSMENT_COUNT:
        total = total + marks[index]
        index = index + 1

    average = total / ASSESSMENT_COUNT

    if marks[ASSESSMENT_COUNT - 1] > marks[0]:
        trend = "Improved"
    elif marks[ASSESSMENT_COUNT - 1] < marks[0]:
        trend = "Declined"
    else:
        trend = "Unchanged"

    print("Assessment marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Performance trend:", trend)
