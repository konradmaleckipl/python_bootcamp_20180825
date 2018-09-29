from zjazd3.zad2 import Employee


class PremiumEmployee(Employee):

    def __init__(self, name='Jan', lastname='Nowak', salary=500, bonus=0):
        super().__init__(name, lastname, salary)
        self.bonus = bonus

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        sal_ret = super().pay_salary()
        sal_ret += self.bonus
        self.bonus = 0
        return sal_ret

    @classmethod
    def create_hero(cls):
        return PremiumEmployee('pracownik', 'miesiaca', 0, 0)

    @classmethod
    def create_emp_from_string(cls, text):
        return PremiumEmployee(text.split()[0], text.split()[1], float(text.split()[2]), float(text.split()[3]))


def test_create():
    emp = PremiumEmployee('Jan', 'Nowak', 100)
    assert emp.name == 'Jan'
    assert emp.lastname == 'Nowak'
    assert emp.salary == 100
    assert emp.bonus == 0

def test_register():
    emp = PremiumEmployee('Jan', 'Nowak', 100)
    emp.register_time(5)
    emp.give_bonus(1000)
    emp.give_bonus(400)
    assert emp.bonus == 1400
    assert emp.pay_salary() == 1900

def test_employee_of_the_month():
    emp = PremiumEmployee.create_hero()
    assert emp.pay_salary() == 0

def test_create_emp_from_string():
    emp = PremiumEmployee.create_emp_from_string('Konrad Malecki 10000 2000')
    assert emp.name == 'Konrad'
    assert emp.lastname == 'Malecki'
    assert emp.salary == 10000
    assert emp.bonus == 2000
