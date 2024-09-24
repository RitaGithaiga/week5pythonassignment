# file creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is a string\n")
        file.write("36\n")
        file.write("this is another string\n")

    print("'my_file.txt' has been created and written into successfully")
except (PermissionError, IOError) as e:
    print(f"error occurred while creating the file: {e}")

# file reading and display
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except PermissionError:
    print("Error: You do not have permission to read the file.")

# file appending

try:
    with open("my_file.txt", "a") as file:
        file.write("i am appending this file\n")
        file.write("47\n")
        file.write("i am appending this file again\n")

    print("three new lines have been appended to the file")
except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except PermissionError:
    print("Error: You do not have permission to append to the file.")

try:
    with open("my_file.txt", "r") as file:
        updated_contents = file.read()
        print(updated_contents)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except PermissionError:
    print("Error: You do not have permission to read the file.")

