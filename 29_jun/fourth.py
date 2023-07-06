def check_is_prime_number(any_number):
    is_prime_number = True
    range_of_numbers = range(2, any_number)

    for number in range_of_numbers:
        if any_number % number == 0:
            is_prime_number = False
            break

    return is_prime_number


input_number = int(input("Input a random number: "))

is_prime_number = check_is_prime_number(input_number)

if is_prime_number:
    print(f"{input_number} is a prime number")
else:
    print(f"{input_number} is not a prime number")
