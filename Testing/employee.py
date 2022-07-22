class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_ammount=5000):
        self.annual_salary += raise_ammount
        return self.annual_salary

    def show_salary(self):
        print(self.annual_salary)

john = Employee('John', 'Johnson', 50000)
john.give_raise(3000)
john.show_salary()
