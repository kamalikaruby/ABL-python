# Case Study 02: ATM Transaction Sequence Simulation
# Syllabus: variables, input/output, operators, if-statements, while loops, strings, lists.

balance = 1000
history = []
history_count = 0

transaction_count = int(input("How many transactions (1-10)? "))

if transaction_count < 1 or transaction_count > 10:
    print("Invalid transaction count. Enter a number from 1 to 10.")
else:
    transaction_number = 1

    while transaction_number <= transaction_count:
        transaction_type = input("Enter D for deposit or W for withdrawal: ")
        amount = int(input("Enter amount: "))

        if transaction_type == "D":
            if amount > 0:
                balance = balance + amount
                history.append("Deposit: " + str(amount) + " accepted")
                history_count = history_count + 1
                print("Deposit accepted.")
            else:
                history.append("Deposit rejected: invalid amount")
                history_count = history_count + 1
                print("Amount must be positive.")
        elif transaction_type == "W":
            if amount > 0 and amount <= balance:
                balance = balance - amount
                history.append("Withdrawal: " + str(amount) + " accepted")
                history_count = history_count + 1
                print("Withdrawal accepted.")
            else:
                history.append("Withdrawal rejected: invalid amount or balance")
                history_count = history_count + 1
                print("Withdrawal rejected. Check amount and balance.")
        else:
            history.append("Rejected: transaction type must be D or W")
            history_count = history_count + 1
            print("Invalid transaction type.")

        transaction_number = transaction_number + 1

    print("\nTransaction history:")
    index = 0
    while index < history_count:
        print(history[index])
        index = index + 1

    print("Final balance:", balance)
