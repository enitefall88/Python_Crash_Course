class User:
    def __init__(self, first_name, last_name, email, username, login_attempts=0, *password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.login_attempts = login_attempts
        self.password = password

    def describe_user(self):
        print(f"The real full name of the user {self.username} is {self.first_name}"
              f" {self.last_name}. The email is {self.email}. The password is "
              f" {self.password}. The user has tried to login {self.login_attempts} times")

    def greet_user(self):
        print(f"Hi {self.first_name.title()} {self.last_name.title()}")

    def increment_login_attempts(self, increment_login_attempts=1):
        self.login_attempts += increment_login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, email, username, login_attempts, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.login_attempts = login_attempts
        self.password = password
        super().__init__(first_name, last_name, email, username, login_attempts, password)

        self.privileges = Privileges()


class Privileges:
    def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
