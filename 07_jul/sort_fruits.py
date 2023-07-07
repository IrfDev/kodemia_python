FRUITS = [
    "banana",
    "orange",
    "Kiwi",
    "melon",
    1,
    20,
    8.7,
    "Cherry",
    "mango",
    "apple",
]


def key_sort_function(item):
    type_of_item = type(item)

    if type_of_item == str:
        return 1
    elif type_of_item == int or type_of_item == float:
        return 3
    else:
        return 2


FRUITS.sort(key=key_sort_function)

print(FRUITS)
