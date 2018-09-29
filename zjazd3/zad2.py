import pytest


class Employee:

    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self.salary = salary
        self.time = 0

    def register_time(self, time):
        if time > 24:
            raise ValueError()
        else:
            self.time += time

    def pay_salary(self):
        if self.time is not None and self.time <= 8:
            result = self.time * self.salary
            self.time = 0
            return result
        if self.time > 8:
            result = (8 * self.salary) + (((self.time - 8)*2) * self.salary)
            self.time = 0
            return result


def test_employee():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.name == 'Jan'
    employee.register_time(5)
    assert employee.pay_salary() == 500
    assert employee.pay_salary() == 0
    employee.register_time(10)
    assert employee.pay_salary() == 1200
    with pytest.raises(ValueError) as e:
        employee.register_time(25)
