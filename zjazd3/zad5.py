

class CashMachine:
    def __init__(self):
        self._money = []

    def is_available(self):
        return len(self._money) > 0

    def put_money(self, bills):
        for bill in bills:
            self._money.append(bill)

    def withdraw_money(self, amount):
        bills_to_be_returned = []
        for bill in sorted(self._money, reverse=True):
            if bill <= amount:
                bills_to_be_returned.append(bill)
                self._money.remove(bill)
                amount = amount - bill

        if amount > 0:
            self.put_money(bills_to_be_returned)
            return []
        else:
            return bills_to_be_returned


def test_is_available_empty():
    cash_machine = CashMachine()
    assert not cash_machine.is_available()

def test_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])

def test_is_available_not_empty():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available()

def test_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150) == [100, 50]

def test_multiple_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(100) == [100]
    assert cash_machine.withdraw_money(300) == [200, 100]
    assert cash_machine.withdraw_money(100) == []
    assert cash_machine.is_available()
    assert cash_machine.withdraw_money(50) == [50]
    assert not cash_machine.is_available()

def test_withdraw_money_with_diff_bills():
    cash_machine = CashMachine()
    cash_machine.put_money([50, 20, 20, 20, 20, 20])
    assert cash_machine.withdraw_money(100) == [20, 20, 20, 20, 20]
