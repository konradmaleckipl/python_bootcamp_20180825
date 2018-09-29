
class Produkt:

    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f'Produkt "{self.nazwa}", id: {self.id}, cena: {self.cena} PLN')


def test_produkt(capsys):
    produkt = Produkt(1, 'Woda', 10.99)
    assert produkt.id == 1
    assert produkt.nazwa == 'Woda'
    assert produkt.cena == 10.99
    produkt.print_info()
    out = capsys.readouterr()[0]
    assert out == 'Produkt "Woda", id: 1, cena: 10.99 PLN\n'


