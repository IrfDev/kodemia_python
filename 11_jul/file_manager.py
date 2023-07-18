# Create a function that create a file, create a function that update a file, create an option that delete a file


# File can have content, or not


import os


def is_content_empty(content: str):
    return content and isinstance(content, str)


def create_file(file_name: str, content: str = None):
    with_content = is_content_empty(content)

    open_mode = "w" if with_content else "x"

    new_file = open(file_name, open_mode)

    if with_content:
        new_file.write(content)

    new_file.close()


def update_file(file_name: str, content: str, overwrite: bool = False):
    open_mode = "w" if overwrite else "a"

    file = open(file_name, open_mode)

    file.write(content)

    file.close()


def delete_file(file_path):
    is_file_exists = os.path.exists(file_path)

    if is_file_exists:
        os.remove(file_path)


def read_file(file_path):
    is_file_exists = os.path.exists(file_path)

    if is_file_exists:
        file = open(file_path)
        print(file.read())
