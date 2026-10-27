# Case Study 06: Password Policy Validation
# Syllabus: strings, variables, loops, comparisons, and conditions.

password = input("Enter a password: ")

character_count = 0
uppercase_found = False
lowercase_found = False
digit_found = False

for character in password:
    character_count = character_count + 1

    if character >= "A" and character <= "Z":
        uppercase_found = True

    if character >= "a" and character <= "z":
        lowercase_found = True

    if character >= "0" and character <= "9":
        digit_found = True

length_ok = character_count >= 8

print("At least 8 characters:", length_ok)
print("Contains uppercase letter:", uppercase_found)
print("Contains lowercase letter:", lowercase_found)
print("Contains digit:", digit_found)

if length_ok and uppercase_found and lowercase_found and digit_found:
    print("Password result: VALID")
else:
    print("Password result: INVALID")
