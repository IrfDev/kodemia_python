import json
import file_manager

NEW_JSON_FILE = "new_json_file.json"

user = [
    {
        "username": "Irf",
        "name": "Irving",
        "last_name": "Suarez",
        "password": "s34d5f6gbytg",
    }
]

# # Convert a dictionary into a string with JSON format
json_user = json.dumps(user)

print(f"This is a string with users: {json_user}")

file_manager.create_file(NEW_JSON_FILE, json_user)

# Convert a string with JSON format into a dictionary

json_content = file_manager.read_file(NEW_JSON_FILE)


py_dictionary = json.loads(json_content)

print(
    f"This is a python dictionary with type = {type(py_dictionary)} , {py_dictionary}"
)
