# Algorithm — Case Study 08: Text Compression Using Character Runs

1. Read the text.
2. If it is empty, display a message.
3. Set the current character to the first character and run count to zero.
4. Scan every character and increase the count while it matches the current character.
5. When the character changes, append the previous character and count, then begin a new run.
6. Append the last run and display the compressed text.
