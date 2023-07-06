string_input = input("Por favor ingresa cualquier texto: ")

it_contains_numbers = any(char.isnumeric() for char in string_input)

if it_contains_numbers:
    print(f"El texto '{string_input}' contiene números")
else:
    print(f"El texto '{string_input}' NO contiene números")