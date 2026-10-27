# Case Study 04: Numeric Pattern Generator
# Syllabus: variables, strings, operators, and nested while loops.

rows = int(input("Enter number of rows (1-10): "))

if rows < 1 or rows > 10:
    print("Invalid row count. Enter a number from 1 to 10.")
else:
    row = 1

    while row <= rows:
        column = 1
        line = ""

        while column <= row:
            line = line + str(column) + " "
            column = column + 1

        print(line)
        row = row + 1
