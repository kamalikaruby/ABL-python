# Case Study 10: Food Waste Monitoring System
# Syllabus: variables, lists, loops, operators, and if-statements.
# The 10 percent target is illustrative for this classroom exercise.

DAY_COUNT = 5
WASTE_TARGET = 10
prepared_list = []
leftover_list = []
day = 1
valid_input = True

while day <= DAY_COUNT and valid_input:
    prepared = int(input("Day " + str(day) + " food prepared (units): "))
    leftover = int(input("Day " + str(day) + " food leftover (units): "))

    if prepared <= 0 or leftover < 0 or leftover > prepared:
        print("Invalid quantities. Prepared must be positive and leftover must be 0 to prepared.")
        valid_input = False
    else:
        prepared_list.append(prepared)
        leftover_list.append(leftover)
        day = day + 1

if valid_input:
    total_prepared = 0
    total_leftover = 0
    index = 0

    while index < DAY_COUNT:
        total_prepared = total_prepared + prepared_list[index]
        total_leftover = total_leftover + leftover_list[index]
        index = index + 1

    waste_percentage = total_leftover / total_prepared * 100

    print("Total food prepared:", total_prepared)
    print("Total food leftover:", total_leftover)
    print("Food waste percentage:", waste_percentage, "%")

    if waste_percentage <= WASTE_TARGET:
        print("Waste target met.")
    else:
        print("Waste target exceeded.")
