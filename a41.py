try:
    # Open the file in read mode ('r')
    file = open('sample.txt', 'r')
    print("Reading file content:")
    content = file.read()
    print(content, end='')  # end='' to avoid extra newline
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
finally:
    # Close the file only if it was opened successfully
    try:
        file.close()
    except NameError:
        pass
    print("File has been closed.")