# Case Study 09: Student Marks Matrix Analysis
# Syllabus: nested lists, nested while loops, operators, and conditions.

STUDENT_COUNT = 3
SUBJECT_COUNT = 3

marks = []
student_index = 0
valid_input = True

while student_index < STUDENT_COUNT and valid_input:
    row = []
    subject_index = 0

    while subject_index < SUBJECT_COUNT and valid_input:
        mark = int(input("Student " + str(student_index + 1) +
                         ", subject " + str(subject_index + 1) + " marks: "))

        if mark < 0 or mark > 100:
            print("Invalid marks. Enter a value from 0 to 100.")
            valid_input = False
        else:
            row.append(mark)
            subject_index = subject_index + 1

    if valid_input:
        marks.append(row)
        student_index = student_index + 1

if valid_input:
    student_index = 0
    while student_index < STUDENT_COUNT:
        student_total = 0
        subject_index = 0

        while subject_index < SUBJECT_COUNT:
            student_total = student_total + marks[student_index][subject_index]
            subject_index = subject_index + 1

        print("Total for student", student_index + 1, ":", student_total)
        student_index = student_index + 1

    subject_index = 0
    while subject_index < SUBJECT_COUNT:
        subject_total = 0
        student_index = 0

        while student_index < STUDENT_COUNT:
            subject_total = subject_total + marks[student_index][subject_index]
            student_index = student_index + 1

        subject_average = subject_total / STUDENT_COUNT
        print("Average for subject", subject_index + 1, ":", subject_average)
        subject_index = subject_index + 1
