# Step 1: Write user input to the file
text_to_write = input("Enter text to write to the file: ")
with open('output.txt', 'w') as file:
    file.write(text_to_write + '\n')
print("Data successfully written to output.txt.")

# Step 2: Append additional data
text_to_append = input("Enter additional text to append: ")
with open('output.txt', 'a') as file:
    file.write(text_to_append + '\n')
print("Data successfully appended.")

# Step 3: Read and display the final content
with open('output.txt', 'r') as file:
    content = file.read()
print("Final content of output.txt:")
print(content)
