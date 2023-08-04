def print_start(func):
    def wrapper():
        print("Function starts here")
        func()

    return wrapper


def print_end(func):
    def wrapper():
        func()
        print("Function ends here")

    return wrapper


@print_start
@print_end
def hello_world():
    print("Hello world")


@print_start
@print_end
def hello_name(name: str):
    print(f"Hello {name}")


hello_name("Daniela")
hello_world()
