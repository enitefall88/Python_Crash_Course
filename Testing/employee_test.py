import unittest
from employee import Employee

class TestEmployeeInit(unittest.TestCase):
    def setUp(self):
        self.new_employee = Employee('John', 'Johnson', 40000)

    def test_give_default_raise(self):
        self.assertEqual(self.new_employee.give_raise(), 45000)

    def test_give_custom_raise(self):
        self.assertEqual(self.new_employee.give_raise(3000), 43000)

if __name__ == '__main__':
    unittest.main()
