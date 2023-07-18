# Create a function that create a file, create a function that update a file, create an option that delete a file


# File can have content, or not
import os


def is_content_empty(content):
    is_content_valid = content and isinstance(content, str)
    if is_content_valid:
        return is_content_valid
    else:
        raise ValueError


def get_is_file_exist(file_path):
    is_file_exists = os.path.exists(file_path)

    if is_file_exists:
        return True
    else:
        raise FileNotFoundError


def create_file(file_name: str, content=None):
    with_content = is_content_empty(content)

    try:
        open_mode = "w" if with_content else "x"

        new_file = open(file_name, open_mode)

        if with_content:
            new_file.write(content)

        new_file.close()
    except ValueError as error:
        raise IOError(f"You need to include some content to create a file") from error


def update_file(file_name: str, content: str, overwrite: bool = False):
    try:
        open_mode = "w" if overwrite else "a"

        file = open(file_name, open_mode)

        file.write(content)

        file.close()
    except FileExistsError as error:
        raise IOError(
            f"File {file_name} already exist, please try again with a new name"
        ) from error
    except PermissionError as error:
        raise IOError(
            f"File {file_name} already exist, please try again with a new name"
        ) from error


def delete_file(file_path):
    try:
        get_is_file_exist(file_path)
        os.remove(file_path)
    except FileNotFoundError as error:
        raise IOError(f"File with path {file_path} doesn't exist") from error
    except PermissionError as error:
        raise IOError(f"You don't have permissions to delete this file") from error


def read_file(file_path):
    try:
        get_is_file_exist(file_path)
        file = open(file_path)
        file_stream = file.read()
        print(file_stream)

        return file_stream

    except FileNotFoundError as error:
        raise IOError(f"File with path {file_path} doesn't exist") from error

    except PermissionError as error:
        raise IOError(f"You don't have permissions to delete this file") from error
