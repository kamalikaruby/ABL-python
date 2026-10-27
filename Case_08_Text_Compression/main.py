# Case Study 08: Text Compression Using Character Runs
# Syllabus: strings, loops, variables, operators, and conditions.

text = input("Enter text to compress: ")

if text == "":
    print("No text entered.")
else:
    current_character = text[0]
    run_count = 0
    compressed_text = ""

    for character in text:
        if character == current_character:
            run_count = run_count + 1
        else:
            compressed_text = compressed_text + current_character + str(run_count)
            current_character = character
            run_count = 1

    compressed_text = compressed_text + current_character + str(run_count)

    print("Original text:", text)
    print("Compressed text:", compressed_text)
