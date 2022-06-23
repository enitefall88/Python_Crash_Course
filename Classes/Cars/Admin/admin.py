from user import User
from privileges import Privileges

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
