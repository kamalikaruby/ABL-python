# Case Study 07: String-Based Examination Answer Evaluation
# Syllabus: strings, lists, loops, operators, and if-statements.

answer_key = ["A", "C", "B", "D", "A"]
answers = []
question = 1
valid_input = True

while question <= 5 and valid_input:
    answer = input("Enter answer for question " + str(question) + " (A/B/C/D): ")

    if answer == "A" or answer == "B" or answer == "C" or answer == "D":
        answers.append(answer)
        question = question + 1
    else:
        print("Invalid answer. Enter uppercase A, B, C, or D.")
        valid_input = False

if valid_input:
    score = 0
    question_index = 0

    while question_index < 5:
        if answers[question_index] == answer_key[question_index]:
            score = score + 1
        question_index = question_index + 1

    percentage = score / 5 * 100

    print("Student answers:", answers)
    print("Correct answers:", answer_key)
    print("Score:", score, "/ 5")
    print("Percentage:", percentage, "%")
