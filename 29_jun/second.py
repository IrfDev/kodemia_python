import first_script as get_list_of_numbers

def multiply_numbers(*args):
    result = 1

    for x in args:
        result = result * x

    print(f"El resultado de la multiplicación es: {result}")



multiply_numbers(*get_list_of_numbers.initial_number_list)
