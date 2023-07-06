index = int(0)
input_numbers=[]

while index < 3:
    new_input_number = int(input("Por favor ingresa un número: "))
    input_numbers.append(new_input_number)
    index= index + 1
  
sum_of_inputs = 0

for some_number in input_numbers:
    sum_of_inputs = sum_of_inputs + some_number

if sum_of_inputs % 3 == 0:
    print(sum_of_inputs*3)
else:
    print(sum_of_inputs)