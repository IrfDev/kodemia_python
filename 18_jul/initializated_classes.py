from datetime import date
import random


class User:
    # Default property
    race = "Human"

    # Dunder method
    # Initialization of the class, it'll run every time you create a new instance of MainUser/any Class
    # The first argument it's always the instance class
    # From there is a tuple of named arguments
    def __init__(self, first_name, last_name, age, password="asdasbd76sadg76asd"):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.age = age

    def greeting(self):
        print(f"Hello! My name is {self.first_name}")

    def as_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
            "age": self.age,
        }

    def raise_age(self):
        self.age += 1


new_user = User("Irving", "Suarez", 27, "super_secure_password")

new_user.raise_age()

print(new_user.as_dict())
