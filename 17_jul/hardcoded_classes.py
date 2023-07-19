from datetime import date


class MainUser:
    first_name = "Irving"
    last_name = "Suarez"
    birth_date = date(1996, 3, 26)
    username = "IrfDev"
    password = "asdasvd65asfd57"
    email = "some_email@some_domain.com"
    user_id = 1

    def greeting(self):
        print(f"Hello! My name is {self.first_name}")
