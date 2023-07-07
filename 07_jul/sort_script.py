PAIR_NUMBERS = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def sort_numbers_by_second_index():
    PAIR_NUMBERS.sort(key=lambda x: x[1])


sort_numbers_by_second_index()

print(PAIR_NUMBERS)
