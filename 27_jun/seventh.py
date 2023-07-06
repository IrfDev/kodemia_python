input_min_number = int(input('Ingresa un número mínimo: '))
input_max_number = int(input('Ingresa un número máximo: '))

range_of_inputs = range(input_min_number, input_max_number)

divisible_numbers = []

for input_number in range_of_inputs:
    if input_number % 3 == 0:
        divisible_numbers.append(input_number)

for divisible_number in divisible_numbers:
    print(f"El numero {divisible_number} es divisible entre 3")