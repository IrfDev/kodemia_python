initial_number_list = []
should_we_add_more_numbers = True
is_first_time = True

while should_we_add_more_numbers == True:
    boolean_input = True if is_first_time else input('Deseas seguir agregando números? y/n : ') == 'y'
    is_first_time = False

    if boolean_input: 
        new_number = int(input("Ingresa un número: "))
        initial_number_list.append(new_number)
    else:
        should_we_add_more_numbers = False
        
max_number = max(initial_number_list)

print(f"El mayor número de tu lista es: {max_number}")