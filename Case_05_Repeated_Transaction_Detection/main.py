# Case Study 05: Repeated Transaction Detection
# Syllabus: lists, nested while loops, operators, and if-statements.
# Equal amounts are treated as repeats for this classroom example.

transaction_count = int(input("How many transactions (1-10)? "))
transactions = []
valid_input = True

if transaction_count < 1 or transaction_count > 10:
    print("Invalid transaction count. Enter a number from 1 to 10.")
    valid_input = False

index = 0
while index < transaction_count and valid_input:
    amount = int(input("Enter transaction amount: "))

    if amount <= 0:
        print("Transaction amount must be positive.")
        valid_input = False
    else:
        transactions.append(amount)
        index = index + 1

if valid_input:
    repeated = []
    repeated_count = 0
    index = 0

    while index < transaction_count:
        matches = 0
        compare_index = 0

        while compare_index < transaction_count:
            if transactions[index] == transactions[compare_index]:
                matches = matches + 1
            compare_index = compare_index + 1

        already_recorded = False
        repeated_index = 0

        while repeated_index < repeated_count:
            if repeated[repeated_index] == transactions[index]:
                already_recorded = True
            repeated_index = repeated_index + 1

        if matches > 1 and not already_recorded:
            repeated.append(transactions[index])
            repeated_count = repeated_count + 1

        index = index + 1

    print("Transactions:", transactions)

    if repeated_count == 0:
        print("No repeated amounts found.")
    else:
        print("Repeated amounts:", repeated)
