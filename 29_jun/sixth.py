def create_fibonacci_serie(max_limit):
    fibonacci_list = [1]

    active_index = 0

    active_loop = True

    while active_loop:
        if len(fibonacci_list) < 2:
            fibonacci_list.append(1)

        first_number = fibonacci_list[active_index]
        second_number = fibonacci_list[active_index + 1]

        active_index = active_index + 1

        new_fibonacci_number = first_number + second_number

        if fibonacci_list[-1] >= max_limit:
            active_loop = False
            break
        else:
            fibonacci_list.append(new_fibonacci_number)

    return fibonacci_list


input_number = int(input("Input a limit number for your fibonacci list: "))

fibonacci_list = create_fibonacci_serie(input_number)

print(f"Final fibonacci list: {fibonacci_list}")
