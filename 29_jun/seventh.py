IS_LOOP_READY = False
list_of_operations = []

while IS_LOOP_READY == False:
    operation_string = input()
    list_of_operations.append(operation_string)

    if "=" in operation_string:
        IS_LOOP_READY = True

# List comprehension to create a string from a list of operations

string_operations = (
    "print(" + "".join(e for e in list_of_operations).replace("=", "") + ")"
)

exec(string_operations)
