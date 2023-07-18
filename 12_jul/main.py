import file_manager

NEW_FILE_NAME = "new_file.txt"

try:
    file_manager.create_file(
        NEW_FILE_NAME,
    )
except IOError as error:
    print(f"The file couldn't be created {error}")


print("Script wasfinished succesfully")
