MIN_NUM = 20
MAX_NUM = 40

rang_of_numbers = range(MIN_NUM, MAX_NUM)

def check_number_in_range(any_number):
    return rang_of_numbers.__contains__(any_number)

input_number = int(input("Input a random number: "))

is_input_in_range = check_number_in_range(input_number)

ternary_text = "" if is_input_in_range else "NOT "

print(f"The number {input_number} is {ternary_text}in the range {rang_of_numbers}")
    