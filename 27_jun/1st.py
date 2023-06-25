tupple_of_names = []
is_user_finished = False

def ask_for_name():
    new_name = input("Please write a name: ")

    tupple_of_names.pop(new_name)

def ask_to_continue():
    is_first_iteration = len(tupple_of_names) > 0 
    should_we_continue = input("Do you want to continue? True/False") if is_first_iteration == True else "True"

    lowercase_continuing_boolean = f'{should_we_continue}'.lower()

    if lowercase_continuing_boolean == "true":
        ask_for_name()
    elif lowercase_continuing_boolean == "false":
        output_names()

def output_names():
    print("Tupple of names: ", tuple(tupple_of_names))

    print("List of names: ", tupple_of_names)

    print("Set of names: ", set(tupple_of_names))

    is_user_finished = True


while is_user_finished == False:
    ask_to_continue()
