from EntityClass import Entity


class User(Entity):
    def __init__(self, first_name, last_name, email, password="asdasbd76sadg76asd"):
        super().__init__(type(self).__name__)
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email

    def as_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
            "email": self.email,
        }
